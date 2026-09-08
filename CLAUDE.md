# Repositorio de Sentido · Branding & Advertising

Este repo aloja dos cosas distintas, publicadas en `propuestas.sentido.mx` vía Vercel:

- **`propuestas/`** — documentos web: propuestas comerciales a prospectos, activos
  de venta y entregables de cliente. Una carpeta por pieza, un `index.html` dentro.
- **`sitio/`** — el sitio institucional de la agencia, servido en `/sitio`.

Antes de escribir una línea, lee **[`SISTEMA-VISUAL.md`](SISTEMA-VISUAL.md)**: es el
sistema gráfico de la marca, con los valores reales. **[`PRODUCT.md`](PRODUCT.md)**
tiene la verdad de producto y las restricciones de publicación.

---

## La regla central: qué es invariable y qué se adapta

Cada pieza cae en uno de tres niveles. **Determínalo antes de diseñar nada.**

### 1 · Superficies institucionales de Sentido

El sitio en `sitio/`, la hoja de espécimen, y cualquier pieza que represente a la
agencia hablando de sí misma.

→ **Sistema estricto.** `SISTEMA-VISUAL.md` manda: tinta y papel, Archivo con
contraste de peso, buril como material, rombo como módulo. No se inventa paleta ni
se cambia la tipografía.

### 2 · Propuestas comerciales

Documentos que Sentido manda a un prospecto. Llevan su logo y hablan en su nombre,
pero **se tropicalizan visualmente al prospecto**: una propuesta a una constructora
industrial no tiene por qué verse igual que una a un club de pádel.

→ **El diseño puede salirse del sistema.** Paleta, tipografía y textura se adaptan
al mundo del prospecto. Eso es criterio de agencia, no descuido.

Lo que **no** se adapta nunca, aunque el resto cambie:

| Invariable | Por qué |
|---|---|
| Las tres aplicaciones del logo | Es la marca de Sentido, no la del prospecto |
| Las restricciones de publicación | Son compromisos con el cliente, no decisiones de diseño |
| La voz | Directa, sin promesas infladas, nombra el problema antes que la solución |
| El piso de contraste 4.5:1 | Accesibilidad, no estética |

Si la propuesta no pide una tropicalización concreta, **el sistema de Sentido es el
punto de partida por defecto** — es el que ya está resuelto.

### 3 · Entregables de cliente

Piezas producidas *para* un cliente, que viven en la marca del cliente: los
artículos de blog de Murotech son el caso claro. Llevan el logo del cliente.

→ **Identidad del cliente.** Aplicarles el sistema de Sentido sería un error de marca.

### Por qué existe esta regla

A septiembre de 2026, las 44 propuestas del repo usan **24 fondos distintos y 11
combinaciones tipográficas**. Tropicalizar es legítimo; improvisar sin punto de
partida no lo es. Las combinaciones más frecuentes —Fraunces, Cormorant Garamond,
Inter, JetBrains Mono— son el molde genérico que el cliente rechazó explícitamente
al rediseñar el sitio, y aparecieron por defecto, no por decisión.

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

**Sobre superficie clara va la variante oscura**: `logo-sentido-dark.png` y
`logo-sentido-nombre-dark.png`. Es una aplicación válida del sistema, no una
excepción.

**Ninguna pieza viaja sola.** Si una composición usa solo el nombre, el isotipo
tiene que estar presente en ella —decorativo o secundario— y al revés. Si eso no
acomoda, va el logo completo. La regla es por composición, no por página: un logo
completo en el pie no cubre un hero que muestra el nombre suelto.

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
