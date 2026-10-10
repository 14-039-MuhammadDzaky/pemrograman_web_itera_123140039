/**
 * ===================================================================
 * SCRIPT.JS - KANTIN ITERA MINI POS (APLIKASI KASIR SEDERHANA)
 * Tugas Praktikum Pengembangan Aplikasi Web (PAW) Pertemuan 1
 * 
 * Pengembang : Muhammad Dzaky
 * NIM        : 123140039
 * Kelas      : RA (Teknik Informatika)
 * Institut   : Institut Teknologi Sumatera (ITERA)
 * ===================================================================
 */

// ==========================================
// 1. STATE MANAGEMENT & INISIALISASI
// ==========================================
const STORAGE_KEY = "pos_cart_123140039";
const PROMO_CODE_KEY = "pos_promo_123140039";

// State Global Aplikasi
let cart = [];
let appliedPromo = ""; // Menyimpan kode promo aktif (misal: "HEMAT10")

// Inisialisasi saat DOM selesai dimuat
document.addEventListener("DOMContentLoaded", () => {
  // 1. Muat data persisten dari LocalStorage
  loadCartFromStorage();

  // 2. Pasang Event Listener Form Input & Validasi
  setupFormValidation();

  // 3. Pasang Event Listener Kalkulator Pembayaran & Promo
  setupCalculatorListeners();

  // 4. Pasang Event Listener Modal Struk
  setupReceiptModalListeners();

  // 5. Render Awal Keranjang & Kalkulasi
  renderCart();
  calculateTotals();
});

// ==========================================
// 2. HELPER FORMATTER MATA UANG RUPIAH
// ==========================================
/**
 * Mengubah angka menjadi format mata uang Rupiah (contoh: Rp 15.000)
 * @param {number} amount
 * @returns {string}
 */
