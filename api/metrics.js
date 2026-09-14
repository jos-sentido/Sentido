// /api/metrics — Lee analítica de Metricool para una marca y un rango de fechas.
//
// Metricool es la fuente única: ya agrega Meta Ads, Google Ads, Instagram y
// Facebook de todas las marcas. Esta función traduce un rango de fechas a las
// llamadas de la API de Metricool y devuelve un JSON normalizado que el panel
// dibuja (KPIs, detalle por canal y series diarias para las gráficas).
//
// ── Variables de entorno (configurar en Vercel → Settings → Environment
//    Variables; NUNCA en el repo: .env y .env.local están en .gitignore) ──
//   METRICOOL_USER_ID    — tu userId de Metricool
//   METRICOOL_USER_TOKEN — tu userToken / Access Token de Metricool
//
// ── Acceso ──
//   Por ahora protegido con la cookie de admin (uso interno). Los hubs por
//   cliente con enlace tokenizado se agregan en el siguiente paso.
//
// ── Contrato ──
//   GET /api/metrics?brand=amancay&from=2026-08-01&to=2026-08-31
//   GET /api/metrics?brand=amancay&from=...&to=...&debug=timeline&metric=FAEV04
//        → devuelve la respuesta CRUDA de Metricool para ese metric (para
//          confirmar el shape en el primer deploy y afinar el parseo).
//
// NOTA DE IMPLEMENTACIÓN: el shape exacto de la respuesta de /stats/timeline
// se confirma en el primer deploy con ?debug=timeline (esta sandbox no puede
// alcanzar metricool.com). El parseo de abajo es defensivo y cubre los shapes
// más probables; si el real difiere, se ajusta extractSeries().

const API = 'https://app.metricool.com/api';

// Registro de marcas. blogId = el id de la marca en Metricool (no es secreto).
// Se irá llenando con las 11 marcas; aquí van las que ya validamos.
const BRANDS = {
  amancay:  { blogId: 1610215, label: 'Amancay',  networks: ['metaAds', 'googleAds', 'instagram', 'facebook'] },
  bolongo:  { blogId: 1140633, label: 'Bolongo',  networks: ['metaAds', 'googleAds', 'instagram', 'facebook'] },
  brelia:   { blogId: 2066332, label: 'Brelia',   networks: ['metaAds', 'googleAds', 'instagram', 'facebook'] },
  heredit:  { blogId: 3777294, label: 'Heredit',  networks: ['metaAds', 'googleAds', 'instagram', 'facebook'] },
  essentia: { blogId: 2425775, label: 'Essentia Country', networks: ['metaAds', 'googleAds', 'instagram', 'facebook'] },
};

// Métricas por red → id de Data Studio de Metricool. Son las mismas que usa el
// conector; las base (aditivas) se suman y las de razón se recalculan.
const METRICS = {
  metaAds:   { spend: 'FAEV04', impressions: 'FAEV01', reach: 'FAEV03', clicks: 'FAEV05' },
  googleAds: { cost: 'GAEV02', impressions: 'GAEV01', clicks: 'GAEV03', conversions: 'GAEV04' },
  instagram: { followers: 'IGEV01', reach: 'IGEV06', views: 'IGEV05', gained: 'IGEV43', lost: 'IGEV44', engaged: 'IGEV42' },
  facebook:  { followers: 'FBEV17', interactions: 'FBEV10', pageViews: 'FBEV03', contentViews: 'FBEV49' },
};

// Cómo se agrega cada métrica sobre el rango: sumar, tomar el último valor
// (stocks como seguidores) o recalcular (razones).
const AGG = {
  spend: 'sum', cost: 'sum', impressions: 'sum', clicks: 'sum', reach: 'sum',
  conversions: 'sum', views: 'sum', gained: 'sum', lost: 'sum', engaged: 'sum',
  interactions: 'sum', pageViews: 'sum', contentViews: 'sum',
  followers: 'last',
};

