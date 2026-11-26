(function () {
  const API_BASE = localStorage.getItem('API_BASE') || window.API_BASE || '';
  async function request(path, opts = {}) {
    const token = window.Auth ? window.Auth.getToken() : (function(){ try { return localStorage.getItem('token'); } catch(e) { return null; } })();
    const headers = { 'Content-Type': 'application/json', ...(opts.headers || {}) };
    if (token) headers.Authorization = `Bearer ${token}`;
    const res = await fetch(API_BASE + path, { ...opts, headers });
    const text = await res.text();
    let data;
    try { data = text ? JSON.parse(text) : null; } catch { data = text; }
    if (!res.ok) {
      const msg = (data && (data.detail || data.message)) || res.statusText || 'Request failed';
      const err = new Error(msg);
      err.status = res.status; err.data = data; throw err;
    }
    return data;
  }
  window.API = {
    get: (p) => request(p),
    post: (p, b) => request(p, { method: 'POST', body: JSON.stringify(b) }),
    put: (p, b) => request(p, { method: 'PUT', body: JSON.stringify(b) }),
    patch: (p, b) => request(p, { method: 'PATCH', body: JSON.stringify(b) }),
    del: (p) => request(p, { method: 'DELETE' }),
    base: API_BASE,
  };
})();
