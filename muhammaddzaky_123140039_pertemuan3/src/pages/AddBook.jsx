// src/pages/AddBook.jsx
import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useBooks } from '../context/BookContext';
import PropTypes from 'prop-types';

const statusOptions = ['milik', 'baca', 'beli'];

function AddBook() {
  const { addBook } = useBooks();
  const navigate = useNavigate();
  const [form, setForm] = useState({ title: '', author: '', status: '' });
  const [errors, setErrors] = useState({});

  const validate = () => {
    const newErrors = {};
    if (!form.title.trim()) newErrors.title = 'Judul wajib diisi';
    if (!form.author.trim()) newErrors.author = 'Penulis wajib diisi';
    if (!form.status) newErrors.status = 'Status wajib dipilih';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validate()) return;
    addBook(form);
    navigate('/');
  };

  return (
    <section className="add-book-page card">
      <div className="form-header">
        <h2>Tambah Buku Baru</h2>
      </div>
      <form className="book-form" onSubmit={handleSubmit} noValidate>
        <div className="form-group">
          <label htmlFor="title">Judul</label><br />
          <input
            type="text"
            id="title"
            name="title"
            value={form.title}
            onChange={handleChange}
            className={errors.title ? 'error' : ''}
          />
          {errors.title && <span className="error-msg">{errors.title}</span>}
        </div>
        <div className="form-group">
          <label htmlFor="author">Penulis</label><br />
          <input
            type="text"
            id="author"
            name="author"
            value={form.author}
            onChange={handleChange}
            className={errors.author ? 'error' : ''}
          />
          {errors.author && <span className="error-msg">{errors.author}</span>}
        </div>
        <div className="form-group">
          <label htmlFor="status">Status</label><br />
          <select
            id="status"
            name="status"
            value={form.status}
            onChange={handleChange}
            className={errors.status ? 'error' : ''}
          >
            {statusOptions.map((opt) => (
              <option key={opt} value={opt}>
                {opt.charAt(0).toUpperCase() + opt.slice(1)}
              </option>
            ))}
          </select>
          {errors.status && <span className="error-msg">{errors.status}</span>}
        </div>
        <button type="submit" className="btn submit-btn">
          Simpan
        </button>

        <Link to="/" className="btn edit-btn back-btn">← Kembali</Link><br />
      </form>
    </section>
  );
}

AddBook.propTypes = {};

export default AddBook;
