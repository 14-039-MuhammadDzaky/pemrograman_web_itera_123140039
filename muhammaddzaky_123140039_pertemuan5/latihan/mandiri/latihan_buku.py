"""
latihan_buku.py
Praktikum Pemrograman Web - Pertemuan 5
Materi: Latihan 2 - Class Buku dengan Diskon & Dunder Method __len__

Deskripsi Tugas:
- Membuat class Buku dengan atribut: judul, penulis, harga_asli, jumlah_halaman.
- Menambahkan method hitung_harga_diskon(persen) untuk mengembalikan harga setelah potongan.
- Menambahkan method __str__ untuk mencetak kartu buku yang rapi.
- Menambahkan dunder method __len__(self) yang mengembalikan jumlah_halaman saat fungsi len(buku) dipanggil.
"""


class Buku:
    """Class representasi buku dengan fitur kalkulasi diskon dan dunder length."""

    def __init__(self, judul: str, penulis: str, harga_asli: float, jumlah_halaman: int) -> None:
        self.judul: str = judul
        self.penulis: str = penulis
        self.harga_asli: float = float(harga_asli)
        self.jumlah_halaman: int = max(0, jumlah_halaman)

    def hitung_harga_diskon(self, persen: float) -> float:
        """
        Menghitung harga buku setelah diberikan diskon.
        Validasi persen diskon antara 0% hingga 100%.
        """
        if not (0.0 <= persen <= 100.0):
            raise ValueError(f"Persentase diskon {persen}% tidak valid! Harus antara 0 - 100%.")

        potongan = self.harga_asli * (persen / 100.0)
        return self.harga_asli - potongan

    def __str__(self) -> str:
        """Mencetak kartu informasi buku secara rapi dan estetis."""
        return (
            f"┌{'─' * 50}┐\n"
            f"│ {'KARTU INFORMASI BUKU':^48} │\n"
            f"├{'─' * 50}┤\n"
            f"│ Judul   : {self.judul:<38} │\n"
            f"│ Penulis : {self.penulis:<38} │\n"
            f"│ Halaman : {str(self.jumlah_halaman) + ' hlm':<38} │\n"
            f"│ Harga   : Rp {self.harga_asli:<35,.2f} │\n"
            f"└{'─' * 50}┘"
        )

    def __len__(self) -> int:
        """
        Dunder method __len__:
        Memungkinkan pemanggilan fungsi bawaan Python `len(buku)`
        untuk mengembalikan jumlah halaman buku.
        """
        return self.jumlah_halaman


def main() -> None:
    print("=" * 70)
    print(" LATIHAN 2: CLASS BUKU, DISKON, DAN DUNDER METHOD __len__ ")
    print("=" * 70)

    # Inisialisasi beberapa objek Buku
    buku1 = Buku("Clean Code", "Robert C. Martin", 250_000.0, 464)
    buku2 = Buku("Fluent Python", "Luciano Ramalho", 380_000.0, 792)

    # 1. Cetak Menggunakan __str__
    print("\n--- 1. Informasi Buku (via __str__) ---")
    print(buku1)
    print()
    print(buku2)

    # 2. Pengujian Dunder Method __len__
    print("\n--- 2. Pengujian Dunder Method len(buku) ---")
    print(f"Jumlah halaman '{buku1.judul}': {len(buku1)} halaman")
    print(f"Jumlah halaman '{buku2.judul}': {len(buku2)} halaman")

    # 3. Pengujian Perhitungan Diskon
    print("\n--- 3. Pengujian Hitung Harga Diskon ---")
    diskon = 25.0  # Diskon 25%
    harga_akhir1 = buku1.hitung_harga_diskon(diskon)
    harga_akhir2 = buku2.hitung_harga_diskon(diskon)

    print(f"Buku '{buku1.judul}':")
    print(f"  Harga Asli     : Rp {buku1.harga_asli:,.2f}")
    print(f"  Diskon ({diskon}%) : Rp {buku1.harga_asli * (diskon/100):,.2f}")
    print(f"  Harga Bayar    : Rp {harga_akhir1:,.2f}")

    print(f"\nBuku '{buku2.judul}':")
    print(f"  Harga Asli     : Rp {buku2.harga_asli:,.2f}")
    print(f"  Diskon ({diskon}%) : Rp {buku2.harga_asli * (diskon/100):,.2f}")
    print(f"  Harga Bayar    : Rp {harga_akhir2:,.2f}")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()

