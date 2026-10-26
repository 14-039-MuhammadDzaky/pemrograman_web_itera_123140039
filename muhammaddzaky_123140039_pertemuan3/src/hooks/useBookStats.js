// src/hooks/useBookStats.js
import { useMemo } from 'react';
/**
 * Custom hook that calculates book statistics.
 * Returns total count and counts per status.
 * @param {Array} books - array of book objects
 */
export default function useBookStats(books) {
  return useMemo(() => {
    const total = books.length;
    const milik = books.filter((b) => b.status === 'milik').length;
    const baca = books.filter((b) => b.status === 'baca').length;
    const beli = books.filter((b) => b.status === 'beli').length;
    return { total, milik, baca, beli };
  }, [books]);
}
