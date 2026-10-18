/**
 * ============================================================================
 * MODUL PRAKTIKUM PAW - PERTEMUAN 2
 * Berkas: js/app.js
 * Kumpulan Fungsi Demo ES6+ (Next Gen JavaScript)
 * Mahasiswa: Muhammad Dzaky (123140039) - RA
 * ============================================================================
 */

// ----------------------------------------------------------------------------
// 1. Let dan Const (demoVariables)
// ----------------------------------------------------------------------------
export function demoVariables() {
  // var: function scope
  var oldVar = "Variabel var lama (function scoped)";
  if (true) {
    var oldVar = "var tertimpa di dalam block";
  }

  // let: block scope
  let newLet = "Variabel let awal";
  if (true) {
    let newLet = "let baru terisolasi di dalam block";
  }

  // const: tidak bisa di-reassign
  const PI = 3.14159;

  // const object: referensinya konstan tapi isinya tetap mutable
  const user = {
    name: "Muhammad Dzaky",
    nim: "123140039"
  };
  user.role = "Mahasiswa ITERA"; // mutasi properti diperbolehkan

  return {
    oldVar,
    newLet,
    PI,
    user
  };
}

// ----------------------------------------------------------------------------
// 2. Arrow Functions (demoArrowFunctions)
// ----------------------------------------------------------------------------
export function demoArrowFunctions() {
  // Regular function
  function regularSum(a, b) {
    return a + b;
  }

  // Arrow function lengkap dengan kurung kurawal & return
  const arrowSum = (a, b) => {
    return a + b;
  };

  // Short arrow function (implisit return satu baris)
  const shortArrowSum = (a, b) => a + b;

  // Arrow function tanpa parameter
  const sayHello = () => "Halo dari Arrow Function!";

  // Arrow function dengan parameter tunggal (tanpa tanda kurung wajib)
  const square = x => x * x;

  return {
    regularSum: regularSum(5, 3),
    arrowSum: arrowSum(5, 3),
    shortArrowSum: shortArrowSum(5, 3),
    sayHello: sayHello(),
    square: square(4)
  };
}

// ----------------------------------------------------------------------------
// 3. Template Literals (demoTemplateLiterals)
// ----------------------------------------------------------------------------
export function demoTemplateLiterals() {
  const name = "John";
  const age = 30;

  // String concatenation cara lama
  const oldWay = "Nama saya " + name + " dan umur saya " + age + " tahun.";

  // Template literals (ES6)
  const newWay = `Nama saya ${name} dan umur saya ${age} tahun.`;

  // Template literals multi-baris
  const multiLine = `
    Ini adalah string multi-baris.
    Sangat berguna untuk HTML template.
    Nama: ${name}
    Umur: ${age}
  `;

  // Template literals dengan ekspresi
  const expression = `Tahun lahir: ${new Date().getFullYear() - age}`;

  return {
    oldWay,
    newWay,
    multiLine,
    expression
  };
}

// ----------------------------------------------------------------------------
// 4. Destructuring (demoDestructuring)
// ----------------------------------------------------------------------------
export function demoDestructuring() {
  // Object destructuring
  const person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    email: "john@example.com",
    address: {
      city: "Jakarta",
      postalCode: "12345"
    }
  };

  // Basic destructuring
  const { firstName, lastName } = person;

  // Destructuring dengan nama variabel baru
  const { firstName: fName, lastName: lName } = person;

  // Destructuring dengan nilai default
  const { hobby = "coding" } = person;

  // Nested destructuring
  const { address: { city, postalCode } } = person;

  // Array destructuring
  const colors = ["red", "green", "blue", "yellow", "purple"];

  // Basic array destructuring
  const [firstColor, secondColor] = colors;

  // Skip elements
  const [, , thirdColor] = colors;

  // Rest pattern dalam array destructuring
  const [primary, secondary, ...restColors] = colors;

  // Swap variables menggunakan destructuring
  let a = 1;
  let b = 2;
  [a, b] = [b, a];

  return {
    objectBasic: { firstName, lastName },
    objectRenamed: { fName, lName },
    objectDefault: hobby,
    objectNested: { city, postalCode },
    arrayBasic: { firstColor, secondColor },
    arraySkipped: thirdColor,
    arrayRest: { primary, secondary, restColors },
    swapped: { a, b }
  };
}

