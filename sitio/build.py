#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el sitio de sentido.mx bajo /sitio.

Mundo visual: grabado de buril derivado del isotipo de la marca.
Todo el texto vive aquí — los index.html se regeneran y se pierden los cambios
hechos a mano. Ver sitio/README.md.
"""

import pathlib

ROOT = pathlib.Path("/home/user/Sentido/sitio")
BASE = "/sitio"          # → "" si el sitio pasa a la raíz de un dominio propio
ASSETS = f"{BASE}/assets"
OJO = "/assets/isotipo-sentido.png"          # marca sola, para el favicon
LOGO = "/assets/logo-sentido-light-h.png"   # lockup horizontal, derivado del logo original
WA = "https://wa.me/5213222253390"
MAIL = "jos@sentido.mx"

NAV = [
    ("Método",    f"{BASE}/metodo"),
    ("Servicios", f"{BASE}/servicios"),
    ("Casos",     f"{BASE}/casos"),
    ("Blog",      f"{BASE}/blog"),
]

PRELOAD = ["archivo-latin.woff2"]

CONTRATO = """<!--
  DIRECCIÓN · Sentido — sentido.mx
  TESIS: cuatro capas operadas desde una sola cabeza. Rechaza la página de
  agencia que apila tarjetas de servicio con eyebrow y flecha.
  MUNDO-PROPIO: grabado de buril derivado del isotipo (ojo en rombo). Campos de
  línea como material y el rombo como módulo; tinta cálida #0B0A09 sobre hueso
  #F1EADC. Una familia (Archivo): contraste ligera/negra y caja hueso como
  marcador, tomados del feed real de la marca. Sin serif, sin monoespaciada,
  sin tarjetas, sin iconos, sin imágenes.
  HISTORIA: quien ya oyó el nombre llega a corroborar, encuentra criterio y
  agenda el diagnóstico.
  PRIMER VIEWPORT: titular a la izquierda en ligera+negra con una palabra en
  caja hueso; a la derecha el ojo en sus rombos con la trama grabándose;
  debajo la franja de las cuatro capas.
  FORMA: grabado; dirección fijada por la marca sobre la tirada; seed 1a292619.
-->
"""


def head(title, desc, canonical, extra=""):
    pre = "".join(
        f'<link rel="preload" href="{ASSETS}/fonts/{f}" as="font" type="font/woff2" crossorigin />\n'
        for f in PRELOAD)
    return CONTRATO + f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="theme-color" content="#0B0A09" />
<!-- Preview bajo propuestas.sentido.mx: no debe indexarse ni competir con sentido.mx.
     Quitar esta línea cuando el sitio se publique en su dominio definitivo. -->
<meta name="robots" content="noindex, nofollow" />
<link rel="canonical" href="https://sentido.mx{canonical}" />
<meta property="og:type" content="website" />
<meta property="og:site_name" content="Sentido · Branding &amp; Advertising" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:locale" content="es_MX" />
<meta name="twitter:card" content="summary_large_image" />
<link rel="icon" href="{OJO}" />
{pre}<link rel="stylesheet" href="{ASSETS}/fonts.css" />
<link rel="stylesheet" href="{ASSETS}/sentido.css" />
{extra}</head>
<body>
<a class="salta" href="#main">Saltar al contenido</a>
"""


def nav(activa=None):
    links = "".join(
        '<a class="nav-a" href="%s"%s>%s</a>' % (h, ' aria-current="page"' if l == activa else "", l)
        for l, h in NAV)
    panel = "".join('<a href="%s">%s<span class="rombo"></span></a>' % (h, l) for l, h in NAV)
    return f"""<header class="nav">
  <div class="nav-int">
    <a class="marca" href="{BASE}/" aria-label="Sentido — inicio">
      <img src="{LOGO}" alt="Sentido · Branding &amp; Advertising" />
    </a>
    <nav class="nav-links" aria-label="Principal">{links}</nav>
    <a class="boton boton--linea nav-cta" href="{BASE}/contacto">Hablemos</a>
    <button class="nav-btn" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="panel">
      <span></span><span></span>
    </button>
  </div>
</header>
<div class="panel" id="panel">{panel}<a href="{BASE}/contacto">Hablemos<span class="rombo rombo--lleno"></span></a></div>
"""


def cierre(titulo, texto, sec=None):
    b = f'<a class="enlace" href="{sec[1]}">{sec[0]}</a>' if sec else ""
    return f"""<section class="seccion">
  <div class="wrap">
    <div class="cierre">
      <div class="buril"></div>
      <h2>{titulo}</h2>
      <p>{texto}</p>
      <div class="acciones">
        <a class="boton" href="{BASE}/contacto">Agendar diagnóstico <span class="fl">→</span></a>
        {b}
      </div>
    </div>
  </div>
</section>
"""


