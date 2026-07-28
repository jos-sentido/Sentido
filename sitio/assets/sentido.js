/* ═══════════════════════════════════════════════════════════════
   SENTIDO · sentido.mx
   Navegación, menú móvil y formulario. El movimiento vive en CSS:
   un solo momento autoral al cargar la portada, no reveals sueltos.
   ═══════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* ── Barra: se esconde al bajar, vuelve al subir ── */
  var nav = document.querySelector('.nav');
  var previo = window.scrollY;
  var pendiente = false;

  function alScroll() {
    var y = window.scrollY;
    if (nav) {
      nav.classList.toggle('bajo', y > 10);
      var baja = y > previo && y > 260;
      nav.classList.toggle('oculto', baja && !document.querySelector('.panel.abierto'));
    }
    previo = y;
  }

  window.addEventListener('scroll', function () {
    if (pendiente) return;
    pendiente = true;
    window.requestAnimationFrame(function () { alScroll(); pendiente = false; });
  }, { passive: true });
  alScroll();

  /* ── Menú móvil ── */
  var btn = document.querySelector('.nav-btn');
  var panel = document.querySelector('.panel');

  if (btn && panel) {
    btn.addEventListener('click', function () {
      var abierto = panel.classList.toggle('abierto');
      btn.classList.toggle('abierto', abierto);
      btn.setAttribute('aria-expanded', String(abierto));
      document.body.style.overflow = abierto ? 'hidden' : '';
      if (abierto && nav) nav.classList.remove('oculto');
    });

    panel.addEventListener('click', function (e) {
      if (!e.target.closest('a')) return;
      panel.classList.remove('abierto');
      btn.classList.remove('abierto');
      btn.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && panel.classList.contains('abierto')) btn.click();
    });
  }

  /* ── Año del pie ── */
  document.querySelectorAll('[data-anio]').forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });

  /* ── Formulario → /api/lead ── */
  var form = document.getElementById('lead-form');
  if (!form) return;

  var estado = document.getElementById('lead-estado');
  var enviar = form.querySelector('[data-enviar]');
  var flecha = enviar ? enviar.querySelector('.fl') : null;

  function aviso(texto, esError) {
    if (!estado) return;
    estado.textContent = texto;
    estado.classList.add('visible');
    estado.classList.toggle('error', !!esError);
  }

  function valor(nombre) {
    var el = form.elements[nombre];
    return el && el.value ? el.value.trim() : '';
  }

  function marcados() {
    return Array.prototype.slice
      .call(form.querySelectorAll('input[name="interes"]:checked'))
      .map(function (i) { return i.value; });
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    var interes = marcados();
    if (interes.length === 0) {
      aviso('Marca al menos una opción en «¿En qué necesitas apoyo?» para saber por dónde empezar.', true);
      return;
    }
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    var correo = valor('email');
    var datos = {
      Nombre: valor('nombre'),
      Empresa: valor('empresa'),
      Email: correo,
      WhatsApp: valor('whatsapp'),
      'Sitio / IG': valor('sitio') || '—',
      'Necesita apoyo en': interes.join(', '),
      Presupuesto: valor('presupuesto') || 'sin especificar',
      'Cuándo arranca': valor('tiempo') || 'sin especificar',
      Contexto: valor('contexto') || '—',
      Fuente: form.dataset.fuente || 'sentido.mx',
      Enviado: new Date().toLocaleString('es-MX', { dateStyle: 'medium', timeStyle: 'short' })
    };

    if (enviar) enviar.disabled = true;
    if (flecha) flecha.textContent = '·';
    aviso('Enviando…', false);

    fetch(form.dataset.webhook || '/api/lead', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(datos)
    })
      .then(function (r) {
        if (!r.ok) throw new Error('El servidor respondió ' + r.status);
        aviso('Recibido. Un estratega de Sentido te responde en menos de 24 horas hábiles a ' + correo + '.', false);
        form.reset();
        if (flecha) flecha.textContent = '✓';
      })
      .catch(function (err) {
        console.error('[sentido] lead:', err);
        aviso('No pudimos enviar tu mensaje. Escríbenos directo a jos@sentido.mx o por WhatsApp y lo resolvemos.', true);
        if (enviar) enviar.disabled = false;
        if (flecha) flecha.textContent = '→';
      });
  });
})();
