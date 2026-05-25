// /api/lead — Recibe submits del formulario del brochure y envía
// correo branded a jos@sentido.mx vía Resend.
//
// Variables de entorno requeridas:
//   RESEND_API_KEY — API key de Resend (https://resend.com/api-keys)
//   LEAD_TO        — opcional, override del destinatario (default: jos@sentido.mx)
//   LEAD_FROM      — opcional, override del remitente (default: onboarding@resend.dev)

export default async function handler(req, res) {
  // CORS — mismo origen pero por si acaso
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).json({ error: 'Method not allowed' });

  const apiKey = process.env.RESEND_API_KEY;
  if (!apiKey) {
    console.error('[lead] RESEND_API_KEY no configurada');
    return res.status(500).json({ error: 'Servidor mal configurado — falta API key' });
  }

  const to = process.env.LEAD_TO || 'jos@sentido.mx';
  const from = process.env.LEAD_FROM || 'Brochure Sentido <onboarding@resend.dev>';

  // Vercel parsea JSON automáticamente cuando Content-Type es application/json
  const data = req.body || {};

  if (!data.Nombre || !data.Email) {
    return res.status(400).json({ error: 'Faltan campos requeridos (Nombre, Email)' });
  }

  const empresa = (data.Empresa || '').trim() || 'Sin empresa';
  const subject = `Lead nuevo · ${empresa} · brochure`;
  const html = buildEmailHTML(data);

  try {
    const resendRes = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        from,
        to: [to],
        reply_to: data.Email,
        subject,
        html
      })
    });

    if (!resendRes.ok) {
      const errBody = await resendRes.text();
      console.error('[lead] Resend respondió', resendRes.status, errBody);
      return res.status(502).json({ error: 'No se pudo enviar el correo' });
    }

    return res.status(200).json({ success: true });
  } catch (err) {
    console.error('[lead] Fetch error:', err);
    return res.status(500).json({ error: 'Error de red al enviar el correo' });
  }
}

// ─────────────────────────────────────────────────────────
// EMAIL TEMPLATE
// Diseño con tablas (compatible con clientes de correo viejos),
// estilos inline (algunos clientes strippean <style>),
// fuentes de fallback seguras (Georgia / system sans),
// logo Sentido en hero, paleta dark + beige.
// ─────────────────────────────────────────────────────────

