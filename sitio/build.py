#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el sitio estático de sentido.mx bajo /sitio."""

import os, pathlib

ROOT = pathlib.Path("/home/user/Sentido/sitio")
BASE = "/sitio"          # prefijo de rutas — cambiar a "" si el sitio pasa a la raíz del dominio
ASSETS = f"{BASE}/assets"
LOGO = "/assets/logo-sentido-light.png"
WA = "https://wa.me/5213222253390"   # mismo número que usa el brochure de Sentido
MAIL = "jos@sentido.mx"

NAV = [
    ("Método",    f"{BASE}/metodo"),
    ("Servicios", f"{BASE}/servicios"),
    ("Casos",     f"{BASE}/casos"),
    ("Blog",      f"{BASE}/blog"),
]

# Tipografías auto-hospedadas: sin dependencia de Google, sin FOUT por DNS externo.
PRELOAD = [
    "inter-tight-300600-normal-latin.woff2",
    "instrument-serif-400-normal-latin.woff2",
]


def head(title, desc, canonical, extra=""):
    preloads = "".join(
        f'<link rel="preload" href="{ASSETS}/fonts/{f}" as="font" type="font/woff2" crossorigin />\n'
        for f in PRELOAD
    )
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="theme-color" content="#08080A" />
<link rel="canonical" href="https://sentido.mx{canonical}" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Sentido · Branding &amp; Advertising" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:locale" content="es_MX" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="/assets/isotipo-sentido.png" />
{preloads}<link rel="stylesheet" href="{ASSETS}/fonts.css" />
<link rel="stylesheet" href="{ASSETS}/sentido.css" />
{extra}</head>
<body>
<div class="progress" aria-hidden="true"></div>
<a class="skip" href="#main">Saltar al contenido</a>
"""


def nav(active=None):
    links = "".join(
        '<a class="nav-a" href="%s"%s>%s</a>' % (
            href, ' aria-current="page"' if label == active else "", label
        )
        for label, href in NAV
    )
    panel = "".join(
        f'<a href="{href}">{label}<span>0{i+1}</span></a>'
        for i, (label, href) in enumerate(NAV)
    )
    return f"""<header class="nav">
  <div class="nav-inner">
    <a class="brand" href="{BASE}/" aria-label="Sentido — inicio">
      <img src="{LOGO}" alt="Sentido" data-fallback />
    </a>
    <nav class="nav-links" aria-label="Principal">{links}</nav>
    <a class="nav-cta" href="{BASE}/contacto">Hablemos</a>
    <button class="nav-toggle" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav-panel">
      <span></span><span></span>
    </button>
  </div>
</header>
<div class="nav-panel" id="nav-panel">
  {panel}
  <a href="{BASE}/contacto">Hablemos<span>→</span></a>
</div>
"""


def cta_block(title, text, primary=("Agendar diagnóstico", f"{BASE}/contacto"), secondary=None):
    sec = ""
    if secondary:
        sec = f'<a class="btn btn--ghost" href="{secondary[1]}">{secondary[0]} <span class="arw">→</span></a>'
    return f"""<section class="section">
  <div class="wrap">
    <div class="cta-block reveal">
      <span class="eyebrow">Siguiente paso</span>
      <h2>{title}</h2>
      <p class="dim">{text}</p>
      <div class="btn-row" style="margin-top:8px">
        <a class="btn btn--solid" href="{primary[1]}">{primary[0]} <span class="arw">→</span></a>
        {sec}
      </div>
    </div>
  </div>
</section>
"""


def footer():
    servicios = "".join(
        f'<li><a href="{BASE}/servicios/{s["slug"]}">{s["short"]}</a></li>' for s in SERVICES
    )
    return f"""<footer class="footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <img src="{LOGO}" alt="Sentido" data-fallback />
        <p>Marca, pauta, tecnología y datos en un mismo sistema — para que cada peso invertido en marketing produzca leads, ventas y clientes que regresan.</p>
      </div>
      <div class="footer-col">
        <span class="kicker">Servicios</span>
        <ul>{servicios}</ul>
      </div>
      <div class="footer-col">
        <span class="kicker">Agencia</span>
        <ul>
          <li><a href="{BASE}/metodo">Método</a></li>
          <li><a href="{BASE}/servicios">Todos los servicios</a></li>
          <li><a href="{BASE}/casos">Casos y sectores</a></li>
          <li><a href="{BASE}/blog">Blog</a></li>
          <li><a href="{BASE}/contacto">Contacto</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <span class="kicker">Contacto</span>
        <ul>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
          <li><a href="{WA}" rel="noopener">WhatsApp</a></li>
          <li><a href="/brochure">Brochure interactivo</a></li>
          <li><a href="https://propuestas.sentido.mx" rel="noopener">Propuestas</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bot">
      <p>© <span data-year>2026</span> Sentido · Branding &amp; Advertising</p>
      <p>Estrategia digital · desde 2010</p>
    </div>
  </div>
