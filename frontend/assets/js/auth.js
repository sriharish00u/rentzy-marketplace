(function () {
  const memoryStore = {};
  function storageAvailable() {
    try {
      const test = '__storage_test__';
      localStorage.setItem(test, test);
      localStorage.removeItem(test);
      return true;
    } catch (e) {
      return false;
    }
  }

  const hasStorage = storageAvailable();

  function getItem(k) {
    if (hasStorage) {
      try { return localStorage.getItem(k); } catch (e) { return memoryStore[k] || null; }
    }
    return memoryStore[k] || null;
  }

  function setItem(k, v) {
    try {
      localStorage.setItem(k, v);
      return;
    } catch (e) {
      // Catch DOMException / QuotaExceededError
      try {
        localStorage.clear();
        localStorage.setItem(k, v);
        return;
      } catch (err2) {
        console.warn('LocalStorage unavailable or quota reached, using in-memory store.');
      }
    }
    memoryStore[k] = v;
    try { sessionStorage.setItem(k, v); } catch (_) {}
  }

  function removeItem(k) {
    if (hasStorage) {
      try { localStorage.removeItem(k); } catch (_) {}
    }
    delete memoryStore[k];
    try { sessionStorage.removeItem(k); } catch (_) {}
  }

  function getUser() { try { return JSON.parse(getItem('user') || 'null'); } catch { return null; } }
  function getToken() { return getItem('token'); }
  function setSession(token, user) { setItem('token', token); setItem('user', JSON.stringify(user)); }
  function clear() { removeItem('token'); removeItem('user'); }
  function isLoggedIn() { return !!getToken(); }
  function role() { const u = getUser(); return u ? u.role : null; }
  function requireAuth(roles) {
    const u = getUser();
    if (!u || !getToken()) { location.href = '/login.html'; return null; }
    if (roles && !roles.includes(u.role)) {
      location.href = u.role === 'admin' ? '/admin-dashboard.html' : u.role === 'owner' ? '/owner-dashboard.html' : '/home.html';
      return null;
    }
    return u;
  }
  function logout() { clear(); location.href = '/login.html'; }
  window.Auth = { getUser, getToken, setSession, clear, isLoggedIn, role, requireAuth, logout, getItem, setItem, removeItem };
})();
