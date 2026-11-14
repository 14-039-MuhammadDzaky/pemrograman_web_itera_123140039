"""
library_item.py
Modul Item Perpustakaan - Tugas Praktikum Pertemuan 5 (PAW ITERA)
Penulis : Muhammad Dzaky (123140039)
Kelas   : RA

Modul ini mendefinisikan hierarki kelas item perpustakaan:
1. LibraryItem (Abstract Base Class)
2. Book (Subclass untuk Buku)
3. Magazine (Subclass untuk Majalah / Terbitan Berkala)
4. DigitalMedia (Subclass untuk Media Digital seperti CD / E-Book)
Menerapkan konsep Abstraksi, Pewarisan (Inheritance), Enkapsulasi, dan Polimorfisme.
"""

from abc import ABC, abstractmethod
from typing import Optional


class LibraryItem(ABC):
    """
    Abstract Base Class yang merepresentasikan setiap entitas koleksi di perpustakaan.
    Menetapkan atribut dasar terenkapsulasi dan kontrak method yang wajib diimplementasikan.
    """

    def __init__(self, item_id: str, judul: str, tahun_terbit: int) -> None:
        # Atribut Protected: Dapat diakses oleh class turunan (subclass)
        self._item_id: str = item_id
        self._judul: str = judul
        self._tahun_terbit: int = tahun_terbit

        # Atribut Private: Terproteksi penuh dari modifikasi luar secara langsung
        self.__is_dipinjam: bool = False
        self.__id_peminjam: Optional[str] = None

    # ==========================================================================
    # PROPERTY GETTERS (Enkapsulasi)
    # ==========================================================================

    @property
    def item_id(self) -> str:
        """Mengembalikan identifier unik dari item perpustakaan."""
        return self._item_id

    @property
    def judul(self) -> str:
        """Mengembalikan judul dari item perpustakaan."""
        return self._judul

    @property
    def tahun_terbit(self) -> int:
        """Mengembalikan tahun terbit publikasi item."""
        return self._tahun_terbit

    @property
    def is_dipinjam(self) -> bool:
        """Mengembalikan status ketersediaan item (True jika sedang dipinjam)."""
        return self.__is_dipinjam

    @property
    def id_peminjam(self) -> Optional[str]:
        """Mengembalikan ID anggota yang sedang meminjam item ini, jika ada."""
        return self.__id_peminjam

    # ==========================================================================
    # BUSINESS METHODS
    # ==========================================================================

    def pinjam_item(self, id_member: str) -> bool:
        """
        Mengubah status item menjadi dipinjam.
        Mengembalikan True jika peminjaman berhasil, False jika item sudah terpinjam.
        """
        if self.__is_dipinjam:
            return False
        self.__is_dipinjam = True
        self.__id_peminjam = id_member
        return True

    def kembalikan_item(self) -> bool:
        """
        Mereset status ketersediaan item menjadi tersedia kembali di perpustakaan.
        """
        if not self.__is_dipinjam:
            return False
        self.__is_dipinjam = False
        self.__id_peminjam = None
        return True

    # ==========================================================================
    # ABSTRACT METHODS (Kontrak Pewarisan & Polimorfisme)
    # ==========================================================================

    @abstractmethod
    def hitung_denda(self, hari_terlambat: int) -> float:
        """
        Menghitung besaran denda keterlambatan per hari berdasarkan jenis item.
        Wajib dioverride oleh seluruh subclass konkrit.
        """
        pass

    @abstractmethod
    def get_detail(self) -> str:
        """
        Mengembalikan representasi teks detail lengkap spesifik tiap jenis item.
        """
        pass

    @abstractmethod
    def durasi_maksimal_hari(self) -> int:
        """
        Mengembalikan batas waktu peminjaman standar (dalam satuan hari).
        """
        pass

    # ==========================================================================
    # DUNDER METHODS
    # ==========================================================================

    def __str__(self) -> str:
        status = "DIPINJAM" if self.__is_dipinjam else "TERSEDIA"
        return f"[{self._item_id}] {self._judul} ({self._tahun_terbit}) - [{status}]"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(id='{self._item_id}', judul='{self._judul}')"


# ==============================================================================
# SUBCLASS KONKRIT: Book (Buku Fisik)
# ==============================================================================

