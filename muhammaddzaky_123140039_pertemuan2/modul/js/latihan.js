/**
 * ============================================================================
 * MODUL PRAKTIKUM PAW - PERTEMUAN 2
 * Berkas: js/latihan.js
 * Solusi Lengkap Latihan Mandiri Setiap Materi ES6+
 * Mahasiswa: Muhammad Dzaky (123140039) - RA
 * ============================================================================
 */

// ============================================================================
// LATIHAN 1: Let, Const, dan Arrow Functions
// ============================================================================

/**
 * 1.1 Coba ubah nilai const dan lihat error yang muncul
 */
export function latihanConstReassign() {
  const KAMPUS = "ITERA";
  try {
    // Mencoba reassign variabel konstan
    eval("KAMPUS = 'Institut Teknologi Sumatera'");
    return { success: true, value: KAMPUS };
  } catch (error) {
    return {
      success: false,
      errorName: error.name,
      errorMessage: error.message,
      explanation: "Variabel const mengikat referensi secara permanen. Percobaan reassign memicu TypeError."
    };
  }
}

/**
 * 1.2 Bandingkan behavior var di dalam dan luar block
 */
export function latihanVarVsLetBlockScope() {
  var varLuar = "var di luar block";
  let letLuar = "let di luar block";

  if (true) {
    var varDalam = "var di DALAM block";
    let letDalam = "let di DALAM block";
  }

  // var tembus keluar block, sedangkan let terlindungi di dalam block scope
  const isVarAccessibleOutside = typeof varDalam !== 'undefined';
  let isLetAccessibleOutside = false;
  try {
    eval("letDalam");
    isLetAccessibleOutside = true;
  } catch (e) {
    isLetAccessibleOutside = false;
  }

  return {
    varAccessibleOutside: isVarAccessibleOutside,
    varValue: varDalam,
    letAccessibleOutside: isLetAccessibleOutside,
    explanation: "var tidak memiliki block scope (function-scoped), sehingga bocor keluar dari blok if. let memiliki block scope ketat sehingga terisolasi."
  };
}

/**
 * 1.3 Buat arrow function dengan berbagai variasi sintaks
 */
export function latihanArrowFunctionVariations() {
  // Tanpa parameter
  const fnNoParam = () => "ITERA Unggul & Bermartabat";

  // Parameter tunggal tanpa tanda kurung
  const fnSingleParam = x => x ** 3; // Kubik angka

  // Dua parameter dengan eksplisit block & return
  const fnMultiParams = (panjang, lebar) => {
    const luas = panjang * lebar;
    return `Luas: ${luas} mÂ²`;
  };

  // Mengembalikan objek literal langsung (dibungkus tanda kurung biasa)
  const fnReturnObject = (nim, nama) => ({
    nim,
    nama,
    prodi: "Teknik Informatika",
    timestamp: Date.now()
  });

  return {
    noParam: fnNoParam(),
    singleParam: fnSingleParam(5),
    multiParams: fnMultiParams(10, 8),
    returnObject: fnReturnObject("123140039", "Muhammad Dzaky")
  };
}

// ============================================================================
// LATIHAN 2: Template Literals
// ============================================================================

/**
 * 2.1 Gunakan template literals untuk membuat HTML string dinamis
 */
