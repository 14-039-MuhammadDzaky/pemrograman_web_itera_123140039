"""
latihan_01_kasir.py
Praktikum Pemrograman Web - Pertemuan 5
Materi: Latihan 1 - Pemodelan Entitas Sistem Kasir Toko Online

Deskripsi Tugas:
- Mengidentifikasi entitas nyata untuk toko online (Produk, Keranjang, dan Pengguna).
- Mendefinisikan minimal 3 atribut data dan 2 metode perilaku untuk tiap entitas.
- Mengimplementasikan pemodelan entitas tersebut ke dalam class Python yang interaktif.
"""

from typing import List, Dict


# ==============================================================================
# 1. ENTITAS PRODUK (PRODUCT)
# ==============================================================================
# Atribut Data:
#   1. id_produk (str)    : Kode pengenal unik produk (SKU).
#   2. nama (str)         : Nama merek / barang.
#   3. harga (float)      : Harga satuan per unit barang.
#   4. stok (int)         : Jumlah stok persediaan di gudang.
# Metode Perilaku:
#   1. kurangi_stok(qty)  : Mengurangi stok saat barang dibeli, dengan validasi ketersediaan.
#   2. tambah_stok(qty)   : Menambah persediaan barang masuk.
# ==============================================================================

class Produk:
    """Class representasi barang/produk jualan di toko online."""

    def __init__(self, id_produk: str, nama: str, harga: float, stok: int) -> None:
        self.id_produk: str = id_produk
        self.nama: str = nama
        self.harga: float = float(harga)
        self.stok: int = max(0, stok)

    def kurangi_stok(self, qty: int) -> bool:
        """Mengurangi stok dengan validasi jumlah mencukupi."""
        if qty <= 0:
            print("[Produk] Jumlah pengurangan harus positif!")
            return False
        if qty > self.stok:
            print(f"[Produk] Stok '{self.nama}' tidak mencukupi (Tersedia: {self.stok}, Diminta: {qty}).")
            return False

        self.stok -= qty
        return True

    def tambah_stok(self, qty: int) -> None:
        """Menambahkan kuantitas stok baru."""
        if qty > 0:
            self.stok += qty
            print(f"[Produk] Stok '{self.nama}' bertambah +{qty}. Total stok: {self.stok}")

    def __str__(self) -> str:
        return f"[{self.id_produk}] {self.nama:<20} - Rp {self.harga:>10,.2f} (Stok: {self.stok})"


# ==============================================================================
# 2. ENTITAS KERANJANG (SHOPPING CART)
# ==============================================================================
# Atribut Data:
#   1. id_keranjang (str)      : Identifier sesi keranjang.
#   2. daftar_item (dict)      : Koleksi item {Produk: kuantitas}.
#   3. diskon_persen (float)   : Potongan promo toko.
# Metode Perilaku:
#   1. tambah_item(produk, qty): Memasukkan barang ke keranjang belanja.
#   2. hitung_total_belanja()  : Menghitung total harga belanjaan setelah diskon.
#   3. kosongkan_keranjang()   : Mengosongkan keranjang belanja setelah checkout.
# ==============================================================================

class Keranjang:
    """Class keranjang belanja yang menampung pesanan sementara pelanggan."""

    def __init__(self, id_keranjang: str) -> None:
        self.id_keranjang: str = id_keranjang
        self.daftar_item: Dict[Produk, int] = {}
        self.diskon_persen: float = 0.0

    def tambah_item(self, produk: Produk, qty: int = 1) -> bool:
        """Menambahkan item ke dalam keranjang."""
        if qty <= 0:
            print("[Keranjang] Kuantitas pembelian harus lebih dari 0!")
            return False
        if produk.stok < qty:
            print(f"[Keranjang] Stok '{produk.nama}' tidak mencukupi!")
            return False

        self.daftar_item[produk] = self.daftar_item.get(produk, 0) + qty
        print(f"[Keranjang] Ditambahkan: {qty}x {produk.nama}")
        return True

    def hitung_total_belanja(self) -> float:
        """Menghitung total subtotal dikurangi diskon promo."""
        subtotal = sum(p.harga * qty for p, qty in self.daftar_item.items())
        potongan = subtotal * (self.diskon_persen / 100.0)
        return subtotal - potongan

    def ringkasan_belanja(self) -> None:
        """Menampilkan rincian item dalam keranjang."""
        print(f"\n--- Rincian Keranjang ({self.id_keranjang}) ---")
        if not self.daftar_item:
            print("Keranjang masih kosong.")
            return

        for p, qty in self.daftar_item.items():
            sub = p.harga * qty
            print(f" - {p.nama:<20} x{qty} = Rp {sub:>10,.2f}")
        print(f"Diskon Terpasang : {self.diskon_persen}%")
        print(f"Total Bayar      : Rp {self.hitung_total_belanja():>10,.2f}")


