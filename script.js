function updateToggleLabel() {
  const isLight = document.getElementById('root').classList.contains('light');
  document.querySelectorAll('.toggle-btn').forEach(btn => {
    btn.innerHTML = isLight
      ? '<span class="toggle-icon">☾</span> DARK'
      : '<span class="toggle-icon">☀</span> LIGHT';
  });
}

function initTheme() {
  const saved = localStorage.getItem('theme');
  if (saved === 'light') {
    document.getElementById('root').classList.add('light');
    document.body.classList.add('light');
  }
  updateToggleLabel();
}

function toggleTheme() {
  const isLight = document.getElementById('root').classList.contains('light');
  if (isLight) {
    document.getElementById('root').classList.remove('light');
    document.body.classList.remove('light');
    localStorage.setItem('theme', 'dark');
  } else {
    document.getElementById('root').classList.add('light');
    document.body.classList.add('light');
    localStorage.setItem('theme', 'light');
  }
  updateToggleLabel();
}

initTheme();

// ── HALFTONE HERO ──
(function() {
  function drawHalftone() {
    const canvas = document.getElementById('halftone-hero');
    if (!canvas) return;
    const W = canvas.offsetWidth || 800;
    const H = canvas.offsetHeight || 220;
    canvas.width = W; canvas.height = H;
    const ctx = canvas.getContext('2d');
    const isDark = !document.getElementById('root').classList.contains('light');
    ctx.fillStyle = isDark ? '#0a0a0a' : '#e8e2d6';
    ctx.fillRect(0, 0, W, H);
    const spacing = 8;
    const cols = Math.ceil(W / spacing);
    const rows = Math.ceil(H / spacing);
        // Brain/head silhouette centered slightly right and up
        const cx = W * 0.7, cy = H * 0.48;
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const x = c * spacing + spacing / 2;
        const y = r * spacing + spacing / 2;
        const dx = (x - cx) / (W * 0.36);
        const dy = (y - cy) / (H * 0.58);
        const dist = Math.sqrt(dx * dx + dy * dy);
        const nx = (x - cx) / 70;
        const ny = (y - cy) / 70;
        const noise = Math.sin(nx * 3.2) * Math.cos(ny * 2.8) * 0.28
                    + Math.sin(nx * 5.1 + 1.3) * Math.cos(ny * 4.2) * 0.18
                    + Math.sin(nx * 1.9 + ny * 2.2) * 0.12;
        if (dist > 1.0 + noise * 0.35) continue;
        const tone = Math.max(0, 1 - dist * 0.75) + noise * 0.2;
        const r_dot = Math.min(spacing * 0.46, tone * spacing * 0.5);
        if (r_dot < 0.5) continue;
        // teal → maroon gradient top to bottom
        const t = y / H;
        let rr, gg, bb;
        if (isDark) {
          rr = Math.round(74  + (134 - 74)  * t);
          gg = Math.round(122 + (31  - 122) * t);
          bb = Math.round(90  + (65  - 90)  * t);
        } else {
          rr = Math.round(140 + (190 - 140) * t);
          gg = Math.round(190 + (140 - 190) * t);
          bb = Math.round(170 + (155 - 170) * t);
        }
        ctx.beginPath();
        ctx.arc(x, y, r_dot, 0, Math.PI * 2);
        ctx.fillStyle = `rgb(${rr},${gg},${bb})`;
        ctx.fill();
      }
    }
  }
  // Draw after layout settles
  setTimeout(drawHalftone, 50);
  window.addEventListener('resize', drawHalftone);
// Redraw on theme toggle
  const origToggle = window.toggleTheme;
  window.toggleTheme = function() { origToggle(); setTimeout(drawHalftone, 50); };
  // Redraw after initTheme (runs after halftone setup)
  setTimeout(drawHalftone, 60);
 })();


// ── CONTENT ALIGNMENT TOGGLE ──
(function() {
  const col = document.querySelector('.project-col');
  if (!col) return;

  const saved = localStorage.getItem('content-align') || 'center';
  if (saved === 'left') col.classList.add('project-col--left');

  const bar = document.createElement('div');
  bar.className = 'align-control-bar';

  const label = document.createElement('span');
  label.className = 'align-control-label';
  label.textContent = 'text alignment';

  const wrap = document.createElement('div');
  wrap.className = 'align-toggle';

  const btnLeft = document.createElement('button');
  btnLeft.className = 'align-btn';
  btnLeft.title = 'Left align';
  btnLeft.textContent = '⇤';

  const btnCenter = document.createElement('button');
  btnCenter.className = 'align-btn';
  btnCenter.title = 'Center';
  btnCenter.textContent = '⊙';

  function updateActive() {
    const isLeft = col.classList.contains('project-col--left');
    btnLeft.classList.toggle('active', isLeft);
    btnCenter.classList.toggle('active', !isLeft);
  }

  btnLeft.addEventListener('click', function() {
    col.classList.add('project-col--left');
    localStorage.setItem('content-align', 'left');
    updateActive();
  });

  btnCenter.addEventListener('click', function() {
    col.classList.remove('project-col--left');
    localStorage.setItem('content-align', 'center');
    updateActive();
  });

  wrap.appendChild(btnLeft);
  wrap.appendChild(btnCenter);
  bar.appendChild(label);
  bar.appendChild(wrap);
  col.prepend(bar);
  updateActive();
})();

// ── SCRAMBLE ──
(function() {
  const CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789·_./-';
  function scramble(el) {
    const original = el.dataset.label || el.textContent;
    const len = original.length;
    let frame = 0;
    const total = 7, resolveStart = 3;
    const tick = () => {
      if (frame >= total) { el.textContent = original; return; }
      const lockTo = frame >= resolveStart
        ? Math.floor((frame - resolveStart) / (total - resolveStart) * len)
        : 0;
      let result = '';
      for (let i = 0; i < len; i++) {
        if (i < lockTo) result += original[i];
        else if (original[i] === ' ') result += ' ';
        else result += CHARS[Math.floor(Math.random() * CHARS.length)];
      }
      el.textContent = result;
      frame++;
      setTimeout(tick, 50);
    };
    tick();
  }
  document.querySelectorAll('.scramble-hover').forEach(el => {
    let running = false;
    el.addEventListener('mouseenter', () => {
      if (running) return;
      running = true;
      scramble(el);
      setTimeout(() => { running = false; }, 200);
    });
  });
})();