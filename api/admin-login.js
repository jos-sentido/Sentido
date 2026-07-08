// /api/admin-login — Valida la contraseña del admin y emite una cookie de sesión.
//
// Variables de entorno requeridas (al menos el par principal):
//   ADMIN_PASSWORD         — contraseña de Jos
//   ADMIN_TOKEN            — token de sesión de Jos
//
// Variables opcionales para usuarios adicionales:
//   ADMIN_PASSWORD_RODRIGO — contraseña de Rodrigo
//   ADMIN_TOKEN_RODRIGO    — token de sesión de Rodrigo

const USERS = [
  { passwordEnv: 'ADMIN_PASSWORD',         tokenEnv: 'ADMIN_TOKEN' },
  { passwordEnv: 'ADMIN_PASSWORD_RODRIGO', tokenEnv: 'ADMIN_TOKEN_RODRIGO' },
];

export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', 'https://propuestas.sentido.mx');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).end();

  const { password } = req.body || {};
  if (!password) return res.status(401).json({ error: 'Contraseña incorrecta' });

  for (const u of USERS) {
    const pw    = process.env[u.passwordEnv];
    const token = process.env[u.tokenEnv];
    if (!pw || !token) continue;
    if (password === pw) {
      const maxAge = 60 * 60 * 24 * 30; // 30 días
      res.setHeader('Set-Cookie', `admin_token=${token}; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=${maxAge}`);
      return res.status(200).json({ ok: true });
    }
  }

  return res.status(401).json({ error: 'Contraseña incorrecta' });
}
