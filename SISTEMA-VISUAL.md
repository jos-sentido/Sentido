# Sistema visual — Sentido · Branding & Advertising

Documento portable del sistema gráfico construido para sentido.mx.
Pensado para compartirse como contexto en Claude Design.

Todo lo que sigue está implementado y en producción en
`propuestas.sentido.mx/sitio`. Los valores son los reales, no aproximaciones.

---

## 1. De dónde sale el sistema

El sistema **no se inventó: se derivó del isotipo de la marca** — un ojo grabado
a línea dentro de un rombo, en técnica de buril (trama de líneas paralelas, alto
contraste, linaje de billete y de grabado mexicano).

De ahí salen las tres decisiones que sostienen todo:

| El isotipo aporta | Se vuelve sistema como |
|---|---|
| Trama de líneas paralelas (buril) | **El material.** Campos de línea con densidad variable, no hairlines decorativos |
| El rombo que enmarca el ojo | **El módulo.** Viñetas, marcadores de estado, marcos anidados |
| Alto contraste tinta/papel | **La paleta.** Tinta cálida sobre hueso, en los dos sentidos |

La voz tipográfica **no** salió del isotipo: se tomó del feed real de la marca en
redes, que usa una grotesca con contraste de peso y una caja hueso como marcador.

Principio operativo del sistema: **la densidad es el énfasis.** Para destacar algo
se sube la densidad de la trama, nunca se añade sombra, elevación ni glow.

---

## 2. Color

Dos materiales: tinta cálida de imprenta y papel hueso. Nunca negro puro (`#000`)
ni blanco puro (`#FFF`).

### Tinta — el fondo

| Token | Hex | Uso |
|---|---|---|
| `--tinta` | `#0B0A09` | Fondo universal |
| `--tinta-2` | `#100E0D` | Plancha elevada: bloques, formulario, pie |
| `--tinta-3` | `#161413` | Fondo de campos de formulario abiertos |
| `--tinta-4` | `#1C1A19` | Reservado, el escalón más alto |

### Hueso — el papel y la tinta clara

| Token | Hex | Contraste sobre tinta | Uso |
|---|---|---|---|
| `--hueso` | `#F1EADC` | 16.52:1 | Títulos, plancha de papel, botón sólido |
| `--hueso-2` | `#B6AE9E` | 8.98:1 | Cuerpo de texto |
| `--hueso-3` | `#948C80` | 5.96:1 | Texto secundario, etiquetas |
| `--hueso-4` | `#898275` | 5.19:1 | Metadatos, texto mínimo |

### Líneas

| Token | Hex | Uso |
|---|---|---|
| `--linea` | `#22201F` | Reglas y divisiones |
| `--linea-2` | `#302E2D` | Bordes de campo y de botón fantasma |

### Superficie clara — el tema no es «oscuro», es de dos materiales

El sistema tiene **dos superficies de igual rango**, no una oscura con excepciones.
Una página puede ser toda de tinta, toda de papel, o alternar secciones.

La inversión se aplica con la clase `.papel`, que **intercambia los valores de los
tokens**. Todo componente ya escrito funciona sobre papel sin una sola regla extra:
el buril graba en tinta, la caja hueso pasa a ser oscura, el botón se invierte solo.

```css
.papel {
  --tinta:   #F1EADC;   /* el fondo pasa a ser el papel */
  --tinta-2: #E8E0D0;
  --tinta-3: #DED5C2;
  --tinta-4: #D5CBB6;

  --hueso:   #0B0A09;   /* 16.52:1 · títulos, caja, botón sólido */
  --hueso-2: #2E2A24;   /* 11.91:1 · cuerpo */
  --hueso-3: #514B42;   /*  7.20:1 · secundario */
  --hueso-4: #5C564C;   /*  6.07:1 · piso */

  --linea:   #D8CFBC;
  --linea-2: #C4B9A2;
}
```

Las dos rampas son espejo. Los cuatro escalones de texto están calibrados contra
**el escalón de fondo más alto**, no solo contra el fondo base: el piso real es
4.55:1 sobre tinta y 4.51:1 sobre papel, en el peor caso de cada rampa.

**Sobre papel va el logo en su variante oscura** — `logo-sentido-dark.png` y
`logo-sentido-nombre-dark.png`. Es aplicación válida del sistema, no excepción.