function formatRupiah(amount) {
  const number = Number(amount) || 0;
  return new Intl.NumberFormat("id-ID", {
    style: "currency",
    currency: "IDR",
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(number);
}

// ==========================================
// 3. VALIDASI FORM INPUT BARANG
// ==========================================
function setupFormValidation() {
  const form = document.getElementById("formTambahBarang");
  const inputNama = document.getElementById("namaBarang");
  const inputHarga = document.getElementById("hargaSatuan");
  const inputQty = document.getElementById("qtyBarang");
  const btnReset = document.getElementById("btnResetForm");

  // Event realtime input untuk menghapus error saat kasir mengetik ulang
  inputNama.addEventListener("input", () => clearFieldError("namaBarang"));
  inputHarga.addEventListener("input", () => clearFieldError("hargaSatuan"));
  inputQty.addEventListener("input", () => clearFieldError("qtyBarang"));

  // Event submit form
  form.addEventListener("submit", (e) => {
    e.preventDefault();

    const namaVal = inputNama.value.trim();
    const hargaVal = parseFloat(inputHarga.value);
    const qtyVal = parseInt(inputQty.value, 10);

    let isValid = true;

    // Validasi 1: Nama Barang wajib diisi, minimal 3 karakter
    if (namaVal.length < 3) {
      showFieldError("namaBarang", "Nama barang wajib diisi (minimal 3 karakter)!");
      isValid = false;
    } else {
      clearFieldError("namaBarang");
    }

    // Validasi 2: Harga Satuan wajib angka positif minimal Rp 500
    if (isNaN(hargaVal) || hargaVal < 500) {
      showFieldError("hargaSatuan", "Harga satuan minimal Rp 500 dan harus berupa angka positif!");
      isValid = false;
    } else {
      clearFieldError("hargaSatuan");
    }

    // Validasi 3: Jumlah / Qty wajib berupa angka bulat minimal 1
    if (isNaN(qtyVal) || qtyVal < 1) {
      showFieldError("qtyBarang", "Jumlah / Qty minimal bernilai 1!");
      isValid = false;
    } else {
      clearFieldError("qtyBarang");
    }

    // Jika seluruh input lolos validasi
    if (isValid) {
      tambahItemKeKeranjang(namaVal, hargaVal, qtyVal);
      form.reset();
      inputQty.value = 1;
      inputNama.focus();
      showToast(`Barang "${namaVal}" berhasil ditambahkan ke keranjang!`, "success");
    } else {
      showToast("Gagal menambahkan barang! Periksa input bertanda merah.", "error");
    }
  });

  // Tombol reset form manual
  btnReset.addEventListener("click", () => {
    form.reset();
    inputQty.value = 1;
    clearFieldError("namaBarang");
    clearFieldError("hargaSatuan");
    clearFieldError("qtyBarang");
  });
}

/**
 * Menampilkan pesan feedback error validasi berwarna merah
 */
function showFieldError(fieldId, message) {
  const inputEl = document.getElementById(fieldId);
  const errorEl = document.getElementById(`err${capitalizeFirst(fieldId)}`);
  
  if (inputEl) inputEl.classList.add("is-invalid");
  if (errorEl) errorEl.innerText = message;
}

/**
 * Membersihkan feedback error validasi
 */
function clearFieldError(fieldId) {
  const inputEl = document.getElementById(fieldId);
  const errorEl = document.getElementById(`err${capitalizeFirst(fieldId)}`);
  
  if (inputEl) inputEl.classList.remove("is-invalid");
  if (errorEl) errorEl.innerText = "";
}

function capitalizeFirst(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

/**
 * Fitur Quick Fill (Mengisi form cepat dari tombol contoh rekomendasi)
 */
function quickFill(nama, harga, qty = 1) {
  document.getElementById("namaBarang").value = nama;
  document.getElementById("hargaSatuan").value = harga;
  document.getElementById("qtyBarang").value = qty;
  clearFieldError("namaBarang");
  clearFieldError("hargaSatuan");
  clearFieldError("qtyBarang");
  showToast(`Form diisi dengan "${nama}"`, "info");
}

// ==========================================
// 4. MANAJEMEN LIST KERANJANG & LOCALSTORAGE
// ==========================================
/**
 * Menyimpan data cart ke LocalStorage menggunakan JSON.stringify
 */
function saveCartToStorage() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(cart));
}

/**
 * Memuat data cart dari LocalStorage menggunakan JSON.parse
 */
function loadCartFromStorage() {
  const savedData = localStorage.getItem(STORAGE_KEY);
  if (savedData) {
    try {
      cart = JSON.parse(savedData);
      if (!Array.isArray(cart)) cart = [];
    } catch (e) {
      console.error("Gagal membaca keranjang dari LocalStorage:", e);
      cart = [];
    }
  } else {
    // Data default awal jika keranjang baru pertama kali dibuka (opsional untuk demo kasir)
    cart = [
      { id: Date.now() - 2000, nama: "Nasi Ayam Geprek", harga: 18000, qty: 2 },
      { id: Date.now() - 1000, nama: "Es Teh Manis Jumbo", harga: 5000, qty: 3 },
      { id: Date.now(), nama: "Buku Catatan Kampus", harga: 12000, qty: 1 }
    ];
    saveCartToStorage();
  }
}

/**
 * Menambahkan item baru ke keranjang belanja
 */
function tambahItemKeKeranjang(nama, harga, qty) {
  // Cek apakah item dengan nama dan harga yang sama sudah ada di keranjang
  const existingItemIndex = cart.findIndex(
    item => item.nama.toLowerCase() === nama.toLowerCase() && item.harga === harga
  );

  if (existingItemIndex > -1) {
    // Jika sudah ada, akumulasikan kuantitasnya
    cart[existingItemIndex].qty += qty;
  } else {
    // Buat item baru
    const newItem = {
      id: Date.now(),
      nama: nama,
      harga: harga,
      qty: qty
    };
    cart.push(newItem);
  }

  saveCartToStorage();
  renderCart();
  calculateTotals();
}

/**
 * Menghapus item dari keranjang berdasarkan index
 */
function hapusItemKeranjang(index) {
  if (index >= 0 && index < cart.length) {
    const itemNama = cart[index].nama;
    cart.splice(index, 1);
    saveCartToStorage();
    renderCart();
    calculateTotals();
    showToast(`"${itemNama}" dihapus dari keranjang.`, "info");
  }
}

/**
 * Mengubah jumlah (qty) item langsung dari keranjang
 */
function updateItemQty(index, delta) {
  if (index >= 0 && index < cart.length) {
    const newQty = cart[index].qty + delta;
    if (newQty <= 0) {
      hapusItemKeranjang(index);
    } else {
      cart[index].qty = newQty;
      saveCartToStorage();
      renderCart();
      calculateTotals();
    }
  }
}

/**
 * Mengosongkan keranjang belanja dan membersihkan LocalStorage (Transaksi Baru)
 */
function resetSeluruhKeranjang() {
  if (cart.length === 0) {
    showToast("Keranjang belanja sudah kosong.", "info");
    return;
  }

  const confirmReset = confirm("Apakah Anda yakin ingin mengosongkan seluruh keranjang belanja (Transaksi Baru)?");
  if (confirmReset) {
    cart = [];
    appliedPromo = "";
    localStorage.removeItem(STORAGE_KEY);
    
    // Reset input kalkulator
    document.getElementById("uangBayar").value = "";
    document.getElementById("promoCode").value = "";
    document.getElementById("promoFeedback").innerText = "";
    
    renderCart();
    calculateTotals();
    showToast("Keranjang belanja berhasil di-reset untuk transaksi baru! 🛒", "success");
  }
}

// ==========================================
// 5. RENDERING TABEL KERANJANG
// ==========================================
function renderCart() {
  const tbody = document.getElementById("cartTableBody");
  const emptyState = document.getElementById("emptyCartState");
  const badgeCount = document.getElementById("cartCountBadge");

  tbody.innerHTML = "";

  // Update badge total jumlah item
  const totalItemCount = cart.reduce((sum, item) => sum + item.qty, 0);
  badgeCount.innerText = `${totalItemCount} Item (${cart.length} Jenis)`;

  if (cart.length === 0) {
    emptyState.classList.add("active");
    return;
  }

  emptyState.classList.remove("active");

  cart.forEach((item, index) => {
    // 1. Kalkulasi Subtotal per baris barang: Subtotal = Harga Satuan * Qty
    const subtotal = item.harga * item.qty;

    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${index + 1}</td>
      <td class="item-name-cell">
        <strong>${item.nama}</strong>
      </td>
      <td style="text-align: right;">${formatRupiah(item.harga)}</td>
      <td style="text-align: center;">
        <div class="item-qty-control">
          <button type="button" class="btn-qty" onclick="updateItemQty(${index}, -1)" title="Kurangi 1">-</button>
          <span class="qty-val">${item.qty}</span>
          <button type="button" class="btn-qty" onclick="updateItemQty(${index}, 1)" title="Tambah 1">+</button>
        </div>
      </td>
      <td style="text-align: right; font-weight: 700; color: #1e1b4b;">${formatRupiah(subtotal)}</td>
      <td style="text-align: center;">
        <button type="button" class="btn-delete-item" onclick="hapusItemKeranjang(${index})" title="Hapus barang">
          <i class="fa-solid fa-trash-can"></i>
        </button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

// ==========================================
// 6. MODUL KALKULATOR & PERHITUNGAN OTOMATIS
// ==========================================
function setupCalculatorListeners() {
  const inputUangBayar = document.getElementById("uangBayar");
  const inputPromo = document.getElementById("promoCode");
  const btnApplyPromo = document.getElementById("btnApplyPromo");
  const btnResetKeranjang = document.getElementById("btnResetKeranjang");
  const btnSelesai = document.getElementById("btnSelesaiTransaksi");

  // Realtime recalculate kembalian saat kasir mengetik uang bayar
  inputUangBayar.addEventListener("input", calculateTotals);

  // Terapkan kode promo
  btnApplyPromo.addEventListener("click", applyPromoCode);
  inputPromo.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      applyPromoCode();
    }
  });

  // Tombol Reset Keranjang
  btnResetKeranjang.addEventListener("click", resetSeluruhKeranjang);

  // Tombol Selesaikan Transaksi
  btnSelesai.addEventListener("click", handleSelesaiTransaksi);
}

/**
 * Menghitung Total Belanja, Diskon, Total Akhir, dan Kembalian
 */
function calculateTotals() {
  // 1. Kalkulasi Total Belanja: Jumlah seluruh subtotal
  const totalBelanja = cart.reduce((sum, item) => sum + (item.harga * item.qty), 0);

  // 2. Kalkulator Diskon Sederhana:
  // - Minimal Rp 50.000 mendapatkan potongan 10%
  // - ATAU jika menggunakan kode promo "HEMAT10"
  let discountPercent = 0;
  let isAutoDiscount = false;

  if (totalBelanja >= 50000) {
    discountPercent = 10;
    isAutoDiscount = true;
  } else if (appliedPromo.toUpperCase() === "HEMAT10") {
    discountPercent = 10;
  }

  const nominalDiskon = (totalBelanja * discountPercent) / 100;
  const totalAkhir = Math.max(0, totalBelanja - nominalDiskon);

  // Update tampilan Diskon & Status
  const displayTotalBelanja = document.getElementById("displayTotalBelanja");
  const displayDiskon = document.getElementById("displayDiskon");
  const displayDiscountPercent = document.getElementById("displayDiscountPercent");
  const displayTotalAkhir = document.getElementById("displayTotalAkhir");
  const discountBadge = document.getElementById("discountStatusBadge");

  displayTotalBelanja.innerText = formatRupiah(totalBelanja);
  displayDiskon.innerText = nominalDiskon > 0 ? `- ${formatRupiah(nominalDiskon)}` : "Rp 0";
  displayDiscountPercent.innerText = `(${discountPercent}%)`;
  displayTotalAkhir.innerText = formatRupiah(totalAkhir);

  if (isAutoDiscount) {
    discountBadge.innerText = "Diskon 10% Aktif (Belanja >= Rp 50.000)";
    discountBadge.style.background = "var(--success-light)";
    discountBadge.style.color = "var(--success-dark)";
  } else if (appliedPromo.toUpperCase() === "HEMAT10") {
    discountBadge.innerText = "Kupon HEMAT10 Aktif (10%)";
    discountBadge.style.background = "var(--success-light)";
    discountBadge.style.color = "var(--success-dark)";
  } else {
    discountBadge.innerText = "Diskon 10% jika >= Rp 50.000";
    discountBadge.style.background = "var(--bg-main)";
    discountBadge.style.color = "var(--text-muted)";
  }

  // 3. Kalkulator Pembayaran & Kembalian:
  // Kembalian = Uang Bayar - Total Akhir
  const inputUangBayar = document.getElementById("uangBayar");
  const uangBayar = parseFloat(inputUangBayar.value) || 0;

  const changeBox = document.getElementById("changeBoxContainer");
  const displayKembalian = document.getElementById("displayKembalian");
  const changeStatusMsg = document.getElementById("changeStatusMsg");

  if (totalBelanja === 0) {
    changeBox.className = "change-box";
    displayKembalian.innerText = "Rp 0";
    changeStatusMsg.innerText = "Keranjang masih kosong.";
    return { totalBelanja, nominalDiskon, totalAkhir, uangBayar, kembalian: 0, isCukup: false };
  }

  if (inputUangBayar.value.trim() === "" || uangBayar === 0) {
    changeBox.className = "change-box";
    displayKembalian.innerText = "Rp 0";
    changeStatusMsg.innerText = "Silakan masukkan nominal uang yang dibayarkan kasir.";
    return { totalBelanja, nominalDiskon, totalAkhir, uangBayar, kembalian: 0, isCukup: false };
  }

  const kembalian = uangBayar - totalAkhir;

  if (kembalian >= 0) {
    // Uang Cukup atau Pas
    changeBox.className = "change-box status-success";
    displayKembalian.innerText = formatRupiah(kembalian);
    if (kembalian === 0) {
      changeStatusMsg.innerText = "Uang Pas (Tidak ada kembalian) ✅";
    } else {
      changeStatusMsg.innerText = `Kembalian yang harus diberikan ke pembeli: ${formatRupiah(kembalian)} ✅`;
    }
    return { totalBelanja, nominalDiskon, totalAkhir, uangBayar, kembalian, isCukup: true };
  } else {
    // Uang Kurang
    const kekurangan = Math.abs(kembalian);
    changeBox.className = "change-box status-danger";
    displayKembalian.innerText = `- ${formatRupiah(kekurangan)}`;
    changeStatusMsg.innerText = `Uang belum mencukupi! Kurang sebesar ${formatRupiah(kekurangan)} ❌`;
    return { totalBelanja, nominalDiskon, totalAkhir, uangBayar, kembalian, isCukup: false };
  }
}

/**
 * Terapkan kode promo dari form
 */
function applyPromoCode() {
  const inputPromo = document.getElementById("promoCode");
  const promoFeedback = document.getElementById("promoFeedback");
  const code = inputPromo.value.trim().toUpperCase();

  if (code === "") {
    appliedPromo = "";
    promoFeedback.innerText = "Kode promo dihapus.";
    promoFeedback.className = "promo-feedback";
    calculateTotals();
    return;
  }

  if (code === "HEMAT10") {
    appliedPromo = code;
    promoFeedback.innerText = "Kode HEMAT10 berhasil diterapkan! Potongan 10%.";
    promoFeedback.className = "promo-feedback success";
    showToast("Kode promo HEMAT10 berhasil diterapkan!", "success");
  } else {
    appliedPromo = "";
    promoFeedback.innerText = "Kode promo tidak valid! Coba 'HEMAT10'.";
    promoFeedback.className = "promo-feedback error";
    showToast("Kode promo tidak valid!", "error");
  }

  calculateTotals();
}

/**
 * Quick Preset Cash Buttons
 */
function setUangPas() {
  const totalBelanja = cart.reduce((sum, item) => sum + (item.harga * item.qty), 0);
  let discountPercent = (totalBelanja >= 50000 || appliedPromo.toUpperCase() === "HEMAT10") ? 10 : 0;
  const nominalDiskon = (totalBelanja * discountPercent) / 100;
  const totalAkhir = Math.max(0, totalBelanja - nominalDiskon);

  document.getElementById("uangBayar").value = totalAkhir;
  calculateTotals();
  showToast("Nominal uang bayar diatur ke 'Uang Pas'", "info");
}

function addQuickCash(nominal) {
  const input = document.getElementById("uangBayar");
  const cur = parseFloat(input.value) || 0;
  input.value = cur + nominal;
  calculateTotals();
}

function clearUangBayar() {
  document.getElementById("uangBayar").value = "";
  calculateTotals();
}

// ==========================================
// 7. STRUK TRANSAKSI & PENYELESAIAN
// ==========================================
function handleSelesaiTransaksi() {
  if (cart.length === 0) {
    showToast("Keranjang belanja masih kosong! Tambahkan barang terlebih dahulu.", "error");
    return;
  }

  const calc = calculateTotals();

  if (!calc.isCukup) {
    showToast("Transaksi tidak dapat diproses: Uang pembayaran belum mencukupi!", "error");
    document.getElementById("uangBayar").focus();
    return;
  }

  // Tampilkan Modal Struk Transaksi
  openReceiptModal(calc);
}

function openReceiptModal(calc) {
  const modal = document.getElementById("receiptModal");
  const receiptItemList = document.getElementById("receiptItemList");

  // Set Tanggal & ID
  const now = new Date();
  const dateStr = now.toLocaleDateString("id-ID", {
    day: "2-digit",
    month: "short",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit"
  });
  document.getElementById("receiptDate").innerText = dateStr;
  document.getElementById("receiptId").innerText = `#POS-${now.getFullYear()}${String(now.getMonth() + 1).padStart(2, "0")}-${Math.floor(1000 + Math.random() * 9000)}`;

  // Populate Items
  receiptItemList.innerHTML = "";
  cart.forEach(item => {
    const sub = item.harga * item.qty;
    const itemRow = document.createElement("div");
    itemRow.className = "receipt-item-block";
    itemRow.innerHTML = `
      <div class="receipt-item-row">
        <span>${item.nama}</span>
        <span>${formatRupiah(sub)}</span>
      </div>
      <div class="receipt-item-detail">
        ${item.qty} x ${formatRupiah(item.harga)}
      </div>
    `;
    receiptItemList.appendChild(itemRow);
  });

  // Populate Summary
  document.getElementById("receiptSubtotal").innerText = formatRupiah(calc.totalBelanja);
  document.getElementById("receiptDiskon").innerText = `- ${formatRupiah(calc.nominalDiskon)}`;
  document.getElementById("receiptTotalAkhir").innerText = formatRupiah(calc.totalAkhir);
  document.getElementById("receiptUangBayar").innerText = formatRupiah(calc.uangBayar);
  document.getElementById("receiptKembalian").innerText = formatRupiah(calc.kembalian);

  modal.classList.add("active");
}

function closeReceiptModal() {
  document.getElementById("receiptModal").classList.remove("active");
}

function setupReceiptModalListeners() {
  const modal = document.getElementById("receiptModal");
  const btnClose = document.getElementById("btnCloseReceipt");
  const btnPrint = document.getElementById("btnPrintReceipt");
  const btnSelesaiModal = document.getElementById("btnSelesaiModal");

  btnClose.addEventListener("click", closeReceiptModal);
  
  modal.addEventListener("click", (e) => {
    if (e.target === modal) closeReceiptModal();
  });

  btnPrint.addEventListener("click", () => {
    window.print();
  });

  btnSelesaiModal.addEventListener("click", () => {
    closeReceiptModal();
    // Bersihkan keranjang belanja setelah transaksi selesai berhasil
    cart = [];
    appliedPromo = "";
    localStorage.removeItem(STORAGE_KEY);
    document.getElementById("uangBayar").value = "";
    document.getElementById("promoCode").value = "";
    document.getElementById("promoFeedback").innerText = "";
    
    renderCart();
    calculateTotals();
    showToast("Transaksi berhasil diselesaikan! Keranjang siap untuk pelanggan berikutnya. 🎉", "success");
  });
}

// ==========================================
// 8. TOAST NOTIFICATION COMPONENT
// ==========================================
function showToast(message, type = "info") {
  const container = document.getElementById("toastContainer");
  if (!container) return;

  const toast = document.createElement("div");
  toast.className = `toast toast-${type}`;

  let icon = "fa-circle-info";
  if (type === "success") icon = "fa-circle-check";
  if (type === "error") icon = "fa-circle-exclamation";

  toast.innerHTML = `<i class="fa-solid ${icon}"></i> <span>${message}</span>`;
  container.appendChild(toast);

  setTimeout(() => {
    toast.style.opacity = "0";
    toast.style.transform = "translateY(10px)";
    toast.style.transition = "all 0.3s ease";
    setTimeout(() => toast.remove(), 300);
  }, 3200);
}