class Book(LibraryItem):
    """
    Subclass Book yang merepresentasikan koleksi buku cetak di perpustakaan.
    Mewarisi LibraryItem dengan atribut tambahan: penulis, jumlah halaman, dan ISBN.
    """

    TARIF_DENDA_PER_HARI: float = 2_000.0  # Rp 2.000 per hari keterlambatan
    BATAS_PINJAM_HARI: int = 14            # Standar pinjam 14 hari

    def __init__(
        self,
        item_id: str,
        judul: str,
        tahun_terbit: int,
        penulis: str,
        jumlah_halaman: int,
        isbn: str
    ) -> None:
        super().__init__(item_id, judul, tahun_terbit)
        self._penulis: str = penulis
        self._jumlah_halaman: int = max(0, jumlah_halaman)
        self._isbn: str = isbn

    @property
    def penulis(self) -> str:
        return self._penulis

    @property
    def isbn(self) -> str:
        return self._isbn

    @property
    def jumlah_halaman(self) -> int:
        return self._jumlah_halaman

    # Implementasi Method Abstract (Polimorfisme)
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Denda buku: Rp 2.000 per hari keterlambatan."""
        if hari_terlambat <= 0:
            return 0.0
        return float(hari_terlambat * self.TARIF_DENDA_PER_HARI)

    def durasi_maksimal_hari(self) -> int:
        return self.BATAS_PINJAM_HARI

    def get_detail(self) -> str:
        status = "Sedang Dipinjam" if self.is_dipinjam else "Tersedia di Rak"
        return (
            f"Tipe: BUKU | Penulis: {self._penulis} | Halaman: {self._jumlah_halaman} hlm | "
            f"ISBN: {self._isbn} | Durasi Pinjam: {self.durasi_maksimal_hari()} hari | Status: {status}"
        )


# ==============================================================================
# SUBCLASS KONKRIT: Magazine (Majalah / Terbitan Berkala)
# ==============================================================================

class Magazine(LibraryItem):
    """
    Subclass Magazine yang merepresentasikan majalah ilmiah atau terbitan periodik.
    Mewarisi LibraryItem dengan atribut tambahan: nomor edisi, kategori, dan penerbit.
    """

    TARIF_DENDA_PER_HARI: float = 1_000.0  # Rp 1.000 per hari keterlambatan
    BATAS_PINJAM_HARI: int = 7             # Terbitan periodik lebih cepat (7 hari)

    def __init__(
        self,
        item_id: str,
        judul: str,
        tahun_terbit: int,
        edisi: str,
        kategori: str,
        penerbit: str
    ) -> None:
        super().__init__(item_id, judul, tahun_terbit)
        self._edisi: str = edisi
        self._kategori: str = kategori
        self._penerbit: str = penerbit

    @property
    def edisi(self) -> str:
        return self._edisi

    @property
    def kategori(self) -> str:
        return self._kategori

    @property
    def penerbit(self) -> str:
        return self._penerbit

    # Implementasi Method Abstract (Polimorfisme)
    def hitung_denda(self, hari_terlambat: int) -> float:
        """Denda majalah: Rp 1.000 per hari keterlambatan."""
        if hari_terlambat <= 0:
            return 0.0
        return float(hari_terlambat * self.TARIF_DENDA_PER_HARI)

    def durasi_maksimal_hari(self) -> int:
        return self.BATAS_PINJAM_HARI

    def get_detail(self) -> str:
        status = "Sedang Dipinjam" if self.is_dipinjam else "Tersedia di Rak"
        return (
            f"Tipe: MAJALAH | Edisi: {self._edisi} | Kategori: {self._kategori} | "
            f"Penerbit: {self._penerbit} | Durasi Pinjam: {self.durasi_maksimal_hari()} hari | Status: {status}"
        )


# ==============================================================================
# SUBCLASS KONKRIT TAMBAHAN: DigitalMedia (CD/DVD / Media Edukasi)
# ==============================================================================

class DigitalMedia(LibraryItem):
    """
    Subclass DigitalMedia yang merepresentasikan media kepingan CD/DVD interaktif.
    """

    TARIF_DENDA_PER_HARI: float = 3_000.0  # Rp 3.000 per hari
    BATAS_PINJAM_HARI: int = 5             # Durasi pinjam 5 hari

    def __init__(
        self,
        item_id: str,
        judul: str,
        tahun_terbit: int,
        format_media: str,
        durasi_menit: int
    ) -> None:
        super().__init__(item_id, judul, tahun_terbit)
        self._format_media: str = format_media
        self._durasi_menit: int = durasi_menit

    def hitung_denda(self, hari_terlambat: int) -> float:
        if hari_terlambat <= 0:
            return 0.0
        return float(hari_terlambat * self.TARIF_DENDA_PER_HARI)

    def durasi_maksimal_hari(self) -> int:
        return self.BATAS_PINJAM_HARI

    def get_detail(self) -> str:
        status = "Sedang Dipinjam" if self.is_dipinjam else "Tersedia di Rak"
        return (
            f"Tipe: DIGITAL MEDIA | Format: {self._format_media} | Durasi: {self._durasi_menit} menit | "
            f"Durasi Pinjam: {self.durasi_maksimal_hari()} hari | Status: {status}"
        )