Se usa sobre `<body>` para una página entera de papel, o sobre una `<section>` para
alternar dentro de una misma página.

### Error — el único color fuera de la paleta

| Uso | Hex |
|---|---|
| Borde de campo inválido | `#B4655A` |
| Texto de error | `#E0A79C` |

### Reglas de color

1. **Regla de la tinta cálida constante.** Todo negro lleva calidez, y la calidez
   es **la misma en toda la rampa**: 3 puntos de R sobre B, medidos en absoluto.
   Si se mantiene el *porcentaje* de saturación en vez del desvío absoluto, la
   calidez crece con la luz y los escalones altos viran a café. Ese fue el error
   de la primera rampa: 30° de matiz a 10% de saturación abajo, que arriba se
   volvían 37° a 21%. `#000` está prohibido salvo dentro de máscaras CSS, donde
   no es color sino canal alfa.
2. **Regla de la alternancia deliberada.** Tinta y papel tienen el mismo rango, y
   una página puede alternarlos. Pero cada cambio de superficie tiene que responder
   a un cambio de contenido —del argumento al procedimiento, del sistema a la
   acción— y no a ganas de variar. Si dos secciones seguidas cambian de superficie
   sin razón, el ritmo se vuelve decoración.
3. **Regla del piso de contraste.** Ningún texto por debajo de 4.5:1 **contra la
   superficie sobre la que se para de verdad**, no contra el fondo base. Los cuatro
   escalones de hueso ya están calibrados para eso.

---

## 3. Tipografía

**Una sola familia: Archivo** (variable, peso 100–900, ancho 75–125).
Auto-hospedada en woff2, sin dependencia de Google Fonts en runtime.

El contraste **nunca** es entre familias: siempre es de peso.

### Pesos

| Token | Valor | Uso |
|---|---|---|
| `--ligera` | 300 | Primera mitad del titular, entradas, declaraciones |
| `--media` | 400 | Cuerpo |
| `--fuerte` | 600 | Énfasis, enlaces, navegación |
| `--negra` | 800 | Segunda mitad del titular, todos los encabezados |

### Escala

| Nivel | Tamaño | Interlínea | Tracking |
|---|---|---|---|
| h1 | `clamp(2.75rem, 6.6vw, 5.75rem)` | 0.98 | −0.032em |
| h2 | `clamp(2rem, 4.2vw, 3.5rem)` | 0.98 | −0.032em |
| h3 | `clamp(1.375rem, 2.2vw, 1.875rem)` | 1.1 | −0.032em |
| h4 | `clamp(1.125rem, 1.5vw, 1.3125rem)` | 1.18 | −0.022em |
| Entrada | `clamp(1.1875rem, 1.9vw, 1.5rem)` | 1.4 | −0.02em, peso 300 |
| Cuerpo | `1.0625rem` | 1.75 | — |
| Chico | `0.9375rem` | 1.65 | — |
| Rótulo | `0.6875rem` | — | 0.24em, versalitas, peso 700 |

La escala es deliberadamente **extrema arriba y abajo, vacía en medio**: no hay
nada entre 1.2 y 1.6rem salvo la entrada ligera.

**Piso duro: 0.6875rem (11px).** Ningún texto baja de ahí, ni las etiquetas ni
las notas al pie. Por debajo, la versalita espaciada deja de leerse y el peso
700 se vuelve una mancha. Si algo no cabe a 11px, sobra o va en otro lugar.

**Sin cursiva.** Archivo no la trae. Cuando el navegador la pide, la sintetiza:
inclina el trazo y deforma la letra. El énfasis del sistema es **peso y color**,
nunca inclinación.

```css
em, i, cite, dfn, address { font-style: normal; }
em, i { font-weight: var(--fuerte); color: var(--hueso); }
```

### Recursos tipográficos de marca

**1. Titular de dos pesos.** La ligera y la negra conviven dentro del mismo
titular. Es el recurso que la marca ya usaba en redes.

```html
<h1><span class="ligera">No se trata de hacer<br>más publicidad.</span><br>
Se trata del <span class="alta">sistema</span><br>que lo vuelve negocio.</h1>
```