export function latihanHtmlTemplateLiterals() {
  const student = {
    name: "Muhammad Dzaky",
    nim: "123140039",
    classRoom: "RA",
    gpa: 3.88,
    courses: ["PAW", "Basis Data", "Struktur Data", "Kecerdasan Buatan"],
    isActive: true
  };

  const htmlCard = `
    <div class="student-card-preview" style="border: 2px solid #2563eb; border-radius: 12px; padding: 1.25rem; background: #1e293b; color: #fff;">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
        <h4 style="margin: 0; color: #60a5fa; font-size: 1.1rem;">${student.name}</h4>
        <span style="background: ${student.isActive ? '#10b981' : '#ef4444'}; color: #fff; font-size: 0.75rem; padding: 0.2rem 0.6rem; border-radius: 9999px;">
          ${student.isActive ? 'Mahasiswa Aktif' : 'Cuti'}
        </span>
      </div>
      <p style="margin: 0 0 0.5rem; color: #94a3b8; font-size: 0.85rem;">
        NIM: <strong>${student.nim}</strong> &bull; Kelas: <strong>${student.classRoom}</strong>
      </p>
      <p style="margin: 0 0 0.75rem; font-size: 0.9rem;">
        Predikat IPK: <strong>${student.gpa}</strong> (${student.gpa >= 3.5 ? 'Dengan Pujian / Cumlaude' : 'Sangat Memuaskan'})
      </p>
      <div style="margin-top: 0.5rem; border-top: 1px solid #334155; padding-top: 0.5rem;">
        <small style="color: #cbd5e1;">Mata Kuliah Diambil:</small>
        <ul style="margin: 0.35rem 0 0 1.2rem; padding: 0; font-size: 0.85rem; color: #e2e8f0;">
          ${student.courses.map(course => `<li>${course}</li>`).join('')}
        </ul>
      </div>
    </div>
  `;

  return {
    rawString: htmlCard,
    student
  };
}

// ============================================================================
// LATIHAN 3: Destructuring dan Operators
// ============================================================================

/**
 * 3.1 Destructure object dengan nested properties minimal 3 level
 */
export function latihanNestedDestructuring() {
  const iteraOrganization = {
    campus: "ITERA Lampung",
    faculty: {
      name: "Fakultas Teknologi Industri dan Kebumian",
      department: {
        name: "Jurusan Teknologi Produksi dan Industri",
        programStudy: {
          code: "IF",
          title: "Teknik Informatika",
          accreditation: "Baik Sekali",
          headOfStudy: "Dosen Pembina IF"
        }
      }
    }
  };

  // Ekstraksi 3 level: faculty -> department -> programStudy
  const {
    faculty: {
      name: facultyName,
      department: {
        name: departmentName,
        programStudy: { title: prodiTitle, accreditation: prodiAkreditasi }
      }
    }
  } = iteraOrganization;

  return {
    facultyName,
    departmentName,
    prodiTitle,
    prodiAkreditasi
  };
}

/**
 * 3.2 Function yang menerima rest parameters dan mengembalikan statistik (min, max, average)
 */
export function calculateStats(...numbers) {
  if (numbers.length === 0) {
    return { count: 0, min: null, max: null, average: 0, sum: 0 };
  }

  const sum = numbers.reduce((acc, curr) => acc + curr, 0);
  const min = Math.min(...numbers);
  const max = Math.max(...numbers);
  const average = Number((sum / numbers.length).toFixed(2));

  return {
    count: numbers.length,
    inputNumbers: numbers,
    sum,
    min,
    max,
    average
  };
}

/**
 * 3.3 Merge 3 objects dengan spread operator dan override beberapa properties
 */
export function latihanMergeObjects() {
  const baseConfig = {
    appName: "ITERA Academic Hub",
    version: "1.0.0",
    theme: "light",
    language: "id"
  };

  const userPreference = {
    theme: "dark", // Meng-override 'light'
    notifications: true,
    fontSize: "15px"
  };

  const environmentOverride = {
    version: "2.1.0-prod", // Meng-override '1.0.0'
    debugMode: false,
    apiUrl: "https://api.open-meteo.com/v1"
  };

  // Merge 3 Objek menggunakan Spread Operator (...)
  const finalMergedConfig = {
    ...baseConfig,
    ...userPreference,
    ...environmentOverride,
    lastSynced: new Date().toISOString()
  };

  return finalMergedConfig;
}

/**
 * 3.4 Gunakan destructuring dalam loop for...of
 */
