/**
 * ============================================================================
 * MODUL PRAKTIKUM PAW - PERTEMUAN 2
 * Berkas: js/main.js
 * Runner & Integrasi Antarmuka Web untuk 12 Demo ES6+ dan Solusi Latihan
 * Mahasiswa: Muhammad Dzaky (123140039) - RA
 * ============================================================================
 */

// Import seluruh fungsi demo dari app.js (12 Materi Utama)
import {
  demoVariables,
  demoArrowFunctions,
  demoTemplateLiterals,
  demoDestructuring,
  demoSpreadRest,
  demoDefaultParams,
  demoClasses,
  demoObjectLiterals,
  demoArrayMethods,
  demoAdvancedArrays,
  demoPromises,
  demoAsyncAwait
} from './app.js';

// Import seluruh fungsi solusi latihan dari latihan.js
import {
  latihanConstReassign,
  latihanVarVsLetBlockScope,
  latihanArrowFunctionVariations,
  latihanHtmlTemplateLiterals,
  latihanNestedDestructuring,
  calculateStats,
  latihanMergeObjects,
  latihanDestructuringInForOf,
  latihanClassInheritance,
  latihanComputedPropertyNames,
  createAcademicCard,
  demoGroupByExercise,
  calculateAverageOfObjects,
  latihanFlattenNestedArray,
  latihanComplexArrayChaining,
  fetchAndCombineEndpoints,
  fetchWithExponentialBackoff,
  asyncErrorBoundary,
  fetchPaginatedTodos
} from './latihan.js';

/**
 * Helper: Menambahkan blok kartu output ke dalam kontainer antarmuka
 */
export function addOutput(title, subtitle, content, isHtml = false) {
  const outputEl = document.getElementById("output");
  if (!outputEl) return;

  const card = document.createElement("div");
  card.className = "output-item";

  const header = document.createElement("div");
  header.className = "output-header";
  header.innerHTML = `
    <h3>${title}</h3>
    <p class="subtitle">${subtitle}</p>
  `;

  const resultBody = document.createElement("div");
  resultBody.className = "result";

  if (isHtml) {
    resultBody.innerHTML = content;
  } else {
    const pre = document.createElement("pre");
    pre.textContent = content;
    resultBody.appendChild(pre);
  }

  card.appendChild(header);
  card.appendChild(resultBody);
  outputEl.appendChild(card);
}

/**
 * Fungsi utama untuk menjalankan seluruh 12 demo materi ES6+
 */