**2. Caja hueso.** Una palabra —nunca más— se resalta con fondo hueso y texto
tinta. Es el marcador de la marca.

```css
.alta {
  background: #F1EADC;
  color: #0B0A09;
  padding: 0.02em 0.18em 0.08em;
  box-decoration-break: clone;
}
```

**3. Una sola voz de etiqueta.** Existe un único registro de versalitas
espaciadas (`--hueso-3`, 0.6875rem, 0.24em). No hay eyebrow sobre cada sección:
las secciones abren con pleca y titular.

### Medida de lectura

Todo párrafo tope en **68 caracteres**. La entrada, en 32.

---

## 4. El material — trama de buril

El elemento gráfico central. **Es material, no adorno**: campos de línea que
ocupan superficies, con densidad variable.

```css
.buril {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: repeating-linear-gradient(
    var(--ang, 90deg),
    var(--trazo, #F1EADC) 0 var(--peso, 0.6px),
    transparent var(--peso, 0.6px) var(--paso, 5px)
  );
  opacity: var(--tono, 0.16);
}
```

Cinco parámetros, fijados por contexto:

| Propiedad | Qué controla | Rango usado |
|---|---|---|
| `--ang` | Ángulo del trazo | 90deg, 104deg, 118deg |
| `--paso` | Separación entre líneas | 3–6px |
| `--peso` | Grosor del trazo | 0.6–1.15px |
| `--tono` | Opacidad del campo | 0 → 0.26 |
| `--trazo` | Color del trazo | hueso, o tinta sobre plancha de papel |

`--trazo` es lo que permite grabar **en los dos sentidos**: líneas hueso sobre
tinta, o líneas de tinta sobre la plancha de papel.

### Los cuatro registros

El grabado del isotipo no tiene un solo tipo de trazo: tiene tres, y en el
sistema cada uno cumple una **función distinta**. Esto no es decoración
intercambiable.

| Registro | Trazo del isotipo | Función | Dónde |
|---|---|---|---|
| **Recto** | Las zonas de trama plana | Reposo y estructura | Campo base, planchas, formulario |
| **Arco** | Los trazos del párpado | Atmósfera y superficie | Portada, declaración, arranque, cierre, pie |
| **Iris** | Los radios de la pupila | **Interacción y estado** | Hover de fila, rombo del ojo |
| **Anillo** | Los círculos de la pupila | Momento singular | Reservado |

```css
/* Arco — líneas paralelas curvadas */
.buril--arco {
  background-image: repeating-radial-gradient(
    ellipse var(--rx, 210%) var(--ry, 140%) at var(--foco, 50% 185%),
    var(--trazo) 0 var(--peso, 0.7px),
    transparent var(--peso, 0.7px) var(--paso, 6px));
}

/* Iris — radios que convergen */
.buril--iris {
  background-image: repeating-conic-gradient(
    from var(--giro, 0deg) at var(--foco, -8% 50%),
    var(--trazo) 0deg var(--radio, 0.3deg),
    transparent var(--radio, 0.3deg) var(--salto, 1.9deg));
}

/* Anillo — círculos concéntricos */
.buril--anillo {
  background-image: repeating-radial-gradient(
    circle at var(--foco, 50% 50%),
    var(--trazo) 0 var(--peso, 0.7px),
    transparent var(--peso, 0.7px) var(--paso, 8px));
}
```

Existe también `.buril--onda`, una sinusoide real por máscara SVG. Se conserva
como recurso, pero **los arcos son más fieles** al trazo del logo: los párpados
del isotipo son arcos, no ondas.

### El estado es de iris

Al pasar el cursor sobre una fila **no se ilumina, no se eleva y no cambia de
fondo**: se abre un abanico de radios, como el iris. Va en `::after`, así que no
necesita marcado adicional.

```css
.renglon::after {
  content: ''; position: absolute; inset: 0; pointer-events: none;
  background-image: repeating-conic-gradient(
    from 0deg at var(--foco-estado, -55% 50%),
    var(--hueso) 0deg 0.08deg,
    transparent 0.08deg var(--salto-estado, 0.3deg));
  opacity: 0;
  transition: opacity 0.45s var(--ease);
}
.renglon:hover::after { opacity: 0.20; }
```

### Reglas del buril

