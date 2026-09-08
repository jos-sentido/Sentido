# Repositorio de Sentido · Branding & Advertising

Este repo aloja dos cosas distintas, publicadas en `propuestas.sentido.mx` vía Vercel:

- **`propuestas/`** — documentos web: propuestas comerciales a prospectos, activos
  de venta y entregables de cliente. Una carpeta por pieza, un `index.html` dentro.
- **`sitio/`** — el sitio institucional de la agencia, servido en `/sitio`.

Antes de escribir una línea, lee **[`SISTEMA-VISUAL.md`](SISTEMA-VISUAL.md)**: es el
sistema gráfico de la marca, con los valores reales. **[`PRODUCT.md`](PRODUCT.md)**
tiene la verdad de producto y las restricciones de publicación.

---

## La regla central: de quién es la identidad

Cada pieza pertenece a una de dos familias. **Determina esto antes de diseñar nada.**

### Identidad Sentido

Propuestas comerciales, activos de venta, brochures, páginas de servicio, el sitio.
Llevan el logo de Sentido y hablan en nombre de la agencia.

→ **Usan el sistema de `SISTEMA-VISUAL.md`, sin excepciones.** Tinta cálida `#0B0A09`
sobre hueso `#F1EADC`, una sola familia tipográfica (Archivo) con contraste de peso,
la trama de buril como material y el rombo como módulo.

No inventes una paleta ni elijas otra tipografía «que le quede mejor al sector». El
sistema existe justamente para que eso no pase.

### Identidad del cliente

Entregables producidos *para* un cliente y que viven en la marca del cliente: los
artículos de blog de Murotech son el caso claro. Llevan el logo del cliente.

→ **Usan la identidad del cliente, no la de Sentido.** Aplicar el sistema de Sentido
aquí sería un error de marca.

Si no está claro a qué familia pertenece una pieza, **pregunta antes de diseñar**.

### Por qué existe esta regla

A septiembre de 2026, las 44 propuestas del repo usan **24 fondos distintos y 11
combinaciones tipográficas**. Las más frecuentes —Fraunces, Cormorant Garamond,
Inter, JetBrains Mono— son el molde genérico que el cliente rechazó explícitamente
en el rediseño del sitio. Cada sesión improvisó porque no había nada escrito.

---

## Restricciones de publicación

Confirmadas con el cliente. **No son negociables y no se infieren.**

| Restricción | Detalle |
|---|---|
| **Sin nombres de clientes** | No hay autorización para publicarlos. Los casos van por sector, nunca por marca nombrada. |
| **Sin precios en el sitio** | El sitio institucional no publica precios. Las propuestas comerciales sí pueden publicar **un solo piso «desde»** por página, nunca un techo. |
| **Sin ciudad ni cobertura** | No afirmar sede ni geografía en ninguna superficie pública. |
| **Sin métricas de cliente** | No existen resultados autorizados. Nada de ROAS, porcentajes de crecimiento ni capturas de dashboard. |
| **Cifras de industria** | Solo las que el material ya cita como tales, y marcadas explícitamente como referencias del sector, no como mediciones de Sentido. |

Único dato de trayectoria autorizado: **«desde 2010»**.

---

## Uso del logo

**El logo no se recompone.** No se coloca el ojo al lado del nombre ni se arma
ninguna variante que no exista en el archivo original. Tres aplicaciones válidas:

| Aplicación | Archivo | Cuándo |
|---|---|---|
| Completo, composición original | `assets/logo-sentido-light.png` | Cuando hay espacio vertical |
| Solo el nombre | `assets/logo-sentido-nombre-light.png` | Cuando el completo no acomoda y hay que identificar a la agencia |
| Solo el ojo | `assets/isotipo-sentido.png` | Uso decorativo |

Existen las variantes `-dark` para fondos claros.

---

## Cómo trabajar cada parte

### Una propuesta nueva

```
propuestas/[nombre-kebab]/index.html
```

Nombre en kebab-case, sin acentos. Se registra en `proposals.json`. Vercel la
publica en `propuestas.sentido.mx/[nombre-kebab]` por la reescritura `/:prospecto`.

Si es de identidad Sentido, parte del sistema. `propuestas/brochure/` es la
referencia de tono y estructura, aunque su paleta es anterior al sistema actual.

### El sitio institucional

**Todo el contenido vive en `sitio/build.py`.** Los `index.html` se regeneran:
editarlos a mano pierde los cambios.

```bash
python3 sitio/build.py    # reescribe las 16 páginas
```

El CSS y el JS sí se editan directo en `sitio/assets/`. Ver `sitio/README.md`.

`sitio/sistema/index.html` es la hoja de espécimen: documenta el sistema
renderizándolo con su propio CSS. Está escrita a mano, no la genera `build.py`.

---

## Qué no romper

- **`vercel.json`** — la reescritura `/:prospecto` es lo que hace funcionar todas
  las URLs de propuestas. La regla `/sitio` va antes que la genérica.
- **`/api/lead`** — endpoint compartido de formularios, manda correo vía Resend a
  `jos@sentido.mx`. Cada superficie se identifica con su campo `Fuente`.
- **`proposals.json`** — lo lee el panel en `/admin`. Registra ahí cada pieza nueva.
- **Las 16 páginas del sitio llevan `noindex`** mientras vivan bajo
  `propuestas.sentido.mx`, para no competir con el sentido.mx actual. Se quita al
  publicar en el dominio definitivo, junto con `BASE = ""` en `build.py`.

---

## Antes de dar algo por terminado

- Verifica el render de verdad, no solo el código: captura escritorio y móvil.
- Sin overflow horizontal ni errores de consola.
- Contraste mínimo 4.5:1 en todo texto. Los tokens de hueso ya están calibrados.
- Ningún texto en gris: lo secundario se tinta desde el hueso.
- Si el trabajo es de identidad Sentido, contrástalo con la lista de rechazos de
  `SISTEMA-VISUAL.md`: sin tarjetas, sin íconos, sin monoespaciada de disfraz, sin
  serif, sin gradientes ni glow, sin negro puro.