// ----------------------------------------------------------------------------
// 5. Spread dan Rest Operators (demoSpreadRest)
// ----------------------------------------------------------------------------
export function demoSpreadRest() {
  // Spread operator dengan array
  const numbers = [1, 2, 3];
  const moreNumbers = [...numbers, 4, 5];

  // Copy array dengan spread
  const numbersCopy = [...numbers];

  // Merge arrays
  const array1 = [1, 2, 3];
  const array2 = [4, 5, 6];
  const mergedArray = [...array1, ...array2];

  // Spread operator dengan objek
  const person = {
    name: "John",
    age: 30
  };

  // Copy objek
  const personCopy = { ...person };

  // Extend objek
  const extendedPerson = {
    ...person,
    email: "john@example.com",
    age: 31 // Override properti yang ada
  };

  // Rest parameter dalam fungsi
  function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
  }

  // Rest parameter dengan parameter reguler
  function process(first, second, ...rest) {
    return {
      first,
      second,
      rest
    };
  }

  return {
    spreadArray: moreNumbers,
    copyArray: numbersCopy,
    mergedArrays: mergedArray,
    spreadObject: extendedPerson,
    restSum: sum(1, 2, 3, 4, 5),
    restProcess: process("a", "b", "c", "d", "e")
  };
}

// ----------------------------------------------------------------------------
// 6. Default Parameters (demoDefaultParams)
// ----------------------------------------------------------------------------
export function demoDefaultParams() {
  // Cara lama (ES5)
  function greetOld(name, greeting) {
    name = name || "Guest";
    greeting = greeting || "Hello";
    return `${greeting}, ${name}!`;
  }

  // Dengan default parameters (ES6)
  function greet(name = "Guest", greeting = "Hello") {
    return `${greeting}, ${name}!`;
  }

  // Default parameters dengan ekspresi
  function createUser(name, role = "user", createdAt = new Date().toISOString()) {
    return { name, role, createdAt };
  }

  // Default parameters bisa menggunakan parameter sebelumnya
  function createOrder(product, quantity = 1, price = 500000, total = price * quantity) {
    return { product, quantity, price, total };
  }

  return {
    oldWay: greetOld(),
    oldWayParams: greetOld("John", "Hi"),
    newWay: greet(),
    newWayParams: greet("John", "Hi"),
    withExpression: createUser("Alice"),
    usingPrevious: createOrder("Laptop", 2, 1000000)
  };
}

// ----------------------------------------------------------------------------
// 7. ES6 Classes (demoClasses)
// ----------------------------------------------------------------------------
export function demoClasses() {
  // Definisi class
  class User {
    // Constructor
    constructor(name, email) {
      this.name = name;
      this.email = email;
      this.createdAt = new Date();
    }
    
    // Methods
    getInfo() {
      return `${this.name} (${this.email})`;
    }
    
    getCreatedDate() {
      return this.createdAt.toLocaleDateString();
    }
  }

  // Inheritance
  class Admin extends User {
    constructor(name, email, role = "admin") {
      // Memanggil constructor parent class
      super(name, email);
      this.role = role;
    }
    
    // Override method
    getInfo() {
      return `${this.name} (${this.email}) - ${this.role}`;
    }
    
    // Admin method
    hasAccess(module) {
      return true; // Untuk contoh, admin selalu punya akses
    }
  }

  // Instances
  const user = new User("John Doe", "john@example.com");
  const admin = new Admin("Admin User", "admin@example.com");

  return {
    user: {
      info: user.getInfo(),
      createdDate: user.getCreatedDate()
    },
    admin: {
      info: admin.getInfo(),
      createdDate: admin.getCreatedDate(),
      hasAccess: admin.hasAccess("dashboard")
    },
    isUserInstance: user instanceof User,
    isAdminInstance: admin instanceof User // true karena inheritance
  };
}

// ----------------------------------------------------------------------------
// 8. Enhanced Object Literals (demoObjectLiterals)
// ----------------------------------------------------------------------------
export function demoObjectLiterals() {
  // Property shorthand
  const name = "John";
  const age = 30;

  // Cara lama
  const oldPerson = {
    name: name,
    age: age,
    sayHello: function() {
      return "Hello!";
    }
  };

  // Object literal modern (ES6)
  const newPerson = {
    name,
    age,
    // Method shorthand
    sayHello() {
      return "Hello!";
    },
    // Computed property names
    ["skill_" + 1]: "JavaScript",
    ["skill_" + 2]: "React"
  };

  // Combining with other features
  const prefix = "user";
  const userData = {
    [`${prefix}_id`]: 123,
    [`${prefix}_name`]: "john_doe",
    [Date.now()]: "timestamp"
  };

  return {
    oldWay: oldPerson,
    newWay: newPerson,
    methods: {
      old: oldPerson.sayHello(),
      new: newPerson.sayHello()
    },
    computedProps: {
      skill1: newPerson.skill_1,
      skill2: newPerson.skill_2
    },
    dynamicProps: userData
  };
}