# ==============================================================================
# 3. ENTITAS PENGGUNA / PELANGGAN (USER)
# ==============================================================================
# Atribut Data:
#   1. id_user (str)       : Identitas unik pengguna.
#   2. nama (str)          : Nama lengkap pelanggan.
#   3. saldo_dompet (float): Saldo akun pengguna untuk transaksi.
#   4. keranjang (Keranjang): Objek keranjang milik pengguna.
# Metode Perilaku:
#   1. top_up_saldo(nominal): Menambah saldo dompet pengguna.
#   2. checkout()          : Melakukan pembayaran keranjang dan pemotongan stok.
# ==============================================================================

class Pengguna:
    """Class entitas pengguna/pelanggan toko online."""

    def __init__(self, id_user: str, nama: str, saldo_awal: float = 0.0) -> None:
        self.id_user: str = id_user
        self.nama: str = nama
        self.saldo_dompet: float = float(saldo_awal)
        self.keranjang: Keranjang = Keranjang(f"CART-{id_user}")

    def top_up_saldo(self, nominal: float) -> None:
        """Mengisi saldo dompet akun."""
        if nominal > 0:
            self.saldo_dompet += nominal
            print(f"[{self.nama}] Top up Rp {nominal:,.2f} sukses! Saldo sekarang: Rp {self.saldo_dompet:,.2f}")

    def checkout(self) -> bool:
        """Melakukan validasi pembayaran, pemotongan stok, dan pemotongan saldo."""
        total = self.keranjang.hitung_total_belanja()
        if total == 0:
            print(f"[{self.nama}] Keranjang kosong! Tidak ada yang perlu dibayar.")
            return False

        if self.saldo_dompet < total:
            print(f"[{self.nama}] Saldo tidak cukup! (Saldo: Rp {self.saldo_dompet:,.2f}, Total: Rp {total:,.2f})")
            return False

        # Potong stok dari inventaris produk
        for p, qty in self.keranjang.daftar_item.items():
            p.kurangi_stok(qty)

        self.saldo_dompet -= total
        print(f"\n[Checkout Sukses] Transaksi untuk {self.nama} berhasil!")
        print(f"Terpotong: Rp {total:,.2f} | Sisa Saldo: Rp {self.saldo_dompet:,.2f}")
        self.keranjang.daftar_item.clear()
        return True


# ==============================================================================
# DEMO PROGRAM
# ==============================================================================

def main() -> None:
    print("=" * 75)
    print(" LATIHAN 1: PEMODELAN ENTITAS SISTEM KASIR TOKO ONLINE ")
    print("=" * 75)

    # 1. Instansiasi Produk
    laptop = Produk("P001", "Laptop ASUS ROG", 15_000_000.0, stok=5)
    mouse = Produk("P002", "Logitech Mouse", 250_000.0, stok=20)
    keyboard = Produk("P003", "Mechanical Keyboard", 750_000.0, stok=10)

    print("\n--- Katalog Produk Toko ---")
    print(laptop)
    print(mouse)
    print(keyboard)

    # 2. Instansiasi Pengguna
    user_dzaky = Pengguna("USR001", "Muhammad Dzaky", saldo_awal=20_000_000.0)

    # 3. Belanja Memasukkan Barang ke Keranjang
    print(f"\n--- Belanja Pelanggan: {user_dzaky.nama} ---")
    user_dzaky.keranjang.tambah_item(laptop, 1)
    user_dzaky.keranjang.tambah_item(mouse, 2)
    user_dzaky.keranjang.diskon_persen = 10.0  # Diskon 10%

    user_dzaky.keranjang.ringkasan_belanja()

    # 4. Proses Checkout
    user_dzaky.checkout()

    # 5. Cek Sisa Stok Setelah Checkout
    print("\n--- Sisa Stok Gudang Pasca Pembelian ---")
    print(laptop)
    print(mouse)
    print("=" * 75)


if __name__ == "__main__":
    main()

