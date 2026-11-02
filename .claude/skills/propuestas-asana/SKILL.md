---
name: propuestas-asana
description: Seguimiento de propuestas comerciales de Sentido en Asana. Úsalo SIEMPRE que se trabaje una propuesta (propuestas.sentido.mx) — al arrancar un prospecto nuevo, al publicar la propuesta y al hacer ajustes/activación de una propuesta existente. Crea la tarea en Sentido ⚡️ → 📑 PROPUESTAS bajo la madre del mes, comenta el enlace al publicar, lee los comentarios (recursos, notas de reunión) como insumo de los ajustes y deja constancia de cada ronda. Recuerda qué tarea es de cada propuesta para no tener que buscarla ni duplicarla.
---

# Agente de propuestas · seguimiento en Asana

**Objetivo:** Jos ya no crea ni gestiona a mano las tareas de propuestas. El agente las
crea, les pega el enlace y las usa como bitácora; Jos (y Mel/Beth) solo comentan ahí.

Esta skill es **autosuficiente**: solo necesita el conector/MCP de **Asana**. Funciona igual
en Claude Code (nube o local, en cualquier repo), en claude.ai (chat/Proyectos) y en Cowork.
Si además hay acceso a los repos, usa las capas extra de memoria (ver «Memoria»).

## Estructura en Asana (no inventar otra)

- Workspace `1113680433356414` · proyecto **Sentido ⚡️** `1130481524551722` →
  sección **📑 PROPUESTAS** `1150716302405709`.
- **Madre del mes:** `Sentido - Propuestas {Mmm} {AAAA}` con Mmm ∈ Ene Feb Mar Abr May Jun
  Jul Ago Sep Oct Nov Dic (ej. `Sentido - Propuestas Nov 2026`). Las madres viejas tienen
  variantes ("Abril 2026", "Sept 2025", "Dic 2025 "): reconocer por mes+año, no texto exacto.
- **Propuesta = subtarea de la madre** (solo `parent`, no se agrega al proyecto):
  `Sentido - Propuesta {Prospecto}`.
  - **Notas** = brief/contexto (servicios, costos, comisiones) + la línea marcador
    `PROPUESTA: https://propuestas.sentido.mx/{slug}`.
  - **Comentarios** = bitácora: recursos, notas de reunión, enlaces, ajustes.
- Equipo (gid de usuario): Jos `29910024506284` · Mel `29891836434073`.

## Memoria — cómo se recuerda qué tarea es de qué propuesta

`slug` = kebab-case sin acentos = carpeta `propuestas/{slug}/` = URL `propuestas.sentido.mx/{slug}`.
Tres capas; se usa la que esté disponible y se escriben **todas** las que estén disponibles:

1. **Asana (universal, siempre disponible):** el marcador `PROPUESTA: https://propuestas.sentido.mx/{slug}`
   en las notas de la tarea. Se encuentra con `search_tasks(text="propuestas.sentido.mx/{slug}",
   projects_any=…)` o, si falla la búsqueda, recorriendo las subtareas de las madres.
2. **Repo de propuestas `jos-sentido/Sentido`:** en `proposals.json`, el registro del slug lleva
   `"asana": {"tarea_gid": "…", "madre_gid": "…"}` (lo muestra el panel `/admin`).
3. **Repo `jos-sentido/sentido-core`:** `propuestas/{slug}.yaml` (estado + bitácora de eventos) y
   la CLI `python core/propuestas/asana_propuestas.py buscar|plan-alta|--selftest`
   (spec: `core/docs/16_Agente_Propuestas_Asana.md`).

## Paso 0 · ¿Qué propuesta es? (siempre primero, antes de crear nada)

1. Memoria de repo si existe: `proposals.json` → `asana.tarea_gid`, o `buscar "<prospecto>"` en sentido-core.
2. Si no: `search_tasks(text="propuestas.sentido.mx/{slug}")`, luego `search_tasks(text="<prospecto>")`.
3. Si no: `get_tasks(section=1150716302405709)` → madres incompletas → `get_task(madre)` y
   comparar los nombres de sus subtareas, normalizados (sin acentos/mayúsculas; aguanta
   "AsianStory", "Propusta BLACKROCK", "CDM" = Casa de Maty).
   - Un candidato claro → es esa. **Vincúlala** (escribe la memoria y agrega el marcador si falta).
   - Varios o dudoso → preguntar a Jos cuál es (por nombre de tarea, no por gid).
   - Ninguno → prospecto nuevo → Momento 1.

## Momento 1 · Prospecto NUEVO (al arrancar, antes de diseñar)

