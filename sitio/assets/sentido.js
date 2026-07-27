/* ═══════════════════════════════════════════════════════════════
   SENTIDO · sentido.mx — comportamiento compartido
   Nav, progreso, reveals, menú móvil, formulario de contacto.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* ───────────── Nav: ocultar al bajar, mostrar al subir ───────────── */
  var nav = document.querySelector('.nav');
  var lastY = window.scrollY;

  function onScroll() {
    var y = window.scrollY;

    if (nav) {
      nav.classList.toggle('is-scrolled', y > 12);
      var goingDown = y > lastY && y > 240;
      var panelOpen = document.querySelector('.nav-panel.is-open');
      nav.classList.toggle('is-hidden', goingDown && !panelOpen);
    }

    var bar = document.querySelector('.progress');
    if (bar) {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.width = (max > 0 ? (y / max) * 100 : 0) + '%';
    }

    lastY = y;
  }

  var ticking = false;
  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(function () { onScroll(); ticking = false; });
  }, { passive: true });
  onScroll();

  /* ───────────── Menú móvil ───────────── */
  var toggle = document.querySelector('.nav-toggle');
  var panel = document.querySelector('.nav-panel');

  if (toggle && panel) {
    toggle.addEventListener('click', function () {
      var open = panel.classList.toggle('is-open');
      toggle.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
      if (open) nav.classList.remove('is-hidden');
    });

    panel.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        panel.classList.remove('is-open');
        toggle.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && panel.classList.contains('is-open')) toggle.click();
    });
  }

  /* ───────────── Reveal al hacer scroll ───────────── */
  var reveals = document.querySelectorAll('.reveal');

  if (!('IntersectionObserver' in window)) {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        io.unobserve(entry.target);
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -8% 0px' });

    reveals.forEach(function (el) { io.observe(el); });
  }

  /* ───────────── Logo: fallback a wordmark si no carga ───────────── */
  document.querySelectorAll('img[data-fallback]').forEach(function (img) {
    img.addEventListener('error', function () {
      var fb = document.createElement('span');
      fb.className = 'brand-fallback';
      fb.textContent = 'Sentido';
      img.replaceWith(fb);
    });
  });

  /* ───────────── Año en el footer ───────────── */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ───────────── Formulario de contacto → /api/lead ───────────── */
  var form = document.getElementById('lead-form');
  if (!form) return;

  var statusEl = document.getElementById('lead-status');
  var submitBtn = form.querySelector('[data-submit]');
  var arrowEl = submitBtn ? submitBtn.querySelector('.arw') : null;

  function setStatus(msg, isError) {
    if (!statusEl) return;
    statusEl.textContent = msg;
    statusEl.classList.add('is-visible');
    statusEl.classList.toggle('is-error', !!isError);
  }

  function checkedValues(name) {
    return Array.prototype.slice
      .call(form.querySelectorAll('input[name="' + name + '"]:checked'))
      .map(function (i) { return i.value; });
  }

  function val(name) {
    var el = form.elements[name];
    return el && el.value ? el.value.trim() : '';
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    var interes = checkedValues('interes');
    if (interes.length === 0) {
      setStatus('Selecciona al menos una opción en "¿En qué necesitas apoyo?".', true);
      return;
    }
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    var email = val('email');
    var payload = {
      Nombre: val('nombre'),
      Empresa: val('empresa'),
      Email: email,
      WhatsApp: val('whatsapp'),
      'Sitio / IG': val('sitio') || '—',
      'Necesita apoyo en': interes.join(', '),
      Presupuesto: val('presupuesto') || 'sin especificar',
      'Cuándo arranca': val('tiempo') || 'sin especificar',
      Contexto: val('contexto') || '—',
      Fuente: form.dataset.fuente || 'sentido.mx',
      Enviado: new Date().toLocaleString('es-MX', { dateStyle: 'medium', timeStyle: 'short' })
    };

    if (submitBtn) submitBtn.disabled = true;
    if (arrowEl) arrowEl.textContent = '…';
    setStatus('Enviando…', false);

    fetch(form.dataset.webhook || '/api/lead', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
      .then(function (res) {
        if (!res.ok) throw new Error('El servidor respondió ' + res.status);
        setStatus('Recibido. Un estratega de Sentido te responde en menos de 24 horas hábiles a ' + email + '.', false);
        form.reset();
        if (arrowEl) arrowEl.textContent = '✓';
      })
      .catch(function (err) {
        console.error('[sentido] lead:', err);
        setStatus('No pudimos enviar tu mensaje. Escríbenos directo a jos@sentido.mx o por WhatsApp y lo resolvemos.', true);
        if (submitBtn) submitBtn.disabled = false;
        if (arrowEl) arrowEl.textContent = '→';
      });
  });
})();
