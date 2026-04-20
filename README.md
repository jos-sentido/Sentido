# Sentido — Repositorio de Propuestas

Repositorio que aloja las propuestas estratégicas de **Sentido Branding & Advertising**, publicadas automáticamente en `propuestas.sentido.mx` vía Vercel.

## Estructura

```
Sentido/
├── README.md                       ← este archivo
├── vercel.json                     ← configuración de Vercel
├── index.html                      ← landing raíz (propuestas.sentido.mx/)
├── assets/
│   ├── logo-sentido-light.png      ← logo blanco, para fondos oscuros
│   └── logo-sentido-dark.png       ← logo negro, para fondos claros
└── propuestas/
    ├── premium-used-car/
    │   └── index.html
    ├── [siguiente-prospecto]/
    │   └── index.html
    └── ...
```

## URLs generadas

```
propuestas.sentido.mx/                        → landing raíz
propuestas.sentido.mx/premium-used-car        → propuesta Premium Used Car
propuestas.sentido.mx/[nombre-kebab]          → siguientes propuestas
```

## Cómo agregar una propuesta nueva

### Opción A — Desde GitHub (navegador, sin setup)

1. Entrar a `github.com/jos-sentido/Sentido`
2. Click en **Add file** → **Create new file**
3. En el campo del nombre escribir: `propuestas/[nombre-kebab]/index.html`
   - El `/` crea automáticamente la carpeta
4. Pegar el HTML completo de la propuesta
5. Scroll abajo → **Commit changes** con mensaje `feat: propuesta [Nombre]`
6. Vercel redeploya en 30-60 segundos
7. URL viva: `propuestas.sentido.mx/[nombre-kebab]`

### Opción B — Desde terminal (si se clona el repo local)

```bash
cd ~/Sentido-repo
mkdir -p propuestas/[nombre-kebab]
cp ~/ruta/al/archivo.html propuestas/[nombre-kebab]/index.html
git add propuestas/[nombre-kebab]/
git commit -m "feat: propuesta [Nombre]"
git push
```

## Convenciones de nombres

- **Siempre kebab-case**: minúsculas, guiones entre palabras
- **Sin acentos ni caracteres especiales** (Google los mapea raro)
- **Corto pero descriptivo**
  - ✅ `premium-used-car`, `tienda-pitico`, `the-tonic-club`, `dulces-pillo`
  - ❌ `PremiumUsedCar`, `propuesta-premium-used-car-abril-2026`, `premium_used_car`

## Uso de los logos en cada propuesta

Cada propuesta referencia los logos con rutas absolutas al root del repo:

**Para fondos oscuros** (negro, grafito, marino, emerald oscuro):
```html
<img src="/assets/logo-sentido-light.png" alt="Sentido Branding & Advertising" />
```

**Para fondos claros** (cream, blanco, beige, gris claro):
```html
<img src="/assets/logo-sentido-dark.png" alt="Sentido Branding & Advertising" />
```

**Tamaños recomendados en la propuesta**:
- Hero: 48px de alto
- Footer: 40px de alto

Ejemplo CSS:
```css
.brand-logo { height: 48px; width: auto; }
.footer-brand-logo { height: 40px; width: auto; }
```

## Retirar una propuesta (opcional)

Si una propuesta queda obsoleta o fue rechazada y quieres que deje de ser pública:

```
propuestas/
└── _archivo/
    └── [prospecto-rechazado]/
        └── index.html
```

Mueve la carpeta a `_archivo/` (guion bajo al inicio lo saca de la ruta pública). La URL original deja de funcionar pero el contenido queda guardado para referencia interna.

Alternativamente, elimina la carpeta completa si no necesitas el histórico.

## Stack técnico

- **Hosting**: Vercel (plan Hobby, gratis)
- **DNS**: gestionado en A2 Hosting (cPanel)
- **CNAME**: `propuestas.sentido.mx` → `dd818eba16bdb4be.vercel-dns-017.com`
- **SSL**: automático vía Vercel
- **Deploy**: automático al hacer push a main

## Configuración de Vercel (`vercel.json`)

El archivo `vercel.json` mapea cada carpeta de `propuestas/` a una URL limpia:

```
propuestas.sentido.mx/premium-used-car
    ↓ (rewrite interno)
/propuestas/premium-used-car/index.html
```

Esto permite que el usuario vea URLs limpias y profesionales sin `/propuestas/` en la ruta.

## Documentación de Vercel

Si algo falla o necesitas entender algo del setup: https://vercel.com/docs