// ----------------------------------------------------------------------------
// 9. Modern Array Methods (demoArrayMethods)
// ----------------------------------------------------------------------------
export function demoArrayMethods() {
  // Data contoh
  const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  const users = [
    { id: 1, name: "John", age: 25, active: true },
    { id: 2, name: "Jane", age: 30, active: false },
    { id: 3, name: "Bob", age: 22, active: true },
    { id: 4, name: "Alice", age: 28, active: true },
    { id: 5, name: "Charlie", age: 35, active: false }
  ];

  // map
  const doubled = numbers.map(num => num * 2);

  // filter
  const evenNumbers = numbers.filter(num => num % 2 === 0);
  const activeUsers = users.filter(user => user.active);

  // find
  const userJane = users.find(user => user.name === "Jane");

  // some dan every
  const hasAdult = users.some(user => user.age >= 18);
  const allAdults = users.every(user => user.age >= 18);

  // reduce
  const sum = numbers.reduce((total, num) => total + num, 0);
  const oldest = users.reduce((oldest, user) => 
    user.age > oldest.age ? user : oldest, users[0]);

  // Menggabungkan methods (chaining)
  const activeUsersNames = users
    .filter(user => user.active)
    .map(user => user.name);

  const totalActiveAge = users
    .filter(user => user.active)
    .reduce((sum, user) => sum + user.age, 0);

  return {
    map: doubled,
    filter: {
      evenNumbers,
      activeUsers: activeUsers.length
    },
    find: userJane,
    some: hasAdult,
    every: allAdults,
    reduce: {
      sum,
      oldest: oldest.name
    },
    chaining: {
      activeUsersNames,
      totalActiveAge
    }
  };
}

// ----------------------------------------------------------------------------
// 10. Advanced Arrays (demoAdvancedArrays)
// ----------------------------------------------------------------------------
export function demoAdvancedArrays() {
  const numbers = [1, 2, 3, 4, 5];

  // Clone dan concat
  const numbersCopy = [...numbers];
  const moreNumbers = [...numbers, 6, 7, 8];
  const combinedArrays = [...numbers, ...[6, 7, 8, 9]];

  // Array.from
  const fromIterable = Array.from("hello");
  const withMapFn = Array.from(numbers, n => n * n);

  // Array.of
  const newArray = Array.of(1, "two", { three: 3 });

  // Flat dan FlatMap
  const nestedArrays = [1, [2, 3], [[4, 5], 6]];
  const flattened = nestedArrays.flat();
  const deepFlattened = nestedArrays.flat(2);

  const flatMapped = numbers.flatMap(n => [n, n * 2]);

  // Includes
  const hasThree = numbers.includes(3);

  return {
    clone: numbersCopy,
    concat: {
      moreNumbers,
      combinedArrays
    },
    arrayFrom: {
      fromIterable,
      withMapFn
    },
    arrayOf: newArray,
    flatAndFlatMap: {
      flattened,
      deepFlattened,
      flatMapped
    },
    includes: hasThree
  };
}

// ----------------------------------------------------------------------------
// 11. Promises (demoPromises)
// ----------------------------------------------------------------------------
export function demoPromises() {
  // Simulasi operasi asinkron dengan Promise
  function fetchData(id) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (id > 0) {
          resolve({ id, name: `User ${id}`, success: true });
        } else {
          reject(new Error("ID tidak valid"));
        }
      }, 1000);
    });
  }

  // Buat elemen untuk update promise
  const outputDiv = document.createElement('div');
  outputDiv.className = 'promise-outputs';

  const createPromiseElement = (id, label) => {
    const el = document.createElement('div');
    el.className = 'promise-result';
    el.innerHTML = `<strong>${label}:</strong> <span id="${id}">Memuat...</span>`;
    outputDiv.appendChild(el);
  };

  createPromiseElement('promise-basic', 'Promise Dasar');
  createPromiseElement('promise-chain', 'Promise Chain');
  createPromiseElement('promise-all', 'Promise.all');
  createPromiseElement('promise-race', 'Promise.race');

  // Penggunaan Promise dasar
  fetchData(1)
    .then(data => {
      const el = document.getElementById('promise-basic');
      if (el) el.textContent = `Sukses: ${JSON.stringify(data)}`;
    })
    .catch(err => {
      const el = document.getElementById('promise-basic');
      if (el) el.textContent = `Error: ${err.message}`;
    });

  // Promise chaining
  fetchData(2)
    .then(user => {
      return fetchData(3).then(secondUser => `${user.name} & ${secondUser.name}`);
    })
    .then(combined => {
      const el = document.getElementById('promise-chain');
      if (el) el.textContent = `Dapat user berantai: ${combined}`;
    })
    .catch(err => {
      const el = document.getElementById('promise-chain');
      if (el) el.textContent = `Error: ${err.message}`;
    });

  // Promise.all
  Promise.all([fetchData(4), fetchData(5), fetchData(6)])
    .then(results => {
      const el = document.getElementById('promise-all');
      if (el) el.textContent = `Semua selesai: ${results.map(r => r.name).join(', ')}`;
    })
    .catch(err => {
      const el = document.getElementById('promise-all');
      if (el) el.textContent = `Error di salah satu: ${err.message}`;
    });

  // Promise.race
  Promise.race([
    fetchData(7),
    fetchData(8),
    new Promise((_, reject) => 
      setTimeout(() => reject(new Error("Timeout")), 1500))
  ])
    .then(winner => {
      const el = document.getElementById('promise-race');
      if (el) el.textContent = `Pemenang race: ${winner.name}`;
    })
    .catch(err => {
      const el = document.getElementById('promise-race');
      if (el) el.textContent = `Error race: ${err.message}`;
    });

  return outputDiv;
}

