"""
member.py
Modul Entitas Anggota Perpustakaan - Tugas Praktikum Pertemuan 5 (PAW ITERA)
Penulis : Muhammad Dzaky (123140039)
Kelas   : RA

Modul ini mengimplementasikan class Member untuk mengelola data anggota
perpustakaan, kuota peminjaman aktif, dan riwayat item yang sedang dipinjam
dengan prinsip enkapsulasi data penuh.
"""

from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from library_item import LibraryItem


class Member:
    """
    Class representasi anggota perpustakaan ITERA.
    Menerapkan enkapsulasi penuh untuk melindungi daftar pinjaman dan kuota anggota.
    """

    def __init__(
        self,
        id_member: str,
        nama: str,
        email: str,
        tipe_keanggotaan: str = "Mahasiswa",
        maks_pinjaman: int = 3
    ) -> None:
        self.__id_member: str = id_member
        self.__nama: str = nama
        self.__email: str = email
        self.__tipe_keanggotaan: str = tipe_keanggotaan
        self.__maks_pinjaman: int = max(1, maks_pinjaman)
        self.__daftar_pinjaman: List["LibraryItem"] = []

    # ==========================================================================
    # PROPERTY GETTERS (Enkapsulasi)
    # ==========================================================================

    @property
    def id_member(self) -> str:
        """Mengembalikan ID unik anggota."""
        return self.__id_member

    @property
    def nama(self) -> str:
        """Mengembalikan nama lengkap anggota."""
        return self.__nama

    @property
    def email(self) -> str:
        """Mengembalikan email resmi anggota."""
        return self.__email

    @property
    def tipe_keanggotaan(self) -> str:
        """Mengembalikan tipe keanggotaan (Mahasiswa / Dosen / Staf)."""
        return self.__tipe_keanggotaan

    @property
    def maks_pinjaman(self) -> int:
        """Mengembalikan batas maksimal kuota item yang boleh dipinjam bersamaan."""
        return self.__maks_pinjaman

    @property
    def jumlah_pinjaman(self) -> int:
        """Mengembalikan jumlah item yang saat ini sedang aktif dipinjam."""
        return len(self.__daftar_pinjaman)

    @property
    def daftar_pinjaman(self) -> List["LibraryItem"]:
        """
        Mengembalikan salinan (copy) daftar pinjaman agar list internal
        tidak dapat dimanipulasi secara ilegal dari luar class.
        """
        return list(self.__daftar_pinjaman)

    # ==========================================================================
    # BUSINESS LOGIC METHODS
    # ==========================================================================

    def bisa_pinjam(self) -> bool:
        """Mengecek apakah anggota masih memiliki sisa kuota peminjaman."""
        return self.jumlah_pinjaman < self.__maks_pinjaman

    def tambah_pinjaman(self, item: "LibraryItem") -> bool:
        """
        Menambahkan item ke daftar pinjaman aktif anggota.
        Memvalidasi kuota sebelum menambahkan.
        """
        if not self.bisa_pinjam():
            print(f"[Kuota Penuh] Anggota {self.__nama} telah mencapai batas pinjam ({self.__maks_pinjaman} item).")
            return False

        if item in self.__daftar_pinjaman:
            print(f"[Duplikasi] Item '{item.judul}' sudah ada di daftar pinjaman anggota.")
            return False

        self.__daftar_pinjaman.append(item)
        return True

    def hapus_pinjaman(self, item: "LibraryItem") -> bool:
        """Menghapus item dari daftar pinjaman saat dikembalikan."""
        if item in self.__daftar_pinjaman:
            self.__daftar_pinjaman.remove(item)
            return True
        return False

    def tampilkan_kartu_anggota(self) -> str:
        """Menghasilkan format kartu anggota perpustakaan."""
        sisa_kuota = self.__maks_pinjaman - self.jumlah_pinjaman
        return (
            f"┌{'─' * 52}┐\n"
            f"│ {'KARTU ANGGOTA PERPUSTAKAAN ITERA':^50} │\n"
            f"├{'─' * 52}┤\n"
            f"│ ID Member  : {self.__id_member:<37} │\n"
            f"│ Nama       : {self.__nama:<37} │\n"
            f"│ Tipe       : {self.__tipe_keanggotaan:<37} │\n"
            f"│ Email      : {self.__email:<37} │\n"
            f"│ Pinjaman   : {f'{self.jumlah_pinjaman} / {self.__maks_pinjaman} item (Sisa kuota: {sisa_kuota})':<37} │\n"
            f"└{'─' * 52}┘"
        )

    def __str__(self) -> str:
        return f"Member({self.__id_member} - {self.__nama} [{self.__tipe_keanggotaan}] | Aktif: {self.jumlah_pinjaman} item)"

    def __repr__(self) -> str:
        return f"Member(id='{self.__id_member}', nama='{self.__nama}', tipe='{self.__tipe_keanggotaan}')"

