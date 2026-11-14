"""
library.py
Modul Sistem Perpustakaan - Tugas Praktikum Pertemuan 5 (PAW ITERA)
Penulis : Muhammad Dzaky (123140039)
Kelas   : RA

Modul ini mengimplementasikan class Library yang bertindak sebagai controller sentral:
1. Menyimpan dan memproteksi koleksi item perpustakaan (__koleksi).
2. Menyimpan data anggota terdaftar (__daftar_member).
3. Menyediakan fitur:
   - Tambah item koleksi
   - Tampilkan katalog item (seluruhnya atau hanya yang tersedia)
   - Pencarian item berdasarkan ID dan Judul
   - Peminjaman item dengan validasi ketersediaan dan kuota member
   - Pengembalian item dengan perhitungan denda polimorfik
"""

from typing import Dict, List, Optional, Tuple
from library_item import LibraryItem
from member import Member


class Library:
    """
    Class Library yang mengelola seluruh siklus operasional perpustakaan.
    Data koleksi dan anggota diproteksi dengan atribut private.
    """

    def __init__(self, nama_perpustakaan: str) -> None:
        self.__nama_perpustakaan: str = nama_perpustakaan

        # Atribut Private: Koleksi item menggunakan dictionary {item_id: LibraryItem}
        self.__koleksi: Dict[str, LibraryItem] = {}

        # Atribut Private: Data anggota menggunakan dictionary {id_member: Member}
        self.__daftar_member: Dict[str, Member] = {}

    # ==========================================================================
    # PROPERTY GETTERS (Enkapsulasi)
    # ==========================================================================

    @property
    def nama_perpustakaan(self) -> str:
        """Mengembalikan nama resmi perpustakaan."""
        return self.__nama_perpustakaan

    @property
    def total_koleksi(self) -> int:
        """Mengembalikan jumlah seluruh koleksi item yang ada."""
        return len(self.__koleksi)

    @property
    def total_member(self) -> int:
        """Mengembalikan jumlah anggota terdaftar."""
        return len(self.__daftar_member)

    # ==========================================================================
    # MANAJEMEN KOLEKSI ITEM & ANGGOTA
    # ==========================================================================

    def tambah_item(self, item: LibraryItem) -> bool:
        """
        Menambahkan item koleksi baru ke dalam perpustakaan.
        Validasi memastikan item adalah turunan LibraryItem dan ID belum terdaftar.
        """
        if not isinstance(item, LibraryItem):
            print(f"[Gagal Tambah] Objek bukan merupakan turunan dari LibraryItem!")
            return False

        if item.item_id in self.__koleksi:
            print(f"[Gagal Tambah] Item dengan ID '{item.item_id}' sudah terdaftar dalam sistem!")
            return False

        self.__koleksi[item.item_id] = item
        print(f"[Sukses Tambah] Berhasil mendaftarkan: {item.judul} (ID: {item.item_id})")
        return True

    def daftarkan_member(self, member: Member) -> bool:
        """
        Mendaftarkan anggota baru ke dalam sistem perpustakaan.
        """
        if not isinstance(member, Member):
            print(f"[Gagal Member] Objek bukan instansiasi dari Member!")
            return False

        if member.id_member in self.__daftar_member:
            print(f"[Gagal Member] Member dengan ID '{member.id_member}' sudah ada!")
            return False

        self.__daftar_member[member.id_member] = member
        print(f"[Sukses Member] Anggota baru terdaftar: {member.nama} (ID: {member.id_member})")
        return True

    # ==========================================================================
    # FITUR PENCARIAN & KATALOG
    # ==========================================================================

    def cari_item_by_id(self, item_id: str) -> Optional[LibraryItem]:
        """
        Mencari item di koleksi perpustakaan secara spesifik berdasarkan ID.
        """
        return self.__koleksi.get(item_id.strip())

    def cari_item_by_judul(self, judul_query: str) -> List[LibraryItem]:
        """
        Mencari item berdasarkan pencocokan substring nama judul (case-insensitive).
        """
        query = judul_query.lower().strip()
        return [item for item in self.__koleksi.values() if query in item.judul.lower()]

    def cari_item(self, keyword: str) -> List[LibraryItem]:
        """
        Pencarian multifungsi yang mencocokkan kata kunci terhadap ID maupun Judul.
        """
        query = keyword.lower().strip()
        hasil: List[LibraryItem] = []
        for item in self.__koleksi.values():
            if query in item.item_id.lower() or query in item.judul.lower():
                hasil.append(item)
        return hasil

    def get_daftar_item_tersedia(self) -> List[LibraryItem]:
        """
        Mengembalikan daftar seluruh item yang statusnya belum dipinjam.
        """
        return [item for item in self.__koleksi.values() if not item.is_dipinjam]

    def tampilkan_katalog(self, hanya_tersedia: bool = False) -> None:
        """
        Menampilkan tabel katalog koleksi perpustakaan secara rapi dan terstruktur.
        Parameter `hanya_tersedia` menyaring item yang siap dipinjam saja.
        """
        daftar = self.get_daftar_item_tersedia() if hanya_tersedia else list(self.__koleksi.values())
        header_judul = "KATALOG ITEM TERSEDIA" if hanya_tersedia else "SELURUH KATALOG PERPUSTAKAAN"

        print("\n" + "=" * 90)
        print(f" {self.__nama_perpustakaan.upper()} ")
        print(f" {header_judul} (Total: {len(daftar)} Item)")
        print("=" * 90)

        if not daftar:
            print("Tidak ada koleksi item yang dapat ditampilkan.")
            print("=" * 90)
            return

        print(f"{'ID Item':<8} | {'Judul Koleksi':<35} | {'Tahun':<6} | {'Status':<12} | {'Tipe / Info Spesifik'}")
        print("-" * 90)

        for item in daftar:
            status_str = "DIPINJAM" if item.is_dipinjam else "TERSEDIA"
            tipe_info = item.__class__.__name__
            print(f"{item.item_id:<8} | {item.judul[:33]:<35} | {item.tahun_terbit:<6} | {status_str:<12} | [{tipe_info}] {item.get_detail()[:40]}...")

        print("=" * 90 + "\n")

    # ==========================================================================
    # SIRKULASI: PEMINJAMAN & PENGEMBALIAN
    # ==========================================================================

    def pinjam_item(self, item_id: str, id_member: str) -> bool:
        """
        Memproses peminjaman item oleh anggota perpustakaan.
        Validasi mencakup: keberadaan item, keberadaan member, ketersediaan item, dan kuota member.
        """
        item = self.cari_item_by_id(item_id)
        if not item:
            print(f"[Peminjaman Ditolak] Item ID '{item_id}' tidak ditemukan di katalog perpustakaan!")
            return False

        member = self.__daftar_member.get(id_member)
        if not member:
            print(f"[Peminjaman Ditolak] Anggota dengan ID '{id_member}' belum terdaftar!")
            return False

        if item.is_dipinjam:
            print(f"[Peminjaman Ditolak] Item '{item.judul}' sedang dipinjam oleh anggota lain!")
            return False

        if not member.bisa_pinjam():
            print(f"[Peminjaman Ditolak] Anggota {member.nama} telah mencapai batas pinjaman ({member.maks_pinjaman} item)!")
            return False

        # Eksekusi peminjaman
        item.pinjam_item(id_member)
        member.tambah_pinjaman(item)
        print(f"[Peminjaman Sukses] Item '{item.judul}' (ID: {item.item_id}) berhasil dipinjam oleh {member.nama}.")
        print(f"  -> Batas Pengembalian: {item.durasi_maksimal_hari()} hari ke depan.")
        return True

    def kembalikan_item(self, item_id: str, id_member: str, hari_terlambat: int = 0) -> Tuple[bool, float]:
        """
        Memproses pengembalian item yang dipinjam dan menghitung denda secara polimorfik.
        Mengembalikan tuple: (status_sukses, jumlah_denda).
        """
        item = self.cari_item_by_id(item_id)
        if not item:
            print(f"[Pengembalian Gagal] Item ID '{item_id}' tidak valid!")
            return False, 0.0

        member = self.__daftar_member.get(id_member)
        if not member:
            print(f"[Pengembalian Gagal] Anggota ID '{id_member}' tidak ditemukan!")
            return False, 0.0

        if not item.is_dipinjam or item.id_peminjam != id_member:
            print(f"[Pengembalian Gagal] Item '{item.judul}' tidak tercatat sedang dipinjam oleh {member.nama}!")
            return False, 0.0

        # Hitung denda secara polimorfik memanggil hitung_denda() pada objek item
        denda = item.hitung_denda(hari_terlambat)

        # Update status
        item.kembalikan_item()
        member.hapus_pinjaman(item)

        print("\n" + "-" * 60)
        print(" NOTA BUKTI PENGEMBALIAN ITEM PERPUSTAKAAN ")
        print("-" * 60)
        print(f"Nama Anggota     : {member.nama} (ID: {member.id_member})")
        print(f"Item Koleksi     : {item.judul} (ID: {item.item_id})")
        print(f"Tipe Item        : {item.__class__.__name__}")
        print(f"Keterlambatan    : {hari_terlambat} hari")
        print(f"Total Denda      : Rp {denda:,.2f}")
        print(f"Status Sekarang  : Item Berhasil Dikembalikan ke Rak Perpustakaan")
        print("-" * 60)

        return True, denda

