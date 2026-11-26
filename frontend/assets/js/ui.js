(function () {
  const fmtINR = (n) => '₹' + Number(n || 0).toLocaleString('en-IN', { maximumFractionDigits: 2 });
  function badge(status) {
    const map = { approved:'success', verified:'success', confirmed:'success', completed:'success', paid:'success', active:'success', available:'success',
      pending:'warning', payment_pending:'warning', return_requested:'warning', inspection_pending:'warning',
      rejected:'danger', cancelled:'danger', failed:'danger', blocked:'danger', dispute:'danger' };
    const cls = map[status] || 'info';
    return `<span class="badge badge-${cls}">${String(status||'').replace(/_/g,' ')}</span>`;
  }
  function nav(active) {
    const u = Auth.getUser();
    const role = u?.role;
    let links = '';
    if (!u) {
      links = `<a href="/index.html" ${active==='index'?'class="active"':''}>Home</a><a href="/search.html" ${active==='search'?'class="active"':''}>Browse</a>`;
    } else if (role === 'admin') {
      links = `<a href="/admin-dashboard.html" ${active==='dashboard'?'class="active"':''}>Dashboard</a><a href="/admin-users.html" ${active==='users'?'class="active"':''}>KYC & Users</a><a href="/admin-bookings.html" ${active==='bookings'?'class="active"':''}>Bookings</a><a href="/search.html" ${active==='search'?'class="active"':''}>Marketplace</a>`;
    } else {
      // Unified role (customer + owner): can browse, rent, list products, manage requests, track bookings
      links = `
        <a href="/home.html" ${active==='home'?'class="active"':''}>Home</a>
        <a href="/search.html" ${active==='search'?'class="active"':''}>Browse</a>
        <a href="/owner-dashboard.html" ${active==='dashboard'?'class="active"':''}>Dashboard</a>
        <a href="/add-product.html" ${active==='add'?'class="active"':''}>+ List Item</a>
        <a href="/manage-products.html" ${active==='products'?'class="active"':''}>My Listings</a>
        <a href="/booking-requests.html" ${active==='requests'?'class="active"':''}>Rent Requests</a>
        <a href="/my-bookings.html" ${active==='bookings'?'class="active"':''}>My Rentals</a>
        <a href="/profile.html" ${active==='profile'?'class="active"':''}>Profile</a>`;
    }
    const right = u ? `<span class="text-secondary" style="font-size:13px">${u.name} (${u.role})</span><button class="btn btn-outline btn-sm" onclick="Auth.logout()">Logout</button>` : `<a class="btn btn-outline btn-sm" href="/login.html">Login</a><a class="btn btn-primary btn-sm" href="/register.html">Get Started</a>`;
    document.getElementById('app-nav').innerHTML = `
      <div class="topbar"><div class="container topbar-inner">
        <a class="brand" href="${u ? (u.role==='admin'?'/admin-dashboard.html':'/owner-dashboard.html') : '/index.html'}"><span class="brand-mark">R</span>Rentzy</a>
        <nav class="nav">${links}</nav>
        <div class="nav-actions">${right}</div>
      </div></div>`;
  }
  function pageShell(active, content) { nav(active); document.getElementById('app-main').innerHTML = content; }
  function loading(el, msg='Loading...') { el.innerHTML = `<div class="empty">${msg}</div>`; }
  function error(el, err) { el.innerHTML = `<div class="alert alert-danger">${err.message || err}</div>`; }
  window.UI = { fmtINR, badge, nav, pageShell, loading, error };
})();