// ----------------------------------------------------------------------------
// 12. Async/Await (demoAsyncAwait)
// ----------------------------------------------------------------------------
export function demoAsyncAwait() {
  // Simulasi API call
  function fetchUser(id) {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        if (id > 0) {
          resolve({ 
            id, 
            name: `User ${id}`, 
            email: `user${id}@example.com` 
          });
        } else {
          reject(new Error("ID user tidak valid"));
        }
      }, 1000);
    });
  }

  function fetchUserPosts(userId) {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve([
          { id: 1, title: "Post 1", body: "Konten untuk post 1" },
          { id: 2, title: "Post 2", body: "Konten untuk post 2" },
        ]);
      }, 800);
    });
  }

  // Menggunakan async/await
  async function getUserData(id) {
    try {
      const user = await fetchUser(id);
      const posts = await fetchUserPosts(user.id);
      return {
        user,
        posts,
        success: true
      };
    } catch (error) {
      return {
        error: error.message,
        success: false
      };
    }
  }

  // Eksekusi paralel dengan async/await
  async function getMultipleUsers(ids) {
    try {
      // Jalankan promises secara paralel
      const userPromises = ids.map(id => fetchUser(id));
      const users = await Promise.all(userPromises);
      
      // Dapatkan posts untuk semua user secara paralel
      const postPromises = users.map(user => fetchUserPosts(user.id));
      const allPosts = await Promise.all(postPromises);
      
      // Gabungkan hasil
      return users.map((user, i) => ({
        user,
        posts: allPosts[i]
      }));
    } catch (error) {
      return { error: error.message };
    }
  }

  // Buat elemen untuk menampilkan hasil
  const outputDiv = document.createElement('div');
  outputDiv.className = 'async-outputs';

  // Contoh async/await dasar
  const basicAsyncResult = document.createElement('div');
  basicAsyncResult.className = 'async-result';
  basicAsyncResult.innerHTML = '<strong>User Tunggal:</strong> Memuat...';
  outputDiv.appendChild(basicAsyncResult);

  // Contoh async/await paralel
  const parallelAsyncResult = document.createElement('div');
  parallelAsyncResult.className = 'async-result';
  parallelAsyncResult.innerHTML = '<strong>Beberapa User:</strong> Memuat...';
  outputDiv.appendChild(parallelAsyncResult);

  // Jalankan dan update UI
  getUserData(42).then(result => {
    if (result.success) {
      basicAsyncResult.innerHTML = `
        <strong>User Tunggal:</strong> ${result.user.name} (${result.user.email}) | 
        Posts: ${result.posts.length} buah
      `;
    } else {
      basicAsyncResult.innerHTML = `<strong>Error:</strong> ${result.error}`;
    }
  });

  getMultipleUsers([101, 102, 103]).then(results => {
    if (!results.error) {
      parallelAsyncResult.innerHTML = `
        <strong>Beberapa User (Paralel):</strong> 
        ${results.map(r => r.user.name).join(', ')} |
        Total posts: ${results.reduce((sum, r) => sum + r.posts.length, 0)} buah
      `;
    } else {
      parallelAsyncResult.innerHTML = `<strong>Error:</strong> ${results.error}`;
    }
  });

  return outputDiv;
}
