import math
PI: float = 3.141592653589793
EULER: float = 2.718281828459045

# 1. FUNGSI GEOMETRI: PERSEGI (SQUARE)
def luas_persegi(sisi: float) -> float:
    """
    Menghitung luas persegi berdasarkan panjang sisinya.

    Parameter:
        sisi (float): Panjang sisi persegi (harus > 0).

    Mengembalikan:
        float: Luas persegi (sisi * sisi).

    Raises:
        ValueError: Jika sisi <= 0.
    """
    if sisi <= 0:
        raise ValueError("Panjang sisi persegi harus bernilai lebih besar dari 0.")
    return sisi * sisi


def keliling_persegi(sisi: float) -> float:
    """
    Menghitung keliling persegi berdasarkan panjang sisinya.

    Parameter:
        sisi (float): Panjang sisi persegi (harus > 0).

    Mengembalikan:
        float: Keliling persegi (4 * sisi).

    Raises:
        ValueError: Jika sisi <= 0.
    """
    if sisi <= 0:
        raise ValueError("Panjang sisi persegi harus bernilai lebih besar dari 0.")
    return 4.0 * sisi


# 2. FUNGSI GEOMETRI: PERSEGI PANJANG (RECTANGLE)
def luas_persegi_panjang(panjang: float, lebar: float) -> float:
    """
    Menghitung luas persegi panjang berdasarkan panjang dan lebarnya.

    Parameter:
        panjang (float): Panjang persegi panjang (harus > 0).
        lebar (float): Lebar persegi panjang (harus > 0).

    Mengembalikan:
        float: Luas persegi panjang (panjang * lebar).

    Raises:
        ValueError: Jika panjang atau lebar <= 0.
    """
    if panjang <= 0 or lebar <= 0:
        raise ValueError("Panjang dan lebar persegi panjang harus bernilai lebih besar dari 0.")
    return panjang * lebar


def keliling_persegi_panjang(panjang: float, lebar: float) -> float:
    """
    Menghitung keliling persegi panjang berdasarkan panjang dan lebarnya.

    Parameter:
        panjang (float): Panjang persegi panjang (harus > 0).
        lebar (float): Lebar persegi panjang (harus > 0).

    Mengembalikan:
        float: Keliling persegi panjang (2 * (panjang + lebar)).

    Raises:
        ValueError: Jika panjang atau lebar <= 0.
    """
    if panjang <= 0 or lebar <= 0:
        raise ValueError("Panjang dan lebar persegi panjang harus bernilai lebih besar dari 0.")
    return 2.0 * (panjang + lebar)

# 3. FUNGSI GEOMETRI: LINGKARAN (CIRCLE)

def luas_lingkaran(jari_jari: float) -> float:
    """
    Menghitung luas lingkaran berdasarkan jari-jarinya.

    Parameter:
        jari_jari (float): Jari-jari lingkaran (harus > 0).

    Mengembalikan:
        float: Luas lingkaran (PI * r^2).

    Raises:
        ValueError: Jika jari_jari <= 0.
    """
    if jari_jari <= 0:
        raise ValueError("Jari-jari lingkaran harus bernilai lebih besar dari 0.")
    return PI * (jari_jari ** 2)


def keliling_lingkaran(jari_jari: float) -> float:
    """
    Menghitung keliling lingkaran berdasarkan jari-jarinya.

    Parameter:
        jari_jari (float): Jari-jari lingkaran (harus > 0).

    Mengembalikan:
        float: Keliling lingkaran (2 * PI * r).

    Raises:
        ValueError: Jika jari_jari <= 0.
    """
    if jari_jari <= 0:
        raise ValueError("Jari-jari lingkaran harus bernilai lebih besar dari 0.")
    return 2.0 * PI * jari_jari


# 4. FUNGSI GEOMETRI TAMBAHAN: SEGITIGA (TRIANGLE)
def luas_segitiga(alas: float, tinggi: float) -> float:
    """
    Menghitung luas segitiga berdasarkan alas dan tingginya.

    Parameter:
        alas (float): Alas segitiga (harus > 0).
        tinggi (float): Tinggi segitiga (harus > 0).

    Mengembalikan:
        float: Luas segitiga (0.5 * alas * tinggi).

    Raises:
        ValueError: Jika alas atau tinggi <= 0.
    """
    if alas <= 0 or tinggi <= 0:
        raise ValueError("Alas dan tinggi segitiga harus bernilai lebih besar dari 0.")
    return 0.5 * alas * tinggi


