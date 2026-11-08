import math_operations as mo

from math_operations import (
    PI,
    luas_lingkaran,
    keliling_lingkaran,
    celsius_ke_fahrenheit,
    celsius_ke_kelvin,
    celsius_ke_reamur
)

def cetak_judul_seksi(judul: str) -> None:
    """
    Mencetak banner/header pemisah antar-seksi pengujian di terminal.

    Parameter:
        judul (str): Teks judul seksi pengujian.
    """
    lebar = 72
    print("\n" + "=" * lebar)
    print(f" {judul.upper():^70} ")
    print("=" * lebar)


def demonstrasikan_geometri_persegi() -> None:
    """
    Mendemonstrasikan pengujian fungsi luas dan keliling persegi
    menggunakan teknik import dengan alias (mo.luas_persegi).
    """
    cetak_judul_seksi("1. Pengujian Geometri: Persegi")
    daftar_sisi = [4.5, 8.0, 13.5]
    
    print(f"| {'Panjang Sisi (s)':^20} | {'Luas Persegi (s^2)':^22} | {'Keliling Persegi (4s)':^22} |")
    print("|" + "-" * 22 + "|" + "-" * 24 + "|" + "-" * 24 + "|")
    
    for s in daftar_sisi:
        # Pemanggilan via Cara 1 (mo.nama_fungsi)
        luas = mo.luas_persegi(s)
        keliling = mo.keliling_persegi(s)
        print(f"| {s:>18.2f} m | {luas:>19.2f} m2 | {keliling:>19.2f} m |")


def demonstrasikan_geometri_persegi_panjang() -> None:
    """
    Mendemonstrasikan pengujian fungsi luas dan keliling persegi panjang
    menggunakan modul 'mo'.
    """
    cetak_judul_seksi("2. Pengujian Geometri: Persegi Panjang (Rectangle)")
    daftar_dimensi = [
        (7.0, 3.5),
        (14.0, 5.5),
        (22.5, 9.0)
    ]
    
    print(f"| {'Panjang (p)':^14} | {'Lebar (l)':^14} | {'Luas (p x l)':^17} | {'Keliling 2(p+l)':^17} |")
    print("|" + "-" * 16 + "|" + "-" * 16 + "|" + "-" * 19 + "|" + "-" * 19 + "|")
    
    for p, l in daftar_dimensi:
        luas = mo.luas_persegi_panjang(p, l)
        keliling = mo.keliling_persegi_panjang(p, l)
        print(f"| {p:>12.2f} m | {l:>12.2f} m | {luas:>14.2f} m2 | {keliling:>14.2f} m |")


def demonstrasikan_geometri_lingkaran() -> None:
    """
    Mendemonstrasikan pengujian luas dan keliling lingkaran serta konstanta PI
    menggunakan fungsi yang diimpor secara spesifik (direct import).
    """
    cetak_judul_seksi("3. Pengujian Geometri: Lingkaran (Circle)")
    print(f"[*] Menggunakan Nilai Konstanta PI Langsung: {PI:.8f}")
    print("-" * 72)
    
    daftar_jari_jari = [4.0, 8.5, 15.0, 22.0]
    
    print(f"| {'Jari-Jari (r)':^18} | {'Luas (PI x r^2)':^24} | {'Keliling (2 x PI x r)':^22} |")
    print("|" + "-" * 20 + "|" + "-" * 26 + "|" + "-" * 24 + "|")
    
    for r in daftar_jari_jari:
        # Pemanggilan via Cara 2 (fungsi diimpor langsung tanpa prefix)
        luas = luas_lingkaran(r)
        keliling = keliling_lingkaran(r)
        print(f"| {r:>16.2f} m | {luas:>21.2f} m2 | {keliling:>19.2f} m |")