1. **Es capa de material, jamás celda de grid.** Siempre `position: absolute`.
   Hay una regla de especificidad dedicada a garantizarlo — si se convierte en
   celda, desplaza todo el contenido una columna.
2. **La densidad es el énfasis.** Al hover se sube `--tono`; nunca se añade
   sombra ni elevación.
3. **Se enmascara para abrir.** Con `mask-image` radial o lineal, como se abre
   la trama en un grabado clásico.
4. **El foco vive fuera del encuadre** en arco e iris. Dentro genera un
   artefacto de convergencia. La excepción es cuando el centro es el sujeto,
   como en el rombo del ojo.
5. **El salto angular del iris se calibra al tamaño del elemento.** El valor que
   en una fila ancha lee como grabado fino, en una caja chica produce muaré.

### Pleca de imprenta

Regla punteada que abre cada sección, en lugar de eyebrow:

```css
.pleca {
  height: 4px;
  background: repeating-linear-gradient(90deg, #F1EADC 0 2px, transparent 2px 6px);
  opacity: 0.45;
}
```

---

## 5. El módulo — rombo

Tomado del marco del isotipo. Es la forma repetible del sistema.

```css
.rombo {
  width: 7px; height: 7px;
  border: 1px solid #948C80;
  transform: rotate(45deg);
}
.rombo--lleno { background: #F1EADC; border-color: #F1EADC; }
```

Dónde aparece:

- Viñeta de toda lista (nunca un punto, nunca un ícono)
- Marcador de página activa en la navegación
- Indicador de estado en las cuatro capas del sistema
- Marcos anidados alrededor del ojo en la portada

**No se usan íconos.** El rombo cubre la función que normalmente cubriría un set
de íconos.

---

## 6. Logo

Reglas de marca. **El logo no se recompone.** No se coloca el ojo al lado del
nombre ni se arma ninguna variante que no exista en el archivo original.

| Aplicación | Cuándo | Archivo |
|---|---|---|
| **Completo**, composición original | Cuando hay espacio vertical | `logo-sentido-light.png` |
| **Solo el nombre** | Cuando el completo no acomoda y hay que identificar a la agencia | `logo-sentido-nombre-light.png` |
| **Solo el ojo** | Uso decorativo | `isotipo-sentido.png` |

Existen las variantes `-dark`, que son las que van **sobre superficie clara**.

**Tamaño mínimo.** El logo completo lleva la firma manuscrita y el descriptor
debajo del ojo: por debajo de **72px de alto** la firma se vuelve un borrón y el
descriptor desaparece. Ahí no se encoge el completo — se cambia de aplicación.

| Alto disponible | Qué va |
|---|---|
| 72px o más | Logo completo |
| 28–48px (barras, pies) | Solo el nombre |
| Menos de 28px | Solo el ojo, y el nombre en otro punto de la composición |

### Ninguna pieza viaja sola

Si una composición usa **solo el nombre**, el isotipo tiene que estar presente en
ella —decorativo o como secundario— y al revés. Si eso no acomoda, se usa el logo
completo.

La regla es **por composición, no por página**: un logo completo en el pie no cubre
un hero que muestra el nombre suelto.

En el sitio se resuelve así:

| Composición | Nombre | Contraparte |
|---|---|---|
| Portada | Barra | El ojo grande, a la derecha |
| Portadas interiores | Barra | El ojo callado (`.ojo-caja--callado`, 60% de opacidad, un rombo menos) |
| Migas de pan | Barra | Isotipo de 30px junto al enlace (`.marca-doble`) |
| Pie | — | Logo completo |

En el sitio: nombre en la barra (46px), completo en el pie (132px), ojo como
favicon y como máscara de la trama en la portada.

### El ojo grabado

En la portada el ojo **no es una imagen pegada**: es un campo de trama
enmascarado por la silueta del isotipo, de modo que la marca misma se lee como
buril y no como logo encimado sobre el diseño.

```css
.ojo-img {
  background-image: repeating-linear-gradient(92deg,
    #F1EADC 0 1.15px, rgba(241,234,220,0.34) 1.15px 2.3px);
  mask: url("isotipo-sentido.png") center / contain no-repeat;
}
```

### La baldosa de pestaña

