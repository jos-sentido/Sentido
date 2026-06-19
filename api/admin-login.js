// /api/admin-login — Valida la contraseña del admin y emite una cookie de sesión.
//
// Variables de entorno requeridas:
//   ADMIN_PASSWORD — contraseña del panel privado
//   ADMIN_TOKEN    — token de sesión (string largo aleatorio)

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', 'https://propuestas.sentido.mx');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).end();

  const { password } = req.body || {};
  const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD;
  const ADMIN_TOKEN = process.env.ADMIN_TOKEN;

  if (!ADMIN_PASSWORD || !ADMIN_TOKEN) {
    return res.status(500).json({ error: 'Servidor mal configurado' });
  }

  if (!password || password !== ADMIN_PASSWORD) {
    return res.status(401).json({ error: 'Contraseña incorrecta' });
  }

  const maxAge = 60 * 60 * 24 * 30; // 30 días
  res.setHeader('Set-Cookie', `admin_token=${ADMIN_TOKEN}; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=${maxAge}`);
  return res.status(200).json({ ok: true });
}
