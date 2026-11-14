"""
latihan_truk.py
Praktikum Pemrograman Web - Pertemuan 5
Materi: Latihan 3 - Armada Truk Ekspedisi Kargo (Pewarisan dan Overriding)

Deskripsi Tugas:
- Membuat class dasar Kendaraan (atau mengimpor dari modul latihan).
- Membuat subclass Truk(Kendaraan).
- Menambahkan atribut kapasitas_maksimal_ton dan muatan_saat_ini.
- Membuat method muat_barang(berat_ton) dengan validasi kapasitas.
- Meng-override method deskripsi() untuk menampilkan beban muatan saat ini.
"""


class Kendaraan:
    """Class induk dasar transportasi darat."""

    def __init__(self, merk: str, model: str, tahun: int) -> None:
        self.merk: str = merk
        self.model: str = model
        self.tahun: int = tahun

    def deskripsi(self) -> str:
        """Mengembalikan deskripsi dasar kendaraan."""
        return f"{self.tahun} {self.merk} {self.model}"


class Truk(Kendaraan):
    """
    Subclass Truk yang mewarisi Kendaraan untuk armada ekspedisi logistik kargo.
    """

    def __init__(
        self,
        merk: str,
        model: str,
        tahun: int,
        kapasitas_maksimal_ton: float,
        plat_nomor: str = "BE 1234 PAW"
    ) -> None:
        super().__init__(merk, model, tahun)
        self.kapasitas_maksimal_ton: float = float(kapasitas_maksimal_ton)
        self.muatan_saat_ini: float = 0.0
        self.plat_nomor: str = plat_nomor

    def muat_barang(self, berat_ton: float) -> bool:
        """
        Memuat barang ke dalam bak truk dengan validasi kapasitas muatan maksimum.
        """
        if berat_ton <= 0:
            print(f"[{self.merk} {self.model}] Berat muatan harus bernilai positif (> 0 ton)!")
            return False

        if self.muatan_saat_ini + berat_ton > self.kapasitas_maksimal_ton:
            kelebihan = (self.muatan_saat_ini + berat_ton) - self.kapasitas_maksimal_ton
            print(
                f"[Gagal Muat - Overload] Muatan ditolak! Kelebihan beban sebesar {kelebihan:.2f} ton.\n"
                f"  -> Kapasitas: {self.kapasitas_maksimal_ton:.2f} ton | Terisi: {self.muatan_saat_ini:.2f} ton | "
                f"Muatan Baru: {berat_ton:.2f} ton"
            )
            return False

        self.muatan_saat_ini += berat_ton
        sisa = self.kapasitas_maksimal_ton - self.muatan_saat_ini
        print(
            f"[Sukses Muat] +{berat_ton:.2f} ton berhasil dinaikkan ke truk.\n"
            f"  -> Total Muatan: {self.muatan_saat_ini:.2f} / {self.kapasitas_maksimal_ton:.2f} ton "
            f"(Sisa ruang: {sisa:.2f} ton)"
        )
        return True

    def bongkar_muatan(self) -> None:
        """Mengosongkan muatan kargo truk di tempat tujuan."""
        print(f"[{self.merk} {self.model}] Membongkar {self.muatan_saat_ini:.2f} ton muatan kargo.")
        self.muatan_saat_ini = 0.0

    def deskripsi(self) -> str:
        """
        Override method deskripsi() dari class Kendaraan untuk
        menampilkan rincian spesifik armada truk kargo.
        """
        persentase_muatan = (self.muatan_saat_ini / self.kapasitas_maksimal_ton) * 100
        return (
            f"[Armada Truk Logistik] {super().deskripsi()} | Plat: {self.plat_nomor}\n"
            f"  Beban Kargo : {self.muatan_saat_ini:.2f} ton / {self.kapasitas_maksimal_ton:.2f} ton "
            f"({persentase_muatan:.1f}% Terisi)"
        )


def main() -> None:
    print("=" * 75)
    print(" LATIHAN 3: ARMADA TRUK EKSPEDISI KARGO (INHERITANCE & OVERRIDING) ")
    print("=" * 75)

    # Inisialisasi truk Hino 500 dengan kapasitas 15 ton
    truk_ekspedisi = Truk(
        merk="Hino",
        model="500 Series Ranger",
        tahun=2023,
        kapasitas_maksimal_ton=15.0,
        plat_nomor="BE 9039 IT"
    )

    print("\n--- 1. Deskripsi Awal Truk (Kosong) ---")
    print(truk_ekspedisi.deskripsi())

    print("\n--- 2. Proses Pemuatan Kargo Bertahap ---")
    # Pemuatan pertama: 6 ton (Valid)
    truk_ekspedisi.muat_barang(6.0)

    # Pemuatan kedua: 5.5 ton (Valid)
    truk_ekspedisi.muat_barang(5.5)

    print("\n--- 3. Uji Coba Pemuatan Melebihi Kapasitas (Overload) ---")
    # Pemuatan ketiga: 5 ton (Total jadi 16.5 ton > 15 ton -> Harus ditolak)
    truk_ekspedisi.muat_barang(5.0)

    print("\n--- 4. Deskripsi Truk Setelah Pemuatan Maksimal ---")
    print(truk_ekspedisi.deskripsi())

    print("\n--- 5. Pembongkaran Kargo di Gudang Tujuan ---")
    truk_ekspedisi.bongkar_muatan()
    print(truk_ekspedisi.deskripsi())

    print("\n" + "=" * 75)


if __name__ == "__main__":
    main()

