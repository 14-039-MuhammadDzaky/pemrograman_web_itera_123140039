from typing import List, Dict, Any, Tuple

# 1. DEFINISI DATASET MAHASISWA (MINIMAL 5 DATA MAHASISWA)
DAFTAR_MAHASISWA: List[Dict[str, Any]] = [
    {
        "nama": "Muhammad Dzaky",
        "nim": "123140039",
        "nilai_uts": 90.0,
        "nilai_uas": 90.0,
        "nilai_tugas": 90.0,
    },
    {
        "nama": "Marcus",
        "nim": "123140123",
        "nilai_uts": 70.0,
        "nilai_uas": 77.0,
        "nilai_tugas": 74.0,
    },
    {
        "nama": "Arhan Pratama",
        "nim": "123140200",
        "nilai_uts": 63.0,
        "nilai_uas": 66.0,
        "nilai_tugas": 65.0,
    },
    {
        "nama": "Ragnar",
        "nim": "120140099",
        "nilai_uts": 54.0,
        "nilai_uas": 58.0,
        "nilai_tugas": 55.0,
    },
    {
        "nama": "Putri",
        "nim": "124140078",
        "nilai_uts": 43.0,
        "nilai_uas": 47.0,
        "nilai_tugas": 47.0,
    },
    {
        "nama": "Lutfia",
        "nim": "122140030",
        "nilai_uts": 89.0,
        "nilai_uas": 84.0,
        "nilai_tugas": 84.0,
    },
]


# ==============================================================================
# 2. FUNGSI LOGIKA PERHITUNGAN & KLASIFIKASI
# ==============================================================================
def hitung_nilai_akhir(uts: float, uas: float, tugas: float) -> float:
    """
    Menghitung nilai akhir mahasiswa berdasarkan pembobotan komponen nilai:
    UTS (30%), UAS (40%), dan Tugas (30%).

    Parameter:
        uts (float): Nilai Ujian Tengah Semester.
        uas (float): Nilai Ujian Akhir Semester.
        tugas (float): Nilai Tugas.

    Mengembalikan:
        float: Nilai akhir terbobot.
    """
    bobot_uts = 0.30
    bobot_uas = 0.40
    bobot_tugas = 0.30
    return (bobot_uts * uts) + (bobot_uas * uas) + (bobot_tugas * tugas)


def tentukan_grade(nilai_akhir: float) -> Tuple[str, str]:
    """
    Menentukan huruf mutu (grade) dan status kelulusan berdasarkan nilai akhir.

    Parameter:
        nilai_akhir (float): Nilai akhir mahasiswa.

    Mengembalikan:
        Tuple[str, str]: Pasangan (grade, status kelulusan), misalnya ("A", "Lulus (Sangat Memuaskan)").
    """
    if nilai_akhir >= 80.0:
        return "A", "Lulus (Sangat Memuaskan)"
    elif nilai_akhir >= 70.0:
        return "B", "Lulus (Memuaskan)"
    elif nilai_akhir >= 60.0:
        return "C", "Lulus (Cukup)"
    elif nilai_akhir >= 50.0:
        return "D", "Lulus Bersyarat (Kurang)"
    else:
        return "E", "Tidak Lulus (Gagal)"


