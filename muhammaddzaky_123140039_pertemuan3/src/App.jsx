// src/App.jsx
// Main application router with BookProvider and premium UI.

import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { BookProvider } from './context/BookContext';
import Home from './pages/Home';
import AddBook from './pages/AddBook';
import EditBook from './pages/EditBook';
import './App.css';

function App() {
  return (
    <BookProvider>
      <Router>
        <div className="app-wrapper">
          <aside className="sidebar">
            <h1 className="logo">📚 Book Manager</h1>
            <ul className="nav-links">
              <li><Link to="/">Daftar Buku</Link></li>
              <li><Link to="/add">Tambah Buku</Link></li>
            </ul>
          </aside>
          <main className="main-content">
            <Routes>
              <Route path="/" element={<Home />} />
              <Route path="/add" element={<AddBook />} />
              <Route path="/edit/:id" element={<EditBook />} />
            </Routes>
          </main>
        </div>
        <footer className="footer">© 2026 Book Manager – Dibuat dengan React & Vite</footer>
      </Router>
    </BookProvider>
  );
}

export default App;
