/* ===== 牛排行銷 landing shared JS ===== */
// 名單接收端點:接 n8n webhook / Apps Script 時填入。空字串 = demo 模式(只顯示成功畫面、不送出)。
const FORM_ENDPOINT = "";

// scroll reveal (fade-up on enter)
const io = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
}), { threshold: .12 });
document.querySelectorAll('.reveal,.svc').forEach((el, i) => { el.style.transitionDelay = (i % 5) * 70 + 'ms'; io.observe(el); });

// service card hover background (uses --img if set, else gold gradient)
document.querySelectorAll('.svc .bg').forEach(b => {
  const img = getComputedStyle(b).getPropertyValue('--img').trim();
  b.style.setProperty('--x', img || 'none');
});
const st = document.createElement('style');
st.textContent = '.svc .bg::before{background-image:var(--x, radial-gradient(circle at 20% 20%,rgba(217,189,110,.5),transparent 45%),radial-gradient(circle at 80% 80%,rgba(217,189,110,.4),transparent 45%),linear-gradient(135deg,#2b2620,#5a4a25))}';
document.head.appendChild(st);

// portfolio filter
const fs = document.querySelectorAll('#filters button'), pjs = document.querySelectorAll('.pj');
fs.forEach(b => b.addEventListener('click', () => {
  fs.forEach(x => x.classList.remove('on')); b.classList.add('on');
  const f = b.dataset.f;
  pjs.forEach(p => {
    const ok = f === 'all' || p.dataset.c.split(' ').includes(f);
    p.classList.toggle('hide', !ok);
    if (ok) { p.classList.remove('in'); requestAnimationFrame(() => p.classList.add('in')); }
  });
}));

// mobile menu
document.querySelectorAll('#menu a').forEach(a => a.addEventListener('click', () => document.getElementById('menu').classList.remove('open')));

// lead form
const lf = document.getElementById('leadForm');
if (lf) {
  lf.addEventListener('submit', async e => {
    e.preventDefault();
    const fd = new FormData(lf);
    const data = Object.fromEntries(fd.entries());
    data.services = fd.getAll('services').join(', ');
    data.page = location.pathname;
    data.ts = new Date().toISOString();
    const params = new URLSearchParams(location.search);
    ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content'].forEach(k => { if (params.get(k)) data[k] = params.get(k); });
    const btn = lf.querySelector('button[type=submit]');
    btn.disabled = true; btn.textContent = '送出中…';
    try {
      if (FORM_ENDPOINT) {
        await fetch(FORM_ENDPOINT, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(data) });
      } else {
        console.log('[demo] lead payload', data);
      }
      if (window.dataLayer) window.dataLayer.push({ event: 'generate_lead', form_id: 'bull_lead', services: data.services });
      lf.innerHTML = '<div class="form-ok"><b>已收到,謝謝你!</b><p>我們會在 1 個工作天內與你聯繫,安排 30 分鐘免費診斷。</p>' +
        (FORM_ENDPOINT ? '' : '<small style="color:#8a8378">(demo 模式:尚未接後端,資料未送出)</small>') + '</div>';
    } catch (err) {
      btn.disabled = false; btn.textContent = '再試一次';
      alert('送出失敗,請直接加 LINE 聯繫我們。');
    }
  });
}
