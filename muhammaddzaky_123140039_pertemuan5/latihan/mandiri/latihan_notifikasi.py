"""
latihan_notifikasi.py
Praktikum Pemrograman Web - Pertemuan 5
Materi: Latihan 5 - Engine Dispatcher Multi-Saluran Notifikasi (Polimorfisme)

Deskripsi Tugas:
- Membuat 3 class saluran komunikasi: NotifikasiEmail, NotifikasiSMS, dan NotifikasiWhatsApp.
- Masing-masing class memiliki method kirim(pesan, penerima).
- Menerapkan fungsi broadcast_pengumuman(daftar_channel, pesan, penerima) untuk mengirim pesan ke seluruh kanal sekaligus.
- Menunjukkan fleksibilitas polimorfisme dalam memproses berbagai saluran dengan interface yang seragam.
"""

from typing import List, Protocol


class SaluranNotifikasi(Protocol):
    """Protokol interface untuk memastikan saluran memiliki method kirim."""

    def kirim(self, pesan: str, penerima: str) -> bool:
        ...


class NotifikasiEmail:
    """Implementasi pengiriman notifikasi via Electronic Mail (SMTP)."""

    def __init__(self, smtp_server: str = "smtp.itera.ac.id") -> None:
        self.smtp_server: str = smtp_server

    def kirim(self, pesan: str, penerima: str) -> bool:
        print(
            f"[EMAIL - {self.smtp_server}] Mengirim surel ke <{penerima}>\n"
            f"  Subjek : Pengumuman Akademik ITERA\n"
            f"  Isi    : \"{pesan}\""
        )
        return True


class NotifikasiSMS:
    """Implementasi pengiriman notifikasi via SMS Gateway Seluler."""

    def __init__(self, gateway_provider: str = "Telkomsel Gateway") -> None:
        self.gateway_provider: str = gateway_provider

    def kirim(self, pesan: str, penerima: str) -> bool:
        # SMS dibatasi 160 karakter untuk simulasi
        pesan_pendek = pesan if len(pesan) <= 160 else pesan[:157] + "..."
        print(
            f"[SMS - {self.gateway_provider}] Mengirim SMS ke [{penerima}]\n"
            f"  Teks : \"{pesan_pendek}\""
        )
        return True


class NotifikasiWhatsApp:
    """Implementasi pengiriman notifikasi via WhatsApp Business API."""

    def __init__(self, nomor_bisnis: str = "+62721-PAW-ITERA") -> None:
        self.nomor_bisnis: str = nomor_bisnis

    def kirim(self, pesan: str, penerima: str) -> bool:
        print(
            f"[WHATSAPP API - {self.nomor_bisnis}] Mengirim pesan WA ke (+{penerima})\n"
            f"  Status Centang : Hijau Terverifikasi (Dua Centang Biru)\n"
            f"  Pesan          : \"{pesan}\""
        )
        return True


def broadcast_pengumuman(daftar_channel: List[SaluranNotifikasi], pesan: str, daftar_penerima: List[str]) -> None:
    """
    Fungsi polimorfik pengiriman multi-kanal:
    Mengeksekusi penyebaran informasi serentak ke berbagai saluran
    tanpa perlu mengetahui detail teknis internal tiap saluran.
    """
    print("\n" + "#" * 75)
    print(f" MEMULAI PROSES BROADCAST PENGUMUMAN MULTI-KANAL ")
    print("#" * 75)
    print(f"Pesan Pengumuman: \"{pesan}\"")
    print(f"Jumlah Kanal     : {len(daftar_channel)}")
    print(f"Target Penerima  : {', '.join(daftar_penerima)}")
    print("-" * 75)

    total_terkirim = 0
    for channel in daftar_channel:
        nama_class = channel.__class__.__name__
        print(f"\n>> Mengirimkan melalui saluran: {nama_class} ...")
        for penerima in daftar_penerima:
            sukses = channel.kirim(pesan, penerima)
            if sukses:
                total_terkirim += 1

    print("-" * 75)
    print(f"[Broadcast Selesai] Total transaksi pesan terkirim: {total_terkirim}")
    print("#" * 75 + "\n")


def main() -> None:
    print("=" * 75)
    print(" LATIHAN 5: ENGINE DISPATCHER NOTIFIKASI MULTI-SALURAN ")
    print("=" * 75)

    # Inisialisasi 3 jenis saluran berbeda
    email_channel = NotifikasiEmail(smtp_server="mail.itera.ac.id")
    sms_channel = NotifikasiSMS(gateway_provider="Indosat Ooredoo API")
    wa_channel = NotifikasiWhatsApp(nomor_bisnis="+628123140039")

    daftar_saluran = [email_channel, sms_channel, wa_channel]

    # Target kontak mahasiswa
    daftar_mahasiswa = [
        "123140039@student.itera.ac.id",
        "081234567890",
    ]

    pesan_akademik = (
        "Pemberitahuan Praktikum PAW: Modul Pertemuan 5 OOP Python telah dibuka. "
        "Harap kumpulkan sebelum tenggat waktu Senin, 16 November 2026 pukul 23.59 WIB."
    )

    # Eksekusi broadcast secara polimorfik
    broadcast_pengumuman(daftar_saluran, pesan_akademik, daftar_mahasiswa)


if __name__ == "__main__":
    main()