def demonstrasikan_geometri_segitiga() -> None:
    """
    Mendemonstrasikan pengujian perhitungan luas dan keliling segitiga.
    """
    cetak_judul_seksi("4. Pengujian Geometri Tambahan: Segitiga (Triangle)")
    contoh_segitiga = [
        {"alas": 8.0, "tinggi": 15.0, "sisi_a": 8.0, "sisi_b": 15.0, "sisi_c": 17.0},
        {"alas": 7.0, "tinggi": 24.0, "sisi_a": 7.0, "sisi_b": 24.0, "sisi_c": 25.0},
    ]
    
    for idx, tri in enumerate(contoh_segitiga, start=1):
        luas = mo.luas_segitiga(tri["alas"], tri["tinggi"])
        keliling = mo.keliling_segitiga(tri["sisi_a"], tri["sisi_b"], tri["sisi_c"])
        print(f"  Kasus #{idx}: Alas={tri['alas']} m, Tinggi={tri['tinggi']} m, Sisi=({tri['sisi_a']}, {tri['sisi_b']}, {tri['sisi_c']})")
        print(f"           -> Luas Segitiga     : {luas:.2f} m2")
        print(f"           -> Keliling Segitiga : {keliling:.2f} m\n")


def demonstrasikan_konversi_suhu() -> None:
    """
    Mendemonstrasikan pengujian fungsi konversi suhu dari Celsius
    ke Fahrenheit, Kelvin, dan Reamur.
    """
    cetak_judul_seksi("5. Pengujian Konversi Temperatur Suhu")
    
    sampel_celsius = [
        (-25.0, "Suhu Freezer Pembeku"),
        (18.0, "Suhu Sejuk Ruangan AC"),
        (29.5, "Suhu Rata-rata Tropis"),
        (39.0, "Suhu Tubuh Saat Demam"),
        (85.0, "Suhu Air Seduhan Kopi"),
    ]
    
    print(f"| {'Celsius':^10} | {'Fahrenheit':^13} | {'Kelvin':^13} | {'Reamur':^11} | {'Kondisi Fenomena':<22} |")
    print("|" + "-" * 12 + "|" + "-" * 15 + "|" + "-" * 15 + "|" + "-" * 13 + "|" + "-" * 24 + "|")
    
    for c, label in sampel_celsius:
        # Gabungan Cara 1 dan Cara 2
        f = celsius_ke_fahrenheit(c)
        k = celsius_ke_kelvin(c)
        r = celsius_ke_reamur(c)
        print(f"| {c:>8.1f} C | {f:>10.2f} F | {k:>10.2f} K | {r:>8.2f} R | {label:<22} |")


def demonstrasikan_error_handling() -> None:
    """
    Mendemonstrasikan penanganan error (exception handling) terhadap input
    nilai parameter yang tidak valid (angka negatif / di bawah nol mutlak).
    """
    cetak_judul_seksi("6. Pengujian Robustness: Pencegahan Nilai Negatif")
    
    print("[*] Menguji validasi sisi negatif pada luas_persegi(-4.0):")
    try:
        mo.luas_persegi(-4.0)
    except ValueError as e:
        print(f"    [SUKSES DITANGANI] ValueError tertangkap: {e}")
        
    print("[*] Menguji validasi jari-jari negatif pada luas_lingkaran(-12.0):")
    try:
        luas_lingkaran(-12.0)
    except ValueError as e:
        print(f"    [SUKSES DITANGANI] ValueError tertangkap: {e}")

    print("[*] Menguji suhu di bawah nol mutlak pada celsius_ke_kelvin(-290.0):")
    try:
        celsius_ke_kelvin(-290.0)
    except ValueError as e:
        print(f"    [SUKSES DITANGANI] ValueError tertangkap: {e}")


def main() -> None:
    """
    Fungsi eksekusi utama pengujian modul 'math_operations': menjalankan seluruh fungsi
    demonstrasi geometri dan konversi suhu serta pengujian error handling.
    """
    print(" PRAKTIKUM PEMROGRAMAN WEB - PERTEMUAN 4       ")
    print(" Nama : Muhammad Dzaky")
    print(" NIM : 123140039")
    print(" Kelas : RA ")
    print(" Teknik Impor yang Digunakan:")
    print("   1. 'import math_operations as mo'         (Aliased Module Import)")
    print("   2. 'from math_operations import PI, ...'  (Selective Function Import)")
    
    # Jalankan seluruh rangkaian demonstrasi
    demonstrasikan_geometri_persegi()
    demonstrasikan_geometri_persegi_panjang()
    demonstrasikan_geometri_lingkaran()
    demonstrasikan_geometri_segitiga()
    demonstrasikan_konversi_suhu()
    demonstrasikan_error_handling()
    
    print("\n" + "=" * 72)
    print(" [SELESAI] Seluruh fungsi modul math_operations telah berhasil diuji! ")
    print("=" * 72 + "\n")


if __name__ == "__main__":
    main()
