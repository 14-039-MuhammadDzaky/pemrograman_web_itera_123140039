"""
latihan_storage.py
Praktikum Pemrograman Web - Pertemuan 5
Materi: Latihan 6 - Interface File Storage Service (Abstract Base Class)

Deskripsi Tugas:
- Membuat abstract class FileStorage(ABC) dengan abstract method upload_file(nama_file, data_bytes) dan download_file(nama_file).
- Mengimplementasikan dua class konkrit:
  1. LocalDiskStorage (simulasi penyimpanan di partisi disk/folder lokal).
  2. CloudStorage (simulasi penyimpanan di bucket cloud seperti AWS S3 atau Google Cloud Storage).
- Menguji pengunggahan dan pengunduhan berkas menggunakan prinsip antarmuka seragam (polimorfisme).
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional


class FileStorage(ABC):
    """
    Abstract Base Class yang mendefinisikan antarmuka (interface contract)
    layanan penyimpanan file terpadu.
    """

    def __init__(self, nama_penyedia: str) -> None:
        self.nama_penyedia: str = nama_penyedia

    @abstractmethod
    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        """Mengunggah file ke media penyimpanan."""
        pass

    @abstractmethod
    def download_file(self, nama_file: str) -> Optional[bytes]:
        """Mengunduh file dari media penyimpanan."""
        pass


class LocalDiskStorage(FileStorage):
    """Implementasi penyimpanan berkas di sistem file lokal (hard drive/SSD)."""

    def __init__(self, direktori_dasar: str = "C:/storage/local/") -> None:
        super().__init__("Local Disk Storage")
        self.direktori_dasar: str = direktori_dasar
        self._penyimpanan_memori: Dict[str, bytes] = {}

    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        path_lengkap = f"{self.direktori_dasar}{nama_file}"
        self._penyimpanan_memori[nama_file] = data_bytes
        print(f"[{self.nama_penyedia}] Menulis berkas ke disk: {path_lengkap} ({len(data_bytes)} bytes)")
        return True

    def download_file(self, nama_file: str) -> Optional[bytes]:
        path_lengkap = f"{self.direktori_dasar}{nama_file}"
        if nama_file in self._penyimpanan_memori:
            print(f"[{self.nama_penyedia}] Membaca berkas dari disk lokal: {path_lengkap}")
            return self._penyimpanan_memori[nama_file]
        print(f"[{self.nama_penyedia}] Gagal: Berkas '{nama_file}' tidak ditemukan di disk lokal!")
        return None


class CloudStorage(FileStorage):
    """Implementasi penyimpanan berkas di infrastruktur Cloud Object Storage (S3 / GCS)."""

    def __init__(self, nama_bucket: str, region: str = "ap-southeast-1") -> None:
        super().__init__("Cloud Object Storage (AWS S3)")
        self.nama_bucket: str = nama_bucket
        self.region: str = region
        self._bucket_store: Dict[str, bytes] = {}

    def upload_file(self, nama_file: str, data_bytes: bytes) -> bool:
        uri = f"s3://{self.nama_bucket}/{nama_file}"
        self._bucket_store[nama_file] = data_bytes
        print(f"[{self.nama_penyedia}] PUT Object ke URI: {uri} [Region: {self.region}] ({len(data_bytes)} bytes)")
        return True

    def download_file(self, nama_file: str) -> Optional[bytes]:
        uri = f"s3://{self.nama_bucket}/{nama_file}"
        if nama_file in self._bucket_store:
            print(f"[{self.nama_penyedia}] GET Object dari cloud bucket: {uri}")
            return self._bucket_store[nama_file]
        print(f"[{self.nama_penyedia}] 404 Not Found: Kunci objek '{nama_file}' tidak ditemukan di bucket!")
        return None


def sinkronisasi_dokumen(storage: FileStorage, nama_file: str, konten: str) -> None:
    """
    Fungsi polimorfik: Memproses penyimpanan berkas ke backend storage apa pun
    yang mematuhi kontrak FileStorage.
    """
    print(f"\n--- Pengujian Backend: {storage.nama_penyedia} ---")
    data = konten.encode("utf-8")

    # 1. Upload
    storage.upload_file(nama_file, data)

    # 2. Download dan verifikasi
    konten_unduh = storage.download_file(nama_file)
    if konten_unduh:
        print(f"Isi berkas berhasil diverifikasi: \"{konten_unduh.decode('utf-8')}\"")


def main() -> None:
    print("=" * 75)
    print(" LATIHAN 6: INTERFACE FILE STORAGE SERVICE (LOCAL VS CLOUD) ")
    print("=" * 75)

    # Inisialisasi dua penyedia penyimpanan
    local_store = LocalDiskStorage("D:/itera_web/uploads/")
    cloud_store = CloudStorage("itera-paw-mahasiswa-bucket", "ap-southeast-3")

    berkas_uji = "laporan_praktikum_123140039.pdf"
    teks_konten = "Isi Laporan Praktikum Pemrograman Web Minggu 5 - Muhammad Dzaky"

    # Pengujian pada disk lokal
    sinkronisasi_dokumen(local_store, berkas_uji, teks_konten)

    # Pengujian pada cloud storage
    sinkronisasi_dokumen(cloud_store, berkas_uji, teks_konten)

    # Pengujian file tidak ada (404)
    print("\n--- Pengujian File Tidak Ditemukan ---")
    local_store.download_file("file_hilang.txt")
    cloud_store.download_file("file_hilang.txt")

    print("\n" + "=" * 75)


if __name__ == "__main__":
    main()

