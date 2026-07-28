# Sitio institucional — sentido.mx (renovación)

Sitio multi-página de **Sentido Branding & Advertising**, escrito como HTML estático puro.
Vive bajo `/sitio` para poder revisarse en producción **sin tocar el dominio actual**:

```
https://propuestas.sentido.mx/sitio
```

---

## Estructura

```
sitio/
├── build.py                    ← generador (fuente de verdad del contenido)
├── sitemap.xml
├── assets/
│   ├── sentido.css             ← sistema de diseño completo
│   ├── sentido.js              ← nav, scroll, reveals, formulario
│   ├── fonts.css               ← @font-face de las 3 tipografías
│   └── fonts/                  ← 8 woff2 auto-hospedados (~232 KB)
├── index.html                  ← Home
├── metodo/
├── servicios/                  ← índice + 7 páginas de módulo
│   ├── redes-meta/
│   ├── google-ads/
│   ├── crm-automatizacion/
│   ├── google-business-profile/
│   ├── email-marketing/
│   ├── branding/
│   └── sitios-web/
├── casos/
├── blog/                       ← índice + 3 artículos
└── contacto/
```

16 páginas en total.

---

## Cómo editar el contenido

**Todo el texto vive en `build.py`.** No edites los `index.html` a mano: se regeneran y
perderías los cambios.

```bash
cd ~/Sentido-repo
python3 sitio/build.py     # reescribe las 16 páginas + sitemap
git add sitio/ && git commit -m "content: ..." && git push
```

Dónde está cada cosa dentro de `build.py`:

| Qué quieres cambiar | Dónde |
|---|---|
| Textos de un módulo de servicio | lista `SERVICES` |
| Las 4 capas del sistema | lista `LAYERS` |
| Método de trabajo (5 prácticas) | lista `PROCESS` |
| Pasos de arranque | lista `ONBOARDING` |
| Sectores de la página Casos | lista `SECTORS` |
| Nombres de clientes mostrados | lista `PROJECTS` |
| Artículos del blog | lista `POSTS` |
| Menú, correo, WhatsApp | constantes `NAV`, `MAIL`, `WA` (arriba del archivo) |
| Home, Método, Casos, Contacto | funciones `build_*()` |

El CSS y el JS **sí** se editan directo en `assets/`.

---

## Sistema de diseño

Dark cálido con acento **hueso**, sin oro. Los tokens están al inicio de `assets/sentido.css`.

| Token | Valor | Uso |
|---|---|---|
| `--bg` | `#08080A` | fondo (negro cálido, no azulado) |
| `--surface` | `#0E0E11` | tarjetas y bloques |
| `--bone` | `#F5F0E6` | acento de marca: títulos, reglas, botones sólidos |
| `--text` | `#B4AFA6` | cuerpo de texto |
| `--text-dim` | `#7C776F` | texto secundario |
| `--line` | `#1D1D23` | hairlines del grid |

Tipografías, todas auto-hospedadas (sin Google Fonts en runtime):

- **Instrument Serif** — display, con itálica como recurso de énfasis
- **Inter Tight** (variable 300–600) — interfaz y cuerpo
- **JetBrains Mono** (variable 400–500) — eyebrows, etiquetas, metadatos

---

## Formulario de contacto

`/sitio/contacto` postea a `/api/lead`, el mismo endpoint que usa el brochure
(Resend → `jos@sentido.mx`). Se distingue por el campo `Fuente: sentido.mx`,
mientras el brochure manda `brochure.sentido.mx`.

Requiere `RESEND_API_KEY` en las variables de entorno de Vercel — ya configurada
para el proyecto actual.

---

## Pasar el sitio a sentido.mx

Hoy las rutas están escritas con el prefijo `/sitio`. Para moverlo a la raíz de un
dominio propio:

1. En `build.py`, cambiar `BASE = "/sitio"` por `BASE = ""`.
2. Correr `python3 sitio/build.py`.
3. Publicar el contenido de `sitio/` como raíz del proyecto de Vercel que sirva `sentido.mx`.

Los enlaces a `/brochure`, `/sitios-web-ia` y `/reactivacion-ghl-resenas` apuntan a
páginas que viven en este repo (`propuestas.sentido.mx`). Si el sitio se separa a otro
proyecto, hay que absolutizarlos a `https://propuestas.sentido.mx/...`.

---

## Sobre el logo

La barra y el pie usan `assets/logo-sentido-light-h.png`: un **lockup horizontal
derivado** del logo original, porque `logo-sentido-light.png` es un lockup
vertical de proporción 1.12 y en una barra de 80px la firma queda ilegible.

Se compuso separando las dos piezas del archivo original —el rombo con el ojo
por un lado, la firma «Sentido» con su descriptor por el otro— y montándolas en
horizontal. No se redibujó nada: son los mismos trazos del PNG original.

Se generó también `logo-sentido-dark-h.png` para fondos claros.

**Limitación real:** al derivarse de un PNG, estas piezas no escalan sin pérdida.
Para producción conviene reemplazarlas por una versión horizontal en vector
(SVG) hecha desde el archivo maestro. Los nombres pueden quedar igual.

## Pendientes antes de publicar

- [ ] **Confirmar los nombres de cliente** de la página Casos (lista `PROJECTS` en `build.py`).
      Están tomados de las propuestas y proyectos del repo, pero no se ha validado
      quién autorizó aparecer públicamente.
- [ ] Revisar que el WhatsApp `+52 1 322 225 3390` sea el correcto para el sitio público
      (se tomó del brochure).
- [ ] Sustituir los lockups horizontales derivados por SVG desde el archivo maestro.
- [ ] Definir imagen `og:image` para compartir en redes.
- [ ] Decidir si el blog sigue creciendo aquí o migra a un CMS.