def pie():
    servs = "".join(f'<li><a href="{BASE}/servicios/{x["slug"]}">{x["short"]}</a></li>' for x in SERVICES)
    return f"""<footer class="pie">
  <div class="buril"></div>
  <div class="wrap">
    <div class="pie-alto">
      <div class="pie-marca">
        <img src="{LOGO}" alt="Sentido · Branding &amp; Advertising" />
        <p>Marca, pauta, tecnología y datos en un mismo sistema — para que cada peso invertido en marketing produzca leads, ventas y clientes que regresan.</p>
      </div>
      <div class="pie-col">
        <span class="rotulo">Servicios</span>
        <ul>{servs}</ul>
      </div>
      <div class="pie-col">
        <span class="rotulo">Agencia</span>
        <ul>
          <li><a href="{BASE}/metodo">Método</a></li>
          <li><a href="{BASE}/servicios">Todos los servicios</a></li>
          <li><a href="{BASE}/casos">Casos y sectores</a></li>
          <li><a href="{BASE}/blog">Blog</a></li>
          <li><a href="{BASE}/contacto">Contacto</a></li>
        </ul>
      </div>
      <div class="pie-col">
        <span class="rotulo">Contacto</span>
        <ul>
          <li><a href="mailto:{MAIL}">{MAIL}</a></li>
          <li><a href="{WA}" rel="noopener">WhatsApp</a></li>
          <li><a href="https://propuestas.sentido.mx" rel="noopener">Propuestas</a></li>
        </ul>
      </div>
    </div>
    <div class="pie-bajo">
      <p>© <span data-anio>2026</span> Sentido</p>
      <p class="firma">branding / advertising · desde 2010</p>
    </div>
  </div>
</footer>
<script src="{ASSETS}/sentido.js" defer></script>
</body>
</html>
"""


def escribe(ruta, html):
    d = ROOT / ruta if ruta else ROOT
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(html, encoding="utf-8")
    print("  ✓", (d / "index.html").relative_to(ROOT.parent))


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
        "note": "El presupuesto de pauta va aparte y se paga directo a Meta con el medio de pago del cliente: no es honorario de Sentido. El monto se calibra al mercado, sector y ambición del negocio durante el diagnóstico.",
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
        "note": "El presupuesto de pauta va aparte y se paga directo a Google con el medio de pago del cliente: no es honorario de Sentido. El monto se calibra al mercado, sector y ambición del negocio durante el diagnóstico.",
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
        "tag2": "Entrega en 4 semanas o menos",
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
        "note": "Inversión única. El alcance específico y la inversión se cierran en la propuesta, después del diagnóstico.",
        "related": ["branding", "google-ads"],
    },
]

SERV_BY_SLUG = {x["slug"]: x for x in SERVICES}

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

