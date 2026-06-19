// /api/admin-proposals — Lee y escribe proposals.json en GitHub.
//
// Variables de entorno requeridas:
//   ADMIN_TOKEN    — token de sesión (debe coincidir con la cookie admin_token)
//   GITHUB_TOKEN   — Personal Access Token con permisos repo:write
//
// Variables opcionales:
//   GITHUB_OWNER   — owner del repo (default: jos-sentido)
//   GITHUB_REPO    — nombre del repo (default: Sentido)
//   GITHUB_BRANCH  — rama (default: main)

const OWNER  = process.env.GITHUB_OWNER  || 'jos-sentido';
const REPO   = process.env.GITHUB_REPO   || 'Sentido';
const BRANCH = process.env.GITHUB_BRANCH || 'main';
const FILE   = 'proposals.json';

function getCookie(header, name) {
  if (!header) return null;
  const m = header.match(new RegExp(`(?:^|;\\s*)${name}=([^;]*)`));
  return m ? decodeURIComponent(m[1]) : null;
}

function isAuthed(req) {
  const token = getCookie(req.headers.cookie, 'admin_token');
  return token && token === process.env.ADMIN_TOKEN;
}

function ghHeaders() {
  return {
    Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
    Accept: 'application/vnd.github.v3+json',
    'Content-Type': 'application/json',
    'User-Agent': 'sentido-admin/1.0'
  };
}

async function getFile() {
  const url = `https://api.github.com/repos/${OWNER}/${REPO}/contents/${FILE}?ref=${BRANCH}`;
  const res = await fetch(url, { headers: ghHeaders() });
  if (!res.ok) throw new Error(`GitHub ${res.status}: ${await res.text()}`);
  const meta = await res.json();
  const content = JSON.parse(Buffer.from(meta.content, 'base64').toString('utf8'));
  return { content, sha: meta.sha };
}

async function putFile(proposals, sha, message = 'admin: actualiza proposals.json') {
  const url = `https://api.github.com/repos/${OWNER}/${REPO}/contents/${FILE}`;
  const body = JSON.stringify({
    message,
    content: Buffer.from(JSON.stringify({ proposals }, null, 2)).toString('base64'),
    sha,
    branch: BRANCH
  });
  const res = await fetch(url, { method: 'PUT', headers: ghHeaders(), body });
  if (!res.ok) throw new Error(`GitHub ${res.status}: ${await res.text()}`);
  const data = await res.json();
  return data.content.sha;
}

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', 'https://propuestas.sentido.mx');
  res.setHeader('Access-Control-Allow-Methods', 'GET, PUT, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  res.setHeader('Cache-Control', 'no-store');

  if (req.method === 'OPTIONS') return res.status(200).end();

  if (!isAuthed(req)) return res.status(401).json({ error: 'No autorizado' });

  if (!process.env.GITHUB_TOKEN) {
    return res.status(500).json({ error: 'GITHUB_TOKEN no configurado' });
  }

  try {
    if (req.method === 'GET') {
      const { content, sha } = await getFile();
      return res.status(200).json({ ...content, _sha: sha });
    }

    if (req.method === 'PUT') {
      const { proposals, _sha } = req.body || {};
      if (!Array.isArray(proposals)) {
        return res.status(400).json({ error: 'proposals debe ser un array' });
      }

      let sha = _sha;
      if (!sha) {
        const current = await getFile();
        sha = current.sha;
      }

      const newSha = await putFile(proposals, sha);
      return res.status(200).json({ ok: true, _sha: newSha });
    }

    return res.status(405).end();
  } catch (err) {
    console.error('[admin-proposals]', err.message);
    return res.status(502).json({ error: err.message });
  }
}