El isotipo suelto es negro sobre transparente: en una pestaña clara desaparece
y en una oscura se pierde. El favicon del sistema **lleva su propio suelo**: un
cuadro de tinta con el ojo en hueso, con 14% de margen. Así se reconoce en
cualquier navegador y en cualquier tema.

- `assets/favicon.png` — 512px, para el navegador
- `assets/favicon-180.png` — para la pantalla de inicio en iOS
- `favicon.ico` — 16/32/48, para la petición por defecto que hace el navegador

```html
<link rel="icon" href="/assets/favicon.png" />
<link rel="apple-touch-icon" href="/assets/favicon-180.png" />
```

Toda pieza los declara. Una página sin ellos pide `/favicon.ico`, no lo
encuentra, y arranca con un 404 en la consola.

---

## 7. Movimiento

**Un solo momento autoral por página, no reveals sueltos en cada bloque.**

Tres keyframes, todos en la portada:

| Nombre | Qué hace |
|---|---|
| `grabar` | `clip-path: inset(0 100% 0 0)` → `inset(0)`. El texto se graba de izquierda a derecha |
| `abrir` | El ojo aparece con escala 0.86 → 1 |
| `escribir` | Los rombos se trazan con escala 0.7 → 1, escalonados |

Las cuatro capas entran escalonadas después, con `--i` como índice.

Curvas:

```css
--ease:   cubic-bezier(0.22, 0.75, 0.20, 1);
--grabar: cubic-bezier(0.16, 1, 0.3, 1);
```

Todo se desactiva bajo `prefers-reduced-motion`.

**Prohibido:** easing con rebote o elástico, animar `width`/`height`/`padding`,
y cualquier animación en bucle.

---

## 8. Profundidad

**Ninguna sombra tiene blur.** La única sombra del sistema es el desplazamiento
de impresión del botón:

```css
box-shadow: 0 2px 0 0 #898275;   /* reposo */
box-shadow: 0 4px 0 0 #898275;   /* hover */
box-shadow: 0 1px 0 0 #898275;   /* activo */
```

La jerarquía se resuelve con densidad de trama, reglas y peso tipográfico.

---

## 9. Métrica y ritmo

| Token | Valor |
|---|---|
| Ancho de contenido | `1300px` |
| Ancho de lectura | `780px` |
| Margen lateral | `clamp(20px, 3.4vw, 48px)` |
| Alto de sección | `clamp(76px, 9vw, 132px)` |
| Alto de barra | `80px` |

**Más aire arriba de un encabezado que debajo.** En las filas: 16px sobre el
título, 7px debajo.

---

## 10. Lo que este sistema rechaza

Lista explícita. Cada punto es una decisión, no un descuido.

- **Tarjetas.** Los servicios son filas grabadas con regla, no cajas. Nada de
  tarjetas dentro de tarjetas.
- **Íconos.** El rombo cubre esa función.
- **Monoespaciada.** No se usa para disfrazar de técnico.
- **Serif.** La familia es una sola y es grotesca.
- **Eyebrow sobre cada sección.** Solo pleca y titular.
- **Numeración decorativa** (01 / 02 / 03) salvo cuando la secuencia informa.
- **Gradientes, glass, glow.** El material es la trama.
- **Imágenes fotográficas.** Decisión de marca: el grabado es puro trazo.
- **Texto en gris.** Todo secundario se tinta desde el hueso.

---

## 11. Dónde vive todo

| Qué | Dónde |
|---|---|
| Tokens y componentes | `sitio/assets/sentido.css` |
| Tipografía auto-hospedada | `sitio/assets/fonts.css` + `fonts/` (176 KB) |
| Comportamiento | `sitio/assets/sentido.js` |
| Contenido y markup | `sitio/build.py` |
| Registro del sistema | `DESIGN.md` y `.impeccable/design.json` |
| Verdad de producto | `PRODUCT.md` |

---

## 12. Pendiente para consolidar el sistema

- Sustituir los PNG del logo por **SVG** desde el archivo maestro.
- Falta la **trama cruzada** (cross-hatch: dos ángulos superpuestos para
  construir tono) y el **rombo a escala de página** como marco o borde de
  plancha. Hoy el rombo vive solo como viñeta y como motivo de portada.
- Definir aplicación del sistema fuera de web: piezas de redes, propuestas,
  presentaciones.