export function runAllDemos() {
  const outputEl = document.getElementById("output");
  if (outputEl) outputEl.innerHTML = "";

  // 1. Demo Let dan Const
  const varResults = demoVariables();
  addOutput(
    "1. Let dan Const",
    "var vs let/const dan block scope",
    `var (function scope): ${varResults.oldVar}
let (block scope): ${varResults.newLet}
const (immutable): ${varResults.PI}
const object (mutable content): ${JSON.stringify(varResults.user, null, 2)}`
  );

  // 2. Demo Arrow Functions
  const arrowResults = demoArrowFunctions();
  addOutput(
    "2. Arrow Functions",
    "Perbandingan fungsi reguler dan arrow functions",
    `Regular function: ${arrowResults.regularSum}
Arrow function: ${arrowResults.arrowSum}
Short arrow: ${arrowResults.shortArrowSum}
No params: ${arrowResults.sayHello}
Single param: ${arrowResults.square}`
  );

  // 3. Demo Template Literals
  const templateResults = demoTemplateLiterals();
  addOutput(
    "3. Template Literals",
    "String concatenation vs template literals",
    `Old way: ${templateResults.oldWay}
New way: ${templateResults.newWay}
With expression: ${templateResults.expression}
Multi-line: ${templateResults.multiLine}`
  );

  // 4. Demo Destructuring
  const destructuringResults = demoDestructuring();
  addOutput(
    "4. Destructuring",
    "Ekstraksi nilai dari objek dan array",
    `Object basic: ${JSON.stringify(destructuringResults.objectBasic)}
Object renamed: ${JSON.stringify(destructuringResults.objectRenamed)}
Object default: ${destructuringResults.objectDefault}
Object nested: ${JSON.stringify(destructuringResults.objectNested)}
Array basic: ${JSON.stringify(destructuringResults.arrayBasic)}
Array skipped: ${destructuringResults.arraySkipped}
Array with rest: ${JSON.stringify(destructuringResults.arrayRest)}
Swapped variables: ${JSON.stringify(destructuringResults.swapped)}`
  );

  // 5. Demo Spread dan Rest Operators
  const spreadRestResults = demoSpreadRest();
  addOutput(
    "5. Spread dan Rest Operators",
    "Penggunaan ... untuk array dan objek",
    `Spread in array: ${JSON.stringify(spreadRestResults.spreadArray)}
Copy array: ${JSON.stringify(spreadRestResults.copyArray)}
Merged arrays: ${JSON.stringify(spreadRestResults.mergedArrays)}
Spread in object: ${JSON.stringify(spreadRestResults.spreadObject, null, 2)}
Rest in function (sum): ${spreadRestResults.restSum}
Rest with regular params: ${JSON.stringify(spreadRestResults.restProcess)}`
  );

  // 6. Demo Default Parameters
  const defaultParamsResults = demoDefaultParams();
  addOutput(
    "6. Default Parameters",
    "Nilai default untuk parameter fungsi",
    `Old way: ${defaultParamsResults.oldWay}
Old way with params: ${defaultParamsResults.oldWayParams}
New way: ${defaultParamsResults.newWay}
New way with params: ${defaultParamsResults.newWayParams}
With expression: ${JSON.stringify(defaultParamsResults.withExpression)}
Using previous params: ${JSON.stringify(defaultParamsResults.usingPrevious)}`
  );

  // 7. Demo Classes
  const classesResults = demoClasses();
  addOutput(
    "7. Classes",
    "Penggunaan class dan inheritance",
    `User: ${classesResults.user.info}
User created: ${classesResults.user.createdDate}
Admin: ${classesResults.admin.info}
Admin created: ${classesResults.admin.createdDate}
Admin has access: ${classesResults.admin.hasAccess}
user instanceof User: ${classesResults.isUserInstance}
admin instanceof User: ${classesResults.isAdminInstance}`
  );

  // 8. Demo Enhanced Object Literals
  const objectLiteralsResults = demoObjectLiterals();
  addOutput(
    "8. Enhanced Object Literals",
    "Penulisan objek yang lebih ringkas",
    `Property shorthand: ${JSON.stringify(objectLiteralsResults.newWay, null, 2)}
Method shorthand: ${objectLiteralsResults.methods.new}
Computed properties: ${JSON.stringify(objectLiteralsResults.computedProps)}
Dynamic properties: ${JSON.stringify(objectLiteralsResults.dynamicProps)}`
  );

  // 9. Demo Array Methods
  const arrayMethodsResults = demoArrayMethods();
  addOutput(
    "9. Modern Array Methods",
    "Higher-Order Functions pada array",
    `map: ${JSON.stringify(arrayMethodsResults.map)}
filter (evenNumbers): ${JSON.stringify(arrayMethodsResults.filter.evenNumbers)}
filter (activeUsers): ${arrayMethodsResults.filter.activeUsers}
find: ${JSON.stringify(arrayMethodsResults.find)}
some (hasAdult): ${arrayMethodsResults.some}
every (allAdults): ${arrayMethodsResults.every}
reduce (sum): ${arrayMethodsResults.reduce.sum}
reduce (oldest): ${arrayMethodsResults.reduce.oldest}
chaining (activeUsersNames): ${JSON.stringify(arrayMethodsResults.chaining.activeUsersNames)}
chaining (totalActiveAge): ${arrayMethodsResults.chaining.totalActiveAge}`
  );

  // 10. Demo Advanced Arrays
  const advArraysResults = demoAdvancedArrays();
  addOutput(
    "10. Advanced Arrays",
    "Fitur array lanjutan",
    `Clone: ${JSON.stringify(advArraysResults.clone)}
Concat: ${JSON.stringify(advArraysResults.concat.combinedArrays)}
Array.from: ${JSON.stringify(advArraysResults.arrayFrom.withMapFn)}
Array.of: ${JSON.stringify(advArraysResults.arrayOf)}
flat: ${JSON.stringify(advArraysResults.flatAndFlatMap.flattened)}
deepFlat: ${JSON.stringify(advArraysResults.flatAndFlatMap.deepFlattened)}
flatMap: ${JSON.stringify(advArraysResults.flatAndFlatMap.flatMapped)}
includes: ${advArraysResults.includes}`
  );

  // 11. Demo Promises
  addOutput(
    "11. Promises",
    "Penanganan operasi asinkron dengan Promise",
    ""
  );
  const promiseOutput = demoPromises();
  const lastPromiseOutput = document.querySelector('.output-item:last-child .result');
  if (lastPromiseOutput) lastPromiseOutput.appendChild(promiseOutput);

  // 12. Demo Async/Await
  addOutput(
    "12. Async/Await",
    "Penanganan operasi asinkron dengan syntax yang lebih bersih",
    ""
  );
  const asyncOutput = demoAsyncAwait();
  const lastAsyncOutput = document.querySelector('.output-item:last-child .result');
  if (lastAsyncOutput) lastAsyncOutput.appendChild(asyncOutput);
}

