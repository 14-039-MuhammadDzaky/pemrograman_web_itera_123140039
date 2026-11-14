"""
main.py
Program Utama Demonstrasi Sistem Manajemen Perpustakaan
Praktikum Pengembangan Aplikasi Web (PAW) - Pertemuan 5
Institut Teknologi Sumatera (ITERA)

Identitas Pengembang:
- Nama  : Muhammad Dzaky
- NIM   : 123140039
- Kelas : RA

Deskripsi:
Skrip demonstrasi ini menguji seluruh fitur sistem perpustakaan dan membuktikan
penerapan 4 pilar Object-Oriented Programming (OOP):
1. Abstraction   : Penggunaan Abstract Base Class (LibraryItem) dengan method abstract.
2. Inheritance   : Pewarisan subclass Book, Magazine, dan DigitalMedia dari LibraryItem.
3. Encapsulation : Proteksi data sensitif dengan atribut private (__koleksi, __is_dipinjam)
                   dan dekorator @property.
4. Polymorphism : Perhitungan denda dan detail informasi polimorfik sesuai tipe objek.
"""

from library_item import LibraryItem, Book, Magazine, DigitalMedia
from member import Member
from library import Library


def cetak_banner_seksi(judul: str) -> None:
    """Mencetak banner pemisah seksi pengujian pada terminal."""
    lebar = 85
    print("\n" + "=" * lebar)
    print(f" {judul.upper():^83} ")
    print("=" * lebar)


