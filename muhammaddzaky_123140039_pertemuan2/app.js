// ---------- OOP Classes ----------
class CourseItem {
  constructor(id, day, start, end, title, room) {
    this.id = id; // unique identifier
    this.day = day;
    this.start = start;
    this.end = end;
    this.title = title;
    this.room = room;
  }
}

class DashboardApp {
  constructor() {
    this.storageKey = 'dzaky-dashboard-schedule';
    this.schedule = [];
    this.editingId = null;
    // Bind UI elements
    this.form = document.getElementById('schedule-form');
    this.weatherDiv = document.getElementById('weather');
    this.cancelBtn = document.getElementById('cancel-edit');
    this.formTitle = document.getElementById('form-title');
    // Event listeners
    this.form.addEventListener('submit', e => this.handleSubmit(e));
    this.cancelBtn.addEventListener('click', () => this.resetForm());
    // Init
    this.loadFromStorage();
    this.renderSchedule();
    this.fetchWeather();
  }

  // ---------- Local Storage ----------
  loadFromStorage() {
    const raw = localStorage.getItem(this.storageKey);
    if (raw) {
      try {
        const arr = JSON.parse(raw);
        this.schedule = arr.map(item => new CourseItem(item.id, item.day, item.start, item.end, item.title, item.room));
      } catch (e) {
        console.error('Failed to parse schedule from storage', e);
        this.schedule = [];
      }
    }
    if (this.schedule.length === 0) {
      this.populateDefaultData();
    }
  }

  saveToStorage() {
    localStorage.setItem(this.storageKey, JSON.stringify(this.schedule));
  }

  populateDefaultData() {
    const defaultData = [
      { day: 'Senin', start: '13:55', end: '15:30', title: 'SI Kesehatan RA', room: 'GK2. 125' },
      { day: 'Selasa', start: '07:30', end: '10:10', title: 'PengWEB', room: 'GK2. 405' },
      { day: 'Rabu', start: '13:00', end: '15:30', title: 'Energi Angin', room: 'GK2. 228' },
      { day: 'Kamis', start: '09:20', end: '12:00', title: 'MahaData', room: 'GK2. 220' },
      { day: 'Kamis', start: '13:00', end: '15:40', title: 'STM', room: 'GK2. 222' },
      { day: 'Jumat', start: '13:00', end: '15:40', title: 'PPL', room: '-' },
    ];
    this.schedule = defaultData.map((data, idx) => new CourseItem(`id-${Date.now()}-${idx}`, data.day, data.start, data.end, data.title, data.room));
    this.saveToStorage();
  }

  // ---------- CRUD Operations ----------
  addCourse(item) {
    this.schedule.push(item);
    this.saveToStorage();
    this.renderSchedule();
  }

  updateCourse(updatedItem) {
    this.schedule = this.schedule.map(item => (item.id === updatedItem.id ? updatedItem : item));
    this.saveToStorage();
    this.renderSchedule();
  }

  deleteCourse(id) {
    this.schedule = this.schedule.filter(item => item.id !== id);
    this.saveToStorage();
    this.renderSchedule();
  }

  // ---------- Form Handling ----------
  handleSubmit(e) {
    e.preventDefault();
    const day = document.getElementById('day').value;
    const start = document.getElementById('start').value;
    const end = document.getElementById('end').value;
    const title = document.getElementById('course').value.trim();
    const room = document.getElementById('room').value.trim();
    if (this.editingId) {
      const updated = new CourseItem(this.editingId, day, start, end, title, room);
      this.updateCourse(updated);
    } else {
      const id = `id-${Date.now()}`;
      const newItem = new CourseItem(id, day, start, end, title, room);
      this.addCourse(newItem);
    }
    this.resetForm();
  }

  resetForm() {
    this.form.reset();
    this.editingId = null;
    this.cancelBtn.classList.add('hidden');
    this.formTitle.textContent = 'Tambah Jadwal';
  }

  // ---------- UI Rendering ----------
  renderSchedule() {
    const calendar = document.getElementById('calendar-container');
    calendar.innerHTML = '';
    const daysOrder = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu'];
    daysOrder.forEach(day => {
      const col = document.createElement('div');
      col.className = 'flex flex-col gap-2';
      const header = document.createElement('h3');
      header.className = 'text-xl font-bold text-center border-b pb-1 mb-2';
      header.textContent = day;
      col.appendChild(header);

      const items = this.schedule.filter(it => it.day === day);
      items.sort((a, b) => a.start.localeCompare(b.start));
      items.forEach(item => {
        const card = document.createElement('div');
        card.className = 'border border-primary rounded-lg p-3 bg-white shadow-sm flex flex-col gap-1';
        card.innerHTML = `
          <p class="font-medium text-lg">${item.title}</p>
          <p class="text-sm text-gray-600">${item.start} - ${item.end}</p>
          <p class="text-sm text-gray-500">${item.room}</p>
          <div class="flex justify-end space-x-2 mt-1">
            <button data-id="${item.id}" class="edit btn text-blue-600 hover:underline text-sm">Edit</button>
            <button data-id="${item.id}" class="delete btn text-red-600 hover:underline text-sm">Hapus</button>
          </div>
        `;
        col.appendChild(card);
      });
      calendar.appendChild(col);
    });
    calendar.querySelectorAll('.edit').forEach(btn => {
      btn.addEventListener('click', () => this.startEdit(btn.dataset.id));
    });
    calendar.querySelectorAll('.delete').forEach(btn => {
      btn.addEventListener('click', () => {
        if (confirm('Yakin ingin menghapus jadwal ini?')) this.deleteCourse(btn.dataset.id);
      });
    });
  }

  startEdit(id) {
    const item = this.schedule.find(it => it.id === id);
    if (!item) return;
    document.getElementById('day').value = item.day;
    document.getElementById('start').value = item.start;
    document.getElementById('end').value = item.end;
    document.getElementById('course').value = item.title;
    document.getElementById('room').value = item.room;
    this.editingId = id;
    this.cancelBtn.classList.remove('hidden');
    this.formTitle.textContent = 'Edit Jadwal';
  }

  // ---------- Weather Widget ----------
  async fetchWeather() {
    try {
      const response = await fetch('https://api.open-meteo.com/v1/forecast?latitude=-5.36&longitude=105.31&current_weather=true');
      const data = await response.json();
      const { temperature, windspeed, weathercode } = data.current_weather;
      const weatherInfo = `⛅ ${temperature}°C, Angin ${windspeed} m/s`;
      this.weatherDiv.textContent = weatherInfo;
    } catch (err) {
      console.error('Weather fetch error', err);
    }
  }
}

document.addEventListener('DOMContentLoaded', () => new DashboardApp());