1. Madre del mes actual: buscarla en la sección; si no existe, `create_tasks` con
   `project` + `section` de arriba y el nombre `Sentido - Propuestas {Mmm} {AAAA}`.
2. Crear **una** subtarea (`parent` = madre): nombre `Sentido - Propuesta {Prospecto}`,
   asignada a Jos (o a quien diga Jos), `due_on` = hoy + 5 días hábiles, notas:
   ```
   PROSPECTO: {Prospecto}
   Origen / contacto: …            (si se sabe)
   Servicios a cotizar: …          (si se sabe)
   CONTEXTO
   …lo que Jos contó: dolores, objetivos, reunión…
   PROPUESTA: https://propuestas.sentido.mx/{slug}   (en producción)
   — Tarea creada por el agente de propuestas. Recursos, notas de reunión y ajustes van en COMENTARIOS.
   ```
3. Escribir memoria (capas 2 y 3 si hay repos). Darle a Jos el enlace `https://app.asana.com/0/0/{gid}`.

## Momento 2 · Propuesta LISTA / publicada

1. Publicar como siempre en `propuestas.sentido.mx/{slug}`.
2. `add_comment` en la tarea:
   ```
   ✅ Propuesta publicada
   https://propuestas.sentido.mx/{slug}
   {resumen de 1–3 líneas: alcance, plan recomendado}
   — agente de propuestas
   ```
3. Memoria: evento `publicada` (sentido-core) y `asana` en `proposals.json`.

## Momento 3 · AJUSTES / activación (seguimiento)

1. Paso 0 → la tarea.
2. **Leer la tarea como insumo:** `get_task` (notas) + `get_task_stories(resource_subtype="comment_added")`.
   Ahí están los recursos que compartió el prospecto, notas de reuniones y pedidos de Jos/Mel.
   Lo nuevo = comentarios posteriores al último comentario firmado `— agente de propuestas`.
   Abrir los enlaces (Drive/Docs) que traigan.
3. Aplicar los cambios a la propuesta y re-publicar (mismo slug, mismo URL).
4. `add_comment`:
   ```
   🔁 Ajustes aplicados a la propuesta (origen: reunión 4 nov / comentario de Mel / …)
   Solicitado:
   • …
   Aplicado:
   • …
   Pendiente / por confirmar:
   • …
   Versión vigente: https://propuestas.sentido.mx/{slug}
   — agente de propuestas
   ```
5. Si cambió la etapa (presentada, negociación, ganada, perdida) → reflejarlo en la memoria
   (`estatus` en `proposals.json`, `estado` en sentido-core).
6. Lo que Jos cuente en el chat (reunión, recurso) y no esté en Asana → asentarlo también como
   comentario (`🗓 Notas de reunión` / `📎 Recurso`) para que la tarea sea la fuente.

## Flujo automático con el equipo de ventas (ronda cada hora)

Una tarea programada en la nube corre cada hora (L–V) y sigue
`sentido-core/agentes/propuestas/ronda-horaria.md`. Estructura que usa ventas:

```
Madre del mes → Tarea del VENDEDOR (asignada a él: prospecto + lo que platicaron)
                  └─ Subtarea para JOS (asignada a Jos: aquí va el borrador y la revisión)
```

Palabras clave (en comentarios, como palabra suelta):

| Palabra | Quién | Qué hace el agente |
|---|---|---|
| *(nueva subtarea para Jos)* | vendedor | arma el borrador v1, lo publica y lo comenta en la subtarea de Jos |
| **`lpc`** — Lista Para Compartir | solo Jos | avisa al vendedor en su tarea (mención) que la vN está aprobada |
| **`pac`** — Producir Ajustes Cliente | vendedor o Jos | produce la vN+1 con lo pedido y la deja en revisión con Jos |

Ciclo: nueva → borrador v1 → `lpc` → `pac` → ajustes v2 → `lpc` → … Cada comentario del agente
termina con `— agente de propuestas · <tipo> v<n> · ref <gid>`: es la memoria de la ronda,
**no borrar ni editar esas firmas**. Cuando Jos trabaja ajustes en vivo (en una sesión), no hace
falta `pac`; al terminar basta con escribir `lpc` en su subtarea para que se avise al vendedor.

## Reglas

- **Nunca duplicar**: si hay memoria o una tarea que coincide, se usa esa.
- **Una tarea por propuesta**, creada de una en una (no en lote: Asana inserta arriba).
- La propuesta se queda en la madre del mes en que **arrancó**, aunque se ajuste meses después.
- Comentarios del agente firmados `— agente de propuestas`.
- Si la tarea la creó Mel/Beth (con costos/comisiones), **respetarla**: solo agregar el marcador y comentar.
- Asana da 5xx transitorios: reintentar antes de asumir fallo.