export default async function handler(req, res) {
  if (req.method !== 'GET') return res.status(405).json({ error: 'Method not allowed' });

  // ── Acceso interno: cookie de admin ──
  const cookie = req.headers.cookie || '';
  const authed = process.env.ADMIN_TOKEN && cookie.includes(`admin_token=${process.env.ADMIN_TOKEN}`);
  const authedR = process.env.ADMIN_TOKEN_RODRIGO && cookie.includes(`admin_token=${process.env.ADMIN_TOKEN_RODRIGO}`);
  if (!authed && !authedR) return res.status(401).json({ error: 'No autorizado' });

  const userId = process.env.METRICOOL_USER_ID;
  const userToken = process.env.METRICOOL_USER_TOKEN;
  if (!userId || !userToken) {
    return res.status(500).json({ error: 'Falta configurar METRICOOL_USER_ID / METRICOOL_USER_TOKEN' });
  }

  const { brand, from, to, debug, metric } = req.query;
  const b = BRANDS[String(brand || '').toLowerCase()];
  if (!b) return res.status(404).json({ error: `Marca desconocida: ${brand}` });

  const start = ymd(from), end = ymd(to);
  if (!start || !end) return res.status(400).json({ error: 'from/to requeridos (YYYY-MM-DD)' });

  const mc = (path, extra = {}) => fetchMetricool(path, { blogId: b.blogId, userId, userToken, start, end, ...extra });

  try {
    // Modo debug: respuesta cruda de un metric, para confirmar el shape.
    if (debug === 'timeline' && metric) {
      const raw = await mc(`/stats/timeline/${metric}`);
      return res.status(200).json({ metric, raw });
    }

    // Trae la serie diaria de cada métrica de las redes de la marca, en paralelo.
    const jobs = [];
    for (const net of b.networks) {
      const ids = METRICS[net] || {};
      for (const [key, id] of Object.entries(ids)) {
        jobs.push(mc(`/stats/timeline/${id}`).then(raw => ({ net, key, series: extractSeries(raw) })));
      }
    }
    const settled = await Promise.all(jobs);

    // Normaliza a { metaAds: {...}, googleAds: {...}, ... , series:{...} }
    const out = { brand: b.label, blogId: b.blogId, from: start, to: end, data: {}, series: {} };
    for (const net of b.networks) out.data[net] = {};

    for (const { net, key, series } of settled) {
      const vals = series.map(p => p.value);
      out.data[net][key] = AGG[key] === 'last' ? (vals.length ? vals[vals.length - 1] : null) : sum(vals);
      // Guarda series diarias clave para las gráficas de tendencia.
      if ((net === 'metaAds' && key === 'spend') || (net === 'instagram' && key === 'reach')) {
        out.series[`${net}_${key}`] = series;
      }
    }

    // Razones recalculadas desde las bases agregadas.
    const m = out.data.metaAds, g = out.data.googleAds;
    if (m) {
      m.ctr = pct(m.clicks, m.impressions);
      m.cpc = ratio(m.spend, m.clicks);
      m.cpm = m.impressions ? (m.spend / m.impressions) * 1000 : null;
      m.frequency = ratio(m.impressions, m.reach);
    }
    if (g) {
      g.ctr = pct(g.clicks, g.impressions);
      g.cpc = ratio(g.cost, g.clicks);
    }
    if (out.data.instagram) out.data.instagram.net = num(out.data.instagram.gained) - num(out.data.instagram.lost);

    res.setHeader('Cache-Control', 's-maxage=1800, stale-while-revalidate=3600');
    return res.status(200).json(out);
  } catch (err) {
    console.error('[metrics]', err);
    return res.status(502).json({ error: 'No se pudo leer Metricool', detail: String(err && err.message || err) });
  }
}

// ─────────────────────────────────────────────────────────
async function fetchMetricool(path, { blogId, userId, userToken, start, end, ...extra }) {
  const qs = new URLSearchParams({ blogId, userId, userToken, start, end, ...extra });
  const url = `${API}${path}?${qs}`;
  const r = await fetch(url, { headers: { 'X-Mc-Auth': userToken, 'Accept': 'application/json' } });
  if (!r.ok) throw new Error(`Metricool ${r.status} en ${path}`);
  return r.json();
}

// Extrae [{date, value}] de la respuesta de timeline, tolerando varios shapes.
function extractSeries(raw) {
  const arr = Array.isArray(raw) ? raw
    : Array.isArray(raw && raw.data) ? raw.data
    : Array.isArray(raw && raw.values) ? raw.values
    : [];
  return arr.map(p => ({
    date: p.date || p.dateTime || (p.day && p.day.date) || null,
    value: Number(p.value != null ? p.value : (Array.isArray(p.values) ? p.values[0] : p)) || 0,
  }));
}

const sum = a => a.reduce((s, v) => s + (Number(v) || 0), 0);
const num = v => Number(v) || 0;
const ratio = (a, b) => (b ? a / b : null);
const pct = (a, b) => (b ? (a / b) * 100 : null);

// 'YYYY-MM-DD' → 'YYYYMMDD'
function ymd(d) {
  const s = String(d || '').trim();
  const m = s.match(/^(\d{4})-(\d{2})-(\d{2})$/);
  return m ? `${m[1]}${m[2]}${m[3]}` : (/^\d{8}$/.test(s) ? s : null);
}