</footer>
<script src="{ASSETS}/sentido.js" defer></script>
</body>
</html>
"""


def write(path, html):
    p = ROOT / path if path else ROOT
    p.mkdir(parents=True, exist_ok=True)
    (p / "index.html").write_text(html, encoding="utf-8")
    print("  ✓", (p / "index.html").relative_to(ROOT.parent))


# ═══════════════════════════════════════════════════════════════
# DATOS · SERVICIOS
# ═══════════════════════════════════════════════════════════════

SERVICES = [
    {
        "slug": "redes-meta",
        "letter": "A",
        "short": "Gestión de Redes Meta",
        "name": "Gestión de Redes Meta",
        "tag": "Módulo mensual",
        "tag2": "Meta Ads incluido",
        "sub": "Instagram + Facebook",
        "lede": "Contenido que distribuye, pauta que alcanza, comunidad que se construye. No publicaciones sueltas — un calendario planeado por segmento de audiencia y respaldado por la pauta que lo pone frente a la gente correcta.",
        "problem": "El error común es tratar las redes como un canal de publicación. Publicar bonito y consistente no mueve el negocio si el contenido no está diseñado para un segmento concreto y no hay presupuesto detrás que lo distribuya. La cuenta crece en seguidores y no en clientes.",
        "includes": [
            "15 publicaciones mensuales: 6 reels, 3 carruseles, 6 posts fijos + adaptación a historias",
            "Planeación estratégica por segmento de audiencia, no calendario genérico",
            "Producción gráfica, edición de video y copywriting de marca",
            "Contenido producido con IA para escalar lo visual sin depender de sesiones constantes",
            "Configuración, segmentación y optimización de campañas Meta Ads — incluido en el módulo",
            "Administración de perfiles, primer contacto automatizado y redirección a WhatsApp o CRM",
            "Reporte mensual de alcance, engagement y leads generados",
        ],
        "ia": "Meta Advantage+ alimentado con las conversiones reales del CRM, A/B testing continuo de creativos generados con IA y optimización automática de audiencias. El algoritmo aprende con datos del negocio, no con señales genéricas de plataforma.",
        "for_whom": "Marcas con producto o servicio definido que necesitan presencia constante y captación por social. Especialmente potente cuando ya existe un CRM que devuelve las conversiones a la plataforma.",
        "kpis": ["Leads generados y costo por lead", "Alcance y frecuencia por segmento", "Engagement por formato", "Conversaciones iniciadas a WhatsApp"],
        "note": "El presupuesto de pauta va aparte y se paga directo a Meta con el medio de pago del cliente. Rango típico: $5,000 – $15,000 MXN al mes, calibrado en el diagnóstico.",
        "related": ["google-ads", "crm-automatizacion"],
    },
    {
        "slug": "google-ads",
        "letter": "B",
        "short": "Google Ads",
        "name": "Google Ads",
        "tag": "Módulo mensual",
        "tag2": "Search · PMax · Demand Gen",
        "sub": "Captura de intención",
        "lede": "Captura de intención de búsqueda en el momento exacto en que tu mercado teclea lo que tu marca resuelve. Es el canal con la intención más caliente que existe — y el que más se desperdicia cuando se configura sin criterio.",
        "problem": "Google Ads mal montado quema presupuesto con una eficiencia notable: keywords amplias sin intención, campañas que mandan todo el tráfico al home, y automatizaciones que optimizan hacia clics porque nadie les enseñó qué es una conversión real.",
        "includes": [
            "Investigación de keywords por intención y por etapa del funnel",
            "Creación de campañas Search + Performance Max, y Demand Gen cuando aplica",
            "Segmentación geográfica calibrada al área real de operación",
            "Landing pages específicas por audiencia, conectadas al sitio",
            "Optimización semanal de pujas, palabras y anuncios",
            "Exclusiones y negativas trabajadas de forma continua, no una vez al arranque",
            "Reporte mensual con CPL, conversiones y ROI estimado",
        ],
        "ia": "Estrategia híbrida humano + máquina. Sentido define el marco, la intención y las exclusiones; Smart Bidding, Performance Max y Demand Gen optimizan dentro de ese marco alimentados con las conversiones del CRM — no con conversiones de formulario sin calificar.",
        "for_whom": "Negocios con demanda existente: alguien ya está buscando lo que vendes. Ideal para servicios locales, inmobiliario, industrial, salud y cualquier categoría con ticket que justifique el costo por clic.",
        "kpis": ["CPL por campaña y por keyword", "Conversiones calificadas vs. totales", "Cuota de impresiones en términos clave", "ROI estimado por canal"],
        "note": "El presupuesto de pauta va aparte y se paga directo a Google con el medio de pago del cliente. Rango típico: $3,000 – $8,000 MXN al mes, calibrado en el diagnóstico.",
        "related": ["sitios-web", "crm-automatizacion"],
    },
    {
        "slug": "crm-automatizacion",
        "letter": "C",
        "short": "CRM + Automatización",
        "name": "CRM + Automatización + Reputación",
        "tag": "Módulo mensual",
        "tag2": "Setup sin costo",
        "sub": "El nervio del sistema",
        "lede": "Donde cada lead que entra se convierte y cada cliente se retiene. Es la capa que casi ninguna marca atiende — y la que decide si la inversión en pauta se transforma en ventas o se queda en una bandeja saturada.",
        "problem": "La mayoría de los leads no se pierden por falta de interés: se pierden por tiempo de respuesta y por seguimiento inconsistente. Sin pipeline, sin automatización y sin atribución, nadie sabe qué campaña trajo al cliente que sí compró.",
        "includes": [
            "Pipeline configurado a la realidad del negocio, con etapas específicas",
            "Captura automática de leads desde redes, sitio, WhatsApp y pauta",
            "Respuesta inicial automatizada en menos de 60 segundos",
            "Recordatorios de pedido recurrente y reactivación de clientes inactivos",
            "Monitoreo y respuesta a reseñas, más campañas para clientes recurrentes",
            "Filtrado estratégico de reseñas negativas hacia un formulario privado",
            "1 número de WhatsApp, mensajes ilimitados, correos ilimitados",
            "Implementación inicial sin costo con mantenimiento mensual activo",
        ],
        "ia": "Scoring de leads por probabilidad de conversión, respuestas iniciales asistidas con LLM en el tono de la marca, y predicción de churn y oportunidades de recompra sobre la base existente.",
        "for_whom": "Cualquier negocio que ya recibe leads y no tiene un proceso que los ordene. Es el módulo que recomendamos activar primero cuando el volumen existe pero el cierre no acompaña.",
        "kpis": ["Tiempo de primera respuesta", "Tasa de contacto y de cita agendada", "Conversión por etapa del pipeline", "Reseñas nuevas y calificación promedio"],
        "note": "Operado sobre GoHighLevel. La implementación inicial no tiene costo adicional mientras el mantenimiento mensual esté activo.",
        "related": ["email-marketing", "google-business-profile"],
    },
    {
        "slug": "google-business-profile",
        "letter": "D",
        "short": "Google Business Profile",
        "name": "Google Business Profile",
        "tag": "Módulo mensual",
        "tag2": "Posicionamiento local",
        "sub": "El activo local más subutilizado",
        "lede": "Cada búsqueda en Maps cerca de tu domicilio debería encontrarte antes que a la competencia. Es tráfico con intención altísima, gratuito, y casi siempre abandonado a su suerte.",
        "problem": "Un perfil sin publicaciones, con fotos viejas, horarios desactualizados y reseñas sin responder le dice a Google exactamente lo que no quieres: que ese negocio no está activo. El resultado es caer en el ranking local frente a competidores que sí lo trabajan.",
        "includes": [
            "Optimización inicial del perfil y verificación",
            "6 publicaciones mensuales derivadas del calendario de redes",
            "Actualización continua de información, horarios, fotos y promociones",
            "Gestión de preguntas y reseñas desde el CRM",
            "Estrategia de posicionamiento en Maps por zona de cobertura",
            "Reporte mensual de visitas, clics y solicitudes de ruta",
        ],
        "ia": "Respuestas a reseñas asistidas con IA preservando el tono de la marca, y análisis de sentimiento para detectar patrones reales de mejora del servicio — no solo apagar fuegos uno por uno.",
        "for_whom": "Todo negocio con ubicación física o área de servicio definida: clínicas, clubes, restaurantes, showrooms, constructoras con oficina, retail local.",
        "kpis": ["Visitas al perfil y búsquedas de descubrimiento", "Clics a sitio, llamadas y solicitudes de ruta", "Reseñas nuevas y calificación promedio", "Posición en el paquete local de Maps"],
        "note": "Incluido dentro del paquete integral. También se puede contratar por separado.",
        "related": ["crm-automatizacion", "redes-meta"],
    },
    {
        "slug": "email-marketing",
        "letter": "E",
        "short": "Email Marketing",
        "name": "Email Marketing + Automatización avanzada",
        "tag": "Módulo mensual",
        "tag2": "Complemento del paquete",
        "sub": "La base de datos como activo",
        "lede": "Tu base de datos no es una lista: es un activo. Email y automatización extraen valor de cada lead y de cada cliente una y otra vez, sin volver a pagar por adquirirlos.",
        "problem": "Adquirir un cliente nuevo cuesta entre cinco y siete veces más que reactivar a uno que ya te compró. Aun así, la mayoría de los negocios acumula miles de contactos dormidos en hojas de cálculo, en el punto de venta y en WhatsApp, sin ninguna comunicación consistente.",
        "includes": [
            "Estrategia de segmentación por etapa del ciclo de cliente",
            "2 campañas mensuales a la base de datos completa",
            "Flujos automatizados: bienvenida, nutrición, recuperación de carrito, recompra y reactivación",
            "Diseño y copywriting de cada plantilla, alineado al branding",
            "Pruebas A/B en subject lines y CTAs para optimizar apertura y clic",
            "Reporte mensual de entregabilidad, apertura, clic y conversión atribuida",
        ],
        "ia": "Send time optimization por receptor, generación y A/B testing continuo de subject lines, segmentación dinámica por comportamiento y personalización de contenido a nivel individual.",
        "for_whom": "Negocios con base histórica acumulada: clubes y fitness con socios, clínicas con pacientes recurrentes, hospitalidad y retail local con clientela repetida, e-commerce con carritos abandonados.",
        "kpis": ["Entregabilidad y tasa de rebote", "Apertura y clic por segmento", "Clientes reactivados", "Ingreso atribuido a email"],
        "note": "Complemento del paquete mensual. Cuando la base es grande y está fría, suele ser el módulo con mejor retorno del primer trimestre.",
        "related": ["crm-automatizacion", "redes-meta"],
    },
    {
        "slug": "branding",
        "letter": "F",
        "short": "Branding e Identidad",
        "name": "Branding · Identidad de Marca",
        "tag": "Inversión única",
        "tag2": "Alcance modular",
        "sub": "El marco que sostiene todo",
        "lede": "Antes del sitio, antes de la pauta, antes del CRM — la marca. Naming, identidad y narrativa con la robustez necesaria para sostener todo lo que viene después.",
        "problem": "Cuando la marca no está resuelta, todo lo demás se vuelve más caro. Cada campaña necesita reinventar el tono, cada pieza se ve distinta, cada landing improvisa su propio lenguaje. El presupuesto se va en resolver de nuevo lo que debió definirse una vez.",
        "includes": [
            "Investigación de mercado, competencia y posicionamiento estratégico",
            "Naming (opcional, según el caso) y arquitectura de marca",
            "Identidad visual completa: logotipo, sistema gráfico, paleta, tipografía, iconografía",
            "Manual de marca con reglas de uso, tono de voz y aplicaciones",
            "Aplicaciones base: tarjetas, papelería digital, plantillas de redes, firma de correo",
            "Versiones para uso digital, impresión, redes y formatos especiales",
        ],
        "ia": "Investigación de mercado y competencia aceleradas con IA, exploración visual asistida para validar dirección antes de invertir en producción, y tono de voz documentado en un formato que los agentes de IA del cliente puedan usar directamente.",
        "for_whom": "Marcas nuevas, marcas que cambian de etapa, y negocios con identidad heredada que ya no sostiene la ambición actual. Si la marca ya resuena en su mercado, este módulo puede esperar.",
        "kpis": ["Consistencia de aplicación entre canales", "Reconocimiento en pruebas con audiencia", "Reducción del costo de producción por pieza"],
        "note": "Inversión única con alcance modular. Se cotiza aparte del paquete mensual y suele ir antes que el sitio web.",
        "related": ["sitios-web", "redes-meta"],
    },
    {
        "slug": "sitios-web",
        "letter": "G",
        "short": "Sitio Web Estratégico",
        "name": "Sitio Web Estratégico",
        "tag": "Inversión única",
        "tag2": "Desde $20,000 MXN · ~2 semanas",
        "sub": "El hub donde converge el sistema",
        "lede": "No una tarjeta de presentación: infraestructura construida para convertir tráfico en lead, integrarse con cada capa del sistema y crecer con la marca. Producido con un workflow potenciado por IA que redujo el tiempo de meses a semanas.",
        "problem": "El sitio suele ser lo último que se atiende y lo primero que rompe la cadena. Campañas que aterrizan en un home genérico, formularios que llegan a un correo que nadie revisa, cero medición. La pauta paga el clic y el sitio lo desperdicia.",
        "includes": [
            "Arquitectura por audiencia con rutas diferenciadas hacia la conversión",
            "Diseño visual alineado al branding, mobile-first",
            "Chatbot entrenado con la información real del negocio: catálogo, precios, políticas",
            "Cotizadores en tiempo real que convierten el cálculo en un lead calificado",
            "Formularios inteligentes con notificación inmediata y conexión a CRM",
            "Integración nativa con CRM, Meta Pixel, Google Ads y GA4",
            "SEO técnico y Core Web Vitals cuidados desde el build",
            "Contenido visual producido con IA, sin depender de una sesión de foto costosa",
            "CMS administrable y arquitectura preparada para crecer",
        ],
        "ia": "Análisis automático de comportamiento y heatmaps para detectar fricciones, A/B testing continuo de hero y CTAs, y personalización dinámica según la fuente de tráfico. La dirección creativa la pone Sentido; la IA pone la velocidad de ejecución.",
        "for_whom": "Marcas que van a invertir en pauta y necesitan un destino que convierta, o negocios cuyo sitio actual ya no representa el nivel del producto. También para quien necesita un cotizador o chatbot que antes era inviable de desarrollar.",
        "kpis": ["Tasa de conversión por audiencia", "Leads por fuente de tráfico", "Core Web Vitals", "Conversaciones y cotizaciones iniciadas"],
        "note": "Inversión única desde $20,000 MXN + IVA, con entrega promedio de ~2 semanas. El alcance específico se cierra después del diagnóstico.",
        "related": ["branding", "google-ads"],
    },
]

SERV_BY_SLUG = {s["slug"]: s for s in SERVICES}

LAYERS = [
    ("01", "Alcance", "Redes Meta · Google Ads · Google Business Profile",
     "Llegar a las personas correctas con el mensaje correcto, en el canal donde ya están buscando o donde ya están consumiendo contenido. Combina presencia orgánica — contenido y comunidad — con captura de intención en search, maps y social ads."),
    ("02", "Captura", "Sitio Web Estratégico · Landings por audiencia",
     "Convertir tráfico en lead o pedido. El sitio no es una tarjeta de presentación: es el destino donde cada campaña aterriza con una ruta clara hacia la conversión, calibrada por audiencia."),
    ("03", "Conversión", "CRM · Automatización · WhatsApp · Email",
     "Convertir leads en clientes. Pipeline configurado a la realidad del negocio, respuesta automática en menos de 60 segundos, seguimiento humano apoyado en flujos automatizados y atribución medida hasta el cierre."),
    ("04", "Retención + Reputación", "Reseñas · Recompra · Reactivación",
     "El cliente no termina en la primera venta. Reseñas que alimentan visibilidad, campañas a base de datos que reactivan inactivos, secuencias de recompra recurrente. La capa que casi nadie atiende y la que más rentabilidad genera."),
]

PROCESS = [
    ("01", "Diagnóstico antes de proponer", "Llamada profunda · Auditoría · Mapa de brechas",
     "No hacemos propuestas desde un catálogo. Antes de cotizar dedicamos 45 a 60 minutos a entender el negocio, su estado actual y dónde está la brecha más cara de no resolver. La propuesta nace del diagnóstico, no de un menú."),
    ("02", "Estrategia escrita, no improvisada", "Plan estratégico · Audiencias · KPIs",
     "Cada cliente recibe un documento estratégico vivo: audiencias priorizadas, mensajes por segmento, métricas que importan y secuencia de prioridades. Es la fuente de verdad de los siguientes doce meses y se actualiza cuando los datos lo piden."),
    ("03", "Construcción en el orden correcto", "Branding → Sitio → CRM → Pauta",
     "Construir en desorden es la causa número uno de presupuesto desperdiciado. El sitio antes que la pauta. El CRM antes que el sitio. Branding antes que todo si la marca aún no resuena. Cada capa se monta sobre la anterior, no en paralelo descoordinado."),
    ("04", "Activación medible desde el día uno", "Pixels · Conversions API · Dashboards",
     "Antes de prender una campaña, el sistema de medición ya está conectado: tracking de conversiones, atribución y dashboards en vivo. Si no se puede medir, no se prende. Es la única manera de saber qué funcionó cuando llegue el momento de optimizar."),
    ("05", "Optimización continua, no entrega", "Reporte mensual · Iteración · Decisiones con datos",
     "El sistema no se entrega, se afina. Cada mes hay un reporte con qué funcionó, qué se ajusta y por qué — y un cliente que entiende sus propios números, no solo recibe una factura."),
]

ONBOARDING = [
    ("01", "Diagnóstico estratégico", "Sin costo · 45 min",
     "Mapeamos el estado actual del sistema — marca, sitio, pauta, CRM — y dónde está la brecha más cara de no resolver."),
    ("02", "Propuesta a medida", "5 días hábiles",
     "Entregamos una propuesta específica para tu marca, mercado y números, con alcance y precios cerrados."),
    ("03", "Onboarding y kickoff", "Semana 1",
     "Firma, accesos a plataformas y kickoff con el equipo asignado. Cronograma de las primeras 4 semanas con entregables semanales."),
    ("04", "Sistema en marcha", "30 días",
     "A 30 días: sitio en vivo, CRM operando, campañas activas y primer reporte. A 90 días: sistema optimizado con data real, no con hipótesis."),
]

MARQUEE = ["Branding", "Meta Ads", "Google Ads", "Sitios web con IA", "CRM & Automatización",
           "WhatsApp", "Email Marketing", "Google Business Profile", "Reseñas", "Reactivación de base",
           "Contenido", "Atribución", "Dashboards"]


# ═══════════════════════════════════════════════════════════════
# HOME
# ═══════════════════════════════════════════════════════════════

def build_home():
    marquee_items = "".join(f"<span>{m}</span>" for m in MARQUEE) * 2

    layers = "".join(f"""
      <article class="layer reveal">
        <div class="layer-num">{n}</div>
        <div class="layer-title">
          <h3>{title}</h3>
          <div class="layer-tag">{tag}</div>
        </div>
        <div class="layer-body">{body}</div>
      </article>""" for n, title, tag, body in LAYERS)

    svc_cards = "".join(f"""
      <a class="card reveal" data-d="{i % 3}" href="{BASE}/servicios/{s['slug']}">
        <div class="card-top">
          <span class="tag">{s['letter']} · {s['tag']}</span>
          <span class="card-arrow">↗</span>
        </div>
        <h4>{s['name']}</h4>
        <p>{s['sub']}. {s['lede'].split('.')[0]}.</p>
      </a>""" for i, s in enumerate(SERVICES))

    ia_fronts = [
        ("01 · Optimización de pauta", "Modelos que aprenden con tus conversiones",
         "Meta Advantage+, Google Performance Max y Demand Gen reciben las conversiones del CRM y refinan audiencias, pujas y creativos sin intervención manual."),
        ("02 · Contenido a escala", "Producción visual y copy sin sesiones constantes",
         "IA para imagen, video y copywriting permite generar variantes para A/B testing sin depender de producción continua. El branding define el marco; la IA acelera la ejecución dentro de él."),
        ("03 · Conversación automatizada", "Respuesta en menos de 60 segundos con criterio humano",
         "LLMs integrados al CRM responden el primer mensaje en el tono de la marca, califican intención y agendan. El humano interviene donde aporta valor real."),
        ("04 · Decisiones con datos", "Una sola vista del sistema completo",
         "Dashboards que combinan pauta, sitio, CRM y reseñas dan una sola vista, no cinco reportes desconectados. La junta mensual deja de ser sobre qué se hizo y pasa a ser sobre qué se ajusta."),
    ]
    ia_grid = "".join(f"""
      <div class="grid-cell reveal" data-d="{i % 2}">
        <span class="kicker" style="margin-bottom:16px">{k}</span>
        <h4 style="margin-bottom:12px">{t}</h4>
        <p class="dim" style="font-size:.9375rem;line-height:1.68">{b}</p>
      </div>""" for i, (k, t, b) in enumerate(ia_fronts))

    products = "".join(f"""
      <a class="card reveal" data-d="{i}" href="{href}">
        <div class="card-top"><span class="tag tag--fill">{tag}</span><span class="card-arrow">↗</span></div>
        <h4>{title}</h4>
        <p>{body}</p>
      </a>""" for i, (tag, title, body, href) in enumerate([
        ("Desde $20,000 MXN", "Sitios web producidos con IA",
         "El sitio que antes costaba una fortuna y tardaba meses — hoy con estética de altísimo nivel, chatbot, cotizador y CRM-ready, entregado en aproximadamente dos semanas.",
         "/sitios-web-ia"),
        ("Operación mensual", "Motor de Reactivación + Reseñas",
         "Operamos tu GoHighLevel: campañas de email y WhatsApp que reactivan a los clientes que ya tienes, más gestión continua del flujo de reseñas en Google.",
         "/reactivacion-ghl-resenas"),
        ("Documento vivo", "Brochure interactivo",
         "El recorrido completo del sistema Sentido: método, proceso, los siete módulos y la capa de IA, en un documento navegable pensado para compartir internamente.",
         "/brochure"),
    ]))

    stats = "".join(f"""
      <div class="stat reveal" data-d="{i % 4}">
        <div class="stat-n">{n}</div>
        <div class="stat-l">{l}</div>
      </div>""" for i, (n, l) in enumerate([
        ("2010", "Operando estrategia digital en México desde entonces"),
        ("4", "Capas del sistema: alcance, captura, conversión y retención"),
        ("&lt;60s", "Tiempo de primera respuesta a cada lead que entra"),
        ("30 días", "Del kickoff al sistema activo con primer reporte"),
    ]))

    html = head(
        "Sentido · Branding &amp; Advertising — El sistema que convierte marketing en negocio",
        "Agencia que conecta marca, pauta, tecnología y datos en un mismo sistema. Branding, Meta y Google Ads, sitios web con IA, CRM y automatización. Guadalajara, México.",
        "/",
    ) + nav() + f"""