def main() -> None:
    # Header Utama
    print("*" * 85)
    print("*" + " " * 83 + "*")
    print("*" + " SISTEM MANAJEMEN PERPUSTAKAAN INSTITUT TEKNOLOGI SUMATERA (ITERA) ".center(83) + "*")
    print("*" + " TUGAS PRAKTIKUM PEMROGRAMAN WEB - PERTEMUAN 5 (PYTHON OOP) ".center(83) + "*")
    print("*" + " Pengembang: Muhammad Dzaky | NIM: 123140039 | Kelas: RA ".center(83) + "*")
    print("*" + " " * 83 + "*")
    print("*" * 85)

    # Inisialisasi Perpustakaan ITERA
    perpustakaan_itera = Library("Perpustakaan Institut Teknologi Sumatera (ITERA)")

    # ==========================================================================
    # SEKSI 1: UJI COBA ABSTRAKSI & INHERITANCE
    # ==========================================================================
    cetak_banner_seksi("1. Pengujian Abstraksi & Penambahan Koleksi Perpustakaan")

    # 1.1 Membuktikan bahwa Abstract Base Class LibraryItem tidak dapat diinstansiasi
    print("\n[Uji Coba Abstraksi] Mencoba menginstansiasi abstract class LibraryItem secara langsung:")
    try:
        item_abstrak = LibraryItem("ABS01", "Buku Abstrak Fiktif", 2026)  # type: ignore
    except TypeError as err:
        print(f"  -> VALIDASI SUKSES: Python menolak instansiasi class abstrak!")
        print(f"  -> Pesan Error: {err}")

    # 1.2 Instansiasi subclass konkrit (Book, Magazine, DigitalMedia)
    print("\n[Instansiasi Objek Koleksi]")
    buku1 = Book(
        item_id="BK-001",
        judul="Clean Code: A Handbook of Agile Software",
        tahun_terbit=2008,
        penulis="Robert C. Martin",
        jumlah_halaman=464,
        isbn="978-0132350884"
    )
    buku2 = Book(
        item_id="BK-002",
        judul="Python Crash Course, 3rd Edition",
        tahun_terbit=2023,
        penulis="Eric Matthes",
        jumlah_halaman=552,
        isbn="978-1718502703"
    )
    buku3 = Book(
        item_id="BK-003",
        judul="Introduction to Algorithms (CLRS)",
        tahun_terbit=2022,
        penulis="Thomas H. Cormen",
        jumlah_halaman=1312,
        isbn="978-0262046305"
    )

    majalah1 = Magazine(
        item_id="MG-001",
        judul="National Geographic Indonesia: Ekspedisi Sumatra",
        tahun_terbit=2024,
        edisi="Vol. 32 No. 04",
        kategori="Sains & Geografi",
        penerbit="Gramedia Majalah"
    )
    majalah2 = Magazine(
        item_id="MG-002",
        judul="IEEE Software: Architectural Patterns for AI",
        tahun_terbit=2025,
        edisi="Vol. 42 Issue 1",
        kategori="Ilmu Komputer & Rekayasa Perangkat Lunak",
        penerbit="IEEE Computer Society"
    )

    media1 = DigitalMedia(
        item_id="DM-001",
        judul="Interactive Python Masterclass & Lab Videos",
        tahun_terbit=2024,
        format_media="ISO / DVD-ROM",
        durasi_menit=360
    )

    # Memasukkan seluruh item ke sistem perpustakaan
    daftar_item_baru = [buku1, buku2, buku3, majalah1, majalah2, media1]
    for item in daftar_item_baru:
        perpustakaan_itera.tambah_item(item)

    print(f"\nTotal koleksi terdaftar saat ini: {perpustakaan_itera.total_koleksi} item.")

    # ==========================================================================
    # SEKSI 2: PENDAFTARAN ANGGOTA PERPUSTAKAAN (MEMBER)
    # ==========================================================================
    cetak_banner_seksi("2. Pendaftaran dan Kartu Anggota Perpustakaan")

    member_dzaky = Member(
        id_member="MBR-001",
        nama="Muhammad Dzaky",
        email="muhammad.123140039@student.itera.ac.id",
        tipe_keanggotaan="Mahasiswa (Teknik Informatika)",
        maks_pinjaman=3
    )
    member_fauzi = Member(
        id_member="MBR-002",
        nama="Ahmad Fauzi",
        email="ahmad.fauzi@staff.itera.ac.id",
        tipe_keanggotaan="Dosen / Peneliti",
        maks_pinjaman=5
    )

    perpustakaan_itera.daftarkan_member(member_dzaky)
    perpustakaan_itera.daftarkan_member(member_fauzi)

    # Cetak kartu anggota
    print()
    print(member_dzaky.tampilkan_kartu_anggota())
    print()
    print(member_fauzi.tampilkan_kartu_anggota())

    # ==========================================================================
    # SEKSI 3: MENAMPILKAN SELURUH KATALOG PERPUSTAKAAN
    # ==========================================================================
    cetak_banner_seksi("3. Menampilkan Seluruh Katalog Perpustakaan")
    perpustakaan_itera.tampilkan_katalog(hanya_tersedia=False)

    # ==========================================================================
    # SEKSI 4: FITUR PENCARIAN ITEM (ID & JUDUL)
    # ==========================================================================
    cetak_banner_seksi("4. Pengujian Fitur Pencarian Item (Berdasarkan ID & Judul)")

    # 4.1 Pencarian berdasarkan ID
    print("\n[Pencarian Berdasarkan ID: 'BK-001']")
    hasil_id = perpustakaan_itera.cari_item_by_id("BK-001")
    if hasil_id:
        print(f"Item Ditemukan: {hasil_id}")
        print(f"Rincian Detail : {hasil_id.get_detail()}")
    else:
        print("Item tidak ditemukan!")

    # 4.2 Pencarian berdasarkan kata kunci Judul
    kata_kunci = "python"
    print(f"\n[Pencarian Berdasarkan Kata Kunci Judul: '{kata_kunci}']")
    hasil_judul = perpustakaan_itera.cari_item_by_judul(kata_kunci)
    print(f"Ditemukan {len(hasil_judul)} item yang cocok:")
    for idx, item in enumerate(hasil_judul, 1):
        print(f"  {idx}. [{item.item_id}] {item.judul} ({item.tahun_terbit})")

    # 4.3 Pencarian item tidak ada
    print(f"\n[Pencarian Item Fiktif: 'Buku Tidak Pernah Ada']")
    hasil_nihil = perpustakaan_itera.cari_item_by_judul("Buku Tidak Pernah Ada")
    print(f"Hasil: {len(hasil_nihil)} item ditemukan (Pencarian aman tanpa crash).")

    # ==========================================================================
    # SEKSI 5: PEMINJAMAN ITEM & ENKAPSULASI
    # ==========================================================================
    cetak_banner_seksi("5. Sirkulasi Peminjaman Item & Validasi Enkapsulasi")

    # Muhammad Dzaky meminjam BK-001 (Clean Code) dan MG-001 (National Geographic)
    print("\n--- Transaksi Peminjaman 1: Muhammad Dzaky ---")
    perpustakaan_itera.pinjam_item("BK-001", "MBR-001")
    perpustakaan_itera.pinjam_item("MG-001", "MBR-001")

    # Ahmad Fauzi meminjam DM-001 (Digital Media)
    print("\n--- Transaksi Peminjaman 2: Ahmad Fauzi ---")
    perpustakaan_itera.pinjam_item("DM-001", "MBR-002")

    # 5.1 Validasi Proteksi: Uji coba meminjam item yang sedang dipinjam
    print("\n--- Uji Coba Pelanggaran: Meminjam Buku yang Sedang Dipinjam ---")
    print("Ahmad Fauzi mencoba meminjam 'BK-001' yang sedang dipegang Dzaky:")
    sukses = perpustakaan_itera.pinjam_item("BK-001", "MBR-002")
    print(f"Hasil Peminjaman Ulang: {'Berhasil (Gagal Proteksi)' if sukses else 'Ditolak Sistem (Proteksi Berhasil)'}")

    # 5.2 Validasi Name Mangling & Enkapsulasi Private
    print("\n--- Pembuktian Enkapsulasi Atribut Private ---")
    print("Mencoba mengakses langsung private attribute '__is_dipinjam' dari objek buku1:")
    try:
        status_rahasia = getattr(buku1, "__is_dipinjam")
    except AttributeError as err:
        print(f"  -> Akses Langsung Ditolak: {err}")

    # Akses status hanya sah melalui @property getter
    print(f"  -> Akses Sah via @property getter (.is_dipinjam): {buku1.is_dipinjam}")

    # ==========================================================================
    # SEKSI 6: MENAMPILKAN DAFTAR ITEM YANG TERSEDIA
    # ==========================================================================
    cetak_banner_seksi("6. Menampilkan Katalog Item yang Tersedia Saja")
    perpustakaan_itera.tampilkan_katalog(hanya_tersedia=True)

    # ==========================================================================
    # SEKSI 7: PENGEMBALIAN ITEM & POLIMORFISME PERHITUNGAN DENDA
    # ==========================================================================
    cetak_banner_seksi("7. Pengembalian Item & Demonstrasi Polimorfisme Denda")

    # 7.1 Pengembalian Tepat Waktu (0 Hari Keterlambatan)
    print("\n[Kasus A] Pengembalian Tepat Waktu (Keterlambatan = 0 hari)")
    perpustakaan_itera.kembalikan_item("DM-001", "MBR-002", hari_terlambat=0)

    # 7.2 Pengembalian Terlambat 5 Hari pada BUKU (Tarif: Rp 2.000 / hari)
    print("\n[Kasus B] Pengembalian Terlambat 5 Hari untuk BUKU (BK-001)")
    perpustakaan_itera.kembalikan_item("BK-001", "MBR-001", hari_terlambat=5)

    # 7.3 Pengembalian Terlambat 5 Hari pada MAJALAH (Tarif: Rp 1.000 / hari)
    print("\n[Kasus C] Pengembalian Terlambat 5 Hari untuk MAJALAH (MG-001)")
    perpustakaan_itera.kembalikan_item("MG-001", "MBR-001", hari_terlambat=5)

    print("\n[Analisis Polimorfisme Denda]")
    print("  -> Buku    terlambat 5 hari: 5 x Rp 2.000 = Rp 10.000,00")
    print("  -> Majalah terlambat 5 hari: 5 x Rp 1.000 = Rp  5.000,00")
    print("  -> Method `hitung_denda()` dieksekusi secara polimorfik sesuai tipe instans!")

    # ==========================================================================
    # SEKSI 8: STATUS AKHIR KATALOG PERPUSTAKAAN
    # ==========================================================================
    cetak_banner_seksi("8. Status Akhir Katalog Setelah Seluruh Item Dikembalikan")
    perpustakaan_itera.tampilkan_katalog(hanya_tersedia=False)

    print("=" * 85)
    print(" SELURUH PENGUJIAN SISTEM MANAJEMEN PERPUSTAKAAN SELESAI DENGAN SUKSES! ")
    print("=" * 85 + "\n")


if __name__ == "__main__":
    main()

