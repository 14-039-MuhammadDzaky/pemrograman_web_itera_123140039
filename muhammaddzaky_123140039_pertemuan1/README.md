# Tugas Praktikum Pengembangan Aplikasi Web (PAW) Pertemuan 1
## Aplikasi Kasir & Keranjang Belanja Sederhana (Mini POS Kantin ITERA)

---

### 👤 Identitas Mahasiswa
- **Nama Lengkap** : Muhammad Dzaky
- **NIM**          : 123140039
- **Mata Kuliah/Kelas**        : Pengembangan Aplikasi Web (PAW)
/ RA

---

## 📌 Deskripsi Proyek
Aplikasi **Kantin ITERA Mini POS** merupakan aplikasi berbasis web satu halaman (*single page web application*) yang dirancang khusus untuk memfasilitasi kebutuhan kasir kantin maupun toko kampus. 

Aplikasi ini mengintegrasikan tiga pilar kompetensi utama praktikum:
1. **Validasi Form Tingkat Klien (*Form Validation & Error Handling*)**: Memastikan integritas data input barang belanja sebelum diproses ke keranjang.
2. **Kalkulator Otomatis (*Automatic Real-time Calculation*)**: Melakukan perhitungan matematis langsung terhadap subtotal barang, akumulasi total belanja, kalkulasi diskon otomatis/kupon promo, serta kalkulasi kembalian uang pelanggan.
3. **Penyimpanan Persisten Berbasis LocalStorage (*Persistent State Management*)**: Mengamankan data keranjang belanja menggunakan Web Storage API (`localStorage`) sehingga data tidak hilang saat halaman di-refresh.

---

## 📂 Struktur Direktori

```text
muhammaddzaky_123140039_pertemuan1/
├── index.html       # Struktur HTML antarmuka aplikasi kasir utama
├── style.css        # Berkas styling CSS responsif dengan tema Sage Green & Warm Oat Cream
├── script.js        # Logika pemrograman JavaScript (validasi, kalkulator, localStorage)
├── README.md        # Dokumentasi lengkap proyek tugas
├── Screenshot/      # Direktori arsip tangkapan layar antarmuka
└── modul/           # Folder kumpulan materi latihan modul praktikum
    ├── latihan1.html # Latihan 1: Dasar JS & Kontrol Alur (Inline Script)
    ├── latihan2.html # Latihan 2: Perulangan & Event Handler (Inline Script)
    ├── latihan3.html # Latihan 3: Array Objek & CRUD Mahasiswa (Inline Script)
    └── latihan4.html # Latihan 4: Form Validation & API (Inline Script)
```

---

## 💻 Panduan Menjalankan Aplikasi
1. Buka berkas `index.html` langsung pada browser web modern (Google Chrome, Mozilla Firefox, Microsoft Edge, atau Safari) dengan klik dua kali.
2. Atau jalankan menggunakan ekstensi **Live Server** di Visual Studio Code.
3. Aplikasi akan langsung memuat tampilan kasir Mini POS secara penuh tanpa memerlukan dependensi eksternal tambahan.

---