<main id="main">

  <section class="hero">
    <div class="wrap">
      <span class="eyebrow reveal">Sentido · Branding &amp; Advertising</span>
      <h1 class="reveal" data-d="1">No se trata de hacer<br />más publicidad.<br /><span class="italic">Se trata del sistema</span><br />que lo vuelve negocio.</h1>
      <p class="hero-sub reveal" data-d="2">
        Conectamos marca, pauta, tecnología y datos en un mismo sistema — para que cada peso
        invertido en marketing produzca leads, ventas y clientes que regresan.
      </p>
      <div class="btn-row reveal" data-d="3">
        <a class="btn btn--solid" href="{BASE}/contacto">Agendar diagnóstico <span class="arw">→</span></a>
        <a class="btn btn--ghost" href="{BASE}/metodo">Ver el método <span class="arw">→</span></a>
      </div>

      <div class="hero-meta reveal" data-d="4">
        <div><span class="kicker">Qué hacemos</span><p>Branding, pauta, sitios web, CRM y retención — operados como una sola estrategia.</p></div>
        <div><span class="kicker">Cómo cobramos</span><p>Módulos mensuales más inversiones únicas. La pauta va directo a Meta y Google.</p></div>
        <div><span class="kicker">Cómo empieza</span><p>Diagnóstico de 45 minutos sin costo. La propuesta nace de ahí, no de un catálogo.</p></div>
      </div>
    </div>
  </section>

  <div class="marquee" aria-hidden="true"><div class="marquee-track">{marquee_items}</div></div>

  <section class="section">
    <div class="wrap">
      <div class="cols cols-sticky">
        <div class="sticky-rail reveal">
          <span class="kicker" style="margin-bottom:20px">01 — El problema</span>
          <h2>Servicios sueltos no construyen un negocio. Un sistema sí.</h2>
        </div>
        <div class="reveal" data-d="1">
          <p class="lede" style="margin-bottom:28px">
            La mayoría de las marcas contratan agencias por pieza: un community por aquí, alguien
            para Google Ads por allá, un diseñador freelance para el sitio. Cada pieza vive en su
            isla, sin hablar con las demás.
          </p>
          <p class="body-lg dim">
            El resultado es predecible: presupuesto que se diluye, decisiones que se contradicen y
            leads que se pierden en el camino entre el anuncio y la venta. Sentido existe porque ese
            modelo ya no alcanza para crecer.
          </p>
          <p class="body-lg dim">
            La marca, la pauta, el sitio y el CRM no son cuatro proyectos. Son cuatro capas del mismo
            sistema — y solo conectadas producen el resultado que cada una promete por separado.
          </p>
          <div class="btn-row">
            <a class="btn btn--ghost" href="{BASE}/metodo">Cómo trabajamos <span class="arw">→</span></a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--line">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">02 — El sistema</span>
        <h2>Cuatro capas, una sola estrategia.</h2>
        <p class="lede">Cada negocio que llega a Sentido se atiende desde estas cuatro capas. Algunas marcas necesitan las cuatro desde el día uno; otras refuerzan la que tienen débil.</p>
      </div>
      {layers}
    </div>
  </section>

  <section class="statement">
    <div class="wrap">
      <p class="reveal">Tu producto ya está listo.<br /><span class="soft">Tu mercado ya está esperando.</span><br />Falta el sistema que los conecta.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">03 — Servicios</span>
        <h2>Lo que componemos en cada capa.</h2>
        <p class="lede">Siete módulos. Algunos clientes activan los cinco mensuales desde el día uno; otros arrancan con dos o tres y suman conforme el sistema demuestra tracción.</p>
      </div>
      <div class="cols cols-2" style="gap:20px">{svc_cards}</div>
      <div class="btn-row">
        <a class="btn btn--ghost" href="{BASE}/servicios">Ver todos los servicios <span class="arw">→</span></a>
      </div>
    </div>
  </section>

  <section class="section section--surface">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">04 — La capa de IA</span>
        <h2>Cada pieza alimenta a las demás.</h2>
        <p class="lede">Las piezas no operan en paralelo desconectado: operan en circuito. Cada lead capturado entrena al modelo de la pauta, cada conversión refina la segmentación, cada reseña alimenta el contenido. La IA no es un módulo aparte — es la capa que conecta y hace que el sistema se optimice mes con mes.</p>
      </div>
      <div class="grid grid-2">{ia_grid}</div>
      <p class="body-lg dim reveal" style="margin-top:32px">
        Esta es la razón por la que el trabajo es continuo y no de entrega única. El sistema del mes
        seis vale más que el del mes uno — con la misma inversión.
      </p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">05 — Productos</span>
        <h2>Servicios que se contratan solos.</h2>
        <p class="lede">Además del sistema integral, hay piezas que resuelven un problema concreto y se activan sin comprometerse con todo el paquete.</p>
      </div>
      <div class="cols" style="grid-template-columns:repeat(3,1fr);gap:20px">{products}</div>
    </div>
  </section>

  <section class="section section--line">
    <div class="wrap">
      <div class="stats">{stats}</div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">06 — Cómo arrancamos</span>
        <h2>De esta página a un sistema en marcha.</h2>
        <p class="lede">Cuatro pasos. El primero es sin costo y sirve para ambas partes: tú entiendes si Sentido encaja con lo que necesitas, y nosotros entendemos si podemos prometer resultados con honestidad.</p>
      </div>
      <div class="steps">""" + "".join(f"""
        <div class="step reveal">
          <div class="step-n">{n}</div>
          <div>
            <h4>{t}</h4>
            <p class="dim">{b}</p>
            <span class="kicker">{meta}</span>
          </div>
        </div>""" for n, t, meta, b in ONBOARDING) + f"""
      </div>
    </div>
  </section>

