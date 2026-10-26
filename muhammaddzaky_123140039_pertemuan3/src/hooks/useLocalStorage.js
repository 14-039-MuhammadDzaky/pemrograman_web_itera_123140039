// src/hooks/useLocalStorage.js
import { useState, useEffect } from 'react';

/**
 * Custom hook that syncs a state value with localStorage.
 * @param {string} key - The localStorage key.
 * @param {*} initialValue - Initial value if nothing is stored.
 * @returns {[any, function]} - Current value and setter that also updates localStorage.
 */
export default function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.warn('useLocalStorage: error reading from localStorage', error);
      return initialValue;
    }
  });

  useEffect(() => {
    try {
      window.localStorage.setItem(key, JSON.stringify(storedValue));
    } catch (error) {
      console.warn('useLocalStorage: error writing to localStorage', error);
    }
  }, [key, storedValue]);

  return [storedValue, setStoredValue];
}