def proses_data_mahasiswa(daftar_raw: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Memproses daftar data mentah mahasiswa dengan menghitung nilai akhir,
    grade, dan status kelulusan untuk setiap mahasiswa.

    Parameter:
        daftar_raw (List[Dict[str, Any]]): Daftar kamus berisi nama, nim, dan nilai mentah.

    Mengembalikan:
        List[Dict[str, Any]]: Daftar data mahasiswa yang telah dilengkapi nilai akhir, grade, dan status.
    """
    data_terproses: List[Dict[str, Any]] = []
    
    for mhs in daftar_raw:
        akhir = hitung_nilai_akhir(mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"])
        grade, status = tentukan_grade(akhir)
        
        entri_lengkap = {
            "nama": mhs["nama"],
            "nim": mhs["nim"],
            "nilai_uts": mhs["nilai_uts"],
            "nilai_uas": mhs["nilai_uas"],
            "nilai_tugas": mhs["nilai_tugas"],
            "nilai_akhir": akhir,
            "grade": grade,
            "status": status,
        }
        data_terproses.append(entri_lengkap)
        
    return data_terproses


def cari_nilai_ekstrem(daftar_data: List[Dict[str, Any]]) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Mencari mahasiswa dengan nilai akhir tertinggi dan terendah dari sekumpulan data.

    Parameter:
        daftar_data (List[Dict[str, Any]]): Daftar data mahasiswa yang sudah diproses.

    Mengembalikan:
        Tuple[Dict[str, Any], Dict[str, Any]]: Pasangan (mahasiswa_tertinggi, mahasiswa_terendah).
    """
    mahasiswa_tertinggi = max(daftar_data, key=lambda m: m["nilai_akhir"])
    mahasiswa_terendah = min(daftar_data, key=lambda m: m["nilai_akhir"])
    return mahasiswa_tertinggi, mahasiswa_terendah


# ==============================================================================
# 3. FUNGSI PENYAJIAN TABEL DAN STATISTIK
# ==============================================================================
def cetak_tabel_mahasiswa(daftar_data: List[Dict[str, Any]]) -> None:
    """
    Mencetak tabel rekapitulasi nilai akademik seluruh mahasiswa secara rapi dan terformat.

    Parameter:
        daftar_data (List[Dict[str, Any]]): Daftar data mahasiswa yang telah terproses.
    """

    print("\n" + "=" * 90)
    print("                     DAFTAR REKAPITULASI NILAI AKADEMIK MAHASISWA                 ")
    print("                      PROGRAM STUDI TEKNIK INFORMATIKA                    ")
    print("=" * 90)
    
    # Header Tabel
    print(f"| {'No':^3} | {'NIM':^11} | {'Nama Mahasiswa':<22} | {'UTS':^6} | {'UAS':^6} | {'Tugas':^6} | {'Akhir':^7} | {'Grade':^5} |")
    print("|" + "-" * 5 + "|" + "-" * 13 + "|" + "-" * 24 + "|" + "-" * 8 + "|" + "-" * 8 + "|" + "-" * 8 + "|" + "-" * 9 + "|" + "-" * 7 + "|")
    
    # Isi Baris Data
    for no, m in enumerate(daftar_data, start=1):
        print(
            f"| {no:^3} "
            f"| {m['nim']:^11} "
            f"| {m['nama']:<22} "
            f"| {m['nilai_uts']:>6.1f} "
            f"| {m['nilai_uas']:>6.1f} "
            f"| {m['nilai_tugas']:>6.1f} "
            f"| {m['nilai_akhir']:>7.2f} "
            f"|   {m['grade']:^3} |"
        )
        
    print("=" * 90)


def cetak_sorotan_ekstrem(tertinggi: Dict[str, Any], terendah: Dict[str, Any]) -> None:
    """
    Menampilkan informasi mendalam mahasiswa yang meraih nilai akhir tertinggi dan terendah.

    Parameter:
        tertinggi (Dict[str, Any]): Data mahasiswa dengan nilai akhir tertinggi.
        terendah (Dict[str, Any]): Data mahasiswa dengan nilai akhir terendah.
    """
    print("\n--- INFORMASI CAPAIAN EKSTREM NILAI AKHIR ---")
    
    print("\n[+] MAHASISWA DENGAN NILAI AKHIR TERTINGGI:")
    print(f"    - Nama Lengkap : {tertinggi['nama']}")
    print(f"    - NIM          : {tertinggi['nim']}")
    print(f"    - Nilai Akhir  : {tertinggi['nilai_akhir']:.2f}")
    print(f"    - Grade        : {tertinggi['grade']} ({tertinggi['status']})")
    print(f"    - Rincian      : UTS={tertinggi['nilai_uts']}, UAS={tertinggi['nilai_uas']}, Tugas={tertinggi['nilai_tugas']}")
    
    print("\n[-] MAHASISWA DENGAN NILAI AKHIR TERENDAH:")
    print(f"    - Nama Lengkap : {terendah['nama']}")
    print(f"    - NIM          : {terendah['nim']}")
    print(f"    - Nilai Akhir  : {terendah['nilai_akhir']:.2f}")
    print(f"    - Grade        : {terendah['grade']} ({terendah['status']})")
    print(f"    - Rincian      : UTS={terendah['nilai_uts']}, UAS={terendah['nilai_uas']}, Tugas={terendah['nilai_tugas']}")


def cetak_ringkasan_statistik(daftar_data: List[Dict[str, Any]]) -> None:
    """
    Menghitung dan mencetak ringkasan statistik kelas: jumlah mahasiswa,
    rata-rata nilai akhir, distribusi frekuensi grade, dan persentase kelulusan.

    Parameter:
        daftar_data (List[Dict[str, Any]]): Daftar data mahasiswa yang telah terproses.
    """
    total_mhs = len(daftar_data)
    semua_nilai = [m["nilai_akhir"] for m in daftar_data]
    rata_rata = sum(semua_nilai) / total_mhs if total_mhs > 0 else 0.0
    
    distribusi_grade: Dict[str, int] = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
    for m in daftar_data:
        distribusi_grade[m["grade"]] += 1
        
    jumlah_lulus = sum(1 for m in daftar_data if m["grade"] in ("A", "B", "C", "D"))
    persentase_kelulusan = (jumlah_lulus / total_mhs) * 100 if total_mhs > 0 else 0.0
    
    print("\n" + "-" * 62)
    print("                    STATISTIK KELAS                      ")
    print("-" * 62)
    print(f" Jumlah Mahasiswa Terdaftar : {total_mhs} orang")
    print(f" Rata-rata Nilai Akhir      : {rata_rata:.2f}")
    print(f" Distribusi Perolehan Grade : " + ", ".join([f"Grade {k}: {v}" for k, v in distribusi_grade.items()]))
    print(f" Tingkat Kelulusan (A-D)    : {persentase_kelulusan:.1f}% ({jumlah_lulus}/{total_mhs} mahasiswa)")
    print("-" * 62)


# ==============================================================================
# 4. FUNGSI EKSEKUSI UTAMA (ENTRY POINT)
# ==============================================================================
def main() -> None:
    """
    Fungsi eksekusi utama pengolahan nilai mahasiswa: mengorkestrasi
    kalkulasi nilai, penampilan tabel, sorotan nilai ekstrem, dan statistik kelas.
    """

    # 1. Proses kalkulasi nilai akhir dan grade
    data_hasil = proses_data_mahasiswa(DAFTAR_MAHASISWA)
    
    # 2. Tampilkan tabel komprehensif
    cetak_tabel_mahasiswa(data_hasil)
    
    # 3. Cari dan tampilkan nilai tertinggi serta terendah
    tertinggi, terendah = cari_nilai_ekstrem(data_hasil)
    cetak_sorotan_ekstrem(tertinggi, terendah)
    
    # 4. Tampilkan wawasan statistik kelas
    cetak_ringkasan_statistik(data_hasil)


if __name__ == "__main__":
    main()