export function latihanDestructuringInForOf() {
  const students = [
    { id: 1, nim: "123140039", name: "Muhammad Dzaky", score: 92 },
    { id: 2, nim: "123140050", name: "Ahmad Rizky", score: 85 },
    { id: 3, nim: "123140051", name: "Siti Nurhaliza", score: 88 },
    { id: 4, nim: "123140052", name: "Budi Santoso", score: 78 }
  ];

  const results = [];

  // Destructuring langsung di parameter loop for...of
  for (const { nim, name, score } of students) {
    const grade = score >= 85 ? "A" : score >= 75 ? "B" : "C";
    results.push(`${name} (${nim}) -> Nilai: ${score} [Grade: ${grade}]`);
  }

  return results;
}

// ============================================================================
// LATIHAN 4: Classes dan Object Literals
// ============================================================================

/**
 * 4.1 & 4.2 Class Product dengan inheritance ke DigitalProduct & PhysicalProduct + Getter/Setter
 */
export class Product {
  constructor(name, price = 0) {
    this.name = name;
    this._price = price;
    this._discountRate = 0; // dalam persen (0 - 100)
  }

  // Getter & Setter untuk Harga & Diskon
  get price() {
    return this._price;
  }

  set price(val) {
    if (val < 0) throw new Error("Harga tidak boleh negatif");
    this._price = val;
  }

  get discount() {
    return this._discountRate;
  }

  set discount(rate) {
    if (rate < 0 || rate > 100) throw new Error("Diskon harus di antara 0 dan 100%");
    this._discountRate = rate;
  }

  get finalPrice() {
    return this._price * (1 - this._discountRate / 100);
  }

  get formattedFinalPrice() {
    return `Rp ${this.finalPrice.toLocaleString('id-ID')}`;
  }

  getInfo() {
    return `Produk: ${this.name} | Harga Normal: Rp ${this._price.toLocaleString('id-ID')} | Harga Diskon: ${this.formattedFinalPrice}`;
  }
}

export class DigitalProduct extends Product {
  constructor(name, price, downloadUrl, fileSizeMb) {
    super(name, price);
    this.downloadUrl = downloadUrl;
    this.fileSizeMb = fileSizeMb;
  }

  // Override method
  getInfo() {
    return `[Digital Download] ${super.getInfo()} | Ukuran File: ${this.fileSizeMb} MB`;
  }
}

export class PhysicalProduct extends Product {
  constructor(name, price, weightKg, courier) {
    super(name, price);
    this.weightKg = weightKg;
    this.courier = courier;
  }

  get shippingCost() {
    return this.weightKg * 12000; // Rp 12.000 per kg
  }

  // Override method
  getInfo() {
    return `[Barang Fisik] ${super.getInfo()} | Berat: ${this.weightKg} kg (Ongkir: Rp ${this.shippingCost.toLocaleString('id-ID')})`;
  }
}

export function latihanClassInheritance() {
  const ebook = new DigitalProduct("E-Book Tutorial Pemrograman Web Modern ES6+", 150000, "https://itera.ac.id/ebook-paw.pdf", 45);
  ebook.discount = 20; // Diskon 20%

  const hoodie = new PhysicalProduct("Hoodie Himpunan Mahasiswa Informatika ITERA", 220000, 0.8, "JNE Reguler");
  hoodie.discount = 10; // Diskon 10%

  return {
    digital: {
      info: ebook.getInfo(),
      finalPrice: ebook.formattedFinalPrice,
      isProductInstance: ebook instanceof Product,
      isDigitalInstance: ebook instanceof DigitalProduct
    },
    physical: {
      info: hoodie.getInfo(),
      shippingCost: `Rp ${hoodie.shippingCost.toLocaleString('id-ID')}`,
      isProductInstance: hoodie instanceof Product,
      isPhysicalInstance: hoodie instanceof PhysicalProduct
    }
  };
}

/**
 * 4.3 Computed Property Names untuk Dynamic Keys
 */
export function latihanComputedPropertyNames() {
  const dynamicCategory = "praktikum";
  const modId = 2;
  const timestampKey = `generated_at_${Date.now()}`;

  const assessmentReport = {
    [`modul_${modId}_title`]: "JavaScript Next Generation (ES6+)",
    [`score_${dynamicCategory}`]: 98,
    [`asisten_${dynamicCategory}`]: "Tim Asisten PAW ITERA",
    [timestampKey]: new Date().toLocaleString('id-ID')
  };

  return assessmentReport;
}

