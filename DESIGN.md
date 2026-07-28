---
name: Sentido · Branding & Advertising
description: Buril engraving derived from the brand's own isotipo — line fields as material, the rhombus as module, warm ink under bone.
colors:
  tinta: "#0B0A09"
  tinta-2: "#100E0C"
  tinta-3: "#171410"
  tinta-4: "#1E1A15"
  hueso: "#F1EADC"
  hueso-2: "#B6AE9E"
  hueso-3: "#948C80"
  hueso-4: "#857E72"
  linea: "#262119"
  linea-2: "#352F25"
  tenue: "#6B6459"
  error: "#B4655A"
  error-texto: "#E0A79C"
typography:
  display:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(2.75rem, 6.6vw, 5.75rem)"
    fontWeight: 800
    lineHeight: 0.98
    letterSpacing: "-0.032em"
    fontVariation: "'wdth' 100"
  display-ligera:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(2.75rem, 6.6vw, 5.75rem)"
    fontWeight: 300
    lineHeight: 0.98
    letterSpacing: "-0.022em"
  headline:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(2rem, 4.2vw, 3.5rem)"
    fontWeight: 800
    lineHeight: 0.98
    letterSpacing: "-0.032em"
  title:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(1.375rem, 2.2vw, 1.875rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "-0.032em"
  subtitle:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(1.125rem, 1.5vw, 1.3125rem)"
    fontWeight: 800
    lineHeight: 1.18
    letterSpacing: "-0.022em"
  entrada:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(1.1875rem, 1.9vw, 1.5rem)"
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: "-0.02em"
  declaracion:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "clamp(1.625rem, 4vw, 3.25rem)"
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: "-0.035em"
  body:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: "normal"
  body-chico:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: "normal"
  label:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "0.6875rem"
    fontWeight: 700
    lineHeight: 1.68
    letterSpacing: "0.24em"
  label-accion:
    fontFamily: "Archivo, system-ui, -apple-system, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 700
    lineHeight: 1.68
    letterSpacing: "0.18em"
rounded:
  none: "0"
spacing:
  gut: "clamp(20px, 3.4vw, 48px)"
  sec: "clamp(76px, 9vw, 132px)"
  bloque: "clamp(26px, 3vw, 38px)"
  placa: "clamp(36px, 5vw, 72px)"
  nav-h: "72px"
  wrap: "1300px"
components:
  boton:
    backgroundColor: "{colors.hueso}"
    textColor: "{colors.tinta}"
    typography: "{typography.label-accion}"
    rounded: "{rounded.none}"
    padding: "17px 28px"
  boton-hover:
    backgroundColor: "#FFFFFF"
    textColor: "{colors.tinta}"
  boton-linea:
    backgroundColor: "transparent"
    textColor: "{colors.hueso}"
    typography: "{typography.label-accion}"
    rounded: "{rounded.none}"
    padding: "17px 28px"
  enlace:
    backgroundColor: "transparent"
    textColor: "{colors.hueso}"
    typography: "{typography.label-accion}"
    padding: "0 0 5px 0"
  nav-a:
    backgroundColor: "transparent"
    textColor: "{colors.hueso-3}"
    typography: "{typography.label-accion}"
    padding: "4px 0"
  nav-a-active:
    textColor: "{colors.hueso}"
  campo-ent:
    backgroundColor: "{colors.tinta}"
    textColor: "{colors.hueso}"
    typography: "{typography.body-chico}"
    rounded: "{rounded.none}"
    padding: "14px 16px"
    width: "100%"
  campo-check:
    backgroundColor: "transparent"
    textColor: "{colors.hueso-2}"
    rounded: "{rounded.none}"
    padding: "12px 14px"
  renglon:
    backgroundColor: "transparent"
    textColor: "{colors.hueso-3}"
    rounded: "{rounded.none}"
    padding: "clamp(26px, 3vw, 38px) 0"
  placa-cierre:
    backgroundColor: "{colors.tinta-2}"
    textColor: "{colors.hueso-2}"
    rounded: "{rounded.none}"
    padding: "{spacing.placa}"
  declara:
    backgroundColor: "{colors.hueso}"
    textColor: "{colors.tinta}"
    typography: "{typography.declaracion}"
    rounded: "{rounded.none}"
    padding: "clamp(76px, 10vw, 142px) 0"
  rombo:
    backgroundColor: "transparent"
    rounded: "{rounded.none}"
    size: "7px"
---

# Design System: Sentido · Branding & Advertising

## Overview

**Creative North Star: "The Burin Plate"**

The system is an engraved plate, not a page of components. Its material is the line field: repeating parallel strokes at a declared angle, pitch, and weight, laid behind whole sections the way a burin lays hatching behind a figure. Density is the only emphasis device the material has — a section is louder because its hatching is tighter, not because a box was drawn around it. The mark the whole world derives from is the brand's own isotipo, an eye inside a rhombus, and the rhombus recurs as the structural module at every scale: the 5px nav marker, the 6px list bullet, the 7px layer marker, and the three nested frames around the hero eye.

Density is high and the surface is nearly all ink. Warm printing black (`#0B0A09`, never pure black) is the ground for fifteen of sixteen page-regions; bone (`#F1EADC`) appears as paper only where the system deliberately flips — one declaration band per page, the bone highlight box inside a headline, and the primary button. Structure is drawn with hairlines and grid borders, never with fills, shadows, or corner radii. There are no cards: a service, a layer, a module, and an article all render as a full-bleed table row under a shared rule.

Confirmed rejections, all held by the shipped code: no serif and no monospace (one variable family, Archivo, carries every role), no photographic or illustrative imagery, no icon set, no card containers, and no per-section eyebrow. Typographic contrast is achieved by weight (300 against 800) inside a single headline, taken from the brand's real Instagram feed, not by mixing families.

**Key Characteristics:**
- One typeface (Archivo variable, 100–900), self-hosted, contrast by weight alone
- Warm ink ground everywhere; bone is the exception and reads as paper
- Line fields (`.buril`) as material, driven by custom properties, never as content
- Rhombus as the only recurring ornament, at four sizes
- Zero corner radius, zero blur shadows, one hard offset shadow on the primary button
- Rows and rules instead of cards; hover reveals hatching, not elevation
- One authored motion moment on load; nothing animates on scroll

## Colors

A two-material palette: warm printing ink and bone paper, with four neutral steps between them and a single desaturated brick reserved for form errors.

### Primary
- **Bone** (`{colors.hueso}`): The paper. Used as headline color, as the fill of the highlight box inside headlines, as the primary button ground, as the one bone-ground band per page, and as the `::selection` and focus-ring color. On ink it measures 16.3:1.

### Neutral
- **Warm Ink** (`{colors.tinta}`): The page ground and the body background. Deliberately warm; pure `#000` is out of the system.
- **Ink Plate** (`{colors.tinta-2}`): The one-step-lifted plate for footer, closing block, form panel, mobile menu panel, and `.seccion--placa`. The only tonal-layering device in the system.
- **Ink Deep / Ink Warm** (`{colors.tinta-3}`, `{colors.tinta-4}`): Reserved depths; `tinta-3` backs native `<select>` options.
- **Bone Text** (`{colors.hueso-2}`): Default body text on ink (9.0:1). The reading color.
- **Bone Muted** (`{colors.hueso-3}`): Secondary prose, labels, row descriptions, rhombus borders (5.96:1).
- **Bone Quiet** (`{colors.hueso-4}`): The quietest legible tier — timestamps, placeholders, footer legal, the primary button's offset shadow (4.92:1).
- **Rule** (`{colors.linea}`): Every hairline divider, section top-border, and row border.
- **Rule Raised** (`{colors.linea-2}`): Input borders and the mobile menu button border — one step brighter, used only where a control needs to read as touchable.
- **Ink on Paper Muted** (`{colors.tenue}`): The dimmed clause inside the bone declaration band (4.84:1 on bone, used at display size only).

### Error
- **Brick** (`{colors.error}`): Invalid input border only.
- **Brick Light** (`{colors.error-texto}`): Error message text in the form status region.

### Named Rules
**The Warm Ink Rule.** The ground is `{colors.tinta}` and it is never `#000`. Every neutral in the system carries the same warm cast; a cool gray anywhere reads as foreign material.

**The One Plate Rule.** Exactly one region per page inverts to bone ground — the declaration band. Everything else is ink ground. A second bone panel destroys the contrast that makes the first one land.

**The Bone Floor Rule.** No text color below `{colors.hueso-4}` (4.92:1) is used on ink. `{colors.hueso-3}` and `{colors.hueso-4}` were set at these exact values to clear WCAG AA; darkening them for atmosphere is not available.

## Typography

**Display / Body / Label Font:** Archivo (variable, weight 100–900, width 75–125, self-hosted woff2, latin + latin-ext subsets), falling back to `system-ui, -apple-system, sans-serif`.

**Character:** One industrial grotesk doing every job. Personality comes from the spread between its extremes — hairline 300 set against near-black 800 in the same line — and from tight negative tracking at display sizes against wide 0.18–0.24em tracking at label sizes. Headlines are set at `line-height: 0.98`, tighter than their own cap height, so a two-line headline reads as a single engraved block.

### Hierarchy
- **Display** (`{typography.display}` / `{typography.display-ligera}`): Page H1. Always composed as a mixed-weight sentence — a light clause, a black clause, and one word in the bone box. Interior pages step the ceiling down to `clamp(2.25rem, 5.2vw, 4.25rem)`.
- **Headline** (`{typography.headline}`): Section H2 and the closing block's call.
- **Title** (`{typography.title}`): Row titles — layers, service modules, article entries.
- **Subtitle** (`{typography.subtitle}`): Process step titles inside `.paso`.
- **Entrada** (`{typography.entrada}`): The light-weight lead sentence that opens a column, capped at 32ch.
- **Declaración** (`{typography.declaracion}`): The centered light statement on the bone band, capped at 20ch, balanced wrap.
- **Body** (`{typography.body}`): Long-form prose and article text, capped at 68ch by the global `p` rule.
- **Body Chico** (`{typography.body-chico}`): Row descriptions, form fields, footer links.
- **Label** (`{typography.label}` at 0.24em, `{typography.label-accion}` at 0.18em): Uppercase micro-type. The 0.24em variant is the single section-label voice; the 0.18em variant belongs to actions (buttons, links, nav).

### Named Rules
**The Two-Weight Headline Rule.** Weight contrast happens inside one headline, never between two typefaces. Light (300) sets the setup clause, black (800) sets the claim, and exactly one word wears the bone box.

**The Bone Box Rule.** The highlight box (`.alta`) is a marker, not a highlighter. One word per headline, `box-decoration-break: clone` so it survives wrapping, and never applied to body copy.

**The One Label Voice Rule.** There is a single uppercase micro-type register in the site, and it does not appear above every section. A label earns its place by naming a column or a step, not by decorating a heading.

**The 68ch Rule.** Paragraphs are capped at 68ch globally (60–64ch inside rows, 700px inside articles). Full-width prose is not a layout option.

## Layout

The page is a 1300px max-width container (`{spacing.wrap}`) with fluid gutters (`{spacing.gut}`), and a 780px narrow variant for centered reading. Vertical rhythm is one fluid section step (`{spacing.sec}`), collapsing to a flat 64px below 640px — the only token the system redefines at a breakpoint.

Sections are separated by a 1px top rule (`.seccion--regla`) or by a tonal plate (`.seccion--placa`, ink-plate ground bounded by rules above and below). Nothing is separated by whitespace alone at a section boundary.

Content structures are grids of rows, not grids of boxes:
- **Layer strip:** four equal columns with 1px inter-column borders; 2-up at 1080px, 1-up at 640px, with the borders migrating from right to bottom.
- **Service / article rows:** `1fr / 1.35fr / 118px` (services) and `150px / 1fr / 92px` (articles), baseline-aligned, collapsing to a single stacked column at 900px where the right-hand action column left-aligns.
- **Process steps:** an 84px numeral column against content, collapsing to one column at 640px.
- **Two-column sections:** `0.8fr / 1.2fr` with the left column sticky under the nav; sticky is released and the grid flattens at 1080px.

The fixed 72px nav shares its height with `scroll-padding-top` (+20px) so anchor targets clear it. Breakpoints in use: 1080px (sticky and 4-up structures), 900px (nav-to-hamburger, row collapse), 640px (single column, section rhythm, full-width buttons).

## Elevation & Depth

The system is flat and has no blur shadows. Depth is produced three ways, in order of use: **hatching density** (a `.buril` field at higher `--tono` reads nearer), **tonal plates** (`{colors.tinta-2}` lifted one step from the ground), and **hairlines** (`{colors.linea}`).

### Shadow Vocabulary
- **Print offset** (`box-shadow: 0 2px 0 0 {colors.hueso-4}`): The primary button only. Hard, unblurred, single-color — it reads as a second impression of the plate, not as a light source. It deepens to `0 4px 0 0` on hover and compresses to `0 1px 0 0` on active.

### Named Rules
**The No-Blur Rule.** Every shadow in the system has zero blur radius. A soft drop shadow anywhere is out of material.

**The Density-Is-Emphasis Rule.** To make a region read as forward, raise its hatching `--tono` (0 → 0.10–0.17 on hover); never add a shadow, a border glow, or a lighter fill.

## Shapes

Zero corner radius everywhere (`{rounded.none}`) — buttons, inputs, plates, panels and the nav are all hard-cornered. Borders are 1px and always a warm rule color; the only 2px stroke in the system is the focus ring.

The **rhombus** is the recurring silhouette: a square rotated 45° with a 1px `{colors.hueso-3}` border, at 5px (nav active marker, absolutely centered under the link), 6px (list bullet), 7px (layer marker, mobile menu row), and as three nested percentage-sized frames at 58/74/90% around the hero eye at opacities 0.30 / 0.16 / 0.07. A filled variant (`.rombo--lleno`, bone ground) marks the single primary destination in the mobile panel.

The **pleca** — a 4px dashed print rule (2px on, 4px off, 45% opacity) — opens every section heading at 56px wide, and runs vertically at 3px wide as the article blockquote's left edge. It is the system's substitute for a decorative section number.

## Components

### Buttons
- **Shape:** Hard-cornered rectangle (0 radius), 1px border matching its own fill.
- **Primary (`.boton`):** Bone ground, ink text, uppercase 0.75rem at 0.18em, 17px/28px padding, print-offset shadow. Carries a trailing `→` glyph that translates 4px right on hover. Hover lifts the ground to pure white and deepens the offset to 4px; active compresses it to 1px; disabled drops to 0.5 opacity and no shadow.
- **Ghost (`.boton--linea`):** No fill, bone text, `{colors.linea-2}` border, no shadow. On hover only the border brightens to bone. This is the nav CTA and any secondary action beside a primary.
- **Text link (`.enlace`):** Uppercase micro-label with a 1px `{colors.hueso-4}` underline offset 5px below the baseline, brightening to bone on hover. Inline prose links (`.enlace-txt`) use the same underline at reading size.
- **Full width at 640px:** actions stack and the button centers its content.

### Inputs / Fields
- **Style:** Ink ground (one step *darker* than the form plate it sits on), 1px `{colors.linea-2}` border, 14px/16px padding, 0.9375rem, no radius. Labels are uppercase 0.6875rem micro-type at 0.18em with a bone-colored required asterisk.
- **Focus:** Border goes to full bone, native outline suppressed. No glow, no fill change.
- **Error:** Border to brick (`{colors.error}`) via `aria-invalid="true"`; the shared status region shows brick-light text on a brick-dark border.
- **Select:** Native appearance stripped; the dropdown indicator is an inline SVG **rhombus**, not a chevron — the module carries even this.
- **Checkbox rows (`.check`):** Bordered rectangles in an auto-fit grid (min 208px), border brightening on hover and staying at `{colors.hueso-3}` while checked via `:has(input:checked)`. Bone accent color on the native control.

### Navigation
Fixed 72px bar over a translucent ink backdrop (`rgba(11,10,9,0.86)` + 14px blur). Transparent bottom border at rest, gaining a rule once scrolled past 10px; the whole bar translates fully out of view when scrolling down past 260px and returns on scroll up. Links are bone-muted uppercase 0.6875rem at 0.2em; hover and `aria-current="page"` both go bone, and the current page additionally carries a 5px filled rhombus centered 6px below. Below 900px the link row and the CTA are replaced by a 44px bordered button whose two 1px rules cross into an X, opening a full-width ink-plate panel of 1.5rem black-weight links, each with a trailing rhombus, dismissible on link click or Escape.

### Row Plate (`.plancha` / `.renglon`)
The system's replacement for the service card. A shared top rule; each row is a baseline-aligned grid with a bordered bottom edge, an uppercase frame label, a title, a description, and a right-aligned action word. Hovering the row raises a hidden hatch field from `--tono: 0` to `0.10` and brings the action word from `{colors.hueso-4}` to bone. There is no background change, no lift, no border highlight. `.nota` (article list) is the same component at different column proportions.

### Layer Strip (`.capas` / `.capa`)
Four bordered cells that read as a single engraved band under the hero, each with its own hatch field (revealed to `--tono: 0.13` on hover), a rhombus pinned top-right, a layer numeral in micro-type, a title, and one line of body. Its stagger index is passed in as `--i` on the element.

### Declaration Band (`.declara`)
The page's one bone plate. Ground flips to bone, and the hatch field flips with it: `--trazo: var(--tinta)` makes the same `.buril` material draw ink lines on paper instead of bone lines on ink. The field is masked by a radial gradient that keeps the center clear and lets the hatching close in at the edges. Content is a single centered light-weight statement at 20ch with one dimmed clause.

### The Burin Field (`.buril`) — signature material
An absolutely positioned, pointer-transparent layer filling its parent, painted with a `repeating-linear-gradient` and driven entirely by five custom properties: `--ang` (stroke angle, default 90deg), `--paso` (pitch, default 5px), `--peso` (stroke weight, default 0.6px), `--tono` (opacity, default 0.16), and `--trazo` (stroke color, default bone — set to ink to invert the field for bone-ground regions). It is masked per context by linear or radial gradients so the hatching opens and closes the way engraved shading does. Contexts set their own values inline: the hero uses 104deg at 5px under a radial mask, the closing block 118deg under a diagonal mask, rows and layers start at `--tono: 0` and rise on hover.

Its one hard invariant: the field is a material layer and never a grid cell. An explicit specificity guard re-asserts `position: absolute` for `.buril` under every container that would otherwise capture it as a child (`.renglon`, `.nota`, `.cierre`, `.forma`, `.pie`, `.declara`, `.capa`, `.portada`, `.seccion`, `.seccion--placa`). Any new container that hosts a burin field must be added to that guard.

### The Eye (`.ojo-caja`) — signature composition
The hero mark is not an image element. Three nested rhombus frames at descending opacity surround a rotated, overflow-clipped rhombus containing a 45° hatch field; at the center, a `div` whose background is a dense 92° hatch (1.15px bone strokes at 2.3px pitch) is masked by the isotipo PNG, so the mark itself is composed of engraved lines rather than placed as artwork. It carries `role="img"` and an accessible name.

### Motion
One authored moment, on load, on the hero only. The `grabar` keyframe wipes `clip-path: inset(0 100% 0 0)` open left-to-right — the headline, subtitle, and actions are literally engraved onto the plate. `abrir-ojo` scales and fades the eye in at 0.34s; `escribir-rombo` draws each rhombus frame in sequence at 0.42 / 0.54 / 0.66s. The four layers then enter staggered by `calc(0.72s + var(--i) * 0.09s)`. Easing is `cubic-bezier(0.16, 1, 0.3, 1)` for the engraving moment and `cubic-bezier(0.22, 0.75, 0.20, 1)` for all state transitions (0.2–0.5s). `prefers-reduced-motion: reduce` kills all animation and clamps transitions to 0.01ms.

## Do's and Don'ts

### Do:
- **Do** build new content structures as full-bleed rows on a `.plancha` — a shared top rule, per-row bottom borders, baseline-aligned columns — rather than as cards.
- **Do** give a new region depth by hosting a `.buril` field and tuning `--ang`, `--paso`, and `--tono`, and mask it so the hatching opens or closes across the region.
- **Do** add any new burin-hosting container to the `position: absolute` specificity guard in the same commit that introduces it.
- **Do** flip `--trazo: var(--tinta)` whenever a region takes bone ground, so the material inverts with the plate instead of disappearing.
- **Do** compose H1s as a mixed-weight sentence: 300 setup, 800 claim, exactly one word in the bone box.
- **Do** use the rhombus for any marker, bullet, or indicator that would otherwise want an icon — including form control affordances.
- **Do** keep text at or above `{colors.hueso-4}` on ink, and keep prose capped at 68ch.
- **Do** author every string in `sitio/build.py`; the emitted `index.html` files are regenerated and hand edits are lost.

### Don't:
- **Don't** add a second typeface. Contrast is weight (300 vs 800) and tracking, inside one family.
- **Don't** introduce corner radius. Every surface in the system is hard-cornered.
- **Don't** use a blurred shadow. The only shadow is the button's zero-blur print offset.
- **Don't** put a second bone-ground band on a page; the declaration band is the one plate.
- **Don't** let a `.buril` become a grid or flex child — it is a material layer, and a captured field will reflow the layout it was meant to sit behind.
- **Don't** add photographic or illustrative imagery, or an icon set. The isotipo mask and the rhombus are the only figures.
- **Don't** put an uppercase eyebrow above every section; the label register is one voice used sparingly.
- **Don't** attach scroll-triggered reveals. Motion is the single load-time engraving of the hero plus the layer stagger, and it yields to `prefers-reduced-motion`.
- **Don't** ship `#000` or a cool gray. Both ink and bone neutrals are warm.