function buildEmailHTML(d) {
  const empresa = (d.Empresa || '').trim();
  const nombre = (d.Nombre || '').trim();
  const email = (d.Email || '').trim();

  const fields = [
    ['Nombre', d.Nombre],
    ['Empresa', d.Empresa],
    ['Email', d.Email],
    ['WhatsApp', d.WhatsApp],
    ['Sitio / IG', d['Sitio / IG']],
    ['Necesita apoyo en', d['Necesita apoyo en']],
    ['Presupuesto', d.Presupuesto],
    ['Cuándo arranca', d['Cuándo arranca']],
    ['Contexto', d.Contexto],
    ['Fuente', d.Fuente],
    ['Enviado', d.Enviado]
  ].filter(([_, v]) => v && v !== '—' && v !== 'sin especificar');

  const rowsHTML = fields.map(([label, value]) => `
    <tr>
      <td style="padding: 16px 32px 16px 40px; border-bottom: 1px solid #1F1F26; font-family: 'Courier New', Menlo, monospace; font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase; color: #8B8680; width: 32%; vertical-align: top; line-height: 1.4;">${escapeHTML(label)}</td>
      <td style="padding: 16px 40px 16px 12px; border-bottom: 1px solid #1F1F26; font-family: Georgia, serif; font-size: 15px; color: #EDEAE4; line-height: 1.55; vertical-align: top;">${escapeHTML(value)}</td>
    </tr>
  `).join('');

  const replyHref = `mailto:${encodeURIComponent(email)}?subject=${encodeURIComponent('Re: tu mensaje al brochure de Sentido')}`;
  const whatsappRaw = String(d.WhatsApp || '').replace(/[^\d+]/g, '');
  const whatsappHref = whatsappRaw ? `https://wa.me/${whatsappRaw.replace(/^\+/, '')}` : '';

  return `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="color-scheme" content="dark only">
  <meta name="supported-color-schemes" content="dark only">
  <title>Lead nuevo · Brochure Sentido</title>
</head>
<body style="margin: 0; padding: 0; background-color: #050505; -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%;">

  <!-- Preheader oculto -->
  <div style="display: none; max-height: 0; overflow: hidden; mso-hide: all;">
    ${escapeHTML(nombre)} de ${escapeHTML(empresa || 'sin empresa')} quiere hablar — lead nuevo desde el brochure.
  </div>

  <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #050505;">
    <tr>
      <td align="center" style="padding: 40px 16px;">

        <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="600" style="max-width: 600px; width: 100%; background-color: #0D0D11; border: 1px solid #1F1F26;">

          <!-- Hero / logo -->
          <tr>
            <td align="center" style="padding: 52px 40px 36px; border-bottom: 1px solid #1F1F26; background-color: #0A0A0E;">
              <img src="https://propuestas.sentido.mx/assets/logo-sentido-light.png" alt="Sentido" width="140" style="height: auto; display: block; border: 0; outline: none; text-decoration: none; max-width: 140px;" />
            </td>
          </tr>

          <!-- Eyebrow + título -->
          <tr>
            <td style="padding: 44px 40px 24px;">
              <p style="margin: 0 0 14px; font-family: 'Courier New', Menlo, monospace; font-size: 10px; letter-spacing: 0.24em; text-transform: uppercase; color: #C9B896; font-weight: 600;">Lead nuevo · brochure</p>
              <h1 style="margin: 0; font-family: Georgia, 'Times New Roman', serif; font-weight: 400; font-style: italic; font-size: 34px; line-height: 1.1; color: #EDEAE4; letter-spacing: -0.02em;">${escapeHTML(empresa)}</h1>
              <p style="margin: 18px 0 0; font-family: Georgia, serif; font-style: italic; font-weight: 300; font-size: 17px; color: #8B8680; line-height: 1.4;">${escapeHTML(nombre)} quiere hablar.</p>
            </td>
          </tr>

          <!-- Divider beige -->
          <tr>
            <td style="padding: 0 40px;">
              <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                <tr><td style="height: 1px; background-color: #C9B896; line-height: 1px; font-size: 1px;">&nbsp;</td></tr>
              </table>
            </td>
          </tr>

          <!-- Tabla de campos -->
          <tr>
            <td style="padding: 8px 0 8px;">
              <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%" style="background-color: #0D0D11;">
                ${rowsHTML}
              </table>
            </td>
          </tr>

          <!-- CTAs -->
          <tr>
            <td style="padding: 32px 40px 8px;">
              <table role="presentation" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td style="background-color: #C9B896; padding: 0;">
                    <a href="${replyHref}" style="display: inline-block; padding: 14px 28px; font-family: 'Courier New', Menlo, monospace; font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase; color: #1A1A1A; text-decoration: none; font-weight: 700;">Responder a ${escapeHTML(firstName(nombre))} →</a>
                  </td>
                  ${whatsappHref ? `
                  <td style="padding-left: 12px;">
                    <a href="${whatsappHref}" style="display: inline-block; padding: 14px 28px; font-family: 'Courier New', Menlo, monospace; font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase; color: #C9B896; text-decoration: none; border: 1px solid #5A4F3D; font-weight: 600;">WhatsApp →</a>
                  </td>
                  ` : ''}
                </tr>
              </table>
            </td>
          </tr>

          <!-- Nota -->
          <tr>
            <td style="padding: 24px 40px 0;">
              <p style="margin: 0; font-family: Georgia, serif; font-style: italic; font-weight: 300; font-size: 13px; color: #55524E; line-height: 1.6;">
                El correo trae <em>Reply-To</em> al email del prospecto — si respondes desde tu cliente de correo, le llega directo, no a este buzón.
              </p>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="padding: 40px 40px 44px; border-top: 1px solid #1F1F26; margin-top: 32px;">
              <table role="presentation" cellpadding="0" cellspacing="0" border="0" width="100%">
                <tr>
                  <td align="left" style="font-family: 'Courier New', Menlo, monospace; font-size: 10px; letter-spacing: 0.22em; text-transform: uppercase; color: #55524E;">
                    Sentido · Branding &amp; Advertising
                  </td>
                  <td align="right" style="font-family: 'Courier New', Menlo, monospace; font-size: 10px; letter-spacing: 0.22em; text-transform: uppercase; color: #55524E;">
                    <a href="https://propuestas.sentido.mx/brochure" style="color: #55524E; text-decoration: none;">propuestas.sentido.mx/brochure</a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

        </table>

      </td>
    </tr>
  </table>

</body>
</html>`;
}

function escapeHTML(str) {
  return String(str == null ? '' : str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;')
    .replace(/\n/g, '<br />');
}

function firstName(full) {
  return String(full || '').trim().split(/\s+/)[0] || full;
}