/**
 * 4.4 Combine default parameters dengan destructuring dalam function parameter
 */
export function createAcademicCard({
  name = "Mahasiswa ITERA",
  nim = "123140000",
  prodi = "Teknik Informatika",
  status = "Aktif",
  gpa = 3.50
} = {}) {
  return {
    badge: `[${prodi.toUpperCase()}] ${name} - ${nim}`,
    statusText: `Status: ${status} | Indeks Prestasi: ${gpa}`,
    verified: true
  };
}

// ============================================================================
// LATIHAN 5: Modern Array Methods
// ============================================================================

/**
 * 5.1 Implementasi fungsi groupBy menggunakan reduce()
 */
export function groupBy(array, keyOrFn) {
  return array.reduce((accumulator, currentItem) => {
    const groupKey = typeof keyOrFn === 'function' ? keyOrFn(currentItem) : currentItem[keyOrFn];
    if (!accumulator[groupKey]) {
      accumulator[groupKey] = [];
    }
    accumulator[groupKey].push(currentItem);
    return accumulator;
  }, {});
}

export function demoGroupByExercise() {
  const studentsList = [
    { name: "Muhammad Dzaky", classRoom: "RA", track: "Web Development" },
    { name: "Fathur Rahman", classRoom: "RA", track: "Cyber Security" },
    { name: "Gita Permata", classRoom: "RB", track: "Web Development" },
    { name: "Dimas Anggara", classRoom: "RB", track: "Data Science" },
    { name: "Rina Kartika", classRoom: "RC", track: "Data Science" }
  ];

  return {
    byClass: groupBy(studentsList, "classRoom"),
    byTrack: groupBy(studentsList, "track")
  };
}

/**
 * 5.2 Menghitung rata-rata dari array of objects
 */
export function calculateAverageOfObjects(items, propertyName) {
  if (!items || items.length === 0) return 0;
  const total = items.reduce((acc, curr) => acc + (curr[propertyName] || 0), 0);
  return Number((total / items.length).toFixed(2));
}

/**
 * 5.3 Transform struktur array bersarang menjadi struktur flat
 */
export function latihanFlattenNestedArray() {
  const nestedModulTasks = [
    ["Modul 1: HTML Dasar", "Modul 1: Form Validation"],
    ["Modul 2: ES6+ Classes", ["Modul 2: Async Await", "Modul 2: Destructuring"]],
    ["Modul 3: React Components", ["Modul 3: Hooks State", ["Modul 3: Context API"]]]
  ];

  // Menggunakan flat(Infinity)
  const fullyFlat = nestedModulTasks.flat(Infinity);

  // Implementasi manual dengan reduce + concat (deep recursive flatten)
  const deepFlattenWithReduce = arr =>
    arr.reduce((acc, val) =>
      Array.isArray(val) ? acc.concat(deepFlattenWithReduce(val)) : acc.concat(val),
      []
    );

  return {
    originalDepth: 3,
    flattenedViaMethod: fullyFlat,
    flattenedViaReduce: deepFlattenWithReduce(nestedModulTasks)
  };
}

/**
 * 5.4 Gabungkan filter, map, dan reduce untuk analisis data kompleks
 */
export function latihanComplexArrayChaining() {
  const academicSubmissions = [
    { student: "Muhammad Dzaky", course: "PAW", score: 95, submittedOnTime: true },
    { student: "Budi", course: "PAW", score: 65, submittedOnTime: false },
    { student: "Citra", course: "PAW", score: 88, submittedOnTime: true },
    { student: "Dodi", course: "PAW", score: 55, submittedOnTime: false },
    { student: "Eka", course: "PAW", score: 92, submittedOnTime: true }
  ];

  // Pipeline Chaining:
  // 1. filter() mahasiswa yang mengumpulkan tepat waktu
  // 2. map() menghitung nilai akhir dengan bonus ketepatan waktu (+5 poin, maks 100)
  // 3. reduce() mencari rata-rata nilai akhir mahasiswa teladan
  const onTimeStudents = academicSubmissions.filter(s => s.submittedOnTime);

  const gradedOnTime = onTimeStudents.map(s => ({
    student: s.student,
    originalScore: s.score,
    finalScore: Math.min(100, s.score + 5)
  }));

  const averageFinalScore = gradedOnTime.reduce((sum, s, _, arr) => 
    sum + s.finalScore / arr.length, 0
  );

  return {
    allSubmissionsCount: academicSubmissions.length,
    onTimeCount: onTimeStudents.length,
    gradedList: gradedOnTime,
    averageFinalScore: Number(averageFinalScore.toFixed(2))
  };
}