def keliling_segitiga(sisi_a: float, sisi_b: float, sisi_c: float) -> float:
    """
    Menghitung keliling segitiga berdasarkan ketiga panjang sisinya.

    Parameter:
        sisi_a (float): Panjang sisi pertama (harus > 0).
        sisi_b (float): Panjang sisi kedua (harus > 0).
        sisi_c (float): Panjang sisi ketiga (harus > 0).

    Mengembalikan:
        float: Keliling segitiga (sisi_a + sisi_b + sisi_c).

    Raises:
        ValueError: Jika salah satu sisi <= 0.
    """
    if sisi_a <= 0 or sisi_b <= 0 or sisi_c <= 0:
        raise ValueError("Seluruh sisi segitiga harus bernilai lebih besar dari 0.")
    return sisi_a + sisi_b + sisi_c

# 5. FUNGSI KONVERSI TEMPERATUR SUHU

def celsius_ke_fahrenheit(celsius: float) -> float:
    """
    Mengonversi temperatur dari derajat Celsius ke Fahrenheit.

    Parameter:
        celsius (float): Suhu dalam Celsius.

    Mengembalikan:
        float: Suhu dalam Fahrenheit ((celsius * 9/5) + 32).
    """
    return (celsius * 9.0 / 5.0) + 32.0


def celsius_ke_kelvin(celsius: float) -> float:
    """
    Mengonversi temperatur dari derajat Celsius ke Kelvin.

    Parameter:
        celsius (float): Suhu dalam Celsius (harus >= -273.15).

    Mengembalikan:
        float: Suhu dalam Kelvin (celsius + 273.15).

    Raises:
        ValueError: Jika suhu di bawah nol mutlak (-273.15 Celsius).
    """
    if celsius < -273.15:
        raise ValueError("Suhu tidak boleh lebih rendah dari nol mutlak (-273.15 Celsius).")
    return celsius + 273.15


def celsius_ke_reamur(celsius: float) -> float:
    """
    Mengonversi temperatur dari derajat Celsius ke Reamur.

    Parameter:
        celsius (float): Suhu dalam Celsius.

    Mengembalikan:
        float: Suhu dalam Reamur (celsius * 4/5).
    """
    return celsius * 4.0 / 5.0


def fahrenheit_ke_celsius(fahrenheit: float) -> float:
    """
    Mengonversi temperatur dari derajat Fahrenheit ke Celsius.

    Parameter:
        fahrenheit (float): Suhu dalam Fahrenheit.

    Mengembalikan:
        float: Suhu dalam Celsius ((fahrenheit - 32) * 5/9).
    """
    return (fahrenheit - 32.0) * 5.0 / 9.0


def kelvin_ke_celsius(kelvin: float) -> float:
    """
    Mengonversi temperatur dari Kelvin ke derajat Celsius.

    Parameter:
        kelvin (float): Suhu dalam Kelvin (harus >= 0).

    Mengembalikan:
        float: Suhu dalam Celsius (kelvin - 273.15).

    Raises:
        ValueError: Jika Kelvin < 0 (di bawah nol mutlak).
    """
    if kelvin < 0:
        raise ValueError("Suhu dalam Kelvin tidak boleh bernilai negatif (di bawah nol mutlak).")
    return kelvin - 273.15


# SELF-TESTING IDIOM
if __name__ == "__main__":
    print("=" * 60)
    print(" |TESTING MANDIRI INTERNAL MODUL: math_operations.py| ")
    print("=" * 60)
    print(f"Konstanta PI             : {PI}")
    print(f"Luas Persegi (s=5)       : {luas_persegi(5.0)}")
    print(f"Keliling Persegi (s=5)   : {keliling_persegi(5.0)}")
    print(f"Luas Persegi Pjg (p=8, l=4): {luas_persegi_panjang(8.0, 4.0)}")
    print(f"Luas Lingkaran (r=7)     : {luas_lingkaran(7.0):.2f}")
    print(f"Keliling Lingkaran (r=7) : {keliling_lingkaran(7.0):.2f}")
    print(f"Konversi 100 C -> F      : {celsius_ke_fahrenheit(100.0):.2f} F")
    print(f"Konversi 100 C -> K      : {celsius_ke_kelvin(100.0):.2f} K")
    print(f"Konversi 100 C -> R      : {celsius_ke_reamur(100.0):.2f} R")
    print("Seluruh pengujian internal modul math_operations BERHASIL!")
    print("=" * 60)