</main>
""" + cta_block(
        "Cuéntanos qué estás resolviendo.",
        "Un estratega de Sentido te responde en menos de 24 horas hábiles para agendar el diagnóstico. Sin costo, sin compromiso, y con una lectura honesta de si podemos ayudarte.",
        secondary=("Ver casos y sectores", f"{BASE}/casos"),
    ) + footer()

    write("", html)


# ═══════════════════════════════════════════════════════════════
# MÉTODO
# ═══════════════════════════════════════════════════════════════

def build_metodo():
    layers = "".join(f"""
      <article class="layer reveal">
        <div class="layer-num">{n}</div>
        <div class="layer-title"><h3>{t}</h3><div class="layer-tag">{tag}</div></div>
        <div class="layer-body">{b}</div>
      </article>""" for n, t, tag, b in LAYERS)

    process = "".join(f"""
      <div class="step reveal">
        <div class="step-n">{n}</div>
        <div>
          <h4>{t}</h4>
          <p class="dim" style="margin-bottom:10px">{b}</p>
          <span class="kicker">{meta}</span>
        </div>
      </div>""" for n, t, meta, b in PROCESS)

    principles = "".join(f"""
      <div class="grid-cell reveal" data-d="{i}">
        <div class="layer-num" style="margin-bottom:18px">{n}</div>
        <h4 style="margin-bottom:14px">{t}</h4>
        <p class="dim" style="font-size:.9375rem;line-height:1.7">{b}</p>
      </div>""" for i, (n, t, b) in enumerate([
        ("01", "Una sola cabeza estratégica",
         "Brand, pauta, sitio, CRM y reputación se piensan desde la misma estrategia, no desde cinco proveedores que se enteran tarde de lo que decidió el otro."),
        ("02", "Cada peso se mide al final de su recorrido",
         "No medimos clics ni alcance como meta — medimos leads calificados, conversiones y clientes recurrentes. La pauta vive integrada con CRM y sitio, para saber qué funcionó de verdad."),
        ("03", "Sistema que escala sin rehacerse",
         "El sitio, el CRM y los flujos de automatización se construyen desde el día uno para crecer con la marca: más sucursales, más líneas de producto, más mercados, sin volver a empezar."),
    ]))

    onboarding = "".join(f"""
      <div class="step reveal">
        <div class="step-n">{n}</div>
        <div><h4>{t}</h4><p class="dim" style="margin-bottom:10px">{b}</p><span class="kicker">{meta}</span></div>
      </div>""" for n, t, meta, b in ONBOARDING)

    html = head(
        "Método · Sentido Branding &amp; Advertising",
        "El sistema de cuatro capas de Sentido — alcance, captura, conversión y retención — y el método de trabajo que lo sostiene: diagnóstico, estrategia escrita, construcción en orden y optimización continua.",
        "/metodo",
    ) + nav("Método") + f"""
<main id="main">

  <section class="hero hero--page">
    <div class="wrap">
      <span class="eyebrow reveal">Método</span>
      <h1 class="reveal" data-d="1">El sistema,<br /><span class="italic">en cuatro capas.</span></h1>
      <p class="hero-sub reveal" data-d="2">
        La diferencia entre una agencia que entrega piezas y una que construye sistemas no está en
        lo que ofrece — está en cómo trabaja. Esto es lo que pasa cada mes en Sentido, desde el
        primer día hasta el reporte número doce.
      </p>
    </div>
  </section>

  <section class="section section--line">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">01 — Principios</span>
        <h2>Tres reglas que no negociamos.</h2>
      </div>
      <div class="grid grid-3">{principles}</div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">02 — Las cuatro capas</span>
        <h2>Alcance, captura, conversión, retención.</h2>
        <p class="lede">Cada negocio que llega a Sentido se atiende desde estas cuatro capas. La propuesta puntual se arma una vez que entendemos dónde estás parado — algunas marcas necesitan las cuatro desde el día uno; otras solo refuerzan la que tienen débil.</p>
      </div>
      {layers}
    </div>
  </section>

  <section class="statement">
    <div class="wrap">
      <p class="reveal">Construir en desorden<br /><span class="soft">es la causa número uno</span><br />de presupuesto desperdiciado.</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">03 — Cómo trabajamos</span>
        <h2>El método detrás del sistema.</h2>
        <p class="lede">Cinco prácticas que se repiten en cada cuenta, cada mes, sin excepción.</p>
      </div>
      <div class="steps">{process}</div>
    </div>
  </section>

  <section class="section section--surface">
    <div class="wrap">
      <div class="cols cols-sticky">
        <div class="sticky-rail reveal">
          <span class="kicker" style="margin-bottom:20px">04 — Orden de construcción</span>
          <h2>Branding → Sitio → CRM → Pauta.</h2>
        </div>
        <div class="reveal" data-d="1">
          <p class="lede" style="margin-bottom:28px">
            Es la secuencia que más presupuesto ahorra, y la que más se ignora.
          </p>
          <ul class="checks" style="gap:18px">
            <li><strong>Branding antes que todo</strong> — si la marca aún no resuena en su mercado, cada campaña gasta parte del presupuesto en explicar quién eres. Si la marca ya está resuelta, esta capa se salta.</li>
            <li><strong>Sitio antes que la pauta</strong> — pagar por clics que aterrizan en un destino que no convierte es la forma más cara de aprender que el sitio importaba.</li>
            <li><strong>CRM antes que el volumen</strong> — sin pipeline ni respuesta automática, más leads solo significa más leads perdidos. El CRM es lo que convierte volumen en ventas.</li>
            <li><strong>Pauta al final, medible desde el primer peso</strong> — con pixels, Conversions API y atribución conectados antes de prender la primera campaña. Si no se puede medir, no se prende.</li>
          </ul>
          <div class="btn-row">
            <a class="btn btn--ghost" href="{BASE}/servicios">Ver los módulos <span class="arw">→</span></a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">05 — Arranque</span>
        <h2>De la primera llamada al primer reporte.</h2>
        <p class="lede">Cuatro pasos. El primero es sin costo y sirve para ambas partes.</p>
      </div>
      <div class="steps">{onboarding}</div>
    </div>
  </section>