// ============================================================================
// LATIHAN 6: Async Programming (Promise & Async/Await)
// ============================================================================

/**
 * 6.1 Fetch data dari beberapa endpoint dan gabungkan hasilnya
 */
export async function fetchAndCombineEndpoints() {
  const quoteUrl = "https://dummyjson.com/quotes/random";
  const weatherUrl = "https://api.open-meteo.com/v1/forecast?latitude=-5.36&longitude=105.31&current_weather=true";

  try {
    // Eksekusi paralel dengan Promise.all
    const [quoteRes, weatherRes] = await Promise.all([
      fetch(quoteUrl),
      fetch(weatherUrl)
    ]);

    const quoteData = await quoteRes.json();
    const weatherData = await weatherRes.json();

    return {
      success: true,
      combined: {
        motivation: {
          quote: quoteData.quote,
          author: quoteData.author
        },
        iteraWeather: {
          temp: `${Math.round(weatherData.current_weather.temperature)}Â°C`,
          wind: `${weatherData.current_weather.windspeed} km/h`
        },
        summary: `Kampus ITERA bersuhu ${weatherData.current_weather.temperature}Â°C. Inspirasi hari ini: "${quoteData.quote}" - ${quoteData.author}`
      }
    };
  } catch (error) {
    return {
      success: false,
      error: error.message,
      fallback: "Gagal menggabungkan beberapa endpoint"
    };
  }
}

/**
 * 6.2 Implementasi mekanisme retry dengan exponential backoff
 */
export async function fetchWithExponentialBackoff(fetchFn, maxRetries = 3, baseDelayMs = 400) {
  let attempt = 0;

  while (attempt < maxRetries) {
    try {
      attempt++;
      return await fetchFn(attempt);
    } catch (err) {
      if (attempt >= maxRetries) {
        throw new Error(`Gagal setelah ${maxRetries} percobaan. Alasan: ${err.message}`);
      }
      // Hitung jeda exponential: 400ms, 800ms, 1600ms, ...
      const delay = baseDelayMs * Math.pow(2, attempt - 1);
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
}

/**
 * 6.3 Async Error Boundary Helper
 */
export async function asyncErrorBoundary(asyncFunction, fallbackValue = null) {
  try {
    return {
      data: await asyncFunction(),
      error: null,
      isSuccess: true
    };
  } catch (err) {
    return {
      data: fallbackValue,
      error: err.message,
      isSuccess: false
    };
  }
}

/**
 * 6.4 Implementasi Pagination dengan Async/Await
 */
export async function fetchPaginatedTodos(page = 1, limit = 3) {
  const start = (page - 1) * limit;
  const endpoint = `https://jsonplaceholder.typicode.com/todos?_start=${start}&_limit=${limit}`;

  const res = await fetch(endpoint);
  if (!res.ok) throw new Error("Gagal mengambil data paginasi");
  const data = await res.json();

  return {
    currentPage: page,
    limit,
    items: data.map(todo => ({
      id: todo.id,
      title: todo.title,
      completed: todo.completed
    }))
  };
}

/**
 * 6.5 Debounce Search Helper Function
 */
export function debounce(func, delayMs = 300) {
  let timerId;
  return (...args) => {
    clearTimeout(timerId);
    return new Promise((resolve) => {
      timerId = setTimeout(async () => {
        const result = await func(...args);
        resolve(result);
      }, delayMs);
    });
  };
}