/**
 * Menjalankan seluruh penyelesaian Latihan Praktikum
 */
export async function runAllLatihan() {
  const outputEl = document.getElementById("output");
  if (outputEl) outputEl.innerHTML = "";

  // Latihan 1: Const Reassign Error
  const constErr = latihanConstReassign();
  addOutput(
    "Latihan 1.1: Reassign Const & Penanganan Error",
    "Membuktikan sifat immutabilitas variabel const",
    `Status Eksekusi: ${constErr.success ? "Berhasil" : "Gagal Terdeteksi"}
Nama Error: ${constErr.errorName}
Pesan Error: ${constErr.errorMessage}
Kesimpulan: ${constErr.explanation}`
  );

  // Latihan 1.2: Var vs Let Scope
  const varScope = latihanVarVsLetBlockScope();
  addOutput(
    "Latihan 1.2: Scope Var vs Let",
    "Perbandingan kebocoran blok (block scope leak)",
    `Var bocor keluar block?: ${varScope.varAccessibleOutside} (Nilai: "${varScope.varValue}")
Let bocor keluar block?: ${varScope.letAccessibleOutside}
Kesimpulan: ${varScope.explanation}`
  );

  // Latihan 1.3: Variasi Arrow Functions
  const arrowVar = latihanArrowFunctionVariations();
  addOutput(
    "Latihan 1.3: Variasi Sintaks Arrow Functions",
    "Single param, multi-params, return object",
    `Tanpa Parameter: ${arrowVar.noParam}
Parameter Tunggal (x^3): 5^3 = ${arrowVar.singleParam}
Blok Parameter Ganda: ${arrowVar.multiParams}
Return Objek Literal: ${JSON.stringify(arrowVar.returnObject, null, 2)}`
  );

  // Latihan 2: Dynamic HTML Template Literals
  const htmlTpl = latihanHtmlTemplateLiterals();
  addOutput(
    "Latihan 2: Template Literals untuk Render HTML Dinamis",
    "Merender kartu mahasiswa dengan data dinamis, predikat, dan perulangan array",
    htmlTpl.rawString,
    true
  );

  // Latihan 3.1: Nested Destructuring 3 Level
  const nested3 = latihanNestedDestructuring();
  addOutput(
    "Latihan 3.1: Nested Destructuring (Minimal 3 Level)",
    "Ekstraksi hierarki organisasi kampus ITERA: fakultas -> jurusan -> prodi",
    `Fakultas: ${nested3.facultyName}
Jurusan: ${nested3.departmentName}
Program Studi: ${nested3.prodiTitle}
Akreditasi: ${nested3.prodiAkreditasi}`
  );

  // Latihan 3.2: Rest Parameter untuk Statistik
  const statsResult = calculateStats(85, 92, 78, 96, 68, 88, 74, 95);
  addOutput(
    "Latihan 3.2: Rest Parameter (...numbers) untuk Statistik",
    "Menerima sembarang argumen numerik dan menghitung min, max, average",
    `Data Input: [${statsResult.inputNumbers.join(', ')}]
Jumlah Elemen: ${statsResult.count}
Total Penjumlahan: ${statsResult.sum}
Nilai Terendah (Min): ${statsResult.min}
Nilai Tertinggi (Max): ${statsResult.max}
Rata-Rata: ${statsResult.average}`
  );

  // Latihan 3.3: Merge 3 Objek dengan Spread Operator
  const mergedObj = latihanMergeObjects();
  addOutput(
    "Latihan 3.3: Menggabungkan 3 Objek dengan Spread Operator (...)",
    "Base config + user preferences + environment overrides",
    JSON.stringify(mergedObj, null, 2)
  );

  // Latihan 3.4: Destructuring dalam Loop for...of
  const forOfResults = latihanDestructuringInForOf();
  addOutput(
    "Latihan 3.4: Destructuring di dalam Loop for...of",
    "Mengekstrak properti mahasiswa langsung saat iterasi",
    forOfResults.join("\n")
  );

  // Latihan 4.1 & 4.2: Class Inheritance & Getter/Setter
  const productDemo = latihanClassInheritance();
  addOutput(
    "Latihan 4.1 & 4.2: Class Product, Inheritance & Getter/Setter",
    "Inheritance Product -> DigitalProduct & PhysicalProduct",
    `[Digital Product]
${productDemo.digital.info}
Harga Akhir (Getter): ${productDemo.digital.finalPrice}
instanceof Product: ${productDemo.digital.isProductInstance}
instanceof DigitalProduct: ${productDemo.digital.isDigitalInstance}

[Physical Product]
${productDemo.physical.info}
Ongkos Kirim (Getter): ${productDemo.physical.shippingCost}
instanceof Product: ${productDemo.physical.isProductInstance}
instanceof PhysicalProduct: ${productDemo.physical.isPhysicalInstance}`
  );

  // Latihan 4.3: Computed Dynamic Keys
  const dynKeys = latihanComputedPropertyNames();
  addOutput(
    "Latihan 4.3: Computed Property Names (Dynamic Keys)",
    "Penamaan properti objek menggunakan ekspresi runtime",
    JSON.stringify(dynKeys, null, 2)
  );

  // Latihan 4.4: Default Parameters + Destructuring
  const academicBadge = createAcademicCard({ name: "Muhammad Dzaky", nim: "123140039" });
  addOutput(
    "Latihan 4.4: Kombinasi Default Parameters & Destructuring",
    "Fungsi menerima objek opsi dengan nilai bawaan otomatis",
    `Badge: ${academicBadge.badge}
Info: ${academicBadge.statusText}`
  );

  // Latihan 5.1: groupBy menggunakan reduce()
  const groupedData = demoGroupByExercise();
  addOutput(
    "Latihan 5.1: Implementasi Fungsi groupBy() dengan reduce()",
    "Mengelompokkan data array mahasiswa berdasarkan kelas atau peminatan",
    JSON.stringify(groupedData, null, 2)
  );

  // Latihan 5.2: Rata-Rata Objek
  const sampleScores = [
    { name: "PAW", score: 92 },
    { name: "Basis Data", score: 85 },
    { name: "Struktur Data", score: 88 }
  ];
  const avgScore = calculateAverageOfObjects(sampleScores, "score");
  addOutput(
    "Latihan 5.2: Menghitung Rata-Rata Nilai dari Array of Objects",
    "Agregasi nilai properti objek menggunakan reduce()",
    `Data Matakuliah: ${JSON.stringify(sampleScores)}
Rata-rata Nilai: ${avgScore}`
  );

  // Latihan 5.3: Flattening Array
  const flatResult = latihanFlattenNestedArray();
  addOutput(
    "Latihan 5.3: Transformasi Array Bersarang Menjadi Flat",
    "Membandingkan flat(Infinity) dan deep recursive reduce()",
    `Menggunakan .flat(Infinity):
${JSON.stringify(flatResult.flattenedViaMethod, null, 2)}

Menggunakan reduce() rekursif:
${JSON.stringify(flatResult.flattenedViaReduce, null, 2)}`
  );

  // Latihan 5.4: Chaining filter, map, reduce
  const chainAnalysis = latihanComplexArrayChaining();
  addOutput(
    "Latihan 5.4: Pipeline Chaining (filter -> map -> reduce)",
    "Analisis data pengumpulan tugas tepat waktu dan skor akhir",
    `Total Pengumpulan: ${chainAnalysis.allSubmissionsCount}
Tepat Waktu: ${chainAnalysis.onTimeCount}
Daftar Skor Setelah Bonus Ketepatan: ${JSON.stringify(chainAnalysis.gradedList, null, 2)}
Rata-rata Nilai Akhir: ${chainAnalysis.averageFinalScore}`
  );

  // Latihan 6.1: Multi-endpoint Fetch & Combine
  addOutput(
    "Latihan 6.1: Mengambil Data dari Beberapa Endpoint & Menggabungkannya",
    "Paralel Promise.all dari Open-Meteo & DummyJSON API",
    "Mengunduh data secara bersamaan..."
  );
  const multiFetchCard = document.querySelector('.output-item:last-child .result pre');
  const multiFetchResult = await fetchAndCombineEndpoints();
  if (multiFetchCard) {
    multiFetchCard.textContent = JSON.stringify(multiFetchResult, null, 2);
  }

  // Latihan 6.2: Retry dengan Exponential Backoff
  addOutput(
    "Latihan 6.2: Mekanisme Retry dengan Exponential Backoff",
    "Mencoba ulang operasi async saat terjadi kegagalan jaringan",
    "Menjalankan simulasi retry..."
  );
  const retryCard = document.querySelector('.output-item:last-child .result pre');
  try {
    let mockAttempt = 0;
    const retryResult = await fetchWithExponentialBackoff(async (attempt) => {
      mockAttempt = attempt;
      if (attempt < 3) throw new Error(`Simulasi timeout di percobaan ke-${attempt}`);
      return `Sukses pada percobaan ke-${attempt}! Koneksi berhasil dipulihkan.`;
    }, 3, 300);
    if (retryCard) retryCard.textContent = retryResult;
  } catch (err) {
    if (retryCard) retryCard.textContent = `Error: ${err.message}`;
  }

  // Latihan 6.3: Async Error Boundary
  const errorBoundaryTest = await asyncErrorBoundary(async () => {
    throw new Error("Simulasi gagal koneksi ke database cloud");
  }, { status: "offline", message: "Menggunakan cache offline" });
  addOutput(
    "Latihan 6.3: Async Error Boundary",
    "Menangkap error asinkron tanpa mematikan alur aplikasi",
    `Status Sukses: ${errorBoundaryTest.isSuccess}
Error Terperangkap: ${errorBoundaryTest.error}
Fallback Data Digunakan: ${JSON.stringify(errorBoundaryTest.data)}`
  );

  // Latihan 6.4: Pagination dengan Async/Await
  addOutput(
    "Latihan 6.4: Implementasi Pagination Asinkron (JSONPlaceholder)",
    "Mengambil halaman ke-1 dan ke-2 secara bertahap",
    "Mengambil halaman data..."
  );
  const pageCard = document.querySelector('.output-item:last-child .result pre');
  try {
    const page1 = await fetchPaginatedTodos(1, 2);
    const page2 = await fetchPaginatedTodos(2, 2);
    if (pageCard) {
      pageCard.textContent = `Halaman 1: ${JSON.stringify(page1, null, 2)}\n\nHalaman 2: ${JSON.stringify(page2, null, 2)}`;
    }
  } catch (e) {
    if (pageCard) pageCard.textContent = `Error: ${e.message}`;
  }
}

// Initialize control bar event listeners in a robust way
function initControls() {
  console.log('Initializing control bar listeners');
  const runBtn = document.getElementById("runBtn");
  if (runBtn) {
    runBtn.addEventListener("click", () => {
      console.log('Run Demo button clicked');
      runAllDemos();
    });
  }

  const runLatihanBtn = document.getElementById("runLatihanBtn");
  if (runLatihanBtn) {
    runLatihanBtn.addEventListener("click", () => {
      console.log('Run Latihan button clicked');
      runAllLatihan();
    });
  }

  const clearBtn = document.getElementById("clearBtn");
  if (clearBtn) {
    clearBtn.addEventListener("click", () => {
      console.log('Clear button clicked');
      const outputEl = document.getElementById("output");
      if (outputEl) {
        outputEl.innerHTML = `<div class="empty-prompt">Klik tombol <strong>"Run Demo Materi"</strong> atau <strong>"Jalankan Solusi Latihan"</strong> di atas untuk melihat eksekusi kode.</div>`;
      }
    });
  }
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initControls);
} else {
  initControls();
}
