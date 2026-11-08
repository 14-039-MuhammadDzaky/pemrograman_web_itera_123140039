def hitung_bmi(berat: float, tinggi: float) -> float:
    """
    Menghitung indeks massa tubuh (Body Mass Index / BMI).

    Parameter:
        berat (float): Berat badan dalam satuan kilogram (kg).
        tinggi (float): Tinggi badan dalam satuan meter (m).

    Mengembalikan:
        float: Nilai BMI hasil kalkulasi (berat / (tinggi^2)).
    """
    return berat / (tinggi * tinggi)


def tentukan_kategori_bmi(bmi: float) -> str:
    """
    Menentukan kategori status berat badan berdasarkan nilai BMI menurut standar WHO.

    Parameter:
        bmi (float): Nilai BMI yang telah dihitung.

    Mengembalikan:
        str: Kategori berat badan ("Berat badan kurang", "Berat badan normal",
             "Berat badan berlebih", atau "Obesitas").
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif 18.5 <= bmi < 25:
        return "Berat badan normal"
    elif 25 <= bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


def main() -> None:
    """
    Fungsi utama (entry point) untuk menjalankan program kalkulator BMI.
    Menerima input berat dan tinggi dari pengguna, melakukan validasi,
    menghitung BMI, dan menampilkan ringkasan hasil ke terminal.
    """
    print("=" * 50)
    print("      PROGRAM PENGHITUNG BMI SEDERHANA           ")
    print("=" * 50)

    try:
        # Input berat badan dan tinggi badan dari pengguna
        berat = float(input("Masukkan berat badan (kg, contoh: 65.5) : "))
        tinggi = float(input("Masukkan tinggi badan (m, contoh: 1.70)  : "))

        if berat <= 0 or tinggi <= 0:
            print("\n[Error] Berat dan tinggi badan harus bernilai positif lebih dari 0!")
            return

        # Hitung BMI
        bmi = hitung_bmi(berat, tinggi)

        # Tentukan Kategori BMI
        kategori = tentukan_kategori_bmi(bmi)

        # Cetak hasil diformat 2 angka desimal menggunakan f-string
        print("\n" + "=" * 50)
        print("             HASIL PERHITUNGAN BMI                ")
        print("=" * 50)
        print(f"Berat Badan       : {berat:.2f} kg")
        print(f"Tinggi Badan      : {tinggi:.2f} m")
        print(f"Nilai BMI         : {bmi:.2f}")
        print(f"Kategori Status   : {kategori}")
        print("=" * 50)

    except ValueError:
        print("\n[Error] Masukan tidak valid! Harap masukkan angka numerik.")
    except (EOFError, KeyboardInterrupt):
        print("\n[Batal] Proses dibatalkan oleh pengguna.")


if __name__ == "__main__":
    main()