</main>
""" + cta_block(
        "Empecemos por el diagnóstico.",
        "45 minutos para mapear el estado actual del sistema y encontrar la brecha más cara de no resolver. Sin costo y sin compromiso — si no podemos ayudarte, te lo decimos en esa misma llamada.",
        secondary=("Ver servicios", f"{BASE}/servicios"),
    ) + footer()

    write("metodo", html)


# ═══════════════════════════════════════════════════════════════
# SERVICIOS · índice
# ═══════════════════════════════════════════════════════════════

def build_servicios_index():
    rows = "".join(f"""
      <a class="post-row" href="{BASE}/servicios/{s['slug']}" style="text-decoration:none">
        <div class="post-meta">{s['letter']} · {s['tag']}</div>
        <div>
          <h3>{s['name']}</h3>
          <p>{s['lede']}</p>
        </div>
        <div class="post-go">Ver ↗</div>
      </a>""" for s in SERVICES)

    html = head(
        "Servicios · Sentido Branding &amp; Advertising",
        "Los siete módulos de Sentido: redes Meta, Google Ads, CRM y automatización, Google Business Profile, email marketing, branding y sitio web estratégico.",
        "/servicios",
    ) + nav("Servicios") + f"""
<main id="main">

  <section class="hero hero--page">
    <div class="wrap">
      <span class="eyebrow reveal">Servicios</span>
      <h1 class="reveal" data-d="1">Lo que componemos<br /><span class="italic">en cada capa.</span></h1>
      <p class="hero-sub reveal" data-d="2">
        Siete módulos. Cinco mensuales y dos de inversión única. No es un menú con precios cerrados:
        el alcance específico, el orden de activación y la inversión se definen en la propuesta,
        después del diagnóstico.
      </p>
    </div>
  </section>

  <section class="section section--line">
    <div class="wrap">
      <div class="post-list reveal">{rows}</div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="cols cols-2">
        <div class="card reveal">
          <span class="tag">Nota · Pauta publicitaria</span>
          <h4>El presupuesto de pauta va aparte.</h4>
          <p class="dim">
            Los módulos de redes Meta y Google Ads requieren presupuesto de pauta, pero ese
            presupuesto va directo a Meta y Google con el medio de pago del cliente. No es parte de
            los honorarios de Sentido. El monto se calibra al mercado, sector y ambición del negocio
            durante el diagnóstico.
          </p>
          <ul class="checks checks--dense" style="margin-top:6px">
            <li>Meta Ads · típico $5,000 – $15,000 MXN al mes</li>
            <li>Google Ads · típico $3,000 – $8,000 MXN al mes</li>
          </ul>
        </div>
        <div class="card reveal" data-d="1">
          <span class="tag">Nota · Cómo se combinan</span>
          <h4>Algunos activan todo. Otros arrancan con dos.</h4>
          <p class="dim">
            Algunos clientes activan los cinco módulos mensuales desde el día uno; otros arrancan con
            dos o tres y suman conforme el sistema demuestra tracción. El sitio web y el branding son
            inversiones únicas que se cotizan aparte y suelen ir antes del paquete mensual.
          </p>
          <div class="btn-row" style="margin-top:8px">
            <a class="btn btn--ghost" href="{BASE}/metodo">Ver orden de construcción <span class="arw">→</span></a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--surface">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">También disponible</span>
        <h2>Servicios que se contratan solos.</h2>
        <p class="lede">Piezas productizadas que resuelven un problema concreto sin comprometerse con el sistema completo.</p>
      </div>
      <div class="cols" style="grid-template-columns:repeat(2,1fr);gap:20px">
        <a class="card reveal" href="/sitios-web-ia">
          <div class="card-top"><span class="tag tag--fill">Desde $20,000 MXN</span><span class="card-arrow">↗</span></div>
          <h4>Sitios web producidos con IA</h4>
          <p class="dim">Estética de altísimo nivel, chatbot entrenado con la información del negocio, cotizador en tiempo real y formularios conectados a CRM. Entrega promedio de dos semanas.</p>
        </a>
        <a class="card reveal" data-d="1" href="/reactivacion-ghl-resenas">
          <div class="card-top"><span class="tag tag--fill">Operación mensual</span><span class="card-arrow">↗</span></div>
          <h4>Motor de Reactivación + Reseñas</h4>
          <p class="dim">Operamos tu GoHighLevel mes a mes: campañas de email y WhatsApp que reactivan a tu base dormida, más gestión continua del flujo de reseñas en Google.</p>
        </a>
      </div>
    </div>
  </section>

</main>
""" + cta_block(
        "¿Cuál necesitas primero?",
        "Casi nunca son todos, y casi nunca es el que se cree. En el diagnóstico mapeamos qué capa está frenando al resto y en qué orden conviene activar.",
    ) + footer()

    write("servicios", html)


# ═══════════════════════════════════════════════════════════════
# SERVICIOS · detalle
# ═══════════════════════════════════════════════════════════════

def build_servicio(s):
    includes = "".join(f"<li>{x}</li>" for x in s["includes"])
    kpis = "".join(f"<li>{x}</li>" for x in s["kpis"])
    related = "".join(f"""
      <a class="card reveal" data-d="{i}" href="{BASE}/servicios/{r}">
        <div class="card-top"><span class="tag">{SERV_BY_SLUG[r]['letter']} · {SERV_BY_SLUG[r]['tag']}</span><span class="card-arrow">↗</span></div>
        <h4>{SERV_BY_SLUG[r]['name']}</h4>
        <p class="dim">{SERV_BY_SLUG[r]['sub']}.</p>
      </a>""" for i, r in enumerate(s["related"]))

    html = head(
        f"{s['name']} · Sentido",
        s["lede"][:180],
        f"/servicios/{s['slug']}",
    ) + nav("Servicios") + f"""
<main id="main">

  <section class="hero hero--page">
    <div class="wrap">
      <p class="reveal" style="margin-bottom:22px">
        <a class="post-meta" href="{BASE}/servicios" style="color:var(--text-dim)">← Servicios</a>
      </p>
      <span class="eyebrow reveal">{s['letter']} · {s['tag']} · {s['tag2']}</span>
      <h1 class="reveal" data-d="1">{s['name']}</h1>
      <p class="hero-sub reveal" data-d="2">{s['lede']}</p>
      <div class="btn-row reveal" data-d="3">
        <a class="btn btn--solid" href="{BASE}/contacto">Cotizar este módulo <span class="arw">→</span></a>
      </div>
    </div>
  </section>

  <section class="section section--line">
    <div class="wrap">
      <div class="cols cols-sticky">
        <div class="sticky-rail reveal">
          <span class="kicker" style="margin-bottom:20px">01 — Por qué importa</span>
          <h2>{s['sub']}.</h2>
        </div>
        <div class="reveal" data-d="1">
          <p class="lede">{s['problem']}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="cols cols-sticky">
        <div class="sticky-rail reveal">
          <span class="kicker" style="margin-bottom:20px">02 — Qué incluye</span>
          <h2>El alcance del módulo.</h2>
        </div>
        <div class="reveal" data-d="1">
          <ul class="checks" style="gap:16px">{includes}</ul>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--surface">
    <div class="wrap">
      <div class="cols cols-2">
        <div class="reveal">
          <span class="kicker" style="margin-bottom:18px">03 — IA aplicada</span>
          <h3 style="margin-bottom:18px">Dónde entra la máquina.</h3>
          <p class="dim body-lg">{s['ia']}</p>
        </div>
        <div class="reveal" data-d="1">
          <span class="kicker" style="margin-bottom:18px">04 — Para quién es</span>
          <h3 style="margin-bottom:18px">Cuándo tiene sentido activarlo.</h3>
          <p class="dim body-lg">{s['for_whom']}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="cols cols-sticky">
        <div class="sticky-rail reveal">
          <span class="kicker" style="margin-bottom:20px">05 — Qué se mide</span>
          <h2>Los números del reporte mensual.</h2>
        </div>
        <div class="reveal" data-d="1">
          <ul class="checks" style="gap:16px;margin-bottom:32px">{kpis}</ul>
          <div class="card">
            <span class="tag">Nota</span>
            <p class="dim">{s['note']}</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--line">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">Siguiente</span>
        <h2>Módulos que se acoplan.</h2>
      </div>
      <div class="cols cols-2" style="gap:20px">{related}</div>
    </div>
  </section>

