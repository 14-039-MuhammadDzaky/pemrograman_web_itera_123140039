# Tugas Praktikum Pengembangan Aplikasi Web (PAW) Pertemuan 2
## Aplikasi Personal Dashboard

---

### 👤 Identitas Mahasiswa
- **Nama Lengkap** : Muhammad Dzaky
- **NIM**          : 123140039
- **Mata Kuliah/Kelas** : Pengembangan Aplikasi Web (PAW) / RA

---

### 📋 Deskripsi Aplikasi

**Personal Dashboard** adalah aplikasi web berbasis **single-page** yang berfungsi sebagai dashboard pribadi untuk mengelola jadwal kuliah mahasiswa. Aplikasi ini dibangun menggunakan **HTML**, **Tailwind CSS**, dan **Vanilla JavaScript (ES6+)** .

Aplikasi menampilkan jadwal kuliah dalam tampilan kalender mingguan (Senin–Sabtu), dilengkapi dengan formulir untuk menambah, mengedit, dan menghapus jadwal. Selain itu, terdapat widget cuaca real-time yang mengambil data dari **Open-Meteo API** untuk lokasi ITERA.

---

### ✨ Fitur-Fitur Aplikasi

1. **CRUD Jadwal Kuliah** — Pengguna dapat menambah, mengedit, dan menghapus jadwal mata kuliah melalui form interaktif.
2. **Tampilan Kalender Mingguan** — Jadwal ditampilkan dalam format kolom per hari (Senin–Sabtu) yang terurut berdasarkan jam mulai.
3. **Persistent Storage (localStorage)** — Data jadwal tersimpan secara lokal di browser sehingga tidak hilang saat halaman di-refresh.
4. **Data Default** — Saat pertama kali dibuka (atau saat data kosong), aplikasi otomatis memuat jadwal kuliah default.
5. **Widget Cuaca Real-Time** — Menampilkan informasi suhu dan kecepatan angin untuk lokasi ITERA menggunakan Open-Meteo API secara asinkron.

---

### 🚀 Daftar Fitur ES6+ yang Diimplementasikan

#### 1. `class` (OOP Classes)
Digunakan untuk membuat struktur data dan logika aplikasi secara terorganisir dengan pendekatan OOP.

| Class | Baris | Keterangan |
|-------|-------|------------|
| `CourseItem` | Baris 92–101 | Class untuk merepresentasikan satu item jadwal kuliah (id, day, start, end, title, room) |
| `DashboardApp` | Baris 103–274 | Class utama yang mengelola seluruh logika aplikasi (CRUD, rendering, weather) |

#### 2. Arrow Function (`=>`)
Digunakan sebagai callback yang lebih ringkas dan menjaga konteks `this`.

| Lokasi | Baris | Contoh Penggunaan |
|--------|-------|-------------------|
| Event listener submit | Baris 115 | `this.form.addEventListener('submit', e => this.handleSubmit(e))` |
| Event listener cancel | Baris 116 | `this.cancelBtn.addEventListener('click', () => this.resetForm())` |
| Mapping data storage | Baris 129 | `arr.map(item => new CourseItem(...))` |
| Mapping default data | Baris 153 | `defaultData.map((data, idx) => new CourseItem(...))` |
| Update course (map) | Baris 165 | `this.schedule.map(item => (item.id === updatedItem.id ? updatedItem : item))` |
| Delete course (filter) | Baris 171 | `this.schedule.filter(item => item.id !== id)` |
| Render hari (forEach) | Baris 208 | `daysOrder.forEach(day => { ... })` |
| Filter jadwal per hari | Baris 218 | `this.schedule.filter(it => it.day === day)` |
| Sort jadwal | Baris 220 | `items.sort((a, b) => a.start.localeCompare(b.start))` |
| Render item (forEach) | Baris 221 | `items.forEach(item => { ... })` |
| Event edit (forEach) | Baris 238–239 | `calendar.querySelectorAll('.edit').forEach(btn => { ... })` |
| Event delete (forEach) | Baris 241–244 | `calendar.querySelectorAll('.delete').forEach(btn => { ... })` |
| DOMContentLoaded | Baris 277 | `document.addEventListener('DOMContentLoaded', () => new DashboardApp())` |

