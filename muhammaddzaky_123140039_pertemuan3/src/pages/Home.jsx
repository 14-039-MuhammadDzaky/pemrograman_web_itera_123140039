// src/pages/Home.jsx
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useBooks } from '../context/BookContext';
import useBookStats from '../hooks/useBookStats';

const statusOptions = ['semua', 'milik', 'baca', 'beli'];

function Home() {
  const { books, deleteBook } = useBooks();
  const [filter, setFilter] = useState('semua');
  const [search, setSearch] = useState('');

  const filteredBooks = books.filter((b) => {
    const matchesStatus = filter === 'semua' || b.status === filter;
    const matchesSearch =
      b.title.toLowerCase().includes(search.toLowerCase()) ||
      b.author.toLowerCase().includes(search.toLowerCase());
    return matchesStatus && matchesSearch;
  });

  const { total, milik, baca, beli } = useBookStats(books);

  return (
    <section className="home-page dashboard">
      {/* Top bar with Add button */}
      <div className="dashboard-header">
        <h2>📚 Dashboard Buku</h2>
        <Link to="/add" className="btn submit-btn add-btn">
          ➕ Tambah Buku
        </Link>
      </div>

      {/* Statistic cards */}
      <div className="stats-grid">
        <div className="stats-card">
          <h3>Semua</h3>
          <p>{total}</p>
        </div>
        <div className="stats-card">
          <h3>Milik</h3>
          <p>{milik}</p>
        </div>
        <div className="stats-card">
          <h3>Baca</h3>
          <p>{baca}</p>
        </div>
        <div className="stats-card">
          <h3>Beli</h3>
          <p>{beli}</p>
        </div>
      </div>

      {/* Search & filter controls */}
      <div className="controls">
        <input
          type="text"
          placeholder="Cari judul atau penulis"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        <select value={filter} onChange={(e) => setFilter(e.target.value)}>
          {statusOptions.map((opt) => (
            <option key={opt} value={opt}>
              {opt.charAt(0).toUpperCase() + opt.slice(1)}
            </option>
          ))}
        </select>
      </div>

      {/* Book table */}
      <table className="book-table">
        <thead>
          <tr>
            <th>Judul</th>
            <th>Penulis</th>
            <th>Status</th>
            <th>Aksi</th>
          </tr>
        </thead>
        <tbody>
          {filteredBooks.map((book) => (
            <tr key={book.id} className="book-row">
              <td>{book.title}</td>
              <td>{book.author}</td>
              <td>
                <span className="status badge-{book.status}">{book.status}</span>
              </td>
              <td className="actions">
                <Link to={`/edit/${book.id}`} className="btn edit-btn">
                  ✏️ Edit
                </Link>
                <button
                  className="btn delete-btn"
                  onClick={() => deleteBook(book.id)}
                >
                  🗑️ Hapus
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      {filteredBooks.length === 0 && (
        <p className="empty">Tidak ada buku yang cocok.</p>
      )}
    </section>
  );
}

export default Home;
