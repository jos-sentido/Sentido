// /api/admin-logout — Elimina la cookie de sesión del admin.

export default function handler(req, res) {
  res.setHeader('Set-Cookie', 'admin_token=; HttpOnly; Secure; SameSite=Strict; Path=/; Max-Age=0');
  return res.status(200).json({ ok: true });
}