#### 3. `const` dan `let`
Digunakan sebagai pengganti `var` untuk deklarasi variabel dengan block-scoping.

| Jenis | Baris (contoh) | Contoh Penggunaan |
|-------|----------------|-------------------|
| `const` | Baris 125 | `const raw = localStorage.getItem(this.storageKey)` |
| `const` | Baris 145 | `const defaultData = [...]` |
| `const` | Baris 179–183 | `const day = ...`, `const start = ...`, `const end = ...`, `const title = ...`, `const room = ...` |
| `const` | Baris 205 | `const calendar = document.getElementById('calendar-container')` |
| `const` | Baris 207 | `const daysOrder = ['Senin', 'Selasa', ...]` |
| `const` | Baris 222 | `const card = document.createElement('div')` |
| `const` | Baris 265–268 | `const response = ...`, `const data = ...`, `const { temperature, ... } = ...` |

#### 4. Template Literal (Backtick String ``)
Digunakan untuk menyisipkan ekspresi JavaScript ke dalam string secara dinamis.

| Baris | Contoh Penggunaan |
|-------|-------------------|
| Baris 153 | `` `id-${Date.now()}-${idx}` `` — Membuat ID unik untuk setiap item default |
| Baris 188 | `` `id-${Date.now()}` `` — Membuat ID unik untuk item baru |
| Baris 224–232 | Template HTML untuk card jadwal: `${item.title}`, `${item.start}`, `${item.end}`, `${item.room}`, `${item.id}` |
| Baris 268 | `` `⛅ ${temperature}°C, Angin ${windspeed} m/s` `` — Menampilkan info cuaca |

#### 5. Destructuring Assignment
Digunakan untuk mengekstrak properti objek ke dalam variabel terpisah secara ringkas.

| Baris | Contoh Penggunaan |
|-------|-------------------|
| Baris 267 | `const { temperature, windspeed, weathercode } = data.current_weather` |

#### 6. `async/await`
Digunakan untuk menangani operasi asinkron (fetching API) secara lebih mudah dibaca dibanding `.then()`.

| Baris | Contoh Penggunaan |
|-------|-------------------|
| Baris 263 | `async fetchWeather()` — Deklarasi method asinkron |
| Baris 265 | `const response = await fetch(...)` — Menunggu response dari API |
| Baris 266 | `const data = await response.json()` — Menunggu parsing JSON |

#### 7. Module (`type="module"`)
Digunakan untuk menjalankan script dalam mode module ES6.

| Baris | Contoh Penggunaan |
|-------|-------------------|
| Baris 90 | `<script type="module">` |

#### 8. Method Array Modern (Higher-Order Functions)
Digunakan untuk manipulasi array secara fungsional dan deklaratif.

| Method | Baris | Contoh Penggunaan |
|--------|-------|-------------------|
| `Array.map()` | Baris 129 | Mapping data dari localStorage ke objek `CourseItem` |
| `Array.map()` | Baris 153 | Mapping default data ke objek `CourseItem` |
| `Array.map()` | Baris 165 | Mengupdate item tertentu di dalam array schedule |
| `Array.filter()` | Baris 171 | Menghapus item berdasarkan ID |
| `Array.filter()` | Baris 218 | Memfilter jadwal berdasarkan hari |
| `Array.find()` | Baris 249 | Mencari item berdasarkan ID untuk proses edit |
| `Array.forEach()` | Baris 208, 221 | Iterasi untuk rendering kolom hari dan card jadwal |
| `Array.forEach()` | Baris 238, 241 | Iterasi untuk attach event listener pada tombol edit & hapus |

---