</main>
""" + cta_block(
        "Hablemos de tu caso.",
        "En el diagnóstico revisamos si este módulo es el que más mueve tu negocio hoy — o si conviene resolver otra capa primero. La respuesta honesta suele ahorrar meses.",
        primary=("Agendar diagnóstico", f"{BASE}/contacto"),
        secondary=("Ver todos los servicios", f"{BASE}/servicios"),
    ) + footer()

    write(f"servicios/{s['slug']}", html)


# ═══════════════════════════════════════════════════════════════
# CASOS
# ═══════════════════════════════════════════════════════════════

SECTORS = [
    ("Inmobiliario y constructoras",
     "Desarrolladores, constructoras y consultoría inmobiliaria",
     "Es el sector donde más profundo hemos operado el sistema completo: landing pages por desarrollo, campañas de captación segmentadas por perfil de comprador, CRM con pipeline de bróker y seguimiento automatizado desde el primer mensaje hasta el apartado.",
     ["Landings por desarrollo con cotizador", "Pipeline de bróker en CRM", "Meta + Google segmentado por zona", "Remarketing por etapa de decisión"]),
    ("Industrial y manufactura",
     "Materiales de construcción, procesos y proveeduría B2B",
     "Ciclos de venta largos, decisión técnica y necesidad de posicionarse como referente. Aquí el contenido pesa tanto como la pauta: blog técnico con SEO, Google Ads sobre intención de búsqueda especializada y GBP para la operación local.",
     ["Blog técnico con SEO gestionado", "Google Ads sobre intención especializada", "Sitio con catálogo y ficha técnica", "Captación de distribuidores"]),
    ("Automotriz premium",
     "Showrooms, seminuevos premium y marcas de alto valor",
     "Ticket alto, audiencia estrecha y una marca que no puede verse barata en ningún punto de contacto. El trabajo se concentra en producción de contenido de nivel, segmentación fina y un CRM que no deje enfriar a un prospecto de seis cifras.",
     ["Producción de contenido premium", "Segmentación de audiencia de alto valor", "CRM con respuesta inmediata", "Google Business Profile de showroom"]),
    ("Clubes, deporte y wellness",
     "Clubes deportivos, fitness, spa y membresías",
     "Negocios de membresía donde la base histórica vale más que la captación nueva. Reactivación de socios, renovaciones automatizadas, motor de reseñas y campañas de recompra sobre la base que ya existe.",
     ["Reactivación de socios por email y WhatsApp", "Motor de reseñas en Google", "Campañas de renovación automatizadas", "Captación local por Maps"]),
    ("Consumo, retail y hospitalidad",
     "Restaurantes, retail local, salud estética y servicios recurrentes",
     "Alta frecuencia de compra y dependencia total de la reputación local. El sistema se apoya en Google Business Profile, reseñas, contenido constante y flujos de recompra que traen de vuelta al cliente sin volver a pagar por adquirirlo.",
     ["Google Business Profile y reseñas", "Contenido y comunidad", "Flujos de recompra", "Promociones segmentadas por base"]),
    ("Servicios profesionales y B2B",
     "Consultoría, despachos y servicios especializados",
     "Donde la confianza precede a la venta. Branding sólido, sitio que sostenga el nivel de la propuesta, contenido que demuestre criterio y un CRM que ordene un pipeline de pocas oportunidades pero de alto valor.",
     ["Branding e identidad", "Sitio con arquitectura por audiencia", "Contenido de autoridad", "Pipeline B2B en CRM"]),
]

PROJECTS = [
    ("Murotech", "Industrial · Materiales de construcción", "Sitio, blog con SEO gestionado, redes, pauta Meta y Google, Google Business Profile y CRM."),
    ("G2B Constructora", "Inmobiliario · Constructora", "Sistema de captación y CRM para obra y proyecto."),
    ("JALIE-VALI Constructora", "Inmobiliario · Constructora", "Sitio web y sistema de captación de leads."),
    ("Providencia Padel Club", "Deporte · Club y membresías", "Captación de socios, contenido y reputación local."),
    ("Torobox", "Consumo · Retail y servicio", "Sitio, pauta y reportería mensual del sistema."),
    ("Brelia", "Inmobiliario · Desarrollo", "Landing de desarrollo y proyección de campaña."),
    ("Fragsa", "Industrial · Proveeduría", "Sitio web corporativo."),
    ("Bolongo", "Inmobiliario · Desarrollo", "Landing de unidad y captación."),
]


def build_casos():
    sectors = "".join(f"""
      <article class="layer reveal">
        <div class="layer-num">{i+1:02d}</div>
        <div class="layer-title"><h3>{name}</h3><div class="layer-tag">{sub}</div></div>
        <div class="layer-body">
          <p style="margin-bottom:18px">{body}</p>
          <ul class="checks checks--dense">{"".join(f"<li>{c}</li>" for c in caps)}</ul>
        </div>
      </article>""" for i, (name, sub, body, caps) in enumerate(SECTORS))

    # NOTA PARA JOSÉ: confirmar qué nombres de cliente pueden aparecer públicamente
    # antes de publicar. Si alguno no tiene autorización, borrar su entrada de PROJECTS.
    projects = "".join(f"""
      <div class="grid-cell reveal" data-d="{i % 4}">
        <span class="kicker" style="margin-bottom:12px">{sector}</span>
        <h4 style="margin-bottom:10px">{name}</h4>
        <p class="dim" style="font-size:.875rem;line-height:1.62">{work}</p>
      </div>""" for i, (name, sector, work) in enumerate(PROJECTS))

    html = head(
        "Casos y sectores · Sentido Branding &amp; Advertising",
        "Sectores donde Sentido opera el sistema completo: inmobiliario, industrial, automotriz premium, clubes y wellness, consumo y retail, servicios profesionales.",
        "/casos",
    ) + nav("Casos") + f"""
<main id="main">

  <section class="hero hero--page">
    <div class="wrap">
      <span class="eyebrow reveal">Casos y sectores</span>
      <h1 class="reveal" data-d="1">Dónde ya operamos<br /><span class="italic">el sistema completo.</span></h1>
      <p class="hero-sub reveal" data-d="2">
        El sistema es el mismo en todos lados; lo que cambia es qué capa pesa más. En inmobiliario
        manda la captura y el pipeline. En industrial, el contenido y la intención de búsqueda. En
        clubes, la retención. Esto es lo que hemos aprendido operando cada uno.
      </p>
    </div>
  </section>

  <section class="section section--line">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">01 — Sectores</span>
        <h2>Seis contextos, un mismo sistema.</h2>
      </div>
      {sectors}
    </div>
  </section>

  <section class="section section--surface">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">02 — Proyectos</span>
        <h2>Algunas marcas con las que trabajamos.</h2>
        <p class="lede">Una muestra de cuentas donde el sistema está operando o se construyó por completo.</p>
      </div>
      <!-- CONFIRMAR con el cliente qué nombres pueden mostrarse públicamente antes de publicar -->
      <div class="grid grid-4">{projects}</div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="cols cols-sticky">
        <div class="sticky-rail reveal">
          <span class="kicker" style="margin-bottom:20px">03 — Cómo leemos resultados</span>
          <h2>Sin capturas de pantalla fuera de contexto.</h2>
        </div>
        <div class="reveal" data-d="1">
          <p class="lede" style="margin-bottom:26px">
            No publicamos números de clientes sin su autorización, y desconfiamos de las agencias que
            sí lo hacen: un ROAS aislado, sin ticket promedio ni margen ni ciclo de venta, no dice
            nada sobre si ese negocio ganó dinero.
          </p>
          <p class="body-lg dim">
            Lo que sí hacemos es enseñar el método de medición en el diagnóstico: qué se instrumenta,
            qué se atribuye y cómo se ve un reporte mensual real. Si necesitas referencias directas,
            las conectamos con clientes que aceptaron darlas.
          </p>
          <div class="btn-row">
            <a class="btn btn--ghost" href="{BASE}/contacto">Pedir referencias <span class="arw">→</span></a>
          </div>
        </div>
      </div>
    </div>
  </section>

</main>
""" + cta_block(
        "¿Tu sector no está en la lista?",
        "El sistema no depende del giro: depende de que haya demanda, un ticket que justifique la inversión y una operación capaz de atender lo que llegue. Eso se valida en 45 minutos.",
        secondary=("Ver el método", f"{BASE}/metodo"),
    ) + footer()

    write("casos", html)


# ═══════════════════════════════════════════════════════════════
# BLOG
# ═══════════════════════════════════════════════════════════════

POSTS = [
    {
        "slug": "sistema-vs-servicios-sueltos",
        "date": "2026-07-22",
        "date_h": "22 jul 2026",
        "cat": "Estrategia",
        "read": "7 min",
        "title": "Por qué contratar servicios sueltos sale más caro que contratar un sistema",
        "excerpt": "Cinco proveedores que no se hablan producen menos que tres capas conectadas. El problema no es el presupuesto: es la arquitectura.",
        "body": """
<p class="lede">Casi todos los negocios que llegan a Sentido tienen lo mismo: un community manager, alguien que "les ve el Google Ads", un diseñador freelance que hizo el sitio hace tres años, y un WhatsApp donde los leads se acumulan hasta que alguien tiene tiempo. Cada pieza funciona. El conjunto, no.</p>

<p>La conversación siempre empieza igual: "invertimos bastante en marketing y no vemos resultados". Y casi nunca es un problema de presupuesto. Es un problema de arquitectura.</p>

<h2>El costo invisible de la desconexión</h2>

<p>Cuando cada pieza vive en su isla, el negocio paga tres costos que ninguna factura muestra.</p>

<p><strong>El primero es la contradicción estratégica.</strong> El community construye una narrativa de marca premium mientras la campaña de Google promociona descuentos. El sitio habla de un público y las campañas persiguen a otro. Nadie está haciendo mal su trabajo — simplemente nadie está viendo el conjunto.</p>

<p><strong>El segundo es la fuga entre capas.</strong> La pauta genera el lead, pero el lead cae en una bandeja que se revisa dos veces al día. Para cuando alguien responde, el prospecto ya cotizó con tres competidores. El dinero de la campaña se gastó completo; el resultado se perdió en el último metro.</p>

<p><strong>El tercero, y el más caro, es la ceguera.</strong> Sin atribución conectada, nadie sabe qué campaña trajo al cliente que sí compró. Entonces se optimiza hacia lo que se puede ver — clics, alcance, formularios — en vez de hacia lo que importa. Y el algoritmo aprende exactamente lo que le enseñaste.</p>

<blockquote>Si le enseñas a la máquina a conseguir formularios, te va a traer formularios. Enseñarle a conseguir clientes requiere devolverle las ventas.</blockquote>

<h2>Qué cambia cuando las capas se conectan</h2>

<p>Un sistema no es más servicios. Frecuentemente es menos servicios, mejor ordenados. Estas son las conexiones que hacen la diferencia:</p>

<ul>
  <li><strong>El CRM le devuelve conversiones a la pauta.</strong> Meta Advantage+ y Performance Max no optimizan hacia formularios llenados, sino hacia leads que efectivamente se convirtieron en cliente. Es la misma inversión rindiendo distinto.</li>
  <li><strong>El sitio conoce el origen del visitante.</strong> Quien llega desde una campaña de search con intención alta no debería ver el mismo mensaje que quien llega desde un reel de descubrimiento.</li>
  <li><strong>Las reseñas alimentan el contenido y el posicionamiento local.</strong> Lo que los clientes dicen en Google es la mejor fuente de mensajes para la siguiente campaña — y la señal que más pesa en el ranking de Maps.</li>
  <li><strong>La base de datos vuelve a la pauta como audiencia.</strong> Los clientes que ya compraron son el mejor insumo para audiencias similares, y el público más barato de reactivar.</li>
</ul>

<h2>El orden importa más que la velocidad</h2>

<p>La causa número uno de presupuesto desperdiciado no es elegir el canal equivocado: es construir en desorden. Prender pauta hacia un sitio que no convierte. Meter volumen a un negocio sin pipeline. Invertir en contenido para una marca que todavía no sabe qué está diciendo.</p>

<p>El orden que recomendamos es simple y casi siempre el mismo: <strong>branding → sitio → CRM → pauta</strong>. No porque sea elegante, sino porque cada capa se apoya en la anterior. Saltarse una no acelera el proceso; solo mueve el costo más adelante, cuando ya es más caro corregirlo.</p>

<hr />

<p class="dim">Si estás en la etapa de decidir por dónde empezar, el diagnóstico de 45 minutos existe justo para eso: mapear qué capa está frenando a las demás y en qué orden conviene activar. Sin costo, y con una lectura honesta de si podemos ayudarte.</p>
""",
    },
    {
        "slug": "sitios-web-con-ia",
        "date": "2026-07-15",
        "date_h": "15 jul 2026",
        "cat": "Sitios web",
        "read": "6 min",
        "title": "Sitios web con IA: qué cambió de verdad y qué sigue siendo trabajo humano",
        "excerpt": "El precio y el tiempo se desplomaron. El criterio no. Qué esperar realmente de un sitio producido con un workflow potenciado por IA.",
        "body": """
<p class="lede">Producir un sitio web con un workflow potenciado por IA cambió las reglas de forma concreta: entregamos en semanas en vez de meses, con una estética que antes solo alcanzaban los proyectos grandes, e integramos funcionalidades que hasta hace poco eran carísimas de desarrollar. Vale la pena ser precisos sobre qué cambió y qué no.</p>

<h2>Lo que cambió: la velocidad de ejecución</h2>

<p>El modelo tradicional tenía una estructura de costos rígida. Meses de desarrollo entre diseño, código y revisiones. Un chatbot o un cotizador se cotizaban como proyectos aparte. Y para que el sitio se viera bien hacía falta una sesión de foto y video que muchas veces costaba más que el sitio.</p>

<p>Lo que la IA colapsó es el tiempo de iteración. Probar cinco direcciones de diseño ya no cuesta cinco semanas. Generar el contenido visual del proyecto no requiere agendar una producción. Montar integraciones que antes eran custom hoy es cuestión de días.</p>

<p>El resultado práctico: un sitio con estética premium, chatbot, cotizador y conexión a CRM, entregado en aproximadamente dos semanas, desde $20,000 MXN. No es el mismo producto más barato — es un producto que antes no existía en ese rango.</p>

<h2>Lo que no cambió: qué diseñar y qué dejar fuera</h2>

<p>La herramienta está disponible para cualquiera. La diferencia no está en tenerla, está en saber dirigirla.</p>

<blockquote>La IA acelera la ejecución. La dirección sigue siendo una decisión humana.</blockquote>

<p>Un sitio generado sin criterio produce exactamente lo que se le pidió: secciones genéricas, un hero bonito sin propuesta de valor, y ningún camino claro hacia la conversión. Las decisiones que siguen siendo trabajo humano son las que definen si el sitio funciona:</p>

<ul>
  <li><strong>Arquitectura por audiencia.</strong> Quién llega, desde dónde, con qué intención, y qué necesita ver primero cada perfil.</li>
  <li><strong>Qué funcionalidad merece existir.</strong> Un cotizador es potente cuando el producto es configurable y el precio es un obstáculo real de la decisión. En otros casos es fricción disfrazada de sofisticación.</li>
  <li><strong>Qué se mide y cómo se conecta.</strong> Pixel, Conversions API, GA4 y CRM tienen que estar instrumentados antes del lanzamiento, no después del primer mes sin datos.</li>
  <li><strong>Qué se deja fuera.</strong> Casi siempre es la decisión más valiosa, y la que ninguna herramienta va a tomar por ti.</li>
</ul>

<h2>Las funcionalidades que ahora sí son viables</h2>

<p><strong>Chatbot entrenado con información real.</strong> No un árbol de respuestas prearmadas: un asistente que entiende lenguaje natural y responde con el catálogo, los precios, las preguntas típicas y las políticas del negocio. Atiende a las dos de la mañana y cada conversación puede terminar en un lead.</p>

<p><strong>Cotizador en tiempo real.</strong> Es el diferenciador más fuerte. El visitante elige opciones, ajusta cantidades y ve su número al instante — y en el momento en que lo obtiene, ese resultado se convierte en una solicitud enviada por formulario, con todo el contexto de lo que cotizó. Llega un prospecto que ya sabe qué quiere y cuánto cuesta.</p>

<p><strong>Formularios que trabajan.</strong> Cada envío dispara notificación inmediata y entra al CRM. El seguimiento deja de depender de que alguien se acuerde y pasa a ser un proceso.</p>

<h2>Cómo evaluar una propuesta de sitio con IA</h2>

<p>Si estás cotizando, tres preguntas separan una propuesta seria de una plantilla reciclada: ¿qué se va a medir y cómo se conecta al CRM? ¿Qué pasa con el sitio a los seis meses, quién lo actualiza y con qué CMS? ¿La arquitectura responde a audiencias específicas o es la misma estructura de siempre con otro color?</p>

<hr />

<p class="dim">Si quieres ver el detalle del producto — qué incluye, tiempos y cómo se cotiza — está desglosado en la <a class="link" href="/sitios-web-ia">página de Sitios web con IA</a>.</p>
""",
    },
    {
        "slug": "reactivacion-base-de-datos",
        "date": "2026-07-08",
        "date_h": "8 jul 2026",
        "cat": "Retención",
        "read": "6 min",
        "title": "El activo más caro de ignorar ya lo tienes: tu base de datos",
        "excerpt": "Adquirir un cliente nuevo cuesta entre cinco y siete veces más que reactivar a uno que ya compró. Casi nadie trabaja la segunda opción.",
        "body": """
<p class="lede">Todo negocio con años de operación acumula lo mismo: una lista de clientes, socios y prospectos que compraron, reservaron o preguntaron alguna vez — y que hoy están dormidos. Nadie les vuelve a escribir de forma consistente. Esa base es, casi siempre, el activo más subutilizado del negocio.</p>

<h2>La aritmética que casi nadie corre</h2>

<p>El principio operativo es conocido y rara vez se actúa sobre él: adquirir un cliente nuevo cuesta entre cinco y siete veces más que reactivar a uno que ya te compró alguna vez. La brecha entre ambos costos es donde se pierde — o se gana — el margen del negocio.</p>

<p>A eso se suman dos hechos del comportamiento actual: alrededor del 88% de los usuarios consulta las reseñas de Google antes de elegir un negocio local, y las tasas de apertura de WhatsApp superan el 90%, muy por encima del email por sí solo. Son dos canales con acceso directo a gente que ya te conoce, y ambos suelen estar desatendidos.</p>

<blockquote>La producción de leads nuevos cuesta. Reactivar a quien ya te conoce, no tanto.</blockquote>

<h2>Por qué no se hace</h2>

<p>No es por falta de intención. Es porque el seguimiento manual no escala. Los mensajes uno por uno dependen de quién esté de turno, consumen tiempo y se pierden. Lo que no está sistematizado, no ocurre — por más que esté en la lista de pendientes de todos los lunes.</p>

<p>El segundo obstáculo es el estado de la base. Está repartida entre una hoja de cálculo, el punto de venta, el sistema de reservas y el WhatsApp de tres personas distintas. Con duplicados, teléfonos mal capturados y correos que rebotan. Ordenarla parece un proyecto y se pospone indefinidamente.</p>

<h2>Cómo se ve el recorrido completo</h2>

<ol>
  <li><strong>Carga.</strong> Se importan los contactos desde Excel, punto de venta, WhatsApp o el sistema de reservas.</li>
  <li><strong>Limpieza.</strong> Se eliminan duplicados, se corrigen datos y se validan correos y teléfonos. Sin este paso, la entregabilidad se cae y quemas el dominio.</li>
  <li><strong>Segmentación.</strong> Se agrupa por comportamiento, antigüedad y tipo de cliente. Un socio que se dio de baja hace dos meses no debe recibir el mismo mensaje que uno inactivo desde 2023.</li>
  <li><strong>Envíos multicanal.</strong> Campañas de email y WhatsApp que reactivan a cada segmento en el momento justo, con el mensaje que corresponde a su relación con la marca.</li>
  <li><strong>Métricas en vivo.</strong> Open rate, respuestas, reactivaciones y reseñas nuevas, medidas conforme ocurren.</li>
  <li><strong>Reporte y ajuste.</strong> Cada mes, qué se envió, qué abrió la gente, cuántos volvieron a comprar y qué se ajusta el mes siguiente.</li>
</ol>

<h2>El componente de reseñas</h2>

<p>La reactivación y la reputación se trabajan juntas por una razón simple: el mejor momento para pedir una reseña es justo después de una experiencia positiva, y ese momento lo conoce el CRM. Un flujo bien montado detecta el cierre, pide la reseña automáticamente, y filtra la insatisfacción hacia un formulario privado donde el negocio puede resolverla antes de que se vuelva pública.</p>

<p>Cada estrella adicional en Google se traduce en más ventas orgánicas, sin gastar un peso en pauta. Es la parte del sistema con mejor retorno y la que más se descuida.</p>

<h2>Para quién funciona mejor</h2>

<p>El patrón es consistente: negocios con base histórica acumulada, ubicación física con reservas o afluencia recurrente, presencia relevante en Google Maps, y sin equipo interno de CRM ni automatización. Clubes deportivos y fitness con socios históricos. Clínicas de estética, dental y veterinaria con pacientes recurrentes. Restaurantes, spas, salones y retail local con clientela repetida.</p>

<hr />

<p class="dim">Si esto describe tu negocio, el <a class="link" href="/reactivacion-ghl-resenas">Motor de Reactivación + Reseñas</a> es el servicio que lo opera mes a mes. No entregamos el sistema y deseamos suerte: lo operamos contigo.</p>
""",
    },
]


def build_blog_index():
    rows = "".join(f"""
      <a class="post-row" href="{BASE}/blog/{p['slug']}">
        <div class="post-meta"><time datetime="{p['date']}">{p['date_h']}</time><br />{p['cat']}</div>
        <div>
          <h3>{p['title']}</h3>
          <p>{p['excerpt']}</p>
        </div>
        <div class="post-go">{p['read']} ↗</div>
      </a>""" for p in POSTS)

    html = head(
        "Blog · Sentido Branding &amp; Advertising",
        "Notas sobre estrategia digital, pauta, sitios web con IA, CRM y retención — desde la operación real de una agencia, no desde la teoría.",
        "/blog",
    ) + nav("Blog") + f"""
