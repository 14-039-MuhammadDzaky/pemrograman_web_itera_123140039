// src/context/BookContext.jsx
import React, { createContext, useContext, useState, useEffect } from 'react';
import PropTypes from 'prop-types';
import useLocalStorage from '../hooks/useLocalStorage';

// Define book shape for PropTypes
export const BookPropType = PropTypes.shape({
  id: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  author: PropTypes.string.isRequired,
  status: PropTypes.oneOf(['milik', 'baca', 'beli']).isRequired,
});

const BookContext = createContext();

export const BookProvider = ({ children }) => {
  // Persist books in localStorage under key 'books'
  const [books, setBooks] = useLocalStorage('books', []);

  // Add a new book
  const addBook = (book) => {
    setBooks((prev) => [...prev, { ...book, id: Date.now().toString() }]);
  };

  // Edit existing book by id
  const editBook = (id, updated) => {
    setBooks((prev) =>
      prev.map((b) => (b.id === id ? { ...b, ...updated } : b))
    );
  };

  // Delete a book
  const deleteBook = (id) => {
    setBooks((prev) => prev.filter((b) => b.id !== id));
  };

  // Provide context value
  const value = {
    books,
    addBook,
    editBook,
    deleteBook,
  };

  return <BookContext.Provider value={value}>{children}</BookContext.Provider>;
};

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
};

export const useBooks = () => useContext(BookContext);