SECTORS = [
    ("Inmobiliario y constructoras",
     "Desarrolladores, constructoras y consultoría inmobiliaria",
     "Es un sector donde hemos operado el sistema completo: landing pages por desarrollo, campañas de captación segmentadas por perfil de comprador, CRM con pipeline de bróker y seguimiento automatizado desde el primer mensaje hasta el apartado.",
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

<p>El resultado práctico: un sitio con estética premium, chatbot, cotizador y conexión a CRM, entregado en semanas y no en meses. No es el mismo producto más barato: es un producto que antes no existía a ese alcance.</p>

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

<p class="apagado">Si quieres ver el detalle del producto, qué incluye y cómo se cotiza, está desglosado en la <a class="enlace-txt" href="/sitios-web-ia">página de Sitios web con IA</a>.</p>
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

<p>El principio es conocido en la industria y rara vez se actúa sobre él: se estima que adquirir un cliente nuevo cuesta entre cinco y siete veces más que reactivar a uno que ya compró. La brecha entre ambos costos es donde se pierde — o se gana — el margen del negocio.</p>

<p>A eso se suman dos referencias de industria ampliamente citadas: cerca del 88% de los usuarios consulta reseñas de Google antes de elegir un negocio local, y las tasas de apertura de WhatsApp se reportan por encima del 90%, muy por arriba del email por sí solo. Son cifras del sector, no mediciones de Sentido. Son dos canales con acceso directo a gente que ya te conoce, y ambos suelen estar desatendidos.</p>

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

# ═══════════════════════════════════════════════════════════════
# PIEZAS COMPARTIDAS
# ═══════════════════════════════════════════════════════════════

def ojo(clase=""):
    """El isotipo en sus rombos, con la trama grabándose."""
    return f"""<div class="ojo-caja {clase}">
        <div class="ojo-rombo r3"></div>
        <div class="ojo-rombo r2"></div>
        <div class="ojo-rombo r1"></div>
        <div class="ojo-trama"><div class="buril"></div></div>
        <div class="ojo-img" role="img" aria-label="Sentido"></div>
      </div>"""


def franja_capas():
    return '<div class="capas">' + "".join(f"""
      <article class="capa" style="--i:{i}">
        <div class="buril"></div>
        <span class="rombo"></span>
        <div class="capa-n">Capa {n}</div>
        <h3>{t}</h3>
        <p>{tag}</p>
      </article>""" for i, (n, t, tag, _) in enumerate(LAYERS)) + '</div>'


def cabeza(titulo, entrada=""):
    e = f'<p>{entrada}</p>' if entrada else ""
    return f'<div class="cabeza"><div class="pleca"></div><h2>{titulo}</h2>{e}</div>'


# ═══════════════════════════════════════════════════════════════
# PORTADA
# ═══════════════════════════════════════════════════════════════

def build_home():
    capas_largas = "".join(f"""
      <div class="renglon">
        <div class="buril"></div>
        <div><span class="marco">Capa {n}</span><h3>{t}</h3></div>
        <div><p>{cuerpo}</p></div>
        <div class="ver">{tag.split(' · ')[0]}</div>
      </div>""" for n, t, tag, cuerpo in LAYERS)

    servicios = "".join(f"""
      <a class="renglon" href="{BASE}/servicios/{x['slug']}">
        <div class="buril"></div>
        <div><span class="marco">{x['tag']}</span><h3>{x['name']}</h3></div>
        <div><p>{x['lede']}</p></div>
        <div class="ver">Ver</div>
      </a>""" for x in SERVICES)

    ia = [
        ("Optimización de pauta", "Meta Advantage+, Performance Max y Demand Gen reciben las conversiones reales del CRM y refinan audiencias, pujas y creativos sin intervención manual."),
        ("Contenido a escala", "IA para imagen, video y copy genera variantes para A/B testing sin depender de producción continua. El branding define el marco; la IA acelera dentro de él."),
        ("Conversación automatizada", "LLMs integrados al CRM responden el primer mensaje en menos de 60 segundos, en el tono de la marca, califican intención y agendan."),
        ("Decisiones con datos", "Dashboards que combinan pauta, sitio, CRM y reseñas dan una sola vista. La junta mensual deja de ser sobre qué se hizo y pasa a ser sobre qué se ajusta."),
    ]
    ia_html = "".join(f"""
      <div class="renglon">
        <div class="buril"></div>
        <div><h3>{t}</h3></div>
        <div><p>{b}</p></div>
        <div class="ver"></div>
      </div>""" for t, b in ia)

    productos = "".join(f"""
      <a class="renglon" href="{href}">
        <div class="buril"></div>
        <div><span class="marco">{marco}</span><h3>{t}</h3></div>
        <div><p>{b}</p></div>
        <div class="ver">Ver</div>
      </a>""" for marco, t, b, href in [
        ("Producto", "Sitios web producidos con IA",
         "Estética de altísimo nivel, chatbot entrenado con la información real del negocio, cotizador en tiempo real y formularios conectados a CRM. Entregado en semanas, no en meses.",
         "/sitios-web-ia"),
        ("Operación mensual", "Motor de Reactivación + Reseñas",
         "Operamos tu GoHighLevel mes a mes: campañas de email y WhatsApp que reactivan a los clientes que ya tienes, más gestión continua del flujo de reseñas en Google.",
         "/reactivacion-ghl-resenas"),
        ("Documento", "Brochure interactivo",
         "El recorrido completo del sistema: método, proceso, los siete módulos y la capa de IA, en un documento navegable.",
         "/brochure"),
    ])

    pasos = "".join(f"""
      <div class="paso">
        <div class="paso-n">{n}</div>
        <div><h4>{t}</h4><p>{b}</p><span class="rotulo">{meta}</span></div>
      </div>""" for n, t, meta, b in ONBOARDING)

    html = head(
        "Sentido · Branding &amp; Advertising — El sistema que vuelve el marketing en negocio",
        "Agencia que conecta marca, pauta, tecnología y datos en un mismo sistema. Branding, Meta y Google Ads, sitios web con IA, CRM y automatización.",
        "/",
    ) + nav() + f"""
<main id="main">

  <section class="portada">
    <div class="buril"></div>
    <div class="portada-rej">
      <div>
        <h1><span class="ligera">No se trata de hacer<br />más publicidad.</span><br />Se trata del <span class="alta">sistema</span><br />que lo vuelve negocio.</h1>
        <p class="sub">
          Marca, pauta, sitio y CRM no son cuatro proveedores: son cuatro capas del mismo
          sistema. Sentido las opera desde una sola estrategia, y mide cada peso hasta el
          cliente que compró.
        </p>
        <div class="acciones">
          <a class="boton" href="{BASE}/contacto">Agendar diagnóstico <span class="fl">→</span></a>
          <a class="enlace" href="{BASE}/metodo">Ver el método</a>
        </div>
      </div>
      {ojo()}
    </div>
    <div class="wrap">{franja_capas()}</div>
  </section>

  <section class="seccion seccion--regla">
    <div class="wrap">
      <div class="cols cols-fija">
        <div class="pegado">
          {cabeza('Servicios sueltos no construyen un negocio.')}
        </div>
        <div>
          <p class="entrada" style="margin-bottom:26px">
            La mayoría de las marcas contratan agencias por pieza: un community por aquí,
            alguien para Google Ads por allá, un diseñador freelance para el sitio.
          </p>
          <p class="cuerpo apagado">
            Cada pieza vive en su isla, sin hablar con las demás. El resultado es predecible:
            presupuesto que se diluye, decisiones que se contradicen y leads que se pierden en
            el camino entre el anuncio y la venta.
          </p>
          <p class="cuerpo apagado">
            La marca, la pauta, el sitio y el CRM no son cuatro proyectos. Son cuatro capas del
            mismo sistema, y solo conectadas producen el resultado que cada una promete por
            separado.
          </p>
          <div class="acciones"><a class="enlace" href="{BASE}/metodo">Cómo trabajamos</a></div>
        </div>
      </div>
    </div>
  </section>

  <section class="seccion seccion--regla">
    <div class="wrap">
      {cabeza('Las cuatro capas, una por una.', 'Algunas marcas necesitan las cuatro desde el día uno; otras solo refuerzan la que tienen débil.')}
      <div class="plancha">{capas_largas}</div>
    </div>
  </section>

  <section class="declara">
    <div class="buril"></div>
    <div class="wrap">
      <p>Tu producto ya está listo. <span class="tenue">Tu mercado ya está esperando.</span> Falta el sistema que los conecta.</p>
    </div>
  </section>

  <section class="seccion">
    <div class="wrap">
      {cabeza('Lo que componemos en cada capa.', 'Siete módulos: cinco mensuales y dos de inversión única. El alcance y la inversión se cierran en la propuesta, después del diagnóstico.')}
      <div class="plancha">{servicios}</div>
    </div>
  </section>

  <section class="seccion seccion--placa">
    <div class="buril"></div>
    <div class="wrap">
      {cabeza('Cada pieza alimenta a las demás.', 'Las piezas no operan en paralelo desconectado: operan en circuito. Cada lead capturado entrena al modelo de la pauta, cada conversión refina la segmentación, cada reseña alimenta el contenido.')}
      <div class="plancha">{ia_html}</div>
      <p class="cuerpo apagado" style="margin-top:30px">
        Por eso el trabajo es continuo y no de entrega única: el sistema del mes seis vale más
        que el del mes uno, con la misma inversión.
      </p>
    </div>
  </section>

  <section class="seccion">
    <div class="wrap">
      {cabeza('Servicios que se contratan solos.', 'Además del sistema integral, hay piezas que resuelven un problema concreto sin comprometerse con todo el paquete.')}
      <div class="plancha">{productos}</div>
    </div>
  </section>

  <section class="seccion seccion--regla">
    <div class="wrap">
      {cabeza('De esta página a un sistema en marcha.', 'Cuatro pasos. El primero es sin costo y sirve para ambas partes: tú entiendes si Sentido encaja, y nosotros entendemos si podemos prometer resultados con honestidad.')}
      <div class="pasos">{pasos}</div>
    </div>
  </section>

</main>
""" + cierre(
        "Cuéntanos qué estás resolviendo.",
        "Un estratega de Sentido te responde en menos de 24 horas hábiles para agendar el diagnóstico. Sin costo, sin compromiso, y con una lectura honesta de si podemos ayudarte.",
        ("Ver casos y sectores", f"{BASE}/casos"),
    ) + pie()

    escribe("", html)


# ═══════════════════════════════════════════════════════════════
# MÉTODO
# ═══════════════════════════════════════════════════════════════

def build_metodo():
    capas = "".join(f"""
      <div class="renglon">
        <div class="buril"></div>
        <div><span class="marco">Capa {n}</span><h3>{t}</h3><p class="bajo-titulo">{tag}</p></div>
        <div><p>{b}</p></div>
        <div class="ver"></div>
      </div>""" for n, t, tag, b in LAYERS)

    practicas = "".join(f"""
      <div class="paso">
        <div class="paso-n">{n}</div>
        <div><h4>{t}</h4><p>{b}</p><span class="rotulo">{meta}</span></div>
      </div>""" for n, t, meta, b in PROCESS)

    arranque = "".join(f"""
      <div class="paso">
        <div class="paso-n">{n}</div>
        <div><h4>{t}</h4><p>{b}</p><span class="rotulo">{meta}</span></div>
      </div>""" for n, t, meta, b in ONBOARDING)

    principios = "".join(f"""
      <div class="renglon">
        <div class="buril"></div>
        <div><h3>{t}</h3></div>
        <div><p>{b}</p></div>
        <div class="ver"></div>
      </div>""" for t, b in [
        ("Una sola cabeza estratégica",
         "Brand, pauta, sitio, CRM y reputación se piensan desde la misma estrategia, no desde cinco proveedores que se enteran tarde de lo que decidió el otro."),
        ("Cada peso se mide al final de su recorrido",
         "No medimos clics ni alcance como meta: medimos leads calificados, conversiones y clientes recurrentes. La pauta vive integrada con CRM y sitio, para saber qué funcionó de verdad."),
        ("Sistema que escala sin rehacerse",
         "El sitio, el CRM y los flujos se construyen desde el día uno para crecer con la marca: más sucursales, más líneas de producto, más mercados, sin volver a empezar."),
    ])

    html = head(
        "Método · Sentido Branding &amp; Advertising",
        "El sistema de cuatro capas de Sentido — alcance, captura, conversión y retención — y el método que lo sostiene: diagnóstico, estrategia escrita, construcción en orden y optimización continua.",
        "/metodo",
    ) + nav("Método") + f"""
<main id="main">

  <section class="portada portada--int">
    <div class="buril"></div>
    <div class="portada-rej">
      <div>
        <h1><span class="ligera">El sistema,</span><br />en cuatro <span class="alta">capas</span>.</h1>
        <p class="sub">
          La diferencia entre una agencia que entrega piezas y una que construye sistemas no
          está en lo que ofrece: está en cómo trabaja. Esto es lo que pasa cada mes en Sentido,
          desde el primer día hasta el reporte número doce.
        </p>
      </div>
    </div>
  </section>

  <section class="seccion seccion--regla">
    <div class="wrap">
      {cabeza('Tres reglas que no negociamos.')}
      <div class="plancha">{principios}</div>
    </div>
  </section>

  <section class="seccion">
    <div class="wrap">
      {cabeza('Alcance, captura, conversión, retención.', 'Cada negocio que llega a Sentido se atiende desde estas cuatro capas. La propuesta puntual se arma una vez que entendemos dónde estás parado.')}
      <div class="plancha">{capas}</div>
    </div>
  </section>

  <section class="declara">
    <div class="buril"></div>
    <div class="wrap">
      <p>Construir en desorden <span class="tenue">es la causa número uno</span> de presupuesto desperdiciado.</p>
    </div>
  </section>

  <section class="seccion">
    <div class="wrap">
      {cabeza('El método detrás del sistema.', 'Cinco prácticas que se repiten en cada cuenta, cada mes, sin excepción.')}
      <div class="pasos">{practicas}</div>
    </div>
  </section>

  <section class="seccion seccion--placa">
    <div class="buril"></div>
    <div class="wrap">
      <div class="cols cols-fija">
        <div class="pegado">{cabeza('Branding, sitio, CRM, pauta. En ese orden.')}</div>
        <div>
          <p class="entrada" style="margin-bottom:26px">Es la secuencia que más presupuesto ahorra, y la que más se ignora.</p>
          <ul class="lista">
            <li><strong>Branding antes que todo.</strong> Si la marca aún no resuena en su mercado, cada campaña gasta parte del presupuesto en explicar quién eres. Si ya está resuelta, esta capa se salta.</li>
            <li><strong>Sitio antes que la pauta.</strong> Pagar por clics que aterrizan en un destino que no convierte es la forma más cara de aprender que el sitio importaba.</li>
            <li><strong>CRM antes que el volumen.</strong> Sin pipeline ni respuesta automática, más leads solo significa más leads perdidos.</li>
            <li><strong>Pauta al final, medible desde el primer peso.</strong> Con pixels, Conversions API y atribución conectados antes de prender la primera campaña. Si no se puede medir, no se prende.</li>
          </ul>
          <div class="acciones"><a class="enlace" href="{BASE}/servicios">Ver los módulos</a></div>
        </div>
      </div>
    </div>
  </section>

  <section class="seccion">
    <div class="wrap">
      {cabeza('De la primera llamada al primer reporte.', 'Cuatro pasos. El primero es sin costo y sirve para ambas partes.')}
      <div class="pasos">{arranque}</div>
    </div>
  </section>

</main>
""" + cierre(
        "Empecemos por el diagnóstico.",
        "45 minutos para mapear el estado actual del sistema y encontrar la brecha más cara de no resolver. Si no podemos ayudarte, te lo decimos en esa misma llamada.",
        ("Ver servicios", f"{BASE}/servicios"),
    ) + pie()

    escribe("metodo", html)


# ═══════════════════════════════════════════════════════════════
# SERVICIOS · índice
# ═══════════════════════════════════════════════════════════════

def build_servicios_index():
    filas = "".join(f"""
      <a class="renglon" href="{BASE}/servicios/{x['slug']}">
        <div class="buril"></div>
        <div><span class="marco">{x['tag']} · {x['tag2']}</span><h3>{x['name']}</h3></div>
        <div><p>{x['lede']}</p></div>
        <div class="ver">Ver</div>
      </a>""" for x in SERVICES)

    html = head(
        "Servicios · Sentido Branding &amp; Advertising",
        "Los siete módulos de Sentido: redes Meta, Google Ads, CRM y automatización, Google Business Profile, email marketing, branding y sitio web estratégico.",
        "/servicios",
    ) + nav("Servicios") + f"""
<main id="main">

  <section class="portada portada--int">
    <div class="buril"></div>
    <div class="portada-rej">
      <div>
        <h1><span class="ligera">Lo que componemos</span><br />en cada <span class="alta">capa</span>.</h1>
        <p class="sub">
          Siete módulos: cinco mensuales y dos de inversión única. No es un menú con precios
          cerrados. El alcance específico, el orden de activación y la inversión se definen en
          la propuesta, después del diagnóstico.
        </p>
      </div>
    </div>
  </section>

  <section class="seccion seccion--regla">
    <div class="wrap"><div class="plancha">{filas}</div></div>
  </section>

  <section class="seccion">
    <div class="wrap">
      <div class="cols cols-2">
        <div>
          <h3 style="margin-bottom:14px">El presupuesto de pauta va aparte.</h3>
          <p class="chico apagado">
            Los módulos de redes Meta y Google Ads requieren presupuesto de pauta, pero ese
            presupuesto va directo a Meta y Google con el medio de pago del cliente: no es
            parte de los honorarios de Sentido. El monto se calibra al mercado, sector y
            ambición del negocio durante el diagnóstico.
          </p>
        </div>
        <div>
          <h3 style="margin-bottom:14px">Algunos activan todo. Otros arrancan con dos.</h3>
          <p class="chico apagado">
            Algunos clientes activan los cinco módulos mensuales desde el día uno; otros
            arrancan con dos o tres y suman conforme el sistema demuestra tracción. El sitio web
            y el branding son inversiones únicas que suelen ir antes del paquete mensual.
          </p>
          <div class="acciones"><a class="enlace" href="{BASE}/metodo">Ver orden de construcción</a></div>
        </div>
      </div>
    </div>
  </section>

  <section class="seccion seccion--placa">
    <div class="buril"></div>
    <div class="wrap">
      {cabeza('Servicios que se contratan solos.', 'Piezas productizadas que resuelven un problema concreto sin comprometerse con el sistema completo.')}
      <div class="plancha">
        <a class="renglon" href="/sitios-web-ia">
          <div class="buril"></div>
          <div><span class="marco">Producto</span><h3>Sitios web producidos con IA</h3></div>
          <div><p>Estética de altísimo nivel, chatbot entrenado con la información del negocio, cotizador en tiempo real y formularios conectados a CRM.</p></div>
          <div class="ver">Ver</div>
        </a>
        <a class="renglon" href="/reactivacion-ghl-resenas">
          <div class="buril"></div>
          <div><span class="marco">Operación mensual</span><h3>Motor de Reactivación + Reseñas</h3></div>
          <div><p>Operamos tu GoHighLevel mes a mes: campañas de email y WhatsApp que reactivan tu base dormida, más gestión continua del flujo de reseñas en Google.</p></div>
          <div class="ver">Ver</div>
        </a>
      </div>
    </div>
  </section>

</main>
""" + cierre(
        "¿Cuál necesitas primero?",
        "Casi nunca son todos, y casi nunca es el que se cree. En el diagnóstico mapeamos qué capa está frenando al resto y en qué orden conviene activar.",
    ) + pie()

    escribe("servicios", html)


# ═══════════════════════════════════════════════════════════════
# SERVICIOS · detalle
# ═══════════════════════════════════════════════════════════════

def build_servicio(x):
    incluye = "".join(f"<li>{i}</li>" for i in x["includes"])
    kpis = "".join(f"<li>{i}</li>" for i in x["kpis"])
    ligados = "".join(f"""
      <a class="renglon" href="{BASE}/servicios/{r}">
        <div class="buril"></div>
        <div><span class="marco">{SERV_BY_SLUG[r]['tag']}</span><h3>{SERV_BY_SLUG[r]['name']}</h3></div>
        <div><p>{SERV_BY_SLUG[r]['sub']}.</p></div>
        <div class="ver">Ver</div>
      </a>""" for r in x["related"])

    html = head(
        f"{x['name']} · Sentido",
        x["lede"][:180],
        f"/servicios/{x['slug']}",
    ) + nav("Servicios") + f"""
<main id="main">

  <section class="portada portada--int">
    <div class="buril"></div>
    <div class="portada-rej">
      <div>
        <p style="margin-bottom:20px"><a class="rotulo" href="{BASE}/servicios">← Servicios</a></p>
        <span class="rotulo">{x['tag']} · {x['tag2']}</span>
        <h1 style="margin-top:18px">{x['name']}</h1>
        <p class="sub">{x['lede']}</p>
        <div class="acciones">
          <a class="boton" href="{BASE}/contacto">Cotizar este módulo <span class="fl">→</span></a>
        </div>
      </div>
    </div>
  </section>

  <section class="seccion seccion--regla">
    <div class="wrap">
      <div class="cols cols-fija">
        <div class="pegado">{cabeza(x['sub'] + '.')}</div>
        <div><p class="entrada">{x['problem']}</p></div>
      </div>
    </div>
  </section>

  <section class="seccion">
    <div class="wrap">
      <div class="cols cols-fija">
        <div class="pegado">{cabeza('El alcance del módulo.')}</div>
        <div><ul class="lista">{incluye}</ul></div>
      </div>
    </div>
  </section>

  <section class="seccion seccion--placa">
    <div class="buril"></div>
    <div class="wrap">
      <div class="cols cols-2">
        <div>
          <h3 style="margin-bottom:16px">Dónde entra la máquina.</h3>
          <p class="cuerpo apagado">{x['ia']}</p>
        </div>
        <div>
          <h3 style="margin-bottom:16px">Cuándo tiene sentido activarlo.</h3>
          <p class="cuerpo apagado">{x['for_whom']}</p>
        </div>
      </div>
    </div>
  </section>

  <section class="seccion">
    <div class="wrap">
      <div class="cols cols-fija">
        <div class="pegado">{cabeza('Los números del reporte mensual.')}</div>
        <div>
          <ul class="lista" style="margin-bottom:30px">{kpis}</ul>
          <div class="cierre" style="padding:28px">
            <div class="buril"></div>
            <span class="rotulo">Nota</span>
            <p class="chico apagado" style="margin-top:12px">{x['note']}</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="seccion seccion--regla">
    <div class="wrap">
      {cabeza('Módulos que se acoplan.')}
      <div class="plancha">{ligados}</div>
    </div>
  </section>

</main>
""" + cierre(
        "Hablemos de tu caso.",
        "En el diagnóstico revisamos si este módulo es el que más mueve tu negocio hoy, o si conviene resolver otra capa primero. La respuesta honesta suele ahorrar meses.",
        ("Ver todos los servicios", f"{BASE}/servicios"),
    ) + pie()

    escribe(f"servicios/{x['slug']}", html)


# ═══════════════════════════════════════════════════════════════
# CASOS — por sector, sin nombres de cliente
# ═══════════════════════════════════════════════════════════════

def build_casos():
    sectores = "".join(f"""
      <div class="renglon">
        <div class="buril"></div>
        <div><h3>{n}</h3><p class="bajo-titulo">{sub}</p></div>
        <div>
          <p style="margin-bottom:16px">{b}</p>
          <ul class="lista lista--chica">{"".join(f"<li>{c}</li>" for c in caps)}</ul>
        </div>
        <div class="ver"></div>
      </div>""" for n, sub, b, caps in SECTORS)

    html = head(
        "Casos y sectores · Sentido Branding &amp; Advertising",
        "Sectores donde Sentido opera el sistema completo: inmobiliario, industrial, automotriz premium, clubes y wellness, consumo y retail, servicios profesionales.",
        "/casos",
    ) + nav("Casos") + f"""
<main id="main">

  <section class="portada portada--int">
    <div class="buril"></div>
    <div class="portada-rej">
      <div>
        <h1><span class="ligera">Dónde ya operamos</span><br />el sistema <span class="alta">completo</span>.</h1>
        <p class="sub">
          El sistema es el mismo en todos lados; lo que cambia es qué capa pesa más. En
          inmobiliario manda la captura y el pipeline. En industrial, el contenido y la
          intención de búsqueda. En clubes, la retención.
        </p>
      </div>
    </div>
  </section>

  <section class="seccion seccion--regla">
    <div class="wrap">
      {cabeza('Seis contextos, un mismo sistema.')}
      <div class="plancha">{sectores}</div>
    </div>
  </section>

  <section class="seccion seccion--placa">
    <div class="buril"></div>
    <div class="wrap">
      <div class="cols cols-fija">
        <div class="pegado">{cabeza('Sin nombres ni capturas fuera de contexto.')}</div>
        <div>
          <p class="entrada" style="margin-bottom:26px">
            No publicamos nombres de clientes ni sus números sin autorización, y desconfiamos de
            las agencias que sí lo hacen.
          </p>
          <p class="cuerpo apagado">
            Un ROAS aislado, sin ticket promedio ni margen ni ciclo de venta, no dice nada sobre
            si ese negocio ganó dinero. Y una lista de logos no prueba que el trabajo haya
            funcionado, solo que alguien firmó alguna vez.
          </p>
          <p class="cuerpo apagado">
            Lo que sí hacemos es enseñar el método de medición en el diagnóstico: qué se
            instrumenta, qué se atribuye y cómo se ve un reporte mensual real. Si necesitas
            referencias directas, las conectamos con clientes que aceptaron darlas.
          </p>
          <div class="acciones"><a class="enlace" href="{BASE}/contacto">Pedir referencias</a></div>
        </div>
      </div>
    </div>
  </section>

</main>
""" + cierre(
        "¿Tu sector no está en la lista?",
        "El sistema no depende del giro: depende de que haya demanda, un ticket que justifique la inversión y una operación capaz de atender lo que llegue. Eso se valida en 45 minutos.",
        ("Ver el método", f"{BASE}/metodo"),
    ) + pie()

    escribe("casos", html)


# ═══════════════════════════════════════════════════════════════
# BLOG
# ═══════════════════════════════════════════════════════════════

def build_blog_index():
    filas = "".join(f"""
      <a class="nota" href="{BASE}/blog/{p['slug']}">
        <div class="buril"></div>
        <div class="fecha"><time datetime="{p['date']}">{p['date_h']}</time><br />{p['cat']}</div>
        <div><h3>{p['title']}</h3><p>{p['excerpt']}</p></div>
        <div class="min">{p['read']}</div>
      </a>""" for p in POSTS)

    html = head(
        "Blog · Sentido Branding &amp; Advertising",
        "Notas sobre estrategia digital, pauta, sitios web con IA, CRM y retención — desde la operación real de una agencia, no desde la teoría.",
        "/blog",
    ) + nav("Blog") + f"""
<main id="main">

  <section class="portada portada--int">
    <div class="buril"></div>
    <div class="portada-rej">
      <div>
        <h1><span class="ligera">Notas desde</span><br />la <span class="alta">operación</span>.</h1>
        <p class="sub">
          Lo que vemos trabajando cuentas reales: qué funciona, qué se rompe y qué cuesta más
          caro de lo que parece. Sin fórmulas mágicas y sin capturas fuera de contexto.
        </p>
      </div>
    </div>
  </section>

  <section class="seccion seccion--regla">
    <div class="wrap"><div class="notas">{filas}</div></div>
  </section>

</main>
""" + cierre(
        "¿Algo de esto describe tu situación?",
        "El diagnóstico de 45 minutos sirve para aterrizar cualquiera de estos temas a tu negocio concreto: qué capa está frenando al resto y en qué orden conviene moverse.",
        ("Ver el método", f"{BASE}/metodo"),
    ) + pie()

    escribe("blog", html)


def build_post(p):
    otras = [q for q in POSTS if q["slug"] != p["slug"]][:2]
    mas = "".join(f"""
      <a class="nota" href="{BASE}/blog/{q['slug']}">
        <div class="buril"></div>
        <div class="fecha">{q['cat']}</div>
        <div><h3>{q['title']}</h3><p>{q['excerpt']}</p></div>
        <div class="min">{q['read']}</div>
      </a>""" for q in otras)

    ld = ('<script type="application/ld+json">{"@context":"https://schema.org",'
          '"@type":"BlogPosting","headline":"%s","datePublished":"%s",'
          '"author":{"@type":"Organization","name":"Sentido Branding & Advertising"},'
          '"publisher":{"@type":"Organization","name":"Sentido Branding & Advertising"},'
          '"inLanguage":"es-MX","mainEntityOfPage":"https://sentido.mx/blog/%s"}</script>\n'
          % (p["title"].replace('"', "'"), p["date"], p["slug"]))

    html = head(f"{p['title']} · Sentido", p["excerpt"], f"/blog/{p['slug']}", extra=ld) + nav("Blog") + f"""
<main id="main">

  <section class="portada portada--int" style="padding-bottom:24px">
    <div class="buril"></div>
    <div class="angosto" style="max-width:760px">
      <p style="margin-bottom:20px"><a class="rotulo" href="{BASE}/blog">← Blog</a></p>
      <span class="rotulo">{p['cat']} · {p['read']} de lectura</span>
      <h1 style="font-size:clamp(2rem,4.6vw,3.5rem);margin-top:20px">{p['title']}</h1>
      <p class="rotulo" style="margin-top:24px"><time datetime="{p['date']}">{p['date_h']}</time></p>
    </div>
  </section>

  <article class="seccion" style="padding-top:44px">
    <div class="articulo">{p['body']}</div>
  </article>

  <section class="seccion seccion--regla">
    <div class="wrap">
      {cabeza('Más notas.')}
      <div class="notas">{mas}</div>
    </div>
  </section>

</main>
""" + cierre(
        "Hablemos de tu caso.",
        "45 minutos, sin costo, para mapear el estado actual de tu sistema y dónde está la brecha más cara de no resolver.",
    ) + pie()

    escribe(f"blog/{p['slug']}", html)


# ═══════════════════════════════════════════════════════════════
# CONTACTO
# ═══════════════════════════════════════════════════════════════

def build_contacto():
    intereses = [
        ("pauta", "Pauta (Meta / Google)"), ("redes", "Redes y contenido"),
        ("sitio", "Sitio web"), ("branding", "Branding / Identidad"),
        ("crm", "CRM y automatización"), ("email", "Email marketing"),
        ("reactivacion", "Reactivación y reseñas"), ("paquete", "Paquete integral"),
        ("no-se", "Aún no estoy seguro"),
    ]
    checks = "".join(f'<label class="check"><input type="checkbox" name="interes" value="{v}" /> {t}</label>'
                     for v, t in intereses)
    pasos = "".join(f"""
      <div class="paso">
        <div class="paso-n">{n}</div>
        <div><h4 style="font-size:1.0625rem">{t}</h4><p style="font-size:.875rem">{b}</p><span class="rotulo">{meta}</span></div>
      </div>""" for n, t, meta, b in ONBOARDING)

    html = head(
        "Contacto · Sentido Branding &amp; Advertising",
        "Agenda un diagnóstico estratégico sin costo con Sentido. 45 minutos para mapear tu sistema de marketing y encontrar la brecha más cara de no resolver.",
        "/contacto",
    ) + nav() + f"""
<main id="main">

  <section class="portada portada--int">
    <div class="buril"></div>
    <div class="portada-rej">
      <div>
        <h1><span class="ligera">Cuéntanos qué</span><br />estás <span class="alta">resolviendo</span>.</h1>
        <p class="sub">
          El formulario tarda menos de un minuto. Un estratega de Sentido te responde en menos
          de 24 horas hábiles para agendar el diagnóstico: 45 minutos, sin costo y sin compromiso.
        </p>
      </div>
    </div>
  </section>

  <section class="seccion seccion--regla" style="padding-top:clamp(44px,5vw,64px)">
    <div class="wrap">
      <div class="cols cols-fija">

        <div class="pegado">
          <span class="rotulo">Qué pasa después</span>
          <div class="pasos" style="margin-top:20px">{pasos}</div>
          <div style="margin-top:28px">
            <span class="rotulo">Directo</span>
            <ul class="lista lista--chica" style="margin-top:14px">
              <li><a class="enlace-txt" href="mailto:{MAIL}">{MAIL}</a></li>
              <li><a class="enlace-txt" href="{WA}" rel="noopener">WhatsApp</a></li>
            </ul>
          </div>
        </div>

        <div>
          <div class="forma">
            <div class="buril"></div>
            <form id="lead-form" data-webhook="/api/lead" data-fuente="sentido.mx" novalidate>
              <div class="rej-forma">

                <div class="campo">
                  <label class="etiq" for="f-nombre">Nombre completo <span class="req">*</span></label>
                  <input class="ent" id="f-nombre" name="nombre" type="text" autocomplete="name" required />
                </div>
                <div class="campo">
                  <label class="etiq" for="f-empresa">Empresa o marca <span class="req">*</span></label>
                  <input class="ent" id="f-empresa" name="empresa" type="text" autocomplete="organization" required />
                </div>
                <div class="campo">
                  <label class="etiq" for="f-email">Correo electrónico <span class="req">*</span></label>
                  <input class="ent" id="f-email" name="email" type="email" autocomplete="email" required />
                </div>
                <div class="campo">
                  <label class="etiq" for="f-whatsapp">WhatsApp <span class="req">*</span></label>
                  <input class="ent" id="f-whatsapp" name="whatsapp" type="tel" autocomplete="tel" placeholder="+52 ..." required />
                </div>
                <div class="campo ancho">
                  <label class="etiq" for="f-sitio">Sitio web o Instagram actual</label>
                  <input class="ent" id="f-sitio" name="sitio" type="text" placeholder="sitio.com · @instagram" />
                </div>

                <div class="campo ancho">
                  <span class="etiq">¿En qué necesitas apoyo? <span class="req">*</span></span>
                  <div class="rej-check">{checks}</div>
                </div>

                <div class="campo">
                  <label class="etiq" for="f-presupuesto">¿En qué punto estás?</label>
                  <select class="sel" id="f-presupuesto" name="presupuesto">
                    <option value="">Selecciona una opción</option>
                    <option value="sin-inversion">Todavía no invierto en marketing</option>
                    <option value="invierto-sin-plan">Ya invierto, pero sin estrategia clara</option>
                    <option value="presupuesto-asignado">Tengo presupuesto asignado para este año</option>
                    <option value="por-definir">Depende del alcance que propongan</option>
                  </select>
                </div>
                <div class="campo">
                  <label class="etiq" for="f-tiempo">¿Cuándo te gustaría arrancar?</label>
                  <select class="sel" id="f-tiempo" name="tiempo">
                    <option value="">Selecciona un horizonte</option>
                    <option value="asap">Lo antes posible</option>
                    <option value="1-3-meses">En 1 a 3 meses</option>
                    <option value="3-6-meses">En 3 a 6 meses</option>
                    <option value="explorando">Solo estoy explorando</option>
                  </select>
                </div>

                <div class="campo ancho">
                  <label class="etiq" for="f-contexto">Algo de contexto (opcional)</label>
                  <textarea class="area" id="f-contexto" name="contexto" placeholder="Qué estás intentando resolver, qué ya intentaste, qué te frena hoy."></textarea>
                </div>

                <div class="estado" id="lead-estado" role="status" aria-live="polite"></div>
              </div>

              <div class="pie-forma">
                <span class="rotulo">Respuesta en menos de 24 h hábiles</span>
                <button class="boton" type="submit" data-enviar>Enviar <span class="fl">→</span></button>
              </div>
            </form>
          </div>
        </div>

      </div>
    </div>
  </section>

</main>
""" + pie()

    escribe("contacto", html)


# ═══════════════════════════════════════════════════════════════

def build_sitemap():
    urls = ["/", "/metodo", "/servicios", "/casos", "/blog", "/contacto"]
    urls += [f"/servicios/{x['slug']}" for x in SERVICES]
    urls += [f"/blog/{p['slug']}" for p in POSTS]
    cuerpo = "".join(f"  <url><loc>https://sentido.mx{u}</loc></url>\n" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + cuerpo + '</urlset>\n',
        encoding="utf-8")
    print("  ✓ sitio/sitemap.xml")


if __name__ == "__main__":
    print("Generando sitio…")
    build_home()
    build_metodo()
    build_servicios_index()
    for _s in SERVICES:
        build_servicio(_s)
    build_casos()
    build_blog_index()
    for _p in POSTS:
        build_post(_p)
    build_contacto()
    # sitemap: se genera al publicar en el dominio definitivo, no en preview
    print("Listo.")