<main id="main">

  <section class="hero hero--page">
    <div class="wrap">
      <span class="eyebrow reveal">Blog</span>
      <h1 class="reveal" data-d="1">Notas desde<br /><span class="italic">la operación.</span></h1>
      <p class="hero-sub reveal" data-d="2">
        Lo que vemos trabajando cuentas reales: qué funciona, qué se rompe y qué cuesta más caro de
        lo que parece. Sin fórmulas mágicas y sin capturas de pantalla fuera de contexto.
      </p>
    </div>
  </section>

  <section class="section section--line">
    <div class="wrap">
      <div class="post-list reveal">{rows}</div>
    </div>
  </section>

</main>
""" + cta_block(
        "¿Algo de esto describe tu situación?",
        "El diagnóstico de 45 minutos es gratis y sirve para aterrizar cualquiera de estos temas a tu negocio concreto: qué capa está frenando al resto y en qué orden conviene moverse.",
        secondary=("Ver el método", f"{BASE}/metodo"),
    ) + footer()

    write("blog", html)


def build_post(p, idx):
    others = [q for q in POSTS if q["slug"] != p["slug"]][:2]
    more = "".join(f"""
      <a class="card reveal" data-d="{i}" href="{BASE}/blog/{q['slug']}">
        <div class="card-top"><span class="tag">{q['cat']}</span><span class="card-arrow">↗</span></div>
        <h4>{q['title']}</h4>
        <p class="dim">{q['excerpt']}</p>
      </a>""" for i, q in enumerate(others))

    ld = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BlogPosting","headline":{p['title']!r},"datePublished":"{p['date']}","author":{{"@type":"Organization","name":"Sentido Branding & Advertising"}},"publisher":{{"@type":"Organization","name":"Sentido Branding & Advertising"}},"inLanguage":"es-MX","mainEntityOfPage":"https://sentido.mx/blog/{p['slug']}"}}
</script>
""".replace("'", '"')

    html = head(
        f"{p['title']} · Sentido",
        p["excerpt"],
        f"/blog/{p['slug']}",
        extra=ld,
    ) + nav("Blog") + f"""
<main id="main">

  <section class="hero hero--page" style="padding-bottom:clamp(32px,4vw,48px)">
    <div class="wrap-narrow" style="max-width:760px">
      <p class="reveal" style="margin-bottom:22px">
        <a class="post-meta" href="{BASE}/blog" style="color:var(--text-dim)">← Blog</a>
      </p>
      <span class="eyebrow reveal">{p['cat']} · {p['read']} de lectura</span>
      <h1 class="reveal" data-d="1" style="font-size:clamp(2.125rem,5.2vw,3.75rem);margin-top:24px">{p['title']}</h1>
      <p class="post-meta reveal" data-d="2" style="margin-top:26px">
        <time datetime="{p['date']}">{p['date_h']}</time> · Sentido Branding &amp; Advertising
      </p>
    </div>
  </section>

  <article class="section" style="padding-top:0">
    <div class="article reveal">{p['body']}</div>
  </article>

  <section class="section section--line">
    <div class="wrap">
      <div class="sec-head reveal">
        <span class="kicker">Seguir leyendo</span>
        <h2>Más notas.</h2>
      </div>
      <div class="cols cols-2" style="gap:20px">{more}</div>
    </div>
  </section>

</main>
""" + cta_block(
        "Hablemos de tu caso.",
        "45 minutos, sin costo, para mapear el estado actual de tu sistema y dónde está la brecha más cara de no resolver.",
    ) + footer()

    write(f"blog/{p['slug']}", html)


# ═══════════════════════════════════════════════════════════════
# CONTACTO
# ═══════════════════════════════════════════════════════════════

def build_contacto():
    interests = [
        ("pauta", "Pauta (Meta / Google)"),
        ("redes", "Redes y contenido"),
        ("sitio", "Sitio web"),
        ("branding", "Branding / Identidad"),
        ("crm", "CRM y automatización"),
        ("email", "Email marketing"),
        ("reactivacion", "Reactivación y reseñas"),
        ("paquete", "Paquete integral completo"),
        ("no-se", "Aún no estoy seguro"),
    ]
    checks = "".join(
        f'<label class="check"><input type="checkbox" name="interes" value="{v}" /> {t}</label>'
        for v, t in interests
    )

    html = head(
        "Contacto · Sentido Branding &amp; Advertising",
        "Agenda un diagnóstico estratégico sin costo con Sentido. 45 minutos para mapear tu sistema de marketing y encontrar la brecha más cara de no resolver.",
        "/contacto",
    ) + nav() + f"""
<main id="main">

  <section class="hero hero--page">
    <div class="wrap">
      <span class="eyebrow reveal">Hablemos</span>
      <h1 class="reveal" data-d="1">Cuéntanos qué<br /><span class="italic">estás resolviendo.</span></h1>
      <p class="hero-sub reveal" data-d="2">
        El formulario tarda menos de un minuto. Un estratega de Sentido te responde en menos de 24
        horas hábiles para agendar el diagnóstico — 45 minutos, sin costo y sin compromiso.
      </p>
    </div>
  </section>

  <section class="section section--line" style="padding-top:clamp(48px,6vw,72px)">
    <div class="wrap">
      <div class="cols cols-sticky">

        <div class="sticky-rail reveal">
          <span class="kicker" style="margin-bottom:20px">Qué pasa después</span>
          <div class="steps" style="border-top:none">""" + "".join(f"""
            <div class="step" style="padding-left:0;padding-right:0">
              <div class="step-n">{n}</div>
              <div><h4 style="font-size:1.0625rem">{t}</h4><p class="dim" style="font-size:.875rem">{b}</p><span class="kicker">{meta}</span></div>
            </div>""" for n, t, meta, b in ONBOARDING) + f"""
          </div>
          <div style="margin-top:32px">
            <span class="kicker" style="margin-bottom:14px">Directo</span>
            <ul class="checks checks--dense">
              <li><a class="link" href="mailto:{MAIL}">{MAIL}</a></li>
              <li><a class="link" href="{WA}" rel="noopener">WhatsApp</a></li>
            </ul>
          </div>
        </div>

        <div class="reveal" data-d="1">
          <div class="form-shell">
            <form id="lead-form" data-webhook="/api/lead" data-fuente="sentido.mx" novalidate>
              <div class="form-grid">

                <div class="field">
                  <label class="label" for="f-nombre">Nombre completo <span class="req">*</span></label>
                  <input class="input" id="f-nombre" name="nombre" type="text" autocomplete="name" required />
                </div>

                <div class="field">
                  <label class="label" for="f-empresa">Empresa o marca <span class="req">*</span></label>
                  <input class="input" id="f-empresa" name="empresa" type="text" autocomplete="organization" required />
                </div>

                <div class="field">
                  <label class="label" for="f-email">Correo electrónico <span class="req">*</span></label>
                  <input class="input" id="f-email" name="email" type="email" autocomplete="email" required />
                </div>

                <div class="field">
                  <label class="label" for="f-whatsapp">WhatsApp <span class="req">*</span></label>
                  <input class="input" id="f-whatsapp" name="whatsapp" type="tel" autocomplete="tel" placeholder="+52 ..." required />
                </div>

                <div class="field full">
                  <label class="label" for="f-sitio">Sitio web o Instagram actual</label>
                  <input class="input" id="f-sitio" name="sitio" type="text" placeholder="sitio.com · @instagram" />
                </div>

                <div class="field full">
                  <span class="label">¿En qué necesitas apoyo? <span class="req">*</span></span>
                  <div class="check-grid">{checks}</div>
                </div>

                <div class="field">
                  <label class="label" for="f-presupuesto">Presupuesto mensual aproximado</label>
                  <select class="select" id="f-presupuesto" name="presupuesto">
                    <option value="">Selecciona un rango</option>
                    <option value="menos-10k">Menos de $10,000 MXN</option>
                    <option value="10-20k">$10,000 – $20,000 MXN</option>
                    <option value="20-40k">$20,000 – $40,000 MXN</option>
                    <option value="40k-mas">Más de $40,000 MXN</option>
                    <option value="por-definir">Por definir / depende del alcance</option>
                  </select>
                </div>

                <div class="field">
                  <label class="label" for="f-tiempo">¿Cuándo te gustaría arrancar?</label>
                  <select class="select" id="f-tiempo" name="tiempo">
                    <option value="">Selecciona un horizonte</option>
                    <option value="asap">Lo antes posible</option>
                    <option value="1-3-meses">En 1 a 3 meses</option>
                    <option value="3-6-meses">En 3 a 6 meses</option>
                    <option value="explorando">Solo estoy explorando</option>
                  </select>
                </div>

                <div class="field full">
                  <label class="label" for="f-contexto">Algo de contexto (opcional)</label>
                  <textarea class="textarea" id="f-contexto" name="contexto" placeholder="Qué estás intentando resolver, qué ya intentaste, qué te frena hoy."></textarea>
                </div>

                <div class="form-status" id="lead-status" role="status" aria-live="polite"></div>
              </div>

              <div class="form-foot">
                <span class="form-note">Respuesta en menos de 24 h hábiles · {MAIL}</span>
                <button class="btn btn--solid" type="submit" data-submit>Enviar <span class="arw">→</span></button>
              </div>
            </form>
          </div>
        </div>

      </div>
    </div>
  </section>

</main>
""" + footer()

    write("contacto", html)


# ═══════════════════════════════════════════════════════════════

def build_sitemap():
    urls = ["/", "/metodo", "/servicios", "/casos", "/blog", "/contacto"]
    urls += [f"/servicios/{s['slug']}" for s in SERVICES]
    urls += [f"/blog/{p['slug']}" for p in POSTS]
    body = "".join(f"  <url><loc>https://sentido.mx{u}</loc></url>\n" for u in urls)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + '</urlset>\n')
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")
    print("  ✓ sitio/sitemap.xml")


if __name__ == "__main__":
    print("Generando sitio…")
    build_home()
    build_metodo()
    build_servicios_index()
    for s in SERVICES:
        build_servicio(s)
    build_casos()
    build_blog_index()
    for i, p in enumerate(POSTS):
        build_post(p, i)
    build_contacto()
    build_sitemap()
    print("Listo.")
