"""
latihan_karyawan.py
Praktikum Pemrograman Web - Pertemuan 5
Materi: Latihan 4 - Enkapsulasi Penggajian Karyawan & Property Decorator

Deskripsi Tugas:
- Membuat class Karyawan dengan atribut publik nama dan jabatan.
- Menerapkan atribut private __gaji_pokok.
- Menggunakan dekorator @property dan setter untuk memastikan gaji pokok tidak diatur di bawah UMR (minimal Rp 3.200.000).
- Menambahkan method hitung_gaji_bersih(pajak_persen).
"""


class Karyawan:
    """
    Class representasi data karyawan dengan perlindungan enkapsulasi
    pada komponen gaji pokok sesuai standar regulasi UMR.
    """

    # Konstanta batas UMR minimal (Rp 3.200.000,00)
    UMR_MINIMAL: float = 3_200_000.0

    def __init__(self, nama: str, jabatan: str, gaji_pokok: float) -> None:
        self.nama: str = nama
        self.jabatan: str = jabatan
        self.__gaji_pokok: float = 0.0

        # Inisialisasi melalui setter berenkapsulasi
        self.gaji_pokok = gaji_pokok

    @property
    def gaji_pokok(self) -> float:
        """Getter untuk membaca nilai gaji pokok."""
        return self.__gaji_pokok

    @gaji_pokok.setter
    def gaji_pokok(self, nilai: float) -> None:
        """
        Setter dengan validasi standar UMR.
        Gaji pokok tidak boleh diatur di bawah Rp 3.200.000,00.
        """
        if not isinstance(nilai, (int, float)):
            raise TypeError("Gaji pokok harus berupa angka numerik!")

        if nilai < self.UMR_MINIMAL:
            raise ValueError(
                f"Penetapan gaji ditolak! Gaji pokok Rp {nilai:,.2f} "
                f"berada di bawah standar UMR (Minimal Rp {self.UMR_MINIMAL:,.2f})."
            )

        self.__gaji_pokok = float(nilai)
        print(f"[Payroll Update] Gaji pokok {self.nama} berhasil diatur ke Rp {self.__gaji_pokok:,.2f}")

    def hitung_gaji_bersih(self, pajak_persen: float = 5.0) -> float:
        """
        Menghitung gaji bersih setelah dipotong pajak penghasilan (PPh).
        Formula: Gaji Bersih = Gaji Pokok - (Gaji Pokok * (Pajak / 100))
        """
        if not (0.0 <= pajak_persen <= 100.0):
            raise ValueError("Persentase pajak harus antara 0% hingga 100%!")

        potongan_pajak = self.__gaji_pokok * (pajak_persen / 100.0)
        return self.__gaji_pokok - potongan_pajak

    def cetak_slip_gaji(self, pajak_persen: float = 5.0) -> None:
        """Mencetak slip gaji karyawan."""
        potongan = self.__gaji_pokok * (pajak_persen / 100.0)
        gaji_bersih = self.hitung_gaji_bersih(pajak_persen)

        print("\n" + "=" * 50)
        print(f" SLIP GAJI KARYAWAN ")
        print("=" * 50)
        print(f"Nama Karyawan  : {self.nama}")
        print(f"Jabatan        : {self.jabatan}")
        print(f"Gaji Pokok     : Rp {self.__gaji_pokok:>15,.2f}")
        print(f"Potongan Pajak : Rp {potongan:>15,.2f} ({pajak_persen}%)")
        print("-" * 50)
        print(f"Gaji Bersih    : Rp {gaji_bersih:>15,.2f}")
        print("=" * 50)


def main() -> None:
    print("=" * 75)
    print(" LATIHAN 4: ENKAPSULASI SISTEM PENGGAJIAN KARYAWAN ")
    print("=" * 75)

    # 1. Instansiasi Sukses (Di atas UMR)
    print("\n--- 1. Pendaftaran Karyawan dengan Gaji di Atas UMR ---")
    karyawan1 = Karyawan("Muhammad Dzaky", "Software Engineer Lead", 8_500_000.0)
    karyawan2 = Karyawan("Budi Santoso", "Junior Web Developer", 4_500_000.0)

    # 2. Cetak Slip Gaji
    karyawan1.cetak_slip_gaji(pajak_persen=5.0)
    karyawan2.cetak_slip_gaji(pajak_persen=5.0)

    # 3. Uji Coba Pengaturan Gaji di Bawah UMR (Harus Ditolak oleh Setter)
    print("\n--- 2. Uji Coba Pelanggaran Standar UMR (< Rp 3.200.000) ---")
    try:
        print("Mencoba mengatur gaji Rp 2.500.000 untuk Junior Developer...")
        karyawan2.gaji_pokok = 2_500_000.0
    except ValueError as e:
        print(f"[Validasi Berhasil Ditegakkan]\n  -> {e}")

    # 4. Uji Coba Kenaikan Gaji yang Sah
    print("\n--- 3. Promosi & Kenaikan Gaji yang Sah ---")
    karyawan2.gaji_pokok = 5_500_000.0
    karyawan2.cetak_slip_gaji(pajak_persen=5.0)

    print("\n" + "=" * 75)


if __name__ == "__main__":
    main()

