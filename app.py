import streamlit as st
from streamlit_option_menu import option_menu

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="EcoWeb - Proyecto Eco",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# INYECCIÓN DE INTERFAZ DE ALTO IMPACTO (FUEGO CONTRA CELULARES)
# ==========================================
st.markdown("""
    <style>
    /* Fondo con degradado fluido: verde selva profundo y azul medianoche técnico */
    .stApp {
        background: linear-gradient(135deg, #0b2310 0%, #081018 50%, #05080c 100%) !important;
        color: #E0E6ED !important;
    }
    
    /* Estilo del menú lateral blur */
    [data-testid="stSidebar"] {
        background-color: rgba(11, 25, 16, 0.9) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(46, 125, 50, 0.3);
    }

    /* Títulos Principales en Degradado */
    .main-title {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: 46px !important;
        font-weight: 800;
        letter-spacing: 1px;
        background: linear-gradient(90deg, #A5D6A7, #4CAF50, #00E676);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        text-shadow: 0px 4px 20px rgba(76, 175, 80, 0.2);
    }
    .subtitle {
        font-size: 18px !important;
        font-weight: 300;
        color: #81C784 !important;
        margin-bottom: 30px;
        opacity: 0.9;
    }

    /* Encabezados de Sección */
    .section-header {
        font-size: 26px !important;
        font-weight: 600;
        color: #B9F6CA !important;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    /* Tarjetas con efecto Glassmorphism */
    .glass-card {
        width: 100%; 
        max-width: 800px;
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(165, 214, 167, 0.15);
        word-wrap: break-word; 
        overflow-wrap: break-word;
        border-radius: 16px;
        padding: 1.5rem; 
        box-sizing: border-box;
        margin-bottom: 25px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: all 0.3s ease-in-out;
    }
    .glass-card:hover {
        border: 1px solid rgba(0, 230, 118, 0.4);
        box-shadow: 0 8px 32px 0 rgba(0, 230, 118, 0.15);
        transform: translateY(-3px);
    }

    /* Contenedores para evitar saltos y códigos visibles */
    .info-item {
        margin-bottom: 16px;
        line-height: 1.5;
        font-size: 15.5px;
    }
    .info-bullet {
        color: #00E676;
        font-weight: bold;
        margin-right: 8px;
    }
    .info-tag {
        color: #B9F6CA;
        font-weight: 700;
        margin-right: 6px;
    }

    /* TABLA PREMIUM ESTILO CYBER-GREEN */
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .custom-table th {
        background: rgba(46, 125, 50, 0.6) !important;
        color: #FFFFFF !important;
        text-align: left;
        padding: 14px 18px;
        font-size: 16px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        border-bottom: 2px solid #2E7D32;
    }
    .custom-table td {
        padding: 14px 18px;
        font-size: 15px;
        color: #E0E6ED;
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        background: rgba(255, 255, 255, 0.02);
    }
    .custom-table tr:hover td {
        background: rgba(0, 230, 118, 0.08) !important;
        color: #FFFFFF;
    }
    .pilar-tag {
        background: rgba(0, 230, 118, 0.15);
        color: #00E676;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 14px;
        border: 1px solid rgba(0, 230, 118, 0.3);
    }
    </style>
""", unsafe_allow_html=True)


# ==========================================
# MENÚ LATERAL (SIDEBAR MODULAR)
# ==========================================
with st.sidebar:
    st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/2913/2913520.png' width='80'></div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #B9F6CA; margin-bottom: 0;'>Ecosistema Eco 2026</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #81C784; font-size: 14px;'>E.E.S.T N°7 | 4° 4°</p>", unsafe_allow_html=True)
    st.write("---")

    selected = option_menu(
        menu_title=None,
        options=[
            "Inicio",               # Página 1
            "Objetivo Eco",         # Página 2
            "Fundamentos Eco",      # Página 3
            "Cronología Eco",       # Página 4
            "EcoGalaxy",             # Página 5
            "Fichas Técnicas",      # Página 6
            "Explorador Eco",       # Página 7
            "Sistema Reconocidos",  # Página 9
            "¿Cómo Replicar Eco?",         # Página 10
            "Galería Eco",          # Página 11
            "Preguntas Frecuentes", # Página 12
            "EcoIA"                 # Página 13 <- ¡EL COLOFÓN TECNOLÓGICO!
        ], 
        icons=[
            "house-door-fill", "bullseye", "diagram-3-fill", "clock-history", 
            "stars", "file-earmark-text-fill", "search-heart-fill", 
            "award-fill", "share-fill", "images", "patch-question-fill", "cpu-fill"
        ], # cpu-fill le da el aspecto de núcleo de Inteligencia Artificial
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#00E676", "font-size": "17px"}, 
            "nav-link": {"font-size": "14px", "color": "#E0E6ED", "text-align": "left", "margin":"2px 0px", "--hover-color": "rgba(0, 230, 118, 0.1)"},
            "nav-link-selected": {"background-color": "rgba(46, 125, 50, 0.5)", "border": "1px solid #00E676", "color": "white", "font-weight": "600"},
        }
    )
    
    st.write("---")
    st.caption("Feria Tecnológica 2026")
    
# ==========================================
# PÁGINA 1 — INICIO
# ==========================================
if selected == "Inicio":

    st.markdown('<div class="main-title">PROYECTO ECO 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Plataforma de innovación educativa basada en sustentabilidad, ciencia y trabajo colaborativo.</div>', unsafe_allow_html=True)

    # 1. ¿Qué es EcoWeb?
    st.markdown('<div class="section-header">🧬 ¿Qué es EcoWeb?</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card" style="font-size: 18px; line-height: 1.6; border-left: 5px solid #00E676;">
        <strong>EcoWeb</strong> es la plataforma digital oficial de <strong>Proyecto Eco</strong>.
        Fue desarrollada para centralizar información, documentación, fichas técnicas, recursos educativos y
        materiales relacionados con el proyecto, permitiendo que los conocimientos generados puedan conservarse,
        consultarse y compartirse de forma más sencilla.
        </div>
        """,
        unsafe_allow_html=True
    )

# Columnas centrales
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="section-header">⚠️ ¿Por qué fue creada?</div>', unsafe_allow_html=True)

        st.markdown("""
    <div class="glass-card">

    <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:18px;">
    Necesitábamos resolver varios desafíos:
    </p>

    <p><b style="color:#B9F6CA;">✦ Información dispersa:</b> Reunir en un solo lugar datos, investigaciones y documentos del proyecto.</p>

    <p><b style="color:#B9F6CA;">✦ Crecimiento del proyecto:</b> Organizar cada nueva iniciativa a medida que Proyecto Eco continúa expandiéndose.</p>

    <p><b style="color:#B9F6CA;">✦ Conservación del conocimiento:</b> Evitar que la experiencia y los aprendizajes se pierdan cuando los estudiantes egresan.</p>

    <p><b style="color:#B9F6CA;">✦ Replicabilidad:</b> Facilitar que otras escuelas puedan comprender y aplicar el modelo desarrollado.</p>

    <p><b style="color:#B9F6CA;">✦ Visualización de resultados:</b> Mostrar de forma clara los avances, actividades y logros alcanzados por el proyecto.</p>

    </div>
    """, unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="section-header">⚙️ Funciones de EcoWeb</div>', unsafe_allow_html=True)

        st.markdown("""
    <div class="glass-card">

    <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:18px;">
    ¿Para qué sirve nuestra plataforma digital?
    </p>

    <p><b style="color:#B9F6CA;">✦ Organizar información:</b> Reúne proyectos, investigaciones y documentación en un único espacio.</p>

    <p><b style="color:#B9F6CA;">✦ Almacenar documentación:</b> Permite acceder a fichas técnicas, documentos y procedimientos desarrollados por el equipo.</p>

    <p><b style="color:#B9F6CA;">✦ Difundir iniciativas:</b> Presenta actividades, campañas y experiencias realizadas dentro de Proyecto Eco.</p>

    <p><b style="color:#B9F6CA;">✦ Facilitar consultas:</b> Permite encontrar rápidamente recursos educativos e información relevante.</p>

    <p><b style="color:#B9F6CA;">✦ Mostrar avances:</b> Expone de manera transparente los resultados y progresos del proyecto.</p>

    <p><b style="color:#B9F6CA;">✦ Favorecer la replicabilidad:</b> Facilita que otras instituciones puedan conocer y adaptar la metodología de trabajo.</p>

    </div>
    """, unsafe_allow_html=True)

# ==========================================
# PÁGINA 2 — OBJETIVO ECO
# ==========================================
elif selected == "Objetivo Eco":

    st.markdown('<div class="main-title">OBJETIVO ECO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">El problema que identificó Proyecto Eco y la solución que propone</div>', unsafe_allow_html=True)

    # OBJETIVO GENERAL
    st.markdown('<div class="section-header">🎯 Objetivo General: ¿Qué intenta conseguir Proyecto Eco?</div>', unsafe_allow_html=True)

    st.markdown("""<div class="glass-card" style="font-size: 18px; line-height: 1.6; border-left: 5px solid #00E676; max-width: 100%;">El propósito de <strong>Proyecto Eco</strong> es construir un sistema educativo continuo, sustentable y replicable que permita desarrollar soluciones ambientales, conservar conocimientos técnicos y generar un impacto positivo dentro de la comunidad educativa.</div>""", unsafe_allow_html=True)

    # PROBLEMA Y CONSECUENCIAS
    col_prob, col_cons = st.columns(2)

    with col_prob:
        st.markdown('<div class="section-header">❌ 1. Problema Identificado</div>', unsafe_allow_html=True)
        st.markdown("""<div class="glass-card" style="max-width: 100%; min-height: 380px;">
<p style="margin-top:0; color:#FF5252; font-weight:600; margin-bottom:18px;">¿Qué problema observó Proyecto Eco?</p>
<div class="info-item"><span class="info-bullet" style="color:#FF5252;">✦</span><span class="info-tag">Dependencia de pocas personas:</span> Muchos proyectos escolares quedan sostenidos por un número reducido de alumnos o docentes.</div>
<div class="info-item"><span class="info-bullet" style="color:#FF5252;">✦</span><span class="info-tag">Pérdida de conocimientos:</span> Gran parte de la experiencia adquirida desaparece cuando termina cada ciclo lectivo.</div>
<div class="info-item"><span class="info-bullet" style="color:#FF5252;">✦</span><span class="info-tag">Falta de documentación:</span> Muchas iniciativas carecen de registros organizados, procedimientos o materiales de consulta.</div>
<div class="info-item"><span class="info-bullet" style="color:#FF5252;">✦</span><span class="info-tag">Dificultad para transmitir experiencias:</span> Los nuevos integrantes suelen comenzar sin acceso a los aprendizajes de años anteriores.</div>
<div class="info-item"><span class="info-bullet" style="color:#FF5252;">✦</span><span class="info-tag">Escasa continuidad:</span> Muchas iniciativas pierden impulso o desaparecen con el paso del tiempo.</div>
</div>""", unsafe_allow_html=True)

    with col_cons:
        st.markdown('<div class="section-header">📉 2. Consecuencias del Problema</div>', unsafe_allow_html=True)
        st.markdown("""<div class="glass-card" style="max-width: 100%; min-height: 380px;">
<p style="margin-top:0; color:#FF8A80; font-weight:600; margin-bottom:18px;">¿Por qué es importante resolverlo?</p>
<div class="info-item"><span class="info-bullet" style="color:#FF8A80;">✦</span><span class="info-tag">Reinicio constante:</span> Cada año muchos proyectos deben comenzar nuevamente porque gran parte de la experiencia previa se pierde.</div>
<div class="info-item"><span class="info-bullet" style="color:#FF8A80;">✦</span><span class="info-tag">Desperdicio de recursos:</span> Se pierden materiales, tiempo y trabajo acumulado durante años anteriores.</div>
<div class="info-item"><span class="info-bullet" style="color:#FF8A80;">✦</span><span class="info-tag">Menor participación:</span> La falta de organización puede desmotivar a quienes desean sumarse al proyecto.</div>
<div class="info-item"><span class="info-bullet" style="color:#FF8A80;">✦</span><span class="info-tag">Menor impacto:</span> Las iniciativas ambientales logran resultados más limitados de los que podrían alcanzar.</div>
<div class="info-item"><span class="info-bullet" style="color:#FF8A80;">✦</span><span class="info-tag">Dependencia crítica:</span> El funcionamiento del proyecto puede verse afectado si una persona clave abandona la institución.</div>
</div>""", unsafe_allow_html=True)

    # SOLUCIÓN
    st.markdown('<div class="section-header">🛠️ 3. Solución Propuesta: El Sistema Eco</div>', unsafe_allow_html=True)
    st.markdown("""<div class="glass-card" style="max-width: 100%;">
<p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:18px;">¿Cómo intenta resolver el problema Proyecto Eco?</p>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 15px;">
<div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;"><span style="color:#00E676; font-weight:bold;">🏢 Organización por Secciones:</span> Distribuye las tareas entre diferentes áreas especializadas para mejorar la coordinación y el trabajo en equipo.</div>
<div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;"><span style="color:#00E676; font-weight:bold;">🏆 Sistema de Reconocidos:</span> Busca incentivar la participación, el compromiso y la constancia de los integrantes.</div>
<div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;"><span style="color:#00E676; font-weight:bold;">📋 Fichas Técnicas:</span> Registran materiales, procedimientos, resultados y aprendizajes obtenidos durante cada proyecto.</div>
<div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;"><span style="color:#00E676; font-weight:bold;">🔄 Flujo Eco:</span> Promueve que los conocimientos y recursos generados por un proyecto puedan ser aprovechados por otros.</div>
<div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;"><span style="color:#00E676; font-weight:bold;">⭐ Pilares Eco:</span> Los 7 pilares que orientan y definen el funcionamiento de Proyecto Eco.</div>
<div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;"><span style="color:#00E676; font-weight:bold;">🌐 Herramientas Digitales:</span> EcoWeb y otros recursos tecnológicos ayudan a organizar, conservar y compartir información.</div>
</div>
</div>""", unsafe_allow_html=True)

    # PRINCIPIOS Y VISIÓN FUTURA
    col_pila, col_vis = st.columns([4, 6])

    with col_pila:
        st.markdown('<div class="section-header">⚖️ 4. Principios de la Solución</div>', unsafe_allow_html=True)
        st.markdown("""<div class="glass-card" style="max-width: 100%; min-height: 320px;">
<p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:15px;">¿Sobre qué pilares se construye Proyecto Eco?</p>
<div style="display: flex; flex-wrap: wrap; gap: 8px;">
<span class="pilar-tag">♻️ Replicable</span>
<span class="pilar-tag">🌿 Sustentable</span>
<span class="pilar-tag">🔄 Circular</span>
<span class="pilar-tag">⏳ Continuo</span>
<span class="pilar-tag">🧪 Experimental</span>
<span class="pilar-tag">📊 Medible</span>
<span class="pilar-tag">🤝 Interdisciplinario</span>
</div>
</div>""", unsafe_allow_html=True)

# ==========================================
# PÁGINA 3 — FUNDAMENTOS ECO
# ==========================================
elif selected == "Fundamentos Eco":
    
    st.markdown('<div class="main-title">FUNDAMENTOS ECO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Estructura Metodológica, Matrices de Flujo y Marcos Conceptuales del Sistema</div>', unsafe_allow_html=True)
    
    # SECCIÓN 1: INTRODUCCIÓN A LOS FUNDAMENTOS
    st.markdown('<div class="section-header">🧠 ¿Cómo funciona Proyecto Eco?</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="font-size: 17px; line-height: 1.6; border-left: 5px solid #00E676;">
        Para crear una base del proyecto, no debe de manejarse como un proyecto aislado. Debe de mantener una serie de fundamentos para poder mantenerse en pie. El Proyecto Eco se sostiene por una infraestructura de conocimientos y conceptos que garantizan un proyecto activo, estructurado y replicable para cualquier institución.
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 2: LOS 7 PILARES (Desplegable interactivo premium para feria)
    st.markdown('<div class="section-header">🏛️ 1. Los 7 Pilares: ¿Qué características definen Eco?</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A5D6A7; margin-bottom:15px;">Haz clic en cada pilar para auditar sus definiciones, funciones y aplicaciones prácticas en el mundo real:</p>', unsafe_allow_html=True)
    
    pilares_data = {
        "♻️ Replicable": {
            "def": "Capacidad de que cualquier institución pueda replicar Eco y crear su proyecto estable.",
            "fun": "Estandariza los procesos para que cualquier institución pueda adoptar el modelo rápidamente.",
            "ej": "Fichas técnicas en formato abierto y manuales paso a paso de libre acceso en EcoWeb."
        },
        "🌿 Sustentable": {
            "def": "Capacidad del proyecto de mantener un equilibrio ambiental.",
            "fun": "Garantiza que cada dispositivo o recurso creado reduzca de forma real la contaminación.",
            "ej": "Elaboración de fichas como Nendo Dango para crear una sustentabilidad."
        },
        "🔄 Circular": {
            "def": "El proyecto debe estar enfocado en la eliminación de residuos mediante el upcycling y el aprovechamiento continuo.",
            "fun": "Cierra los ciclos de vida de los materiales de descarte, convirtiendo la salida de un proceso en la entrada de otro.",
            "ej": "Producción de Carbon Ink procesando el descarte y sobrantes inservibles de EcoPapel."
        },
        "⏳ Continuo": {
            "def": "Garantía de preservación y avance del proyecto a través del tiempo, mitigando el recambio generacional.",
            "fun": "Evita la pérdida de conocimiento crítico cuando las camadas de estudiantes egresan de la institución.",
            "ej": "Creación del pilar Replicable, Sistema de Líderes y Sistema de Reconocidos."
        },
        "🧪 Experimental": {
            "def": "Metodología basada en el ensayo, el error documentado, el análisis empírico y la optimización constante.",
            "fun": "Fomenta el pensamiento científico y técnico, permitiendo aprender de los fallos de los prototipos.",
            "ej": "Pruebas constantes y solución de problemas en la gran mayoría de fichas hasta llegar a la conclusión más eficiente."
        },
        "📊 Medible": {
            "def": "Capacidad de medir y valorar los resultados, el rendimiento y el impacto ambiental.",
            "fun": "Aporta rigor matemático y científico a las fichas y proyectos mediante indicadores claros y tangibles.",
            "ej": "-"
        },
        "🤝 Interdisciplinario": {
            "def": "Integración y convergencia de múltiples secciones del conocimiento.",
            "fun": "Rompe el aislamiento de las materias escolares tradicionales. Además de incluir a aquellas personas que no quieran reciclar papel o trabajar en redes sociales.",
            "ej": "EcoTech trabaja en Tecnologia, EcoLab en Quimica, etc."
        }
    }

    for name, info in pilares_data.items():
        with st.expander(name):
            st.markdown(f"""
                <div style="padding: 10px; line-height: 1.6;">
                    <p style="color:#B9F6CA; margin-bottom:5px;"><strong>Definición:</strong> {info['def']}</p>
                    <p style="color:#E0E6ED; margin-bottom:5px;"><strong>Función:</strong> {info['fun']}</p>
                    <p style="color:#81C784; margin-bottom:0;"><strong>Ejemplo en nuestro sistema:</strong> {info['ej']}</p>
                </div>
            """, unsafe_allow_html=True)

    # SECCIÓN 3: FLUJO ECO (Línea de proceso secuencial visualmente impactante)
    st.markdown('<div class="section-header">🔄 2. El Flujo Eco: ¿Cómo circulan las ideas y actividades?</div>', unsafe_allow_html=True)
    st.markdown("""<div class="glass-card">
<p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:20px;">Ciclo de Vida del Desarrollo Sustentable (Línea de Proceso):</p>
<div style="display: flex; flex-direction: column; gap: 12px;">
<div style="background: rgba(255,255,255,0.02); padding: 12px 18px; border-radius: 8px; border-left: 4px solid #64FFDA;">
<span style="color:#64FFDA; font-weight:bold; font-size:16px;">1. Residuo 📦</span><br>
<span style="font-size:14.5px; color:#E0E6ED;">El punto de partida del sistema son los materiales descartados, que se clasifican según su tipo para facilitar su tratamiento: Papel y cartón, Botellas PET, Latas y Residuos orgánicos.</span>
</div>
<div style="background: rgba(255,255,255,0.02); padding: 12px 18px; border-radius: 8px; border-left: 4px solid #00E676;">
<span style="color:#00E676; font-weight:bold; font-size:16px;">2. Transformación 🧪</span><br>
<span style="font-size:14.5px; color:#E0E6ED;">Los residuos son sometidos a distintos procesos según sus características, permitiendo su reutilización: Procesos físicos (corte, compactación, ensamblado), químicos (reacciones, tratamiento de materiales), biológicos (compostaje, descomposición) y tecnológicos (uso de dispositivos o sistemas diseñados).</span>
</div>
<div style="background: rgba(255,255,255,0.02); padding: 12px 18px; border-radius: 8px; border-left: 4px solid #B9F6CA;">
<span style="color:#B9F6CA; font-weight:bold; font-size:16px;">3. Producto 🛠️</span><br>
<span style="font-size:14.5px; color:#E0E6ED;">A partir de la transformación se obtienen nuevos elementos con valor funcional, educativo o experimental: Objetos funcionales, experimentos científicos, materiales reciclados y sistemas tecnológicos.</span>
</div>
<div style="background: rgba(255,255,255,0.02); padding: 12px 18px; border-radius: 8px; border-left: 4px solid #69F0AE;">
<span style="color:#69F0AE; font-weight:bold; font-size:16px;">4. Intercambio 🔄</span><br>
<span style="font-size:14.5px; color:#E0E6ED;">Los productos generados se integran en una dinámica de intercambio mediante el uso de la moneda interna del sistema, denominada <strong>EcoDollars</strong>, que incentiva la participación y el compromiso.</span>
</div>
<div style="background: rgba(255,255,255,0.02); padding: 12px 18px; border-radius: 8px; border-left: 4px solid #A5D6A7;">
<span style="color:#A5D6A7; font-weight:bold; font-size:16px;">5. Medición 📊</span><br>
<span style="font-size:14.5px; color:#E0E6ED;">Se registran datos clave para evaluar el impacto del sistema: Cantidad de residuos recuperados, productos generados y nivel de participación del público.</span>
</div>
<div style="background: rgba(255,255,255,0.02); padding: 12px 18px; border-radius: 8px; border-left: 4px solid #81C784;">
<span style="color:#81C784; font-weight:bold; font-size:16px;">6. Reinversión 🚀</span><br>
<span style="font-size:14.5px; color:#E0E6ED;">Los resultados obtenidos permiten mejorar y expandir el sistema: Optimización de procesos, desarrollo de nuevas fichas y ampliación del alcance del proyecto.</span>
</div>
</div>
</div>""", unsafe_allow_html=True)

    # SECCIÓN 4 & SECCIÓN 5: CONCEPTOS Y RELACIÓN DE FUNDAMENTOS
    col_con, col_rel = st.columns([6, 4])
    
    with col_con:
        st.markdown('<div class="section-header">🧪 3. Conceptos Eco: Marcos de Conocimiento</div>', unsafe_allow_html=True)
        st.markdown("""<div class="glass-card" style="height: 420px; overflow-y: auto;">
<p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:15px;">Filosofía y principios operativos reales del sistema:</p>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">Democratización del "Know-How":</span> El Manual Eco funciona como una franquicia social para que cualquier escuela pase de generar residuos a ser una planta de biotransformación.
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">Sistema de Código Abierto:</span> Innovación abierta con propiedad intelectual colectiva; cualquier institución con residuos básicos puede implementar el modelo.
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">Gamificación del Impacto:</span> Los EcoDollars transforman la ética ambiental en experiencia tangible: pasamos del "debería reciclar" al "me conviene reciclar".
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">Materia Prima como Activo:</span> El residuo no es un gasto, es un activo cuyo valor se define por su utilidad final y el esfuerzo técnico que requiere su transformación.
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">Protocolo de Error y Ajuste:</span> Las Fichas Eco son el resultado de un ciclo iterativo de ingeniería. No fabricamos productos improvisados; validamos prototipos.
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">La Cascada de Valor:</span> Aplicación de simbiótica industrial, donde el residuo o subproducto de una sección es el combustible crítico de la división siguiente.
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">De Espectador a Protagonista:</span> El alumno deja de ser un operario manual para convertirse en un tomador de decisiones estratégicas, con soberanía técnica y liderazgo.
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">El Problema de la "Buena Voluntad":</span> Sustituye la conciencia ambiental volátil por un mecanismo de participación constante forzado por el beneficio y la norma.
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">Combate al "Efecto Evento":</span> Evita la dilución del activismo escolar de corto plazo integrando los proyectos de forma orgánica en la currícula y la economía del colegio.
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">Transformación del Estudiante:</span> Formación de un egresado con perfil técnico-humanista, capaz de comprender sistemas complejos y dominar competencias del siglo XXI.
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">Ética de la Verdad (Anti-Greenwashing):</span> Transparencia y trazabilidad absoluta de los procesos mediante métricas reales. No trabajamos para la foto; transformamos con datos.
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">Capital Humano como Activo:</span> Multidisciplinariedad estratégica donde cada alumno actúa como un especialista asignado al proceso que mejor se alinea con sus habilidades.
</div>
<div class="info-item">
<span class="info-bullet">🧠</span><span class="info-tag">Eficiencia Operativa:</span> Medición del costo real incluyendo recursos invisibles (como agua y energía) para garantizar que el balance ambiental sea verdaderamente sustentable.
</div>
</div>""", unsafe_allow_html=True)
    with col_rel:
        st.markdown('<div class="section-header">🔗 4. Interacción del Sistema</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 380px; display: flex; flex-direction: column; justify-content: center;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:15px; text-align:center;">¿Cómo trabajan juntos los fundamentos?</p>
                <div style="background: rgba(0, 230, 118, 0.05); border: 1px dashed rgba(0, 230, 118, 0.3); padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 12px;">
                    <span style="color:#B9F6CA; font-weight:bold; font-size:16px;">1. LOS PILARES</span><br>
                    <span style="font-size:13.5px; color:#E0E6ED;">Establecen las <strong>reglas y características</strong> obligatorias del sistema.</span>
                </div>
                <div style="background: rgba(100, 255, 218, 0.05); border: 1px dashed rgba(100, 255, 218, 0.3); padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 12px;">
                    <span style="color:#64FFDA; font-weight:bold; font-size:16px;">2. EL FLUJO ECO</span><br>
                    <span style="font-size:13.5px; color:#E0E6ED;">Organiza el <strong>funcionamiento y ciclo de vida</strong> cronológico de las ideas.</span>
                </div>
                <div style="background: rgba(129, 199, 132, 0.05); border: 1px dashed rgba(129, 199, 132, 0.3); padding: 15px; border-radius: 10px; text-align: center;">
                    <span style="color:#81C784; font-weight:bold; font-size:16px;">3. LOS CONCEPTOS</span><br>
                    <span style="font-size:13.5px; color:#E0E6ED;">Justifica <strong>la existencia</strong> del flujo.</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Footer institucional 
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Arquitectura Metodológica del Ecosistema • E.E.S.T N°7
        </div>
    """, unsafe_allow_html=True)
# ==========================================
# PÁGINA 4 — CRONOLOGÍA ECO
# ==========================================
elif selected == "Cronología Eco":
    
    st.markdown('<div class="main-title">CRONOLOGÍA ECO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Evolución Histórica, Hitos de Ingeniería y Línea Temporal del Ecosistema</div>', unsafe_allow_html=True)
    
    # SECCIÓN 1: INTRODUCCIÓN
    st.markdown('<div class="section-header">⏳ ¿Por qué existe una cronología del proyecto?</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="font-size: 17px; line-height: 1.6; border-left: 5px solid #00E676;">
        Escribir la historia de <strong>Proyecto Eco</strong> es fundamental para validar su <strong>continuidad</strong> y mejora constante. El ecosistema actual no surgió de un día para el otro; es el resultado de un proceso de <strong>evolución</strong>, donde los errores previos se transformaron en una solución con el sistema del presente.
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 2: COMPARATIVA DE EVOLUCIÓN (Tabla Premium de Transformación estructural)
    st.markdown('<div class="section-header">📊 1. Cambios de EcoPapel 2025 a Eco</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="padding: 10px 20px 20px 20px;">
        <table class="custom-table">
            <thead>
                <tr>
                    <th style="width: 20%;">Aréa</th>
                    <th style="width: 40%; background: rgba(239, 83, 80, 0.2); color: #FFCDD2;">Fase Origen (2025): EcoPapel 2025</th>
                    <th style="width: 40%; background: rgba(76, 175, 80, 0.2); color: #C8E6C9;">Fase Actual (2026): Proyecto Eco</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Secciones Activas</strong></td>
                    <td>1 Sola división (Producción artesanal de papel).</td>
                    <td><span style="color:#00E676; font-weight:bold;">4 Divisiones</span> (EcoPapel, EcoLab, EcoTech, EcoIndustria).</td>
                </tr>
                <tr>
                    <td><strong>Estructura Técnica</strong></td>
                    <td>Actividades guiadas sueltas sin estandarizar.</td>
                    <td><span style="color:#00E676; font-weight:bold;">24 Fichas Técnicas</span> normalizadas con estructura.</td>
                </tr>
                <tr>
                    <td><strong>Gestión del equipo</strong></td>
                    <td>Participación voluntaria informal y dispersa.</td>
                    <td><span style="color:#00E676; font-weight:bold;">Sistema de Reconocidos</span> con auditoría y puntaje semanal.</td>
                </tr>
                <tr>
                    <td><strong>Infraestructura Digital</strong></td>
                    <td>Poca (Registros en formato papel/físico y Redes sociales).</td>
                    <td><span style="color:#00E676; font-weight:bold;">Alta</span> (EcoWeb, Modelado IA, Servidores de consulta).</td>
                </tr>
                <tr>
                    <td><strong>Impacto</strong></td>
                    <td>Bajo (Reciclaje de papel común).</td>
                    <td><span style="color:#00E676; font-weight:bold;">Alto</span> (Replicabilidad, Continuidad, etc.)</td>
                </tr>
            </tbody>
        </table>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 3 y SECCIÓN 4: ORIGEN VS TRANSFORMACIÓN (Columnas paralelas)
    col_orig, col_trans = st.columns(2)
    
    with col_orig:
        st.markdown('<div class="section-header">🌱 2. El Origen: EcoPapel 2025</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 330px;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:12px;">¿Que era EcoPapel 2025?:</p>
                <div class="info-item"><strong>Tiempo activo:</strong> Abril - Noviembre 2025.</div>
                <div class="info-item"><strong>Contexto y Problema:</strong> Se detectó un desperdicio masivo de hojas, carpetas y cartones en los cestos de la escuela técnica, sin ningún tratamiento de reciclado. Además, la conciencia del reciclaje era teórica más no práctica.</div>
                <div class="info-item"><strong>Objetivo Inicial:</strong> Recuperar esa celulosa escolar para fabricar hojas artesanales y concientizar con la práctica.</div>
                <div class="info-item"><strong>Características:</strong> Un grupo pequeño de alumnos experimentando con licuadoras caseras y bastidores de madera rústicos.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_trans:
        st.markdown('<div class="section-header">🔄 3. La Evolución a Eco</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 330px;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:12px;">¿Por qué dejamos de ser solo "EcoPapel"?</p>
                <div class="info-item"><span style="color:#FFD54F; font-weight:bold;">El Quiebre:</span> Al cerrar el ciclo lectivo 2025, se vio que si los alumnos clave se egresaban, las técnicas y conocimiento se perdían.</div>
                <div class="info-item"><span style="color:#00E676; font-weight:bold;">Mutación Sistémica:</span> Nace la necesidad imperiosa de crear los <strong>7 Pilares Eco</strong> (Continuo, Replicable, Medible...) que establezcan las reglas para que el proyecto trascienda a las personas.</div>
                <div class="info-item"><span style="color:#00E676; font-weight:bold;">Expansión de Fronteras:</span> Al crecer, decidimos expandirnos por otras aréas com la química, tecnología, etc. El residuo se volvió engranaje.</div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 5: LÍNEA TEMPORAL SECUENCIAL CRONOLÓGICA
    st.markdown('<div class="section-header">📅 4. Línea de Tiempo Histórica</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card">
        <div style="display: flex; flex-direction: column; gap: 15px;">
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #D4FFB2;">
                <span style="color:#D4FFB2; font-weight:bold;">1 de Abril del 2025 • Fundación de EcoPapel 🧪</span><br>
                <span style="font-size:14px; color:#E0E6ED;">Organización del grupo y compra de materiales.</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #C2FF9E;">
                <span style="color:#C2FF9E; font-weight:bold;">4 de Mayo del 2025 • Primer papel reciclado 📑</span><br>
                <span style="font-size:14px; color:#E0E6ED;">Primer papel reciclado hecho.</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #B0FF8A;">
                <span style="color:#B0FF8A; font-weight:bold;">14 de Agosto del 2025 • Presentación en la CUDI</span><br>
                <span style="font-size:14px; color:#E0E6ED;">Primera presentación del proyecto EcoPapel 2025 en la Universidad CUDI.</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #9EFF75;">
                <span style="color:#9EFF75; font-weight:bold;">16 de Agosto del 2025 • Primer video en las redes sociales </span><br>
                <span style="font-size:14px; color:#E0E6ED;">Creación de las redes sociales y el primer short subido.</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #8BFF61;">
                <span style="color:#8BFF61; font-weight:bold;">13 de Octubre del 2025 • Evaluación de Saberes</span><br>
                <span style="font-size:14px; color:#E0E6ED;">Primera evaluación del proyecto EcoPapel 2025.</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #79FF4D;">
                <span style="color:#79FF4D; font-weight:bold;">13 de Noviembre del 2025 • Presentación en la Técnica 7</span><br>
                <span style="font-size:14px; color:#E0E6ED;">Presentación del proyecto en E.E.S.T. N7</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #66FF38;">
                <span style="color:#66FF38; font-weight:bold;">4 de Marzo 2026 • Nacimiento de Eco</span><br>
                <span style="font-size:14px; color:#E0E6ED;">Nace formalmente el concepto y idea de "Proyecto Eco".</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #4DFF5E;">
                <span style="color:#4DFF5E; font-weight:bold;">4 de Marzo 2026 • Redacción de los 7 Pilares ⚖️</span><br>
                <span style="font-size:14px; color:#E0E6ED;">Se decretan los 7 pilares / reglas obligatorias del proyecto.</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #33FF85;">
                <span style="color:#33FF85; font-weight:bold;">15 de Abril • Creación y redacción de las 24 fichas</span><br>
                <span style="font-size:14px; color:#E0E6ED;">Se termina de redactar las 24 fichas.</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #1AFFAB;">
                <span style="color:#1AFFAB; font-weight:bold;">19 de Abril • Creación del Flujo Eco y Conceptos </span><br>
                <span style="font-size:14px; color:#E0E6ED;">Se crean el Flujo Eco y los Conceptos.</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #00FFD2;">
                <span style="color:#00FFD2; font-weight:bold;">24 de Abril 2026 • Finalización de la primera ficha</span><br>
                <span style="font-size:14px; color:#E0E6ED;">Se termina la primera ficha: Ficha N7: EcoIA (EcoTech).</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #00F7FF;">
                <span style="color:#00F7FF; font-weight:bold;">25 de Abril 2026 • Creación del sistema de reconocidos y informe semanal</span><br>
                <span style="font-size:14px; color:#E0E6ED;">La creación del sistema de reconocidos y el informe semanal para tener al equipo alineado y enfocado.</span>
            </div>
            <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #00D2FF;">
                <span style="color:#00D2FF; font-weight:bold;">1 de Junio 2026 • Primer cierre del sistema de reconocidos y informe mensual</span><br>
                <span style="font-size:14px; color:#E0E6ED;">Primer grupo de reconocidos y cierre de notas.</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

    # SECCIÓN 7 & SECCIÓN 8: SITUACIÓN ACTUAL VS PROYECCIÓN FUTURA
    st.markdown('<div class="section-header">🔮 7. Proyección futura</div>', unsafe_allow_html=True)
    st.markdown("""
            <div class="glass-card" style="height: 175px; border-left: 4px solid #64FFDA;">
                <p style="margin-top:0; color:#64FFDA; font-weight:600; margin-bottom:15px;">Hacia dónde se proyecta Eco:</p>
                <ul class="custom-list">
                    <li><strong>Nuevas Fichas:</strong> Añadir más fichas según necesidad, experiencia y tamaño del equipo.</li>
                    <li><strong>Replicación Institucional:</strong> Que el proyecto este presente en otras instituciones.</li>
                    <li><strong>Crecimiento y Evolución:</strong> Evolucionar tanto la parte de Fundamentos y Manualidades.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Footer institucional
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Registro Histórico y Memoria Técnica Evolutiva • E.E.S.T N°7
        </div>
    """, unsafe_allow_html=True)
# ==========================================
# PÁGINA 5 — MAPA ECO (REINTEGRADA)
# ==========================================
elif selected == "EcoGalaxy.":
    st.markdown('<div class="main-title">MAPA ECO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Mapeo de Celdas Operativas, Infraestructura Física e Integración de Laboratorios</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card" style="border-left: 5px solid #00E676; margin-bottom: 25px;">
            <p style="margin-top:0; color:#00E676; font-weight:600; font-size:16px;">🗺️ Distribución de la Infraestructura en la E.E.S.T N°7</p>
            Esta sección despliega la distribución espacial y logística del proyecto dentro de los talleres comunes y las áreas de contraturno de la institución, permitiendo auditar visualmente cómo interactúan las celdas entre sí de forma física.
        </div>
    """, unsafe_allow_html=True)
    
    # Contenedor interactivo/boceto para maquetar el mapa físico o el iframe
    st.markdown("""
        <div class="glass-card" style="text-align: center; padding: 50px; border: 1px dashed rgba(100, 255, 218, 0.3); background: rgba(100, 255, 218, 0.01);">
            <p style="font-size: 26px; color: #64FFDA; margin-bottom: 12px;">📐 Matriz del Plano General del Taller</p>
            <p style="color: #90A4AE; font-size: 14.5px; max-width:600px; margin: 0 auto; line-height:1.5;">
                Espacio reservado para renderizar el diagrama de distribución de celdas industriales (EcoPapel, EcoLab, EcoTech, EcoIndustria). Podés incrustar aquí un gráfico SVG interactivo, un mapa físico o imágenes de banco.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Footer institucional de la página
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Planta de Distribución y Flujos de Material • E.E.S.T N°7
        </div>
    """, unsafe_allow_html=True)
    
# ==========================================
# PÁGINA 6 — FICHAS TÉCNICAS
# ==========================================
elif selected == "Fichas Técnicas":
    
    st.markdown('<div class="main-title">FICHAS TÉCNICAS</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Biblioteca de Conocimiento Estandarizado y Protocolos de Ingeniería Sustentable</div>', unsafe_allow_html=True)
    
    # Diccionario Oficial de Fichas del Proyecto
    FICHAS = {
        "1": {"titulo": "Papel Seed", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1S5sREmBrapKftJM5z8iZjtj46rLXer0t/view?usp=sharing", "desc": "Papel artesanal biodegradable con semillas incorporadas."},
        "2": {"titulo": "FibroPapel", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1JV_LZ_25r-gyqP27gndXCKweqzovfaiN/view?usp=sharing", "desc": "Papel compuesto reforzado con fibras textiles de algodón."},
        "3": {"titulo": "Manual del Reciclador", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1icRZmLchhPNXkbqHRKe3rsGF2yQdsXHq/view?usp=sharing", "desc": "Libro educativo para replicar el proyecto."},
        "4": {"titulo": "Marca-Páginas", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1LVUYPIBTA6mY61HVtQn7f15ud1sw-3Rv/view?usp=sharing", "desc": "Souvenir funcional de celulosa (papel y cartón) recuperado."},
        "5": {"titulo": "Eco-Carrier", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1q2m3efrr3WPZtJ_a__8YZ6m42nK-3y31/view?usp=sharing", "desc": "Bolsas de papel que reemplazan el plástico."},
        "6": {"titulo": "Colorantes Naturales", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1EGy35MOOpkKR3-ksINjzhkurokfqwdWz/view?usp=sharing", "desc": "Extracción de pigmentos puros de residuos vegetales, flores y cáscaras."},
        "7": {"titulo": "EcoIA", "division": "EcoTech", "drive_url": "https://drive.google.com/file/d/1H0seDIImClVjA5UrHELyucapO9DzXrHH/view?usp=sharing", "desc": "Inteligencia Artificial cargada con los datos del proyecto para la replicabilidad."},
        "8": {"titulo": "Organizadores Ecomodulares", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1sJP_u9-UgqRWkXk3f3PsvUVzLCa93Uow/view?usp=sharing", "desc": "Sistemas de ordenamiento de escritorio mediante latas y tubos."},
        "9": {"titulo": "Eco-Estelar", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/15qlgSz3v6YOLmHTWVmubTMknKM0WVUNS/view?usp=sharing", "desc": "Lámparas decorativas perforadas mediante técnica avanzada de congelado."},
        "10": {"titulo": "EcoChallenge", "division": "Transversal", "drive_url": "https://drive.google.com/file/d/1n6C2rPadtw662DZfogxJagQrbVvhem90/view?usp=sharing", "desc": "Conjunto transversal de desafíos interactivos aplicable a todas las áreas."},
        "11": {"titulo": "Eco-Hidro", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1q5ImtWBOhHfztDthNQs1yPdmIiK3zZYJ/view?usp=sharing", "desc": "Maceta de riego autónomo por capilaridad optimizado en botellas PET."},
        "12": {"titulo": "EcoTrash", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1XdaHhW7Z5nzfBHBr3dj7I-N0HNQuLp8k/view?usp=sharing", "desc": "Escoba construida con cerdas de PET alineadas."},
        "13": {"titulo": "EcoWallet", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1xWXIx2TAa1QJU2izv0KwqhtEiZSo4GvW/view?usp=sharing", "desc": "Billetera mediante upcycling estructurado de Tetra Pak."},
        "14": {"titulo": "Carbon Ink", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1njzGFWQbRuRo-_ucORzZMYceuOE6uoOt/view?usp=sharing", "desc": "Tinta negra premium obtenida por pirólisis controlada de papel sucio."},
        "15": {"titulo": "Nendo Dango", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1NO2FaJdNvlYZA9X8PKMSUAZ8gXJ4PzG8/view?usp=sharing", "desc": "Bolas de arcilla, sustrato y semillas para reforestación."},
        "16": {"titulo": "EcoWear", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1tDOsmBio3hPoLzTVGfHzaauTz-wmhEtf/view?usp=sharing", "desc": "Cuentas estructurales y elementos decorativos de papel enrollado, metal recuperado y plástico."},
        "17": {"titulo": "Eco-Voz", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1xh5hOjk_HXqaMcFr431Od3z15norhe1q/view?usp=sharing", "desc": "Amplificador acústico pasivo diseñado en cartón corrugado."},
        "18": {"titulo": "Cañón Vortex", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1h8tS94N0edR9Tw7GU94dummpULnt32zi/view?usp=sharing", "desc": "Generador físico de anillos de aire para gamificación."},
        "19": {"titulo": "Eco-Dollars", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1xQSQpyuVH-YSgtjWZYahVeterC99rX70/view?usp=sharing", "desc": "Sistema monetario de economía circular impreso sobre papel reciclado propio."},
        "20": {"titulo": "EcoVolt", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1OmhWYiMxZvxMxHFRO7slATfgt_Brwhui/view?usp=sharing", "desc": "Generación teórica de energía limpia aprovechando el gradiente salino (agua dulce y salada)."},
        "21": {"titulo": "EcoCristales", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1jQwwWbwoUoq3xlcBYY5aVB1WoOieLQ30/view?usp=sharing", "desc": "Criación de Cristales con alumbre para collares."},
        "22": {"titulo": "Biogás", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1m4l9L2Y5sXrWz2KlmgfjfDii76ZwBtS6/view?usp=sharing", "desc": "Investigaciónsobre digestión anaeróbica y captura de metano."},
        "23": {"titulo": "EcoMod", "division": "EcoTech", "drive_url": "https://drive.google.com/file/d/13qfQNtrsH1iAjTEAck-LrFfluuHgZZGf/view?usp=sharing", "desc": "Transforma mecánicas de juego en procesos interactivos de reciclaje, producción sustentable y economía circular (EcoDollars) para un aprendizaje activo en Minecraft."},
        "24": {"titulo": "TerrarIA", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1P3r5UlcdPS4KWDcuYPN45qJWmD_KTBDu/view?usp=sharing", "desc": "Ecosistema cerrado automatizado y monitoreado por matrices de sensores."},
    }

    # SECCIÓN 1 & SECCIÓN 2: DEFINICIÓN Y APORTES OPERATIVOS
    col_def, col_por = st.columns(2)
    
    with col_def:
        st.markdown('<div class="section-header">📄 1. ¿Qué es una Ficha Técnica Eco?</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 330px;">
                <p style="margin-top:0; color:#00E676; font-weight:600; margin-bottom:15px;">Definición y Estandarización de Ingeniería:</p>
                Es un <strong>documento normalizado estricto</strong> que registra de manera exacta los datos, fórmulas, flujos y materiales requeridos para replicar y optimizar una actividad o recurso del sistema.
                <br><br>
                <span style="color:#FFD54F; font-weight:bold;">¿Que no es?:</span>
                <ul style="margin-top:5px; padding-left:20px; font-size:14px; color:#E0E6ED;">
                    <li><strong>No es un apunte:</strong> No contiene anotaciones informales o fragmentadas.</li>
                    <li><strong>No es un informe:</strong> No narra un suceso pasado; es una guía.</li>
                    <li><strong>No es una presentación:</strong> No resume ideas superficiales para exposición visual.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with col_por:
        st.markdown('<div class="section-header">🛡️ 2. ¿Por qué usamos Fichas Técnicas?</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 330px;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:15px;">Problemas de la educación tradicional que soluciona:</p>
                <div class="info-item"><span style="color:#64FFDA;">✦</span> <strong>Evitar la perdida de conocimiento:</strong> Evita la pérdida del conocimiento acumulado cuando los alumnos de último año egresan. El conocimiento queda grabado en documentos, no en personas.</div>
                <div class="info-item"><span style="color:#64FFDA;">✦</span> <strong>Evitar la dependencia:</strong> El proyecto ya no depende de un alumno o docente líder específico; la ficha empodera a cualquiera.</div>
                <div class="info-item"><span style="color:#64FFDA;">✦</span> <strong>Garantiza Continuidad:</strong> Permite retomar un desarrollo exactamente en el mismo punto donde se dejó el ciclo anterior.</div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 3: ESTRUCTURA OFICIAL (Desplegables de anatomía de una ficha)
    st.markdown('<div class="section-header">📐 3. Estructura de las Fichas</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A5D6A7; margin-bottom:12px;">Cada una de las 24 fichas del sistema se redacta bajo la misma estructura (con excepciones):</p>', unsafe_allow_html=True)
    
    with st.expander("🔍 Ver Campos Estructurales Obligatorios"):
        st.markdown("""
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; font-size: 14px;">
                <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:6px;"><strong>1. Concepto:</strong> El marco científico y teórico base que sustenta la actividad.</div>
                <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:6px;"><strong>2. Objetivo:</strong> Qué resultado medible y tangible busca alcanzar el prototipo.</div>
                <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:6px;"><strong>3. Materiales:</strong> Listado exacto, pesado y cubicado de insumos requeridos.</div>
                <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:6px;"><strong>4. Procedimiento:</strong> Algoritmo paso a paso detallado para la manufactura o ensayo.</div>
                <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:6px;"><strong>5. Actividad del Equipo:</strong> Rol y asignación de tareas específicas en el laboratorio.</div>
                <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:6px;"><strong>6. Criterios de Calidad:</strong> Tolerancias y puntos de control para validar el producto.</div>
                <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:6px;"><strong>7. Impacto Ambiental:</strong> Análisis de mitigación de huella de carbono o residuo.</div>
                <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:6px;"><strong>8. Datos Técnicos:</strong> Gráficas, constantes físicas o métricas obtenidas experimentalmente.</div>
                <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:6px;"><strong>9. Costo y Viabilidad:</strong> Presupuesto financiero desglosado de producción.</div>
                <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:6px;"><strong>10. Proyección Futura:</strong> Próximas líneas de optimización o automatización planeadas.</div>
                <div style="background:rgba(255,255,255,0.02); padding:10px; border-radius:6px;"><strong>11. Marco Ampliado:</strong> Enlaces a papers científicos o referencias externas.</div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 5 & SECCIÓN 6: RELACIÓN PILARES Y CICLO DE VIDA (Columnas paralelas)
    col_pil, col_cicl = st.columns([4, 6])
    
    with col_pil:
        st.markdown('<div class="section-header">⚖️ 4. Vinculación con los Pilares</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 340px;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:12px;">Cómo validan los 7 Pilares:</p>
                <div style="font-size:13.5px; line-height:1.5;">
                    • <strong>Replicable:</strong> Permiten reproducir el conocimiento en cualquier lugar.<br>
                    • <strong>Continuo:</strong> Transmiten la experiencia intacta entre generaciones.<br>
                    • <strong>Medible:</strong> Fijan y asientan datos duros y resultados auditables.<br>
                    • <strong>Experimental:</strong> Son la bitácora viva donde se asientan las mejoras de los fallos.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_cicl:
        st.markdown('<div class="section-header">🔄 5. Ciclo de Generación de Conocimiento</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="glass-card" style="height: 340px; display:flex; flex-direction:column; justify-content:center;">
            <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:15px; text-align:center;">
                Flujo Evolutivo de una Ficha:
            </p>
            <div style="display:flex; justify-content:space-between; align-items:center; text-align:center; font-size:12.5px;">
                <div style="background:rgba(255,255,255,0.03); padding:8px; border-radius:6px; width:15%;">
                    <strong>Idea</strong><br>
                    <span style="color:#64FFDA;">Pregunta inicial</span>
                </div>
                <div style="color:#00E676;">➔</div>
                <div style="background:rgba(255,255,255,0.03); padding:8px; border-radius:6px; width:16%;">
                    <strong>Investigación</strong><br>
                    <span style="color:#00E676;">Búsqueda y análisis</span>
                </div>
                <div style="color:#00E676;">➔</div>
                <div style="background:rgba(255,255,255,0.03); padding:8px; border-radius:6px; width:15%;">
                    <strong>Desarrollo</strong><br>
                    <span style="color:#B9F6CA;">Diseño / prueba</span>
                </div>
                <div style="color:#00E676;">➔</div>
                <div style="background:rgba(255,255,255,0.03); padding:8px; border-radius:6px; width:18%;">
                    <strong>Documentación</strong><br>
                    <span style="color:#69F0AE;">Ficha oficial</span>
                </div>
                <div style="color:#00E676;">➔</div>
                <div style="background:rgba(255,255,255,0.03); padding:8px; border-radius:6px; width:15%;">
                    <strong>Evolución</strong><br>
                    <span style="color:#A5D6A7;">Mejoras y versiones</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    # SECCIÓN 4 & SECCIÓN 7: BIBLIOTECA DE CONOCIMIENTO (La base interactiva con tus links)
    st.markdown('<div class="section-header">📚 6. Lista de Fichas</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A5D6A7; margin-bottom:15px;">Filtra y accede directamente a las fichas 2026 de forma segura en Google Drive:</p>', unsafe_allow_html=True)
    
    # Buscador por texto
    busqueda = st.text_input("🔍 Buscar ficha por nombre o palabra clave...", "").lower()
    
    # Pestañas de filtrado por divisiones oficiales
    tab_todas, tab_papel, tab_lab, tab_tech, tab_ind, tab_trans = st.tabs([
        "Todas las Fichas", "EcoPapel", "EcoLab", "EcoTech", "EcoIndustria", "Transversales"
    ])
    
    # Función para renderizar las tarjetas de fichas de manera hiper-limpia
    def renderizar_fichas(division_filtro=None):
        contador = 0
        for num, data in FICHAS.items():
            # Filtro por división
            if division_filtro and data["division"] != division_filtro:
                continue
            # Filtro por transversalidad
            if division_filtro == "Transversal" and data["division"] != "Transversal":
                continue
            # Filtro por barra de búsqueda
            if busqueda and (busqueda not in data["titulo"].lower() and busqueda not in data["desc"].lower()):
                continue
                
            contador += 1
            # Renderizado premium estilo glass
            st.markdown(f"""
                <div style="background: rgba(255, 255, 255, 0.02); border: 1px solid rgba(165, 214, 167, 0.15); border-radius: 12px; padding: 18px; margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span style="background: rgba(0, 230, 118, 0.15); color: #00E676; padding: 3px 8px; border-radius: 5px; font-size: 12px; font-weight: bold; text-transform: uppercase;">Ficha {num} • {data['division']}</span>
                        <h4 style="margin: 8px 0 4px 0; color: #FFFFFF; font-size:18px;">{data['titulo']}</h4>
                        <p style="margin: 0; color: #B0BEC5; font-size: 14px;">{data['desc']}</p>
                    </div>
                    <div>
                        <a href="{data['drive_url']}" target="_blank" style="text-decoration: none;">
                            <button style="background: rgba(46, 125, 50, 0.6); color: white; border: 1px solid #00E676; padding: 8px 16px; border-radius: 8px; cursor: pointer; font-weight: bold; transition: 0.3s;">
                                Open Drive ↗
                            </button>
                        </a>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
        if contador == 0:
            st.warning("No se encontraron fichas técnicas que coincidan con la búsqueda.")

    # Ejecución de la lógica en cada pestaña correspondiente
    with tab_todas:
        renderizar_fichas()
    with tab_papel:
        renderizar_fichas("EcoPapel")
    with tab_lab:
        renderizar_fichas("EcoLab")
    with tab_tech:
        renderizar_fichas("EcoTech")
    with tab_ind:
        renderizar_fichas("EcoIndustria")
    with tab_trans:
        renderizar_fichas("Transversal")

    # Footer institucional
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Repositorio Abierto de Propiedad Intelectual Comunitario • E.E.S.T N°7
        </div>
    """, unsafe_allow_html=True)
# ==========================================
# PÁGINA 7 — FILTRO Y EXPLORADOR DE FICHAS
# ==========================================
elif selected == "Explorador Eco":
    import random

    st.markdown('<div class="main-title">EXPLORADOR ECO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Motor de Búsqueda Avanzado, Métricas de Conocimiento y Rutas de Aprendizaje Guiadas</div>', unsafe_allow_html=True)

    # DICCIONARIO OPTIMIZADO CON METADATOS TÉCNICOS INTEGRADOS (2025 Y 2026)
    FICHAS_AVANZADAS = {
        # --- FICHAS PROYECTO ECO 2026 ---
        "1": {"titulo": "Papel Seed", "division": "EcoPapel 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1S5sREmBrapKftJM5z8iZjtj46rLXer0t/view?usp=sharing", "desc": "Papel artesanal biodegradable con semillas incorporadas.", "dificultad": "I", "pilar": "Sustentable", "estado": "En desarrollo", "siguiente": "2"},
        "2": {"titulo": "FibroPapel", "division": "EcoPapel 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1JV_LZ_25r-gyqP27gndXCKweqzovfaiN/view?usp=sharing", "desc": "Papel compuesto reforzado con fibras textiles de algodón.", "dificultad": "II", "pilar": "Circular", "estado": "En planeación", "siguiente": "5"},
        "3": {"titulo": "Manual del Reciclador", "division": "EcoPapel 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1icRZmLchhPNXkbqHRKe3rsGF2yQdsXHq/view?usp=sharing", "desc": "Documento técnico educativo 100% sustentable.", "dificultad": "I", "pilar": "Replicable", "estado": "En desarrollo", "siguiente": "10"},
        "4": {"titulo": "Marca-Páginas", "division": "EcoPapel 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1LVUYPIBTA6mY61HVtQn7f15ud1sw-3Rv/view?usp=sharing", "desc": "Souvenir funcional de cartón recuperado.", "dificultad": "I", "pilar": "Circular", "estado": "En planeación", "siguiente": "3"},
        "5": {"titulo": "Eco-Carrier", "division": "EcoPapel 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1q2m3efrr3WPZtJ_a__8YZ6m42nK-3y31/view?usp=sharing", "desc": "Bolsas estructurales que reemplazan el plástico de un solo uso.", "dificultad": "II", "pilar": "Circular", "estado": "En planeación", "siguiente": "13"},
        "6": {"titulo": "Colorantes Naturales", "division": "EcoLab 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1EGy35MOOpkKR3-ksINjzhkurokfqwdWz/view?usp=sharing", "desc": "Extracción de pigmentos puros de residuos vegetales.", "dificultad": "III", "pilar": "Experimental", "estado": "Terminado", "siguiente": "14"},
        "7": {"titulo": "EcoIA", "division": "EcoTech 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1H0seDIImClVjA5UrHELyucapO9DzXrHH/view?usp=sharing", "desc": "Asistente inteligente de documentación técnica y auditoría.", "dificultad": "IV", "pilar": "Replicable", "estado": "Terminado", "siguiente": "23"},
        "8": {"titulo": "Organizadores Ecomodulares", "division": "EcoIndustria 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1sJP_u9-UgqRWkXk3f3PsvUVzLCa93Uow/view?usp=sharing", "desc": "Sistemas de ordenamiento mediante latas y tubos.", "dificultad": "I", "pilar": "Circular", "estado": "En planeación", "siguiente": "9"},
        "9": {"titulo": "Eco-Estelar", "division": "EcoIndustria 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/15qlgSz3v6YOLmHTWVmubTMknKM0WVUNS/view?usp=sharing", "desc": "Lámparas decorativas perforadas mediante técnica avanzada de congelado.", "dificultad": "III", "pilar": "Circular", "estado": "En desarrollo", "siguiente": "17"},
        "10": {"titulo": "EcoChallenge", "division": "Transversal 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1n6C2rPadtw662DZfogxJagQrbVvhem90/view?usp=sharing", "desc": "Sistema transversal de desafíos interactivos inter-áreas.", "dificultad": "II", "pilar": "Circular", "estado": "En planeación", "siguiente": "19"},
        "11": {"titulo": "Eco-Hidro", "division": "EcoIndustria 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1q5ImtWBOhHfztDthNQs1yPdmIiK3zZYJ/view?usp=sharing", "desc": "Módulo de riego autónomo por capilaridad optimizado en botellas PET.", "dificultad": "II", "pilar": "Circular", "estado": "Terminado", "siguiente": "24"},
        "12": {"titulo": "EcoTrash", "division": "EcoIndustria 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1XdaHhW7Z5nzfBHBr3dj7I-N0HNQuLp8k/view?usp=sharing", "desc": "Escoba técnica de alta resistencia construida con cerdas de PET.", "dificultad": "II", "pilar": "Circular", "estado": "En planeación", "siguiente": "8"},
        "13": {"titulo": "EcoWallet", "division": "EcoIndustria 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1xWXIx2TAa1QJU2izv0KwqhtEiZSo4GvW/view?usp=sharing", "desc": "Billetera impermeable mediante upcycling estructurado de Tetra Pak.", "dificultad": "I", "pilar": "Circular", "estado": "En planeación", "siguiente": "4"},
        "14": {"titulo": "Carbon Ink", "division": "EcoLab 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1njzGFWQbRuRo-_ucORzZMYceuOE6uoOt/view?usp=sharing", "desc": "Tinta negra premium obtenida por pirólisis controlada.", "dificultad": "IV", "pilar": "Circular", "estado": "Terminado", "siguiente": "21"},
        "15": {"titulo": "Nendo Dango", "division": "EcoLab 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1NO2FaJdNvlYZA9X8PKMSUAZ8gXJ4PzG8/view?usp=sharing", "desc": "Bolas de arcilla, sustrato y semillas para reforestación guiada.", "dificultad": "I", "pilar": "Sustentable", "estado": "En planeación", "siguiente": "1"},
        "16": {"titulo": "EcoWear", "division": "EcoPapel 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1tDOsmBio3hPoLzTVGfHzaauTz-wmhEtf/view?usp=sharing", "desc": "Cuentas estructurales y elementos decorativos de papel enrollado.", "dificultad": "I", "pilar": "Circular", "estado": "En planeación", "siguiente": "13"},
        "17": {"titulo": "Eco-Voz", "division": "EcoIndustria 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1xh5hOjk_HXqaMcFr431Od3z15norhe1q/view?usp=sharing", "desc": "Amplificador acústico pasivo diseñado en cartón corrugado.", "dificultad": "II", "pilar": "Circular", "estado": "En planeación", "siguiente": "18"},
        "18": {"titulo": "Cañón Vortex", "division": "EcoIndustria 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1h8tS94N0edR9Tw7GU94dummpULnt32zi/view?usp=sharing", "desc": "Generador físico de anillos de aire para dinámica de fluidos.", "dificultad": "III", "pilar": "Experimental", "estado": "En planeación", "siguiente": "7"},
        "19": {"titulo": "Eco-Dollars", "division": "EcoPapel 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1xQSQpyuVH-YSgtjWZYahVeterC99rX70/view?usp=sharing", "desc": "Sistema monetario de economía circular impreso sobre papel reciclado.", "dificultad": "III", "pilar": "Medible", "estado": "En desarrollo", "siguiente": "23"},
        "20": {"titulo": "EcoVolt", "division": "EcoLab 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1OmhWYiMxZvxMxHFRO7slATfgt_Brwhui/view?usp=sharing", "desc": "Generación teórica de energía limpia aprovechando el gradiente salino.", "dificultad": "III", "pilar": "Experimental", "estado": "En planeación", "siguiente": "22"},
        "21": {"titulo": "EcoCristales", "division": "EcoLab 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1jQwwWbwoUoq3xlcBYY5aVB1WoOieLQ30/view?usp=sharing", "desc": "Cristalización de alumbre orientada al estudio de la geometría química.", "dificultad": "IV", "pilar": "Experimental", "estado": "En planeación", "siguiente": "20"},
        "22": {"titulo": "Biogás", "division": "EcoLab 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1m4l9L2Y5sXrWz2KlmgfjfDii76ZwBtS6/view?usp=sharing", "desc": "Investigación avanzada sobre digestión anaeróbica y captura de metano.", "dificultad": "III", "pilar": "Experimental", "estado": "En planeación", "siguiente": "24"},
        "23": {"titulo": "EcoMod", "division": "EcoTech 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/13qfQNtrsH1iAjTEAck-LrFfluuHgZZGf/view?usp=sharing", "desc": "Módulo interactivo de reciclaje y economía circular en entornos virtuales.", "dificultad": "IV", "pilar": "Continuo", "estado": "En desarrollo", "siguiente": "7"},
        "24": {"titulo": "TerrarIA", "division": "EcoLab 2026", "año": "2026", "drive_url": "https://drive.google.com/file/d/1P3r5UlcdPS4KWDcuYPN45qJWmD_KTBDu/view?usp=sharing", "desc": "Ecosistema cerrado automatizado y monitoreado por sensores.", "dificultad": "IV", "pilar": "Continuo", "estado": "En planeación", "siguiente": "11"},
        
        # --- FICHAS BASE PROYECTO ECOPAPEL 2025 ---
        "B1": {"titulo": "Ficha Base Papel Reciclado", "division": "EcoPapel 2025", "año": "2025", "drive_url": "#", "desc": "Papel artesanal reciclado de residuos escolares. Base fundamental del proyecto.", "dificultad": "III", "pilar": "Circular", "estado": "Terminado", "siguiente": "1"},
        "B2": {"titulo": "Ficha Base Cartón Reciclado", "division": "EcoPapel 2025", "año": "2025", "drive_url": "#", "desc": "Placas u hojas de alta rigidez para soportes y bases estructurales.", "dificultad": "III", "pilar": "Circular", "estado": "Terminado", "siguiente": "4"},
        "B3": {"titulo": "Ficha Base Colorantes Reciclados", "division": "EcoPapel 2025", "año": "2025", "drive_url": "#", "desc": "Extracción de pigmentos mediante solventes (alcohol). Etapa experimental.", "dificultad": "II", "pilar": "Experimental", "estado": "Terminado", "siguiente": "6"},
        "B4": {"titulo": "Ficha Base Cuaderno de papel reciclado", "division": "EcoPapel 2025", "año": "2025", "drive_url": "#", "desc": "Producto funcional con hojas recicladas y tapas de cartón recuperado.", "dificultad": "II", "pilar": "Circular", "estado": "Terminado", "siguiente": "3"},
        "B5": {"titulo": "Ficha Base Libretita de papel reciclado", "division": "EcoPapel 2025", "año": "2025", "drive_url": "#", "desc": "Libreta portátil de pequeño formato (19x9 cm) con figuras decorativas.", "dificultad": "I", "pilar": "Circular", "estado": "Terminado", "siguiente": "B4"},
        "B6": {"titulo": "Ficha Base Origamis de Papel", "division": "EcoPapel 2025", "año": "2025", "drive_url": "#", "desc": "Figuras artísticas mediante plegado de precisión (Pavo real, Escorpión, Loro).", "dificultad": "I", "pilar": "Circular", "estado": "Terminado", "siguiente": "16"},
        "B7": {"titulo": "Ficha Base Tecnijuego Reciclado", "division": "EcoPapel 2025", "año": "2025", "drive_url": "#", "desc": "Juego de mesa educativo para repaso de contenidos técnicos.", "dificultad": "III", "pilar": "Circular", "estado": "Terminado", "siguiente": "10"},
        }

    # SECCIÓN 1: INTRODUCCIÓN
    st.markdown('<div class="section-header">🔍 ¿Para qué sirve el Explorador Eco?</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="font-size: 16px; border-left: 5px solid #00E676;">
        Debido a que el volumen documental de <strong>Proyecto Eco</strong> cuenta con múltiples vertientes de ingeniería, esta central inteligente permite realizar consultas analíticas cruzadas. El usuario puede mapear y filtrar el conocimiento según el año de desarrollo, la división responsable, la complejidad de ejecución o el eje conceptual científico, garantizando que la información justa llegue al operador adecuado.
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 2: ESTADÍSTICAS GENERALES (Cálculos automáticos en base al diccionario)
    st.markdown('<div class="section-header">📈 1. Datos del Explorador Eco</div>', unsafe_allow_html=True)

    fichas_manuales     = 31  
    secciones_manuales  = 5   
    ejes_manuales       = 6   
    niveles_manuales    = 4   
    
    # Procesamiento de variables en background
    tot_fichas = len(FICHAS_AVANZADAS)
    secciones = set(f["division"] for f in FICHAS_AVANZADAS.values())
    conceptos = set(f["pilar"] for f in FICHAS_AVANZADAS.values())
    niveles = set(f["dificultad"] for f in FICHAS_AVANZADAS.values())
    
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:28px; font-weight:bold; color:#00E676;">{fichas_manuales}</span><br><span style="font-size:13px; color:#B0BEC5;">Fichas Totales</span></div>', unsafe_allow_html=True)
    with col_m2:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:28px; font-weight:bold; color:#64FFDA;">{secciones_manuales}</span><br><span style="font-size:13px; color:#B0BEC5;">Secciones totales por año</span></div>', unsafe_allow_html=True)
    with col_m3:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:28px; font-weight:bold; color:#FFD54F;">{ejes_manuales}</span><br><span style="font-size:13px; color:#B0BEC5;">Pilares en Fichas</span></div>', unsafe_allow_html=True)
    with col_m4:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:28px; font-weight:bold; color:#A5D6A7;">{niveles_manuales}</span><br><span style="font-size:13px; color:#B0BEC5;">Niveles Complejidad</span></div>', unsafe_allow_html=True)
    
    # SECCIÓN 3, 4 & 5: PANEL DE FILTROS CRUZADOS EN COLUMNAS (Añadido Filtro de Año)
    st.markdown('<div class="section-header">🎛️ 2. Panel de filtros para Fichas</div>', unsafe_allow_html=True)
    
    col_f1, col_f2, col_f3, col_f4 = st.columns(4)
    
    with col_f1:
        filtro_año = st.selectbox("📅 Año del Proyecto:", ["Todos", "2026", "2025"])
    with col_f2:
        filtro_sec = st.selectbox("📂 Filtrar por División:", ["Todas"] + sorted(list(secciones)))
    with col_f3:
        filtro_dif = st.selectbox("⚡ Filtrar por Dificultad:", ["Todas", "I", "II", "III", "IV"])
    with col_f4:
        filtro_con = st.selectbox("🔬 Filtrar por Pilar:", ["Todas"] + sorted(list(conceptos)))

    # SECCIÓN 6: RENDERIZADO DE FILTRADO EN MATRIZ DE TARJETAS PREMIUM
    st.markdown('<div class="section-header">📋 3. Fichas Técnicas Encontradas</div>', unsafe_allow_html=True)
    
    tarjetas_renderizadas = 0
    
    # Grid de ejecución lógica
    for k, f in FICHAS_AVANZADAS.items():
        # Lógica cruzada de discriminación de filtros (Se añade validación por año)
        if filtro_año != "Todos" and f["año"] != filtro_año:
            continue
        if filtro_sec != "Todas" and f["division"] != filtro_sec:
            continue
        if filtro_dif != "Todas" and f["dificultad"] != filtro_dif:
            continue
        if filtro_con != "Todas" and f["pilar"] != filtro_con:
            continue
            
        tarjetas_renderizadas += 1
        
        # Color del badge por dificultad
        color_dif = "#81C784" if f["dificultad"] == "I" else "#4CAF50" if f["dificultad"] == "II" else "#FFD54F" if f["dificultad"] == "III" else "#EF5350"
        # Color distintivo para el texto del Año de la ficha
        color_año = "#64FFDA" if f["año"] == "2026" else "#FFB74D"
        
        # Tarjeta HTML Premium
        st.markdown(f"""
            <div class="glass-card" style="margin-bottom: 15px; border-left: 5px solid {color_dif};">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;">
                    <div>
                        <span style="font-size: 12px; font-weight: bold; text-transform: uppercase; color: {color_año}; letter-spacing: 0.5px;">[{f['division']}] — Año {f['año']}</span>
                        <h3 style="margin: 3px 0; color: #FFFFFF; font-size: 19px;">Ficha N°{k}: {f['titulo']}</h3>
                    </div>
                    <div style="text-align: right;">
                        <span style="background: rgba(255,255,255,0.05); color: {color_dif}; border: 1px solid {color_dif}; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">{f['dificultad']}</span>
                        <br><span style="font-size: 11px; color: #90A4AE; display:block; margin-top:4px;">{f['estado']}</span>
                    </div>
                </div>
                <p style="margin: 0 0 12px 0; color: #CFD8DC; font-size: 14.5px; line-height:1.4;">{f['desc']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(0,0,0,0.15); padding: 8px 12px; border-radius: 6px;">
                    <span style="font-size: 13px; color: #A5D6A7;">Pilar Principal: <strong>{f['pilar']}</strong></span>
                    <a href="{f['drive_url']}" target="_blank" style="text-decoration: none; font-weight: bold; color: #00E676; font-size: 13px;">Ver Manual Técnico Completo ↗</a>
                </div>
            </div>
        """, unsafe_allow_html=True)

    if tarjetas_renderizadas == 0:
        st.info("Ninguna ficha técnica cumple simultáneamente con los criterios seleccionados en el panel.")

    # SECCIÓN 8: EXPLORACIÓN ALEATORIA (Botón dinámico interactivo con Session State)
    st.markdown('<div class="section-header">🎲 4. Descubrimiento de Fichas Aleatorias</div>', unsafe_allow_html=True)
    
    # Inicialización del Session State de Streamlit para retener la ficha al azar entre clicks de renderizado
    if "ficha_azar" not in st.session_state:
        st.session_state.ficha_azar = "1"
        
    col_b1, col_b2 = st.columns([3, 7])
    
    with col_b1:
        if st.button("🎰 Lanzar Ficha Aleatoria", use_container_width=True):
            st.session_state.ficha_azar = random.choice(list(FICHAS_AVANZADAS.keys()))
            
    with col_b2:
        fa = FICHAS_AVANZADAS[st.session_state.ficha_azar]
        st.markdown(f"""
            <div style="background: rgba(100, 255, 218, 0.04); border: 1px dashed #64FFDA; padding: 15px; border-radius: 10px;">
                <span style="color:#64FFDA; font-weight:bold; font-size:13px;">✨ FICHA RECOMENDADA POR EL ALGORITMO ECO:</span><br>
                <strong style="color:white; font-size:15px;">Ficha N°{st.session_state.ficha_azar}: {fa['titulo']}</strong> ({fa['division']}) — <span style="font-size:13px; color:#CFD8DC;">{fa['desc']}</span>
            </div>
        """, unsafe_allow_html=True)

    # Footer institucional
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Motor de Consultas Inteligente • E.E.S.T N°7
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# PÁGINA 9 — SISTEMA DE RECONOCIDOS
# ==========================================
elif selected == "Sistema Reconocidos":
    
    st.markdown('<div class="main-title">SISTEMA DE RECONOCIDOS</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Estructura de Incentivo Sociolaboral, Gestión Conductual y Auditoría de Compromiso</div>', unsafe_allow_html=True)

    # DATASET DE CONTROL DE RECONOCIDOS (Base de datos para analítica en tiempo real)
    RECONOCIDOS_DB = [
        {"nombre": "Jonathan Orellana", "division": "EcoIndustria", "periodo": "Abril 2025", "motivo": "Lider de EcoIndustria", "tipo": "Actual"},
        {"nombre": "Facundo Orellana", "division": "EcoPapel, EcoLab y EcoIndustria", "periodo": "Mayo 2026", "motivo": "Participante de EcoPapel, EcoLab y EcoIndustria", "tipo": "Actual"},
        {"nombre": "Titirico Franco", "division": "EcoPapel", "periodo": "Abril 2025", "motivo": "Lider de EcoPapel", "tipo": "Actual"},
        {"nombre": "Tobias Ponce Castaño", "division": "EcoLab", "periodo": "Abril 2025", "motivo": "Lider de EcoLab.", "tipo": "Actual"},
        {"nombre": "Octavio Vidal", "division": "EcoPapel", "periodo": "Mayo 2026", "motivo": "Participante de EcoPapel.", "tipo": "Actual"},
        {"nombre": "Taina Pral", "division": "EcoLab", "periodo": "Mayo 2026", "motivo": "Participante de EcoLab.", "tipo": "Actual"},
        {"nombre": "Romina Colque", "division": "EcoLab", "periodo": "Mayo 2026", "motivo": "Participante de EcoLab.", "tipo": "Actual"},
        {"nombre": "Julian Tejerina", "division": "EcoTech", "periodo": "Abril 2025", "motivo": "Participante de EcoTech.", "tipo": "Actual"},
        {"nombre": "Brandon Regueyra", "division": "2025", "periodo": "Abril 2025", "motivo": "Participante de EcoPapel 2025", "tipo": "Histórico", "anio": 2025},
    ]

    # SECCIÓN 1 & SECCIÓN 2: FILOSOFÍA DEL SISTEMA Y PROBLEMÁTICA
    col_fil, col_prob = st.columns(2)
    
    with col_fil:
        st.markdown('<div class="section-header">🛡️ 1. Filosofía del Sistema: Rompiendo Mitos</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 330px;">
                <p style="margin-top:0; color:#00E676; font-weight:600; margin-bottom:12px;">Principios fundamentales de convivencia técnica:</p>
                El Sistema de Reconocidos <strong>no es un concurso</strong>, una competencia ni un esquema de exclusión. Su diseño tiene un fin puramente profesional: <strong>hacer visible el trabajo constante</strong>.
                <br><br>
                <span style="color:#64FFDA; font-weight:bold;">Declaración de principios:</span>
                <ul style="margin-top:5px; padding-left:18px; font-size:13.5px; color:#E0E6ED; line-height:1.4;">
                    <li>No determina quién vale más o menos en los laboratorios.</li>
                    <li>No otorga privilegios de autoridad técnica.</li>
                    <li>Premia la regularidad, el orden de banco y la persistencia conductual.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with col_prob:
        st.markdown('<div class="section-header">⚠️ 2. La Necesidad: ¿Qué problemas resuelve?</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 330px;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:12px;">Desafíos escolares crónicos que este algoritmo mitiga:</p>
                <div class="info-item"><strong>Falta de Participación Sostenida:</strong> Evita que los alumnos arranquen con alta energía y abandonen el contraturno a mitad de año.</div>
                <div class="info-item"><strong>Invisibilidad de Contribuciones:</strong> Soluciona el clásico problema donde el trabajo minucioso queda opacado por perfiles puramente expositores.</div>
                <div class="info-item"><strong>Desmotivación por Falta de Seguimiento:</strong> Rompe la apatía escolar al registrar formalmente cada hito, validando el tiempo invertido por el operador.</div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 3 & SECCIÓN 4: FUNCIONAMIENTO GENERAL Y CRITERIOS OFICIALES
    st.markdown('<div class="section-header">⚙️ 3. Protocolo de Funcionamiento y Criterios de Evaluación</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A5D6A7; font-size:14px; margin-bottom:12px;">Mapeo claro y auditable del proceso de ponderación semanal:</p>', unsafe_allow_html=True)
    
    
    st.markdown("""
            <div class="glass-card" style="height: 330px;">
                <p style="margin-top:0; color:#A5D6A7; font-weight:600; margin-bottom:12px;">Criterios Técnicos Evaluados:</p>
                <span style="font-size:13px; color:#CFD8DC;">Solo se consideran variables documentadas:</span>
                <div style="margin-top:8px; display:flex; flex-direction:column; gap:8px; font-size:13px;">
                    <div style="background:rgba(0,230,118,0.05); padding:6px; border-radius:4px; border-left:3px solid #00E676;">🤝 <strong>Participación y presencia</strong></div>
                    <div style="background:rgba(0,230,118,0.05); padding:6px; border-radius:4px; border-left:3px solid #00E676;">⏱️ <strong>Responsabilidad</strong></div>
                    <div style="background:rgba(0,230,118,0.05); padding:6px; border-radius:4px; border-left:3px solid #00E676;">🧹 <strong>Calidad de trabajos</strong></div>
                    <div style="background:rgba(0,230,118,0.05); padding:6px; border-radius:4px; border-left:3px solid #00E676;">🔧 <strong>Cumplimiento de Fichas y Secciones</strong></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 7: ESTADÍSTICAS DEL SISTEMA (Procesadas dinámicamente)
    st.markdown('<div class="section-header">📈 4. Analítica de Alcance y Métricas del Sistema</div>', unsafe_allow_html=True)
    
    tot_otorgados = len(RECONOCIDOS_DB)
    unicos_alumnos = len(set(r["nombre"] for r in RECONOCIDOS_DB))
    por_seccion = {}
    for r in RECONOCIDOS_DB:
        por_seccion[r["division"]] = por_seccion.get(r["division"], 0) + 1

    col_s1, col_s2, col_s3 = st.columns(3)
    with col_s1:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:28px; font-weight:bold; color:#00E676;">{tot_otorgados}</span><br><span style="font-size:13px; color:#B0BEC5;">Menciones Otorgadas</span></div>', unsafe_allow_html=True)
    with col_s2:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:28px; font-weight:bold; color:#64FFDA;">{unicos_alumnos}</span><br><span style="font-size:13px; color:#B0BEC5;">Alumnos Únicos de 4° 4°</span></div>', unsafe_allow_html=True)
    with col_s3:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:28px; font-weight:bold; color:#FFD54F;">{len(por_seccion)}</span><br><span style="font-size:13px; color:#B0BEC5;">Divisiones Involucradas</span></div>', unsafe_allow_html=True)

    # SECCIÓN 5 & SECCIÓN 6: RECONOCIDOS ACTUALES E HISTORIAL INTERACTIVO
    st.markdown('<div class="section-header">🥇 5. Cuadro de Honor e Historial de Operadores</div>', unsafe_allow_html=True)
    
    tab_act, tab_hist = st.tabs(["⚡ Período Vigente (Mayo 2026)", "📜 Registro Histórico Acumulado"])
    
    with tab_act:
        for r in RECONOCIDOS_DB:
            if r["tipo"] == "Actual":
                st.markdown(f"""
                    <div style="background: rgba(0, 230, 118, 0.03); border: 1px solid #00E676; border-radius: 10px; padding: 15px; margin-bottom: 12px;">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <strong style="font-size:17px; color:white;">⭐ {r['nombre']}</strong>
                            <span style="background:#00E676; color:black; font-weight:bold; padding:2px 8px; border-radius:4px; font-size:11px; text-transform:uppercase;">{r['division']}</span>
                        </div>
                        <p style="margin:8px 0 0 0; color:#CFD8DC; font-size:14px; line-height:1.4;"><strong>Rol:</strong> {r['motivo']}</p>
                        <span style="font-size:11px; color:#90A4AE; display:block; margin-top:6px;">📆 Registro: {r['periodo']} • E.E.S.T N°7</span>
                    </div>
                """, unsafe_allow_html=True)
                
    with tab_hist:
        # Filtro interactivo de año para el historial
        anio_sel = st.radio("Filtrar historial por Ciclo Lectivo:", [2026, 2025], horizontal=True)
        
        for r in RECONOCIDOS_DB:
            if r["tipo"] == "Histórico" and r["anio"] == anio_sel:
                st.markdown(f"""
                    <div style="background: rgba(255,255,255,0.01); border: 1px solid rgba(255,255,255,0.08); border-radius: 10px; padding: 15px; margin-bottom: 12px;">
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <strong style="font-size:16px; color:#B0BEC5;">{r['nombre']}</strong>
                            <span style="background:rgba(255,255,255,0.08); color:#E0E6ED; padding:2px 8px; border-radius:4px; font-size:11px;">{r['division']}</span>
                        </div>
                        <p style="margin:6px 0 0 0; color:#90A4AE; font-size:13.5px;">{r['motivo']}</p>
                        <span style="font-size:11px; color:#607D8B; display:block; margin-top:4px;">📆 Historial: {r['periodo']}</span>
                    </div>
                """, unsafe_allow_html=True)

    # SECCIÓN 8: RELACIÓN CON LOS PILARES OFICIALES
    st.markdown('<div class="section-header">⚖️ 6. Blindaje de los Pilares Eco mediante la Gestión</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
        <p style="margin-top:0; color:#A5D6A7; font-weight:600; margin-bottom:12px;">Cómo impacta el sistema conductual en la matriz dogmática:</p>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:12px; font-size:13.5px;">
            <div style="background:rgba(0,0,0,0.15); padding:10px; border-radius:6px;">🧪 <strong>Continuo:</strong> Favorece la permanencia ininterrumpida de los alumnos evitando baches operativos.</div>
            <div style="background:rgba(0,0,0,0.15); padding:10px; border-radius:6px;">📊 <strong>Medible:</strong> Asienta un registro cuantitativo exacto del compromiso humano de la división.</div>
            <div style="background:rgba(0,0,0,0.15); padding:10px; border-radius:6px;">🏢 <strong>Interdisciplinar:</strong> Rompe fronteras unificando y valorando aportes de software, metalmecánica o química.</div>
            <div style="background:rgba(0,0,0,0.15); padding:10px; border-radius:6px;">📋 <strong>Replicable:</strong> Su lógica de control matricial puede exportarse intacta a cualquier otra institución técnica.</div>
        </div>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 9: PARTICIPAR Y SER RECONOCIDO (Orientado a nuevos integrantes)
    st.markdown('<div class="section-header">🚀 7. ¿Sos nuevo? Cómo integrarte al Engranaje Eco</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="border-left: 5px solid #64FFDA;">
            <p style="margin-top:0; color:#64FFDA; font-weight:600; margin-bottom:10px;">Guía de embarque para nuevos estudiantes y colaboradores:</p>
            <ol style="margin:0; padding-left:20px; font-size:14px; color:#E0E6ED; display:flex; flex-direction:column; gap:8px;">
                <li><strong>Elegí tu Celda:</strong> Acercate a cualquiera de las 4 divisiones según tu afinidad (Papel, Laboratorio, Software o Matricería).</li>
                <li><strong>Estudiá la Ficha:</strong> Solicitá al Jefe de Sección el manual técnico de la actividad asignada y cumplí los pasos de seguridad de banco.</li>
                <li><strong>Asentá tu Huella:</strong> Tus horas operativas de contraturno y el cuidado de las herramientas se registran de forma automática en la bitácora semanal.</li>
                <li><strong>Evolucioná el Sistema:</strong> Al proponer mejoras validadas para los protocolos existentes, sumás puntos directos para el próximo ciclo de Reconocidos.</li>
            </ol>
        </div>
    """, unsafe_allow_html=True)

    # Footer institucional
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Registro del Capital Humano y Convivencia Técnica • E.E.S.T N°7
        </div>
    """, unsafe_allow_html=True)
    
# ==========================================
# PÁGINA 10 — ¿CÓMO REPLICAR ECO?
# ==========================================
elif selected == "¿Cómo Replicar Eco?":
    
    st.markdown('<div class="main-title">¿CÓMO REPLICAR ECO?</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Guía de Despliegue, Adaptación Institucional y Transferencia de Conocimiento Abierto</div>', unsafe_allow_html=True)

    # SECCIÓN 1 & SECCIÓN 2: INTRODUCCIÓN A LA REPLICABILIDAD Y REQUISITOS INICIALES
    col_rep, col_req = st.columns(2)
    
    with col_rep:
        st.markdown('<div class="section-header">🌐 1. El Manifiesto de la Replicabilidad</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 290px;">
                <p style="margin-top:0; color:#00E676; font-weight:600; margin-bottom:12px;">Descentralización del Conocimiento Técnico:</p>
                Proyecto Eco no fue diseñado para ser un sistema hermético o exclusivo. Su verdadero éxito radica en su capacidad de ser adoptado por otras comunidades. 
                <br><br>
                La replicación puede ser <strong>parcial o completa</strong>: cada institución tiene la libertad de modificar, recortar o expandir las celdas de trabajo según su infraestructura. La replicabilidad es un pilar fundamental porque transforma un proyecto escolar en un <strong>estándar educativo de triple impacto</strong>.
            </div>
        """, unsafe_allow_html=True)
        
    with col_req:
        st.markdown('<div class="section-header">⚙️ 2. Requisitos Mínimos Operativos</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 290px;">
                <p style="margin-top:0; color:#64FFDA; font-weight:600; margin-bottom:12px;">Lo que realmente se necesita para encender el motor:</p>
                <div class="info-item">👥 <strong>Núcleo Humano:</strong> Un grupo de participantes con voluntad de trabajo colaborativo. No importa la cantidad inicial.</div>
                <div class="info-item">📐 <strong>Espacio Físico Mínimo:</strong> Un aula, banco de taller o laboratorio básico para la organización de materiales.</div>
                <div class="info-item">📋 <strong>Sistema de Asiento:</strong> Un entorno (físico o digital) para documentar de forma estricta los procesos y pasos.</div>
                <span style="font-size:12px; color:#FFD54F; font-weight:600; display:block; margin-top:8px;">⚠️ NOTA AUDITORÍA: No existen barreras económicas de entrada obligatorias; el sistema se financia con sus propios residuos estructurados.</span>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 10: RUTA DE IMPLEMENTACIÓN RECOMENDADA (Línea de progreso visual arriba)
    st.markdown('<div class="section-header">🗺️ 3. Ruta de Despliegue Recomendada (Paso a Paso)</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(100,255,218,0.1); padding: 20px; border-radius: 12px; margin-bottom: 25px;">
            <div style="display: flex; justify-content: space-between; position: relative; margin-bottom: 10px;">
                <div style="position: absolute; top: 15px; left: 5%; right: 5%; height: 2px; background: rgba(255,255,255,0.1); z-index: 1;"></div>
                <div style="text-align: center; width: 14%; z-index: 2;"><div style="width: 32px; height: 32px; background: #00E676; color: black; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 auto 5px auto;">1</div><span style="font-size: 11px; color:#CFD8DC;">Formar Equipo</span></div>
                <div style="text-align: center; width: 14%; z-index: 2;"><div style="width: 32px; height: 32px; background: #00E676; color: black; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 auto 5px auto;">2</div><span style="font-size: 11px; color:#CFD8DC;">Adoptar Pilares</span></div>
                <div style="text-align: center; width: 14%; z-index: 2;"><div style="width: 32px; height: 32px; background: #64FFDA; color: black; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 auto 5px auto;">3</div><span style="font-size: 11px; color:#CFD8DC;">Abrir Secciones</span></div>
                <div style="text-align: center; width: 14%; z-index: 2;"><div style="width: 32px; height: 32px; background: #64FFDA; color: black; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 auto 5px auto;">4</div><span style="font-size: 11px; color:#CFD8DC;">Bajar Fichas</span></div>
                <div style="text-align: center; width: 14%; z-index: 2;"><div style="width: 32px; height: 32px; background: #FFD54F; color: black; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 auto 5px auto;">5</div><span style="font-size: 11px; color:#CFD8DC;">Activar Reconocidos</span></div>
                <div style="text-align: center; width: 14%; z-index: 2;"><div style="width: 32px; height: 32px; background: #FFD54F; color: black; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 auto 5px auto;">6</div><span style="font-size: 11px; color:#CFD8DC;">Auditar Datos</span></div>
                <div style="text-align: center; width: 14%; z-index: 2;"><div style="width: 32px; height: 32px; background: #B9F6CA; color: black; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: bold; margin: 0 auto 5px auto;">7</div><span style="font-size: 11px; color:#CFD8DC;">Compartir</span></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 3: FORMACIÓN DEL EQUIPO
    st.markdown('<div class="section-header">👥 4. Gobierno del Equipo Inicial</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
        La escala humana es elástica. Un equipo Eco puede nacer con 3 personas o desplegarse sobre una división técnica completa como <strong>4° 4°</strong>. Lo crucial es evitar estructuras jerárquicas verticales rígidas y adoptar un modelo de <strong>responsabilidad distribuida por afinidad</strong>:
        <br><br>
        • <strong>Líderes de Sección (Jefes de Banco):</strong> Responsables del inventario, el orden físico y el cumplimiento de las normas de seguridad.<br>
        • <strong>Operadores Técnicos:</strong> Ejecutan los pasos de las fichas y asientan las desviaciones experimentales en las bitácoras.<br>
        • <strong>Comunidad Conectores:</strong> Vinculan los residuos generados en las aulas comunes con el flujo de entrada de los talleres.
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 4: APLICACIÓN DE LOS PILARES
    st.markdown('<div class="section-header">📐 5. Los 7 Pilares como ADN del Sistema</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
        <p style="margin-top:0; color:#A5D6A7; font-weight:600; margin-bottom:12px;">Para que una réplica sea oficialmente considerada "Sistema Eco", debe regirse por la matriz fundamental:</p>
        <table class="custom-table" style="font-size:13.5px;">
            <thead>
                <tr>
                    <th style="width: 20%;">Pilar</th>
                    <th style="width: 40%;">Función Teórica</th>
                    <th style="width: 40%;">Aplicación Práctica en la Réplica</th>
                </tr>
            </thead>
            <tbody>
                <tr><td><strong>Replicable</strong></td><td>Permitir la libre transferencia del modelo.</td><td>Usar formatos abiertos de software y documentación accesible.</td></tr>
                <tr><td><strong>Circular</strong></td><td>Eliminar el concepto de residuo final.</td><td>El descarte de un laboratorio alimenta la materia prima del otro.</td></tr>
                <tr><td><strong>Continuo</strong></td><td>Garantizar la supervivencia del proyecto.</td><td>Diseñar fichas simples que puedan retomar alumnos del ciclo entrante.</td></tr>
                <tr><td><strong>Sustentable</strong></td><td>Equilibrar el impacto ecológico y social.</td><td>Reutilizar materiales escolares locales sin depender de compras externas.</td></tr>
                <tr><td><strong>Experimental</strong></td><td>Validar la teoría mediante la práctica empírica.</td><td>Efectuar ensayos físicos repetibles registrando tolerancias de error.</td></tr>
                <tr><td><strong>Medible</strong></td><td>Cuantificar cada avance o retroceso.</td><td>Llevar indicadores numéricos rigurosos de fichas y participantes.</td></tr>
                <tr><td><strong>Interdisciplinario</strong></td><td>Fusionar diversas familias del saber.</td><td>Cruzar química orgánica, lógica de código e ingeniería de materiales.</td></tr>
            </tbody>
        </table>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 5: ORGANIZACIÓN POR SECCIONES
    st.markdown('<div class="section-header">🏢 6. Arquitectura Operativa Adaptable</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#CFD8DC; font-size:14px; margin-bottom:12px;">Estructura sugerida para modularizar las tareas dentro de la nueva institución:</p>', unsafe_allow_html=True)
    
    col_sec1, col_sec2, col_sec3 = st.columns(3)
    with col_sec1:
        st.markdown("""
            <div style="background:rgba(0, 230, 118, 0.02); border:1px solid rgba(0, 230, 118, 0.15); padding:15px; border-radius:8px; height:240px;">
                <h5 style="margin:0 0 8px 0; color:#00E676;">📚 Celda EcoPapel</h5>
                <p style="font-size:12.5px; color:#B0BEC5; margin:0; line-height:1.4;">
                <strong>Objetivo:</strong> Gestión de celulosa en desuso.<br><br>
                <strong>Función:</strong> Reciclar hojas de preceptoría, archivos muertos o cartón.<br><br>
                <strong>Actividad inicial:</strong> Producción artesanal de hojas con agregado de semillas (Papel Seed).
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col_sec2:
        st.markdown("""
            <div style="background:rgba(100, 255, 218, 0.02); border:1px solid rgba(100, 255, 218, 0.15); padding:15px; border-radius:8px; height:240px;">
                <h5 style="margin:0 0 8px 0; color:#64FFDA;">🧪 Celda EcoLab</h5>
                <p style="font-size:12.5px; color:#B0BEC5; margin:0; line-height:1.4;">
                <strong>Objetivo:</strong> Control químico y ensayos físicos.<br><br>
                <strong>Función:</strong> Certificar la viabilidad técnica y ambiental de los desarrollos.<br><br>
                <strong>Actividad inicial:</strong> Confinamiento térmico básico de biomasa para obtención de pigmentos estables.
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col_sec3:
        st.markdown("""
            <div style="background:rgba(255, 213, 79, 0.02); border:1px solid rgba(255, 213, 79, 0.15); padding:15px; border-radius:8px; height:240px;">
                <h5 style="margin:0 0 8px 0; color:#FFD54F;">💻 Celda EcoTech</h5>
                <p style="font-size:12.5px; color:#B0BEC5; margin:0; line-height:1.4;">
                <strong>Objetivo:</strong> Soporte lógico e informático.<br><br>
                <strong>Función:</strong> Visibilizar y automatizar los datos de la organización.<br><br>
                <strong>Actividad inicial:</strong> Construcción de repositorios locales o interfaces sencillas de carga de indicadores.
                </p>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 6 & SECCIÓN 7: FICHAS TÉCNICAS Y RECONOCIDOS EN REPLICACIÓN
    col_fich, col_reco = st.columns(2)
    
    with col_fich:
        st.markdown('<div class="section-header">📄 7. Gestión del Saber: Fichas Técnicas</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 290px;">
                <p style="margin-top:0; color:#A5D6A7; font-weight:600; margin-bottom:10px;">La anatomía del documento que blinda el proyecto:</p>
                Las fichas técnicas son los planos del conocimiento. Evitan que el saber dependa de la memoria de un alumno o docente. 
                <br><br>
                <strong style="color:white;">Estructura obligatoria para la réplica:</strong>
                <ul style="margin:5px 0 0 0; padding-left:18px; font-size:13px; color:#CFD8DC; line-height:1.4;">
                    <li><strong>Código único de control</strong> (Ej: ECO-SEC-001)</li>
                    <li><strong>Eje Científico Asociado</strong> (Concepto químico o físico)</li>
                    <li><strong>Protocolo de Seguridad de Taller</strong> (EPP requeridos)</li>
                    <li><strong>Guía paso a paso</strong> de manufactura o ensayo</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with col_reco:
        st.markdown('<div class="section-header">🥇 8. Dinámica Humana: Reconocidos</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 290px;">
                <p style="margin-top:0; color:#A5D6A7; font-weight:600; margin-bottom:10px;">Cómo estructurar el motor motivacional local:</p>
                Para sostener el interés, la réplica debe instalar el <strong>Sistema de Reconocidos</strong> bajo las siguientes directrices operativas:
                <br><br>
                • <strong>Cero Competencia:</strong> Jamás armar ránkings de puntajes que frustren al alumnado.<br>
                • <strong>Foco Conductual:</strong> Ponderar positivamente el mantenimiento limpio del espacio de trabajo y el orden de los bancos.<br>
                • <strong>Asiento en Bitácora:</strong> Registrar semanalmente quiénes cumplieron con hitos de fichas técnicas para darles visibilidad formal en el grupo.
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 8: USO DE HERRAMIENTAS DE APOYO
    st.markdown('<div class="section-header">🛠️ 9. Herramientas de Soporte Disponibles</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
        <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:12px;">Ecosistema tecnológico desarrollado listo para ser consultado por los nuevos equipos:</p>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:12px; font-size:13px;">
            <div style="background:rgba(0,0,0,0.2); padding:12px; border-radius:6px; border-left:3px solid #00E676;">
                <strong style="color:white;">Suite EcoWeb</strong><br>La plataforma interactiva donde se centralizan y exponen los indicadores de auditoría escolar.
            </div>
            <div style="background:rgba(0,0,0,0.2); padding:12px; border-radius:6px; border-left:3px solid #64FFDA;">
                <strong style="color:white;">Asistente EcoIA</strong><br>Ingeniería de prompts estructurada para guiar la redacción normalizada de nuevas fichas técnicas.
            </div>
            <div style="background:rgba(0,0,0,0.2); padding:12px; border-radius:6px; border-left:3px solid #FFD54F;">
                <strong style="color:white;">Manual Metodológico Eco</strong><br>El compendio doctrinario donde se explica la integración del Flujo Eco con los procesos industriales.
            </div>
        </div>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 9: ADAPTACIÓN LOCAL
    st.markdown('<div class="section-header">🌍 10. Principio de Flexibilidad de Contexto</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="border-left: 5px solid #FFD54F; background: rgba(255, 213, 79, 0.02);">
            <strong style="color:#FFD54F; font-size:15px;">⚠️ Recordatorio de Ingeniería Social:</strong><br>
            Replicar Proyecto Eco <strong>no es fotocopiar nuestro entorno</strong>. Si tu institución no cuenta con tubos de ensayo para la pirólisis de Carbon Ink, puede iniciar optimizando la celda de EcoPapel utilizando marcos de madera viejos y descarte de cartulinas. Se alienta la creación de nuevas fichas y la modificación adaptativa de herramientas, siempre y cuando se honren con rigurosidad matemática los <strong>7 pilares fundamentales</strong> que cuidan el espíritu del proyecto.
        </div>
    """, unsafe_allow_html=True)

    # Footer institucional
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Manual Abierto de Transferencia y Escalabilidad Institucional • E.E.S.T N°7
        </div>
    """, unsafe_allow_html=True)
# ==========================================
# PÁGINA 11 — GALERÍA ECO / MAPA
# ==========================================
elif selected == "Galería Eco":
    st.markdown('<div class="main-title">GALERÍA Y MAPA ECO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Registro Visual de Infraestructura y Evidencias Fotográficas de Laboratorio</div>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card" style="text-align: center; padding: 40px; border: 1px dashed rgba(0, 230, 118, 0.4);">
            <p style="font-size: 24px; color: #00E676; margin-bottom: 10px;">📸 Contenedor Multimedia Activo</p>
            <p style="color: #90A4AE; font-size: 15px;">Espacio reservado para el despliegue del mapeo interactivo de celdas y la galería fotográfica de la E.E.S.T N°7.</p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# PÁGINA 12 — PREGUNTAS FRECUENTES (FAQ)
# ==========================================
elif selected == "Preguntas Frecuentes":
    
    st.markdown('<div class="main-title">PREGUNTAS FRECUENTES</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Centro de Consulta Rápida y Respuestas Fundacionales del Ecosistema</div>', unsafe_allow_html=True)

    # SECCIÓN 1: INTRODUCCIÓN
    st.markdown('<div class="section-header">💡 ¿Para qué sirve esta sección?</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="margin-bottom: 25px;">
        Bienvenido al <strong>Portal Analítico de FAQs</strong>. Esta sección reúne y estructura de forma concisa las dudas y consultas más habituales que tanto visitantes, participantes técnicos, docentes como evaluadores externos suelen plantearse al auditar el <strong>Proyecto Eco</strong>. Nuestro objetivo es que encuentres respuestas directas sin necesidad de navegar exhaustivamente por los manuales técnicos complejos.
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">🔍 Consultas de Auditoría Metodológica</div>', unsafe_allow_html=True)

    # SECCIÓN 2: ¿QUÉ ES PROYECTO ECO?
    with st.expander("❓ 1. ¿Qué es Proyecto Eco y cuál es su objetivo principal?"):
        st.markdown("""
            <div style="padding: 10px; line-height: 1.6; font-size: 14.5px; color: #E0E6ED;">
                <strong>Proyecto Eco</strong> es una matriz de gestión sociolaboral y ambiental desarrollada por estudiantes de la <strong>E.E.S.T N°7</strong>. Su objetivo principal es transformar los desechos institucionales (celulosa y plásticos) en subproductos de alto valor utilitario para el colegio mediante un enfoque estrictamente <strong>interdisciplinario</strong> que fusiona programación, ingeniería de materiales y procesos químicos.
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 3: ¿QUÉ ES UNA FICHA TÉCNICA?
    with st.expander("❓ 2. ¿Qué es una Ficha Técnica y para qué sirve?"):
        st.markdown("""
            <div style="padding: 10px; line-height: 1.6; font-size: 14.5px; color: #E0E6ED;">
                Una <strong>Ficha Técnica</strong> es el plano de ingeniería del conocimiento dentro de Eco. Es un documento normalizado que detalla los elementos químicos, los Equipos de Protección Personal (EPP) y la guía paso a paso para ejecutar un experimento o manufactura. Su función crítica es blindar la <strong>replicabilidad</strong> y asegurar la continuidad de los laboratorios sin depender de la memoria de un operario o docente.
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 4: ¿QUÉ SON LOS PILARES ECO?
    with st.expander("❓ 3. ¿Qué son los Pilares Eco y cómo orientan el proyecto?"):
        st.markdown("""
            <div style="padding: 10px; line-height: 1.6; font-size: 14.5px; color: #E0E6ED;">
                Los Pilares Eco constituyen el marco constitucional del proyecto. Son 7 principios inviolables: <strong>Replicable, Circular, Continuo, Sustentable, Experimental, Medible e Interdisciplinario</strong>. Cualquier actividad, celda de trabajo o nueva ficha debe responder de forma afirmativa a estos pilares para integrarse oficialmente al sistema.
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 5: ¿QUÉ ES EL FLUJO ECO?
    with st.expander("❓ 4. ¿Qué es el Flujo Eco?"):
        st.markdown("""
            <div style="padding: 10px; line-height: 1.6; font-size: 14.5px; color: #E0E6ED;">
                Es el protocolo logístico estandarizado del proyecto. Define cómo ingresan los residuos de la escuela, cómo se distribuyen entre las diferentes celdas operativas (EcoPapel, EcoLab, EcoTech, EcoIndustria), y la secuencia metodológica bajo la cual un residuo se procesa, se valida químicamente y se asienta en la base documental digital.
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 6: ¿QUÉ ES UN RECONOCIDO?
    with st.expander("❓ 5. ¿Qué significa ser un Alumno Reconocido?"):
        st.markdown("""
            <div style="padding: 10px; line-height: 1.6; font-size: 14.5px; color: #E0E6ED;">
                Ser un <strong>Reconocido</strong> significa que la constancia, la responsabilidad de banco y el compromiso del estudiante han sido validados formalmente en la bitácora semanal. Es un sistema cerrado de incentivos sociolaborales diseñado para fomentar la permanencia de contraturno. <strong>No es un concurso</strong> ni persigue dinámicas competitivas; premia el esfuerzo silencioso y regular.
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 7: ¿QUÉ SON LOS ECODOLLARS?
    with st.expander("❓ 6. ¿Qué son los EcoDollars y cuál es su utilidad real?"):
        st.markdown("""
            <div style="padding: 10px; line-height: 1.6; font-size: 14.5px; color: #E0E6ED;">
                El <strong>EcoDollar</strong> es el vector simbólico de nuestra economía circular interna. Representa una unidad de valor acuñada sobre papel reciclado germinable (Papel Seed), utilizada de forma didáctica dentro de la estructura del proyecto para cuantificar el intercambio de recursos recuperados y balancear los aportes de materiales entre las diferentes divisiones técnicas.
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 8: ¿CÓMO PARTICIPAR EN PROYECTO ECO?
    with st.expander("❓ 7. ¿Cómo puede un nuevo estudiante o colaborador participar de Proyecto Eco?"):
        st.markdown("""
            <div style="padding: 10px; line-height: 1.6; font-size: 14.5px; color: #E0E6ED;">
                La integración al sistema se realiza de forma orgánica escogiendo una de nuestras secciones operativas según la afinidad técnica del participante. El nuevo colaborador asume la ejecución de fichas técnicas preexistentes en los talleres de contraturno, registra sus actividades colaborativas y sus contribuciones ingresan directamente al circuito del Sistema de Reconocidos.
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 9: ¿PUEDE REPLICARSE ECO?
    with st.expander("❓ 8. ¿Se puede aplicar e implementar el framework Eco en otras instituciones?"):
        st.markdown("""
            <div style="padding: 10px; line-height: 1.6; font-size: 14.5px; color: #E0E6ED;">
                <strong>Absolutamente sí.</strong> La replicabilidad es uno de nuestros pilares dogmáticos. El framework está pensado para que cualquier otra escuela técnica, comunidad vecinal o equipo de trabajo pueda descargar nuestras fichas analíticas, adaptar las secciones a su infraestructura local y desplegar el sistema sin barreras económicas iniciales, moldeándolo a su propio contexto.
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 10: ¿ECO SIGUE CRECIENDO?
    with st.expander("❓ 9. ¿Es Proyecto Eco una estructura terminada o sigue en evolución?"):
        st.markdown("""
            <div style="padding: 10px; line-height: 1.6; font-size: 14.5px; color: #E0E6ED;">
                Eco es un <strong>sistema vivo y en evolución constante</strong>. No se detiene con los resultados actuales. El proyecto continúa expandiendo de manera continua su base de conocimiento con nuevas fichas de ingeniería, optimizaciones algorítmicas en la suite EcoWeb, nuevas celdas de integración comunitaria y la renovación cíclica de participantes de las nuevas generaciones.
            </div>
        """, unsafe_allow_html=True)

    # Bloque Informativo Final de Soporte
    st.markdown("""
        <div class="glass-card" style="margin-top: 30px; border-left: 4px solid #64FFDA; background: rgba(100, 255, 218, 0.02);">
            <span style="font-weight: bold; color: #64FFDA;">ℹ️ ¿Tu duda técnica no está listada?</span><br>
            <span style="font-size: 13.5px; color: #CFD8DC;">Podés consultar de forma interactiva con nuestro asistente entrenado en la celda de control <strong>EcoIA</strong> o revisar el <strong>Manual Metodológico Completo</strong> impreso en los bancos de trabajo de la E.E.S.T N°7.</span>
        </div>
    """, unsafe_allow_html=True)

    # Footer institucional
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Consultas Frecuentes de la Comunidad y Jurados • E.E.S.T N°7
        </div>
    """, unsafe_allow_html=True)
    
# ==========================================
# PÁGINA 13 — ECOIA (REPARADA SIN NAMEERROR)
# ==========================================
elif selected == "EcoIA":
    st.markdown('<div class="main-title">ECOIA: NÚCLEO COGNITIVO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Modelado Lingüístico de Contraturno entrenado en Protocolos y Fichas Técnicas de Proyecto Eco</div>', unsafe_allow_html=True)

    # -----------------------------------------------------------------
    # 📜 BASE DE DATOS GLOBAL: EL DICCIONARIO VA ACÁ (FUERA DEL BOTÓN)
    # -----------------------------------------------------------------
    TEXTO_COMPLETO_FICHAS = {
        "1": """
        FICHA TÉCNICA #1: PAPEL SEED (Sección: EcoPapel)
        1. CONCEPTO: Papel artesanal biodegradable que contiene semillas en su interior. Cuando se entierra en tierra húmeda, el papel se descompone y las semillas germinan, dando flores o hortalizas.
        2. OBJETIVO: Reutilizar papel en desuso. Crear un producto ecológico y plantable. Demostrar el ciclo natural: residuo → papel → planta.
        3. MATERIALES: Papel reciclado (carpetas viejas, diarios, cartón) picado y remojado 24 hs (Ficha Base Papel Reciclado), semillas pequeñas (copetes, amapolas, lechuga o rúcula), agua, licuadora, batea o recipiente grande, bastidor con malla (mosquitero), tela de algodón y esponja.
        4. PROCEDIMIENTO: 
           Paso 1: Remojar el papel un buen tiempo.
           Paso 2: Licuar hasta obtener pulpa fina (sin grumos grandes).
           Paso 3: Colocar pulpa en batea con agua.
           Paso 4: Agregar semillas y mezclar suavemente (no licuar las semillas).
           Paso 5: Sumergir el bastidor y levantar formando una capa uniforme.
           Paso 6: Dejar escurrir.
           Paso 7: Volcar sobre tela de algodón.
           Paso 8: Presionar con esponja para quitar exceso de agua.
           Paso 9: Dejar secar en lugar ventilado.
        5. ACTIVIDAD PARA EL EQUIPO: Producir 25 hojas para la feria regional de octubre. Producir 5 hojas para la canasta del proyecto. Decorar algunas hojas (sellos naturales o relieve). Plantar 3 hojas en macetas como prueba de germinación.
        6. CRITERIO DE CALIDAD: Hoja resistente (no se rompe al manipular). Semillas visibles pero bien distribuidas. Secado completo (sin humedad interna). Espesor uniforme.
        7. IMPACTO AMBIENTAL: Reduce residuos de papel. Evita papel industrial nuevo. Producto 100% biodegradable. Promueve la plantación y educación ambiental.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Tiempo promedio de secado: __ horas. Porcentaje de germinación: __ %. Tiempo de brote: __ días. Cantidad de papel reutilizado por tanda: __ gramos.
        9. COSTO Y VIABILIDAD: Costo aproximado por hoja: $____. Materiales mayormente reciclados → costo bajo. Puede producirse en cantidad para venta o regalo.
        10. MEJORAS Y PROYECCIÓN FUTURA: Incorporar mezcla de semillas variadas. Añadir colorantes naturales.
        """,
        
        "2": """
        FICHA TÉCNICA #2: FIBROPAPEL (Sección: EcoPapel)
        1. CONCEPTO: Papel reciclado reforzado con fibras textiles (algodón), lo que lo hace más flexible y resistente que el papel común. Ideal para tapas, carpetas o empaques más pesados.
        2. OBJETIVO: Aumentar la resistencia del papel reciclado. Experimentar con refuerzo estructural natural. Comparar propiedades físicas entre papel normal y reforzado.
        3. MATERIALES: Papel blanco de oficina o carpeta (remojado 24 hs), retazos de tela 100% algodón (remeras viejas, sábanas), agua, cola vinílica diluida (1 parte cola, 1 parte agua), licuadora, bastidor con malla, tijeras, tablas de madera o superficie plana para prensado, peso (libros o ladrillos envueltos).
        4. PROCEDIMIENTO:
           Paso 1: Remojar el papel 24 horas.
           Paso 2: Cortar la tela en cuadraditos pequeños (2–3 mm).
           Paso 3: Licuar el papel hasta obtener pulpa fina.
           Paso 4: Agregar la tela y dar solo unos toques de licuadora (no pulverizar completamente).
           Paso 5: Añadir cola vinílica diluida y mezclar.
           Paso 6: Formar hoja más gruesa en el bastidor.
           Paso 7: Escurrir bien.
           Paso 8: Volcar sobre tela.
           Paso 9: Prensar entre tablas con peso durante 24–48 hs.
        5. ACTIVIDAD PARA EL EQUIPO: Fabricar mínimo 15 hojas de Fibropapel. Comparar resistencia con papel reciclado común (misma medida). Crear invitaciones o tapas para el Stand. Analizar efectos visuales según color de las fibras.
        6. CRITERIO DE CALIDAD: Hoja compacta y firme. Fibras bien distribuidas (no acumuladas en un sector). No debe desarmarse al doblar. Espesor uniforme.
        7. IMPACTO AMBIENTAL: Reutiliza textiles viejos (reduce residuos de ropa). Extiende la vida útil del papel reciclado. Alternativa ecológica a cartulinas industriales.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Peso máximo soportado antes de romperse: __ kg. Resistencia al doblez (cantidad de pliegues antes de marcarse): __. Espesor promedio: __ mm. Diferencia de resistencia vs papel común: __ %.
        9. COSTO Y VIABILIDAD: Costo por hoja: $____. Bajo costo si se reutilizan telas. Puede reemplazar tapas comerciales en proyectos escolares.
        10. MEJORAS Y PROYECCIÓN FUTURA: Probar otras fibras naturales (yute, hilo, lana). Crear versión ultra reforzada tipo cartón flexible.
        """,

        "3": """
        FICHA TÉCNICA #3: MANUAL ECO (Sección: EcoPapel)
        1. CONCEPTO: Libro educativo creado 100% por el equipo, que recopila investigación, datos científicos, experimentos y tutoriales del proyecto Eco. Funciona como guía técnica y herramienta educativa para presentar el proyecto como algo replicable y demostrar que no depende totalmente del equipo, sino de la idea y estructura.
        2. OBJETIVO: Organizar todo el conocimiento generado. Crear material para charlas educativas. Demostrar coherencia y profesionalismo del proyecto. Dejar registro permanente del trabajo realizado.
        3. MATERIALES: Tapas de Fibropapel (Ficha 2) o cartón reciclado reforzado, hojas internas del mejor papel reciclado disponible, hilo de algodón o hilo encerado, aguja gruesa, regla metálica, punzón o clavo fino para perforar, cola vinílica (opcional para refuerzo del lomo).
        4. PROCEDIMIENTO:
           Paso 1: Diseñar estructura del manual (índice, secciones, fichas, experimentos).
           Paso 2: Redactar contenidos claros y ordenados.
           Paso 3: Imprimir o escribir en hojas recicladas seleccionadas.
           Paso 4: Cortar y alinear todas las hojas al mismo tamaño.
           Paso 5: Perforar para encuadernación (costura simple o técnica japonesa).
           Paso 6: Coser cuidadosamente el lomo.
           Paso 7: Colocar tapas reforzadas.
           Paso 8: Revisar ortografía, estética y orden final.
        5. ACTIVIDAD PARA EL EQUIPO: Producir 1 manual oficial para los jueces y para uso en charlas educativas. Ensayar exposición usando el manual como apoyo visual.
        6. CRITERIO DE CALIDAD: Contenido claro y bien organizado. Información verificada y coherente. Encuadernación firme. Presentación prolija y profesional.
        7. IMPACTO AMBIENTAL: Utiliza materiales reciclados en su fabricación. Promueve educación ambiental. Multiplica el impacto del proyecto a través de la enseñanza.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Cantidad de páginas: __. Cantidad de fichas incluidas: __. Tiempo total de producción: __ Días / Semanas. Porcentaje de materiales reciclados utilizados: __ %.
        9. COSTO Y VIABILIDAD: Costo aproximado por manual: $____. ¿Mucho más económico que imprimir un libro industrial?: Si / No. ¿Reproducible para talleres o ventas educativas?: Si / No.
        10. MEJORAS Y PROYECCIÓN FUTURA: Versión digital en PDF. Edición ampliada con resultados nuevos. Manual para escuelas primarias adaptado por edad. Registro oficial del proyecto como material educativo.
        """,
        
        "4": """
        FICHA TÉCNICA #4: MARCAPÁGINAS (Sección: EcoPapel)
        1. CONCEPTO: Accesorio funcional y estético para libros, elaborado con materiales reciclados. Permite demostrar técnicas de diseño, reutilización creativa y terminaciones artesanales.
        2. OBJETIVO: Crear un producto pequeño, útil y atractivo. Aplicar técnicas decorativas sustentables. Generar interacción en el stand. Difundir el proyecto mediante obsequios ecológicos.
        3. MATERIALES: Base de cartón reciclado (cajas de cereales o zapatos), decoración con flores prensadas, recortes de revistas o sellos caseros, terminación con cordón de yute, hilo de algodón o tiras de tela sobrantes del Fibropapel, barniz casero (3 partes de plasticola + 1 parte de agua), tijeras, lija fina (opcional), perforadora o punzón.
        4. PROCEDIMIENTO:
           Paso 1: Cortar rectángulos de 5 cm x 15 cm.
           Paso 2: Lijar suavemente bordes si es necesario.
           Paso 3: Perforar a 1 cm del borde superior.
           Paso 4: Diseñar la superficie (flores, sellos o frases).
           Paso 5: Colocar hilo con nudo doble interno.
           Paso 6: Aplicar barniz protector y dejar secar 12 horas.
        5. ACTIVIDAD PARA EL EQUIPO: Producir mínimo 40 marca-páginas. Reservar 15 para entrega estratégica (difusión). Reservar 5 para la canasta del proyecto. Preparar mesa interactiva para personalización en el stand.
        6. CRITERIO DE CALIDAD: Base firme (no debe doblarse fácilmente). Barniz seco al tacto y uniforme. Hilo bien asegurado. Bordes prolijos.
        7. IMPACTO AMBIENTAL: Reutiliza cartón, papel y cordones descartados. Aprovecha sobrantes textiles. Reduce compra de productos industriales. Promueve consumo responsable.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Tiempo promedio de fabricación por unidad: __ minutos / horas. Costo por unidad (aproximado): $__. Cantidad de cartón reutilizado por tanda: __ gramos. Resistencia promedio (prueba de flexión): __ intentos antes de marcarse.
        9. COSTO Y VIABILIDAD: Bajo costo por unidad. Producción rápida y en cantidad. Ideal para venta solidaria o difusión masiva.
        10. MEJORAS Y PROYECCIÓN FUTURA: Edición especial con Papel Seed. Series temáticas (ambiental, frases científicas, botánicas). Marca-páginas con código QR de redes o página del proyecto. Versión laminada con cera natural.
        """,
        
        "5": """
        FICHA TÉCNICA #5: ECO-CARRIER (Sección: EcoPapel)
        1. CONCEPTO: Bolsa reutilizable fabricada con papel reciclado reforzado. Funciona como alternativa ecológica a las bolsas plásticas de un solo uso.
        2. OBJETIVO: Reducir el uso de plástico descartable. Demostrar que el papel reciclado puede tener función estructural. Aplicar técnicas de refuerzo y diseño funcional.
        3. MATERIALES: Hojas A4 recicladas o papel de diario, engrudo (1 taza harina + 1 taza agua, cocción suave), cartón reciclado para base, manijas (yute, tela trenzada o papel retorcido), pincel o espátula para aplicar engrudo, regla y lápiz.
        4. PROCEDIMIENTO:
           Paso 1: Unir hojas solapando 2 cm y pegar con engrudo.
           Paso 2: Formar cilindro y sellar el lateral.
           Paso 3: Doblar la base tipo envoltorio de regalo.
           Paso 4: Colocar refuerzo de cartón en la base interna.
           Paso 5: Marcar fuelle lateral de 3 cm.
           Paso 6: Reforzar borde superior doblando hacia adentro.
           Paso 7: Colocar manijas con nudos internos o refuerzo adicional.
           Paso 8: Dejar secar 24 horas.
        5. ACTIVIDAD PARA EL EQUIPO: Fabricar mínimo 25 Eco-Carriers. Realizar prueba de carga (mínimo 5 minutos por prueba). Registrar peso máximo soportado. Utilizarlas en el stand durante la feria.
        6. CRITERIO DE CALIDAD: Base firme y estable. Manijas resistentes y bien fijadas. Uniones completamente selladas. Bolsa equilibrada al sostener peso.
        7. IMPACTO AMBIENTAL: Reduce bolsas plásticas de un solo uso. Reutiliza papel descartado. Producto biodegradable si no contiene recubrimientos sintéticos. Promueve consumo responsable.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Peso máximo soportado: __ kg. Tiempo de resistencia con carga estática: __ minutos. Cantidad de papel reutilizado por unidad: __ gramos. Número promedio de reutilizaciones antes de deterioro: __.
        9. COSTO Y VIABILIDAD: Costo aproximado por unidad: $____. Materiales de bajo costo y accesibles. Posible producción en pequeña escala para eventos escolares o ecológicos.
        10. MEJORAS Y PROYECCIÓN FUTURA: Versión impermeabilizada con cera vegetal. Modelo reforzado para libros escolares. Diseño plegable. Impresión con tintas naturales y logo EcoPapel.
        """,
        
        "6": """
        FICHA TÉCNICA #6: ECO-CROMA (Sección: EcoLab)
        1. CONCEPTO: Extracción de pigmentos naturales a partir de residuos orgánicos para teñir papel reciclado de forma ecológica.
        2. OBJETIVO: Reemplazar tintes sintéticos por alternativas naturales. Investigar estabilidad y fijación del color. Aplicar principios básicos de química (pH y mordientes).
        3. MATERIALES: Residuos orgánicos según color deseado (Amarillo/Dorado: Cáscaras de cebolla o cúrcuma; Rojo/Rosado: Remolacha o cebolla morada; Verde: Espinaca, yerba mate o pasto; Marrón/Sepia: Café o té negro; Azul/Morado: Repollo colorado como indicador natural de pH), agua, olla, colador o filtro de tela, sal gruesa, vinagre, recipientes resistentes al calor y pulpa de papel reciclado lista para teñir.
        4. PROCEDIMIENTO:
           Paso 1: Hervir el material vegetal durante 30–40 minutos.
           Paso 2: Filtrar para eliminar restos sólidos.
           Paso 3: Agregar mordiente caliente (1 cucharada de sal gruesa y 1 cucharada de vinagre por taza de líquido).
           Paso 4: Mezclar el colorante con la pulpa reciclada.
           Paso 5: Formar hojas en bastidor.
           Paso 6: Secar a la sombra para evitar pérdida de intensidad.
        5. ACTIVIDAD PARA EL EQUIPO: Crear un muestrario cromático rotulado con nombre del pigmento. Realizar demostración de cambio de pH con repollo colorado. Reservar 2 colorantes distintos para la canasta. Preparar mesa interactiva de personalización.
        6. CRITERIO DE CALIDAD: Color uniforme en la hoja. No desprende pigmento en seco. Mantiene tono tras 48 horas. Sin restos sólidos visibles.
        7. IMPACTO AMBIENTAL: Aprovecha residuos orgánicos. Reduce uso de tintas químicas. Proceso biodegradable. Educación sobre química natural y sustentabilidad.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Tiempo de fijación completa: __ horas. Cambio de tono según pH (ácido / neutro / básico): __. Intensidad comparativa entre pigmentos: __. Duración estimada del color en exposición a luz: __ días.
        9. COSTO Y VIABILIDAD: Costo aproximado por color: $____. ¿Los mordientes funcionan?: Si / No.
        10. MEJORAS Y PROYECCIÓN FUTURA: Probar otros mordientes naturales (alumbre vegetal, sal marina). Crear paleta oficial EcoPapel. Desarrollar tintas naturales para estampado. Investigación sobre resistencia a luz solar prolongada.
        """,

        "7": """
        FICHA TÉCNICA #7: ECOIA (Sección: EcoTech)
        1. CONCEPTO: Asistente de inteligencia artificial oficial del proyecto. No es un chat genérico: funciona exclusivamente con la información técnica desarrollada por el equipo (fichas, procesos y fundamentos científicos) para transformar el contenido del proyecto en conocimiento interactivo.
        2. OBJETIVO: Integrar tecnología con sustentabilidad. Facilitar la comprensión del proyecto a visitantes y jurados. Convertir las fichas técnicas en una enciclopedia digital viva. Demostrar innovación dentro del stand.
        3. FUNCIÓN PRINCIPAL: Actuar como enciclopedia interactiva del proyecto. Explicar procesos técnicos (EcoPapel, EcoLab, EcoIndustria, EcoTech). Traducir conceptos científicos complejos a lenguaje claro. Responder preguntas en tiempo real durante la feria.
        4. DESARROLLO TÉCNICO: Base de conocimiento usando las fichas oficiales como fuente de verdad. Actualización previa a la feria. Interfaz web clara con caja de texto y cartel "Preguntarle a EcoIA". Diseño minimalista, profesional y coherente con EcoPapel. Estilo comunicativo técnico, claro y apasionado.
        5. PROCEDIMIENTO DE IMPLEMENTACIÓN:
           Paso 1: Revisar y estandarizar todas las fichas técnicas.
           Paso 2: Organizar la información en categorías claras.
           Paso 3: Integrar las fichas en la base de conocimiento digital.
           Paso 4: Probar funcionamiento con preguntas simuladas.
           Paso 5: Ajustar claridad y coherencia de respuestas.
           Paso 6: Verificar funcionamiento offline o con conexión estable.
        6. ACTIVIDAD PARA EL EQUIPO: Revisar todas las fichas antes de cargarlas. Probar EcoIA con al menos 20 preguntas posibles de jurado. Preparar 5 preguntas técnicas "difíciles" para demostrar profundidad. Ensayar demostración en vivo durante la exposición.
        7. CRITERIO DE CALIDAD: Respuestas coherentes y sin contradicciones. Capacidad de explicar nivel básico y avanzado. Tiempo de respuesta rápido. Interfaz clara y fácil de usar.
        8. IMPACTO EDUCATIVO Y TECNOLÓGICO: Democratiza el acceso a la información del proyecto. Une sustentabilidad con tecnología moderna. Motiva a otros estudiantes a explorar IA aplicada a proyectos ambientales.
        9. DATOS TÉCNICOS: Cantidad de fichas integradas: __. Cantidad de pruebas realizadas: __. Tiempo promedio de respuesta: __ segundos. Plataforma utilizada: __.
        10. PROYECCIÓN FUTURA: Versión ampliada para uso escolar. Integración con código QR en productos físicos. Base de datos expandida con nuevas investigaciones. Versión educativa abierta para otras escuelas.
        """,
        
        "8": """
        FICHA TÉCNICA #8: ORGANIZADORES ECOMODULARES (Sección: EcoIndustria)
        1. CONCEPTO: Sistema modular de escritorio fabricado con latas y tubos reutilizados. Las piezas pueden unirse o separarse según la necesidad del usuario mediante imanes o encastres, permitiendo múltiples configuraciones.
        2. OBJETIVO: Reutilizar residuos metálicos y cartón estructural. Diseñar un producto funcional y adaptable. Introducir el concepto de modularidad y diseño industrial sustentable. Demostrar reutilización con enfoque práctico.
        3. MATERIALES: Latas de conserva limpias (tomate, arvejas, atún), tubos de cartón grueso, cola vinílica o cinta bifaz resistente, pintura a la tiza o papel artesanal del proyecto, imanes pequeños (opcional), lija o lima metálica, barniz casero protector.
        4. PROCEDIMIENTO:
           Paso 1: Lavar y secar completamente las latas.
           Paso 2: Limar cuidadosamente bordes cortantes (paso obligatorio de seguridad).
           Paso 3: Pintar o forrar el exterior con papel artesanal.
           Paso 4: Instalar sistema modular (Opción A: Colocar imanes laterales alineados / Opción B: Crear base de cartón con encastres firmes).
           Paso 5: Aplicar capa protectora (barniz).
           Paso 6: Dejar secar completamente antes de usar.
        5. ACTIVIDAD PARA EL EQUIPO: Construir 2 sets de 5 módulos (3 latas + 2 tubos). Construir 1 set adicional para la canasta (4 módulos). Probar estabilidad en superficie con leve inclinación. Diseñar al menos 2 configuraciones distintas de armado.
        6. CRITERIO DE CALIDAD: Bordes completamente seguros. Pintura o forrado uniforme. Unión firme entre módulos. Estabilidad sin tambaleo en uso normal.
        7. IMPACTO AMBIENTAL: Reutiliza metal y cartón descartado. Extiende vida útil de envases. Reduce compra de organizadores plásticos. Promueve diseño industrial sustentable.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Peso máximo soportado por módulo: __ g. Fuerza necesaria para separar módulos con imanes: __. Estabilidad en inclinación de __ grados. Cantidad de residuos reutilizados por set: __ unidades.
        9. COSTO Y VIABILIDAD: Costo estimado por set: $____. Materiales de fácil acceso doméstico. Producto comercializable en ferias o tiendas ecológicas.
        10. MEJORAS Y PROYECCIÓN FUTURA: Sistema modular expandible tipo "grid". Versión con compartimentos internos ajustables. Edición temática EcoPapel. Incorporación de base antideslizante reciclada.
        """,

        "9": """
        FICHA TÉCNICA #9: ECOESTELAR (Sección: EcoIndustria)
        1. CONCEPTO: Faroles de mesa fabricados con latas reutilizadas. A través de perforado artístico, la luz proyecta patrones decorativos en paredes y superficies.
        2. OBJETIVO: Reutilizar envases metálicos grandes. Aplicar técnica estructural segura de perforado. Crear un producto decorativo funcional. Generar impacto visual en el stand.
        3. MATERIALES: Latas grandes (duraznos, puré de tomate, leche en polvo), clavos de distintos grosores, martillo, lija fina, recipiente con agua, congelador, plantillas de diseño, velas LED o sistema eléctrico recuperado de bajo consumo.
        4. PROCEDIMIENTO:
           Paso 1: Lavar y secar completamente la lata.
           Paso 2: Llenarla con agua y congelar hasta formar un bloque sólido (el hielo evita deformaciones al martillar).
           Paso 3: Colocar la plantilla sobre la lata congelada.
           Paso 4: Perforar siguiendo el diseño utilizando los clavos y el martillo.
           Paso 5: Dejar derretir el hielo y secar completamente.
           Paso 6: Limar interior y exterior para eliminar rebabas y bordes peligrosos.
           Paso 7: Pintar o dejar un acabado metálico natural.
           Paso 8: Colocar la luz LED en el interior.
        5. ACTIVIDAD PARA EL EQUIPO: Construir mínimo 3 diseños distintos. Probar proyección en ambiente oscuro. Comparar tamaño de perforaciones y efecto de luz. Ensayar explicación de la técnica del hielo.
        6. CRITERIO DE CALIDAD: Perforaciones alineadas con el diseño. Sin bordes cortantes internos ni externos. Estructura sin deformaciones. Luz bien distribuida y visible.
        7. IMPACTO AMBIENTAL: Reutiliza envases metálicos de descarte. Promueve uso de iluminación LED de bajo consumo. Reduce compra de lámparas decorativas industriales. Fomenta diseño sustentable.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Cantidad promedio de perforaciones por diseño: __. Tiempo de congelado necesario: __ horas. Intensidad de proyección según tamaño de orificio: __. Consumo energético de la luz LED: __ W.
        9. COSTO Y VIABILIDAD: Costo aproximado por unidad: $____. Materiales mayormente reciclados. Posible producto decorativo para venta artesanal.
        10. MEJORAS Y PROYECCIÓN FUTURA: Diseños temáticos (naturaleza, constelaciones, frases). Incorporar interruptor reciclado. Sistema desmontable para cambiar diseño interno. Versión colgante tipo farol exterior.
        """,
        
        "10": """
        FICHA TÉCNICA #10: ECOCHALLENGE (Sección: Transversal - Todas las secciones)
        1. CONCEPTO: Sistema de juegos y desafíos interactivos diseñados por las distintas áreas del Proyecto Eco, donde los participantes aplican conocimientos ambientales y técnicos para obtener recompensas dentro del sistema EcoDollars.
        2. OBJETIVO: Integrar todas las divisiones del proyecto en una experiencia común. Generar participación activa del público. Evaluar el aprendizaje de forma práctica. Incentivar el uso del sistema EcoDollars. Transformar la feria en una experiencia interactiva.
        3. MATERIALES: Material reciclado (papel, plástico, cartón), dispositivos digitales (celular, PC de EcoTech), elementos físicos (tableros, fichas, cartas), señalética y reglas impresas (EcoPapel), prototipos o dispositivos (EcoIndustria / EcoLab).
        4. PROCEDIMIENTO:
           Paso 1: Cada división diseña al menos un juego o desafío relacionado con su área (clasificación, procesos, energía, etc.).
           Paso 2: Definir reglas claras y tiempo de juego.
           Paso 3: Establecer una recompensa en EcoDollars.
           Paso 4: Probar el juego internamente antes de la feria (fase de testeo).
           Paso 5: En la feria, los visitantes participan y completan desafíos.
        5. ACTIVIDAD PARA EL EQUIPO: Diseñar un juego por división. Testear funcionamiento y dificultad. Ajustar reglas según resultados. Preparar materiales necesarios. Organizar dinámica de participación en la feria.
        6. CRITERIO DE CALIDAD: Reglas claras y fáciles de entender. Relación directa con el contenido del proyecto. Nivel de dificultad adecuado. Participación activa del jugador. Duración corta (ideal 1–3 minutos).
        7. IMPACTO AMBIENTAL / EDUCATIVO: Promueve aprendizaje activo. Refuerza conceptos de reciclaje y sustentabilidad. Aumenta el interés del público. Facilita la comprensión del sistema Eco.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Cantidad de participantes: __. Tiempo promedio por juego: __ min. Tasa de éxito: __ %. Juego más elegido: __. EcoDollars entregados: ____.
        9. COSTO Y VIABILIDAD: Bajo costo (uso de materiales reciclados). Alta adaptabilidad según recursos disponibles. Fácil implementación en feria.
        10. MEJORAS Y PROYECCIÓN FUTURA: Incorporar ranking o competencia entre participantes. Digitalizar algunos juegos (EcoTech). Crear sistema de niveles o misiones. Expandir a eventos escolares.
        11. MARCO AMPLIADO (FORMATO PARA IDEAS DE JUEGO): Requiere recopilar Nombre del juego, Área, Concepto (qué hace el jugador), Objetivo, Materiales, Reglas, Duración, Dificultad (Baja/Media/Alta), Relación con el proyecto y Sistema de recompensa (EcoDollars).
        """,

        "11": """
        FICHA TÉCNICA #11: ECOHIDRO (Sección: EcoIndustria)
        1. CONCEPTO: Sistema de riego autónomo construido con botella PET reutilizada. Funciona mediante el principio de capilaridad, donde una mecha de algodón transporta el agua desde un depósito inferior hacia la tierra, permitiendo que la planta se hidrate de forma constante sin riego manual frecuente.
        2. OBJETIVO: Reutilizar plástico PET con función útil. Aplicar un principio físico natural en un sistema práctico. Reducir consumo innecesario de agua. Demostrar autonomía en sistemas de riego doméstico.
        3. MATERIALES: Botella PET (500 ml o 1,5 L), cordón de algodón grueso o tira de tela absorbente, tierra abonada mezclada con arena o perlita, semilla o brote pequeño, clavo caliente o herramienta para perforar, pintura decorativa (opcional para la parte superior).
        4. PROCEDIMIENTO:
           Paso 1: Cortar la botella un poco arriba de la mitad.
           Paso 2: Perforar la tapa con un clavo caliente (con supervisión).
           Paso 3: Pasar el cordón por la tapa y realizar un nudo interno para asegurarlo.
           Paso 4: Colocar la parte superior invertida (forma de embudo) dentro de la base.
           Paso 5: Llenar el depósito inferior con agua.
           Paso 6: Agregar tierra asegurando que la mecha quede centrada y en contacto directo con el sustrato.
           Paso 7: Plantar la semilla o brote.
           Paso 8: Observar el funcionamiento y el nivel de agua durante varios días.
        5. ACTIVIDAD PARA EL EQUIPO: Armar mínimo 2 sistemas funcionales. Construir 1 sistema adicional para la canasta. Registrar cantidad de días sin riego manual. Comparar con una planta testigo sin sistema Eco-Hidro.
        6. CRITERIO DE CALIDAD: Nivel de agua visible en depósito. Tierra húmeda pero no encharcada. Mecha siempre en contacto con agua y sustrato. Planta saludable tras varios días.
        7. IMPACTO AMBIENTAL: Reutiliza plástico PET. Reduce desperdicio de agua. Promueve cultivo doméstico responsable. Fomenta educación ambiental aplicada.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Días promedio sin riego manual: __. Cantidad de agua consumida por semana: __ ml. Comparación de crecimiento vs maceta tradicional: __. Tiempo de absorción inicial de la mecha: __ minutos.
        9. COSTO Y VIABILIDAD: Costo estimado por unidad: $____. Materiales de fácil acceso doméstico. Reproducible como sistema de bajo costo para hogares.
        10. MEJORAS Y PROYECCIÓN FUTURA: Sistema más grande para huerta. Incorporación de indicador visual de nivel de agua. Versión decorativa oficial EcoPapel. Integración con Papel Seed para plantación directa.
        """,
        
        "12": """
        FICHA TÉCNICA #12: ECOTRASH (Sección: EcoIndustria)
        1. CONCEPTO: Escoba para exteriores construida a partir de tiras flexibles de botellas PET recicladas. El plástico, que normalmente termina como residuo contaminante, se transforma en cerdas resistentes capaces de soportar uso continuo.
        2. OBJETIVO: Reutilizar grandes cantidades de plástico PET. Demostrar que un material flexible puede convertirse en estructura funcional. Diseñar una herramienta doméstica completamente reciclada. Generar impacto visual y práctico en la feria.
        3. MATERIALES: 15 a 20 botellas PET del mismo tamaño, palo de escoba recuperado, alambre fino resistente, clavos pequeños, cúter y tijeras fuertes, marcador para guías de corte.
        4. PROCEDIMIENTO:
           Paso 1: Retirar la base y el cuello de la mayoría de las botellas.
           Paso 2: Cortar los cilindros resultantes en tiras verticales de aproximadamente 0,5 cm, sin llegar al extremo superior.
           Paso 3: Reservar una botella completa con pico para que funcione como el eje central.
           Paso 4: Insertar las botellas cortadas una dentro de otra hasta formar el bloque compacto de cerdas.
           Paso 5: Utilizar otra botella como funda exterior para compactar e inmovilizar la estructura.
           Paso 6: Ajustar firmemente con alambre atravesando todo el conjunto de botellas.
           Paso 7: Fijar el bloque de cerdas al palo de escoba utilizando clavos.
           Paso 8: Verificar la alineación y firmeza estructural antes de su uso.
        5. ACTIVIDAD PARA EL EQUIPO: Construir al menos 1 escoba completamente funcional. Fabricar 1 unidad adicional para la canasta. Probar el barrido en superficie con arena o tierra. Evaluar resistencia tras 10 minutos de uso continuo y registrar el desgaste.
        6. CRITERIO DE CALIDAD: Cerdas rectas y uniformes. Unión firme entre el bloque y el mango. No debe aflojarse ni desarmarse durante el uso. Buen desempeño en recolección de residuos pequeños.
        7. IMPACTO AMBIENTAL: Reutiliza gran volumen de plástico PET. Reduce compra de escobas industriales nuevas. Extiende la vida útil del plástico descartado. Promueve la reutilización estructural del plástico.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Cantidad total de botellas utilizadas: __. Tiempo de armado: __ minutos. Duración de prueba continua: __ minutos. Nivel de desgaste tras prueba: __. Superficie probada: ____.
        9. COSTO Y VIABILIDAD: Costo aproximado por unidad: $____. Materiales accesibles y recuperables. Posible producción comunitaria en talleres ecológicos.
        10. MEJORAS Y PROYECCIÓN FUTURA: Versión reforzada para uso más intensivo. Diseño desmontable para reemplazo de cerdas. Modelo compacto para interiores. Incorporación de etiqueta EcoPapel para venta o exposición.
        """,

        "13": """
        FICHA TÉCNICA #13: ECOWALLET (Sección: EcoIndustria)
        1. CONCEPTO: Billetera funcional fabricada a partir de envases de Tetra Pak reutilizados. A través del upcycling, un material compuesto —difícil de reciclar por sus capas de cartón, plástico y aluminio— se transforma en un objeto resistente, impermeable y de uso cotidiano, con estética vintage/industrial.
        2. OBJETIVO: Demostrar el potencial del upcycling en materiales complejos. Reducir descarte de envases multilaminados. Crear un producto útil, liviano y durable. Integrar diseño y conciencia ambiental en un objeto diario.
        3. MATERIALES: 1 envase Tetra Pak de 1 litro (lavado y completamente seco), tijeras resistentes, regla y marcador para guías de pliegue, sistema de cierre (velcro, botón recuperado o elástico), pegamento fuerte o silicona (opcional), decoración opcional con Fibropapel artesanal (Ficha 2) u otros recortes reutilizados.
        4. PROCEDIMIENTO:
           Paso 1: Desplegar y cortar las solapas superior e inferior hasta obtener un tubo rectangular limpio.
           Paso 2: Lavar cuidadosamente el interior con detergente y secar por completo.
           Paso 3: Aplanar el envase y marcar líneas de pliegue con regla.
           Paso 4: Doblar los laterales hacia adentro formando un fuelle tipo acordeón (“W”).
           Paso 5: Doblar el cuerpo por la mitad para definir el compartimento principal de billetes.
           Paso 6: Recortar una de las caras para generar la solapa de cierre.
           Paso 7: Colocar el sistema de cierre elegido (velcro, botón o elástico).
           Paso 8: Reforzar pliegues si es necesario y verificar la correcta apertura y cierre.
        5. ACTIVIDAD PARA EL EQUIPO: Fabricar mínimo 10 modelos funcionales y 2 para la canasta. Probar impermeabilidad colocando papel en su interior y simulando lluvia leve. Evaluar resistencia tras 1 semana de uso cotidiano. Comparar distintos sistemas de cierre. Preparar explicación sobre qué es el upcycling.
        6. CRITERIO DE CALIDAD: Pliegues firmes y simétricos. Sin olor residual interno. Cierre seguro y resistente. Material sin grietas en zonas de flexión. Capacidad adecuada para billetes y tarjetas.
        7. IMPACTO AMBIENTAL: Reutiliza envases multicapa difíciles de reciclar. Extiende la vida útil de materiales complejos. Promueve diseño consciente y economía circular. Reduce necesidad de comprar billeteras nuevas.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Tiempo de fabricación: __ minutos. Peso final: __ gramos. Capacidad máxima de billetes: __. Resultado de prueba de impermeabilidad: __. Días de uso continuo sin desgaste visible: ____.
        9. COSTO Y VIABILIDAD: Costo estimado por unidad: $____. Material base gratuito (residuo doméstico). Producción replicable en talleres escolares o comunitarios. Posible línea de productos eco con distintos diseños.
        10. MEJORAS Y PROYECCIÓN FUTURA: Versión con tarjeteros internos. Edición personalizada con estampado artesanal. Modelo minimalista tipo tarjetero slim. Producción en serie para venta solidaria o recaudación.
        """,
        
        "14": """
        FICHA TÉCNICA #14: CARBON INK (Sección: EcoLab)
        1. CONCEPTO: Producción de tinta negra artesanal a partir del carbono obtenido mediante la carbonización controlada de restos de papel no reciclables. El residuo vuelve a convertirse en recurso útil, ejemplificando un ciclo de economía circular aplicado.
        2. OBJETIVO: Revalorizar papel no apto para reciclaje tradicional. Comprender el proceso de carbonización. Fabricar un insumo funcional para el propio proyecto. Integrar ciencia y reutilización en un producto real.
        3. MATERIALES: Restos de papel sucio o recortes mínimos, recipiente metálico con tapa, fuente de calor controlada, mortero o recipiente resistente para moler, tela o colador fino, goma arábiga o plasticola transparente, agua destilada o hervida, pizca de sal.
        4. PROCEDIMIENTO:
           Paso 1: Carbonizar el papel en un recipiente metálico cerrado, bajo supervisión.
           Paso 2: Dejar enfriar completamente el contenedor.
           Paso 3: Moler mecánicamente el carbón obtenido hasta convertirlo en polvo ultrafino.
           Paso 4: Filtrar las partículas gruesas con tela o colador fino.
           Paso 5: Mezclar 2 partes de polvo de carbono con 1 parte de aglutinante (goma arábiga o plasticola).
           Paso 6: Agregar agua destilada gradualmente hasta lograr la consistencia líquida adecuada.
           Paso 7: Incorporar una pizca de sal como conservante para el almacenamiento.
           Paso 8: Envasar en un frasco hermético.
        5. ACTIVIDAD PARA EL EQUIPO: Elaborar al menos un frasco funcional de tinta. Probar aplicación con pincel y sello. Medir tiempo de secado. Comparar con tinta comercial y registrar observaciones.
        6. CRITERIO DE CALIDAD: Color negro uniforme. Textura homogénea sin grumos. Buena adherencia al papel reciclado. Secado adecuado sin desprendimiento del pigmento.
        7. IMPACTO AMBIENTAL: Reduce el descarte de papel contaminado. Extiende la vida útil del material. Promueve la fabricación de insumos ecológicos. Refuerza el concepto de economía circular.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Tiempo de carbonización: __. Cantidad de polvo obtenido: __ g. Tiempo de secado promedio: __ min. Estabilidad tras 7 días: __.
        9. COSTO Y VIABILIDAD: Costo estimado por frasco: $____. Materia prima gratuita. Proceso replicable con supervisión. Viable como demostración educativa.
        10. MEJORAS Y PROYECCIÓN FUTURA: Desarrollo de variantes con pigmentos naturales. Producción para uso interno del proyecto. Kit educativo EcoLab. Integración con sellos oficiales EcoPapel.
        """,

        "15": """
        FICHA TÉCNICA #15: NENDO DANGO (Sección: EcoLab)
        1. CONCEPTO: Técnica de siembra sin labranza en la que una mezcla de arcilla, tierra y pulpa de papel reciclado funciona como cápsula protectora para semillas. La bolita mantiene la semilla resguardada de depredadores y clima hostil hasta que la lluvia activa su germinación de forma natural.
        2. OBJETIVO: Promover la restauración ecológica en espacios degradados. Aplicar principios de agricultura natural. Integrar reciclaje y biodiversidad en una sola práctica. Crear un recurso educativo replicable.
        3. MATERIALES: Pulpa de papel reciclado húmeda, arcilla (greda), compost o tierra fértil tamizada, semillas resistentes o nativas, agua (si hace falta ajustar la textura de la mezcla).
        4. PROCEDIMIENTO:
           Paso 1: Mezclar homogéneamente 5 partes de arcilla, 3 partes de tierra y 1 parte de pulpa de papel reciclado.
           Paso 2: Amasar la mezcla hasta lograr una textura moldeable uniforme (tipo plastilina firme).
           Paso 3: Tomar una porción de masa y colocar de 2 a 3 semillas en el centro geométrico.
           Paso 4: Modelar con las manos formando bolitas de 2 a 3 cm de diámetro.
           Paso 5: Secar completamente a la sombra durante 24 a 48 horas para evitar agrietamientos.
           Paso 6: Guardar en un contenedor o lugar seco hasta el momento de su dispersión.
        5. ACTIVIDAD PARA EL EQUIPO: Producir mínimo 15 bombas funcionales y 4 para la canasta del proyecto. Realizar una prueba de germinación controlada en maceta. Documentar fotográficamente la evolución del proceso.
        6. CRITERIO DE CALIDAD: Bolitas compactas sin grietas profundas. Semillas bien protegidas y centradas en el interior. Secado completo antes de almacenar. Evitar que se desarmen al manipularlas en seco.
        7. IMPACTO AMBIENTAL: Fomenta la biodiversidad local mediante la reforestación. No requiere labranza mecánica ni maquinaria pesada. Utiliza materiales 100% naturales y reciclados. Aplicable en zonas urbanas e industriales degradadas.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Diámetro promedio real: __ cm. Tiempo de secado en clima local: __ h. Porcentaje de germinación obtenido: __ %. Comparación empírica: suelo directo __% vs. maceta controlada __%.
        9. COSTO Y VIABILIDAD: Costo estimado por 10 unidades: $__. Alta disponibilidad de materiales en el entorno. Nivel de dificultad de producción bajo-medio.
        10. MEJORAS Y PROYECCIÓN FUTURA: Organizar jornadas comunitarias de siembra. Integración con Papel Seed (Ficha 1). Desarrollar un kit educativo de restauración ecológica para escuelas o municipios.
        """,
        
        "16": """
        FICHA TÉCNICA #16: ECOWEAR (Sección: EcoIndustria / EcoPapel)
        1. CONCEPTO: Línea de accesorios sustentables (pulseras, collares, llaveros) elaborados a partir de residuos sólidos, donde cada producto está fabricado con un único tipo de material (papel, plástico o metal), permitiendo una transformación clara, trazable y específica según el proceso técnico aplicado.
        2. OBJETIVO: Reutilizar residuos sólidos urbanos. Desarrollar productos funcionales y estéticos. Demostrar distintos procesos de transformación según la materia prima. Integrar EcoPapel y EcoIndustria. Generar productos intercambiables en el sistema EcoDollars.
        3. MATERIALES: Línea Papel (Papel reciclado, pegamento, barniz casero de plasticola y agua, palillos); Línea Plástico (Botellas PET limpias, tijeras, lija fina, fuente de calor controlada para termoconformado); Línea Metal (Anillas de latas, alambre fino reciclado, pinza o alicate); Generales (Hilo de algodón, elástico o tanza, tijeras y aguja).
        4. PROCEDIMIENTO:
           Paso 1 (Línea Papel / Paper Beads): Cortar tiras de papel, enrollar firmemente sobre un palillo formando cuentas (beads), aplicar pegamento de fijación, barnizar y dejar secar.
           Paso 2 (Línea Plástico): Seleccionar botellas PET por tipo/grosor evitando mezclas de polímeros. Cortar tiras o placas uniformes con control de ancho. Aplicar termoconformado controlado (aire o superficie caliente sin quemar) para generar curvaturas o rigidez. Perforar con herramienta caliente o broca fina y lijar bordes cortantes.
           Paso 3 (Línea Metal): Seleccionar anillas metálicas homogéneas libres de rebabas. Diseñar un patrón estructural basado en repetición y simetría. Unir mediante torsión controlada de alambre o enganche mecánico tipo cadena. Ajustar con pinza y realizar test de tracción manual.
           Paso 4 (Ensamblado final): Seleccionar una única línea de material (sin mezclar polímeros, metales o celulosa), enhebrar las piezas en el hilo o elástico ajustando el tamaño y cerrar con un nudo firme de seguridad.
        5. ACTIVIDAD PARA EL EQUIPO: Diseñar las 3 líneas de accesorios (papel, plástico, metal) y producir mínimo 15 unidades por línea. Realizar pruebas de resistencia bajo uso cotidiano. Definir el valor en EcoDollars según la complejidad técnica y exhibir en el stand de forma clasificada.
        6. CRITERIO DE CALIDAD: Estructura firme que no se desarme con el uso. Bordes completamente seguros y redondeados sin aristas cortantes. Terminación prolija, comodidad de uso y coherencia estética en la línea.
        7. IMPACTO AMBIENTAL: Reutiliza de forma directa residuos sólidos de descarte. Reduce la demanda de accesorios industriales nuevos. Promueve el ecodiseño y extiende el ciclo de vida de la celulosa, el plástico PET y los metales.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Tiempo de producción por unidad: __ minutos. Resistencia promedio (uso continuo): __ días. Cantidad de material reutilizado por unidad: __ gramos. Línea más resistente: __. Línea más elegida por usuarios: __.
        9. COSTO Y VIABILIDAD: Costo aproximado por unidad: $____ (costo operativo mínimo por uso de descartes). Producción altamente escalable en cantidad. Alta viabilidad de intercambio o venta.
        10. MEJORAS Y PROYECCIÓN FUTURA: Incorporar colecciones temáticas. Añadir sistema de trazabilidad digital con códigos QR. Desarrollar packaging sustentable propio con EcoPapel. Expandir la línea a aros o llaveros complejos.
        """,

        "19": """
        FICHA TÉCNICA #19: ECODOLLARS (Sección: EcoPapel - Transversal)
        1. CONCEPTO: Sistema de moneda interna del stand que permite intercambiar productos y servicios mediante una economía cerrada basada en el reciclaje y la producción propia. El EcoDollar (ED) representa el valor generado a partir de los residuos y el trabajo del equipo.
        2. OBJETIVO: Organizar ventas sin depender exclusivamente de dinero en efectivo. Incentivar que los visitantes traigan residuos reciclables al stand. Demostrar la economía circular aplicada en tiempo real. Enseñar de manera práctica que el reciclaje genera valor económico real y tangible.
        3. MATERIALES: 
           - Billetes: Papel reciclado del proyecto (Ficha Base Papel Reciclado), sello oficial con logo, tinta Carbon Ink (Ficha #14) y marcador para numeración manual.
           - Monedas: Pulpa de papel prensada, moldes circulares (tapas plásticas) y sello del proyecto.
           - Gestión: Cuaderno de registro contable, caja separada para la recepción de residuos, y caja física de Tesorería.
        4. PROCEDIMIENTO:
           - Fase de Fabricación:
             Paso 1: Cortar las hojas de papel artesanal en formato billete del mismo tamaño.
             Paso 2: Estampar el sello oficial con el logo del proyecto y el valor correspondiente.
             Paso 3: Numerar manualmente cada billete para control de seguridad.
             Paso 4: Registrar en el cuaderno la cantidad total de unidades fabricadas.
             Paso 5: Moldear las monedas utilizando pulpa de papel prensada en los moldes.
             Paso 6: Dejar secar un mínimo de 48 horas antes de su puesta en circulación.
           - Fase de Gestión en Feria:
             Paso 1: Cambiar dinero en efectivo o residuos clasificados de los visitantes por EcoDollars.
             Paso 2: Verificar minuciosamente la limpieza y estado de los residuos entregados.
             Paso 3: Registrar cada movimiento de entrada y salida en el cuaderno contable.
             Paso 4: Queda prohibido emitir o entregar EcoDollars sin su debida anotación previa.
        5. ACTIVIDAD PARA EL EQUIPO: Producir una serie inicial estrictamente controlada de ED. Designar un responsable fijo para la Tesorería del stand. Simular 10 transacciones completas antes de la feria. Verificar de forma exhaustiva la coherencia entre los precios de los productos y los valores emitidos.
        6. CRITERIO DE CALIDAD: Billetes resistentes y leyendas completamente legibles. Monedas firmes que no se desgranen ni se rompan al tacto. Numeración analógica clara y sin duplicados de serie. Registro contable perfectamente ordenado y balanceado.
        7. IMPACTO AMBIENTAL: Incentiva de forma directa la entrega de residuos reciclables en la comunidad escolar. Refuerza la economía circular con un enfoque educativo y lúdico. Integra todas las fichas productivas y secciones en un sistema de intercambio común.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Cantidad total de ED emitidos: __. Cantidad de ED en circulación al final de la jornada: __. Masa total de residuos recolectados (kg o unidades): __. Producto o servicio más vendido del stand: __.
        9. COSTO Y VIABILIDAD: Costo de producción por unidad de ED: $__. Relación de ingreso real en pesos vs. ED emitidos: __. Sistema sostenible y escalable para futuras ferias: Sí / No.
        10. MEJORAS Y PROYECCIÓN FUTURA: Desarrollo de una versión digital (transacciones mediante códigos QR o app básica). Integración analítica con el sistema EcoIA. Implementación como sistema de incentivos permanente en eventos escolares. Publicación de los resultados económicos como un caso de estudio real de economía circular.
        11. MARCO AMPLIADO:
            I. VALOR Y CONVERSIONES: Tipo de cambio fijado en 1 ED = 500 Pesos Argentinos ($ ARS). Válido para el intercambio de servicios (pruebas, asesorías, consultas) y productos físicos (EcoCroma, EcoLámparas, EcoTrash, etc.).
            II. ESTRATEGIA DE CIERRE (LOGÍSTICA Y POLÍTICA): Política estricta de "Sin Reembolsos" para mantener la estabilidad de la economía cerrada del proyecto (los EcoDollars no se vuelven a cambiar por pesos argentinos). Si el usuario finaliza su recorrido y no gasta sus ED, se los lleva como un souvenir oficial e interactivo impreso en papel artesanal de alta calidad para demostrar a los jueces el valor tangible generado.
            III. DENOMINACIONES Y FORMATOS: Dividido en Monedas de Pulpa (denominaciones bajas) y Billetes de Fibra (denominaciones altas) -> 0.1 ED (Moneda, equivale a $50 ARS) | 0.5 ED (Moneda, equivale a $250 ARS) | 1 ED (Billete, equivale a $500 ARS) | 5 ED (Billete, equivale a $2500 ARS) | 10 ED (Billete, equivale a $5000 ARS) | 25 ED (Billete, equivale a $12500 ARS).
            IV. SISTEMA DE RECOLECCIÓN (TASAS DE INCENTIVO BANCO DE INTERCAMBIO): 1 Botella PET limpia = 0.5 ED | 1 Lata de aluminio = 0.5 ED | 1 Envoltorio plástico o papel sucio = 0.1 ED | Traer un Eco-Carrier (Ficha #5) = Bonus adicional de 1 ED.
            V. TABLA DE PRECIOS Y CONSUMO COMPLETA (División / Precio ED / Precio Equivalente $ ARS):
               - Uso de la EcoIA (Pack 3 consultas) [EcoTech] -> 1 ED ($500 ARS) | Consultas en vivo a nuestra IA curada con datos rápidos.
               - Marca-páginas de Papel Reciclado (Pack de 3) [EcoPapel] -> 2 ED ($1.000 ARS) | Con frases inspiracionales e hilos de descarte.
               - Bomba de Semillas (Nendo Dango x2) [EcoLab] -> 2 ED ($1.000 ARS) | Arcilla seleccionada y semillas nativas listas para activar.
               - Mini-taller: Armado de Marca-páginas [EcoPapel] -> 4 ED ($2.000 ARS) | El cliente utiliza nuestros sellos y tintas orgánicas en vivo.
               - Taller Express: Bombas Nendo Dango [EcoLab] -> 4 ED ($2.000 ARS) | Meten mano en la tierra, aprenden la técnica y se llevan dos unidades.
               - Llavero con Perla de Papel (Paper Beads) [EcoPapel] -> 4 ED ($2.000 ARS) | Cuentas barnizadas e impermeabilizadas con herraje metálico.
               - Test de pH Casero con EcoCroma [EcoLab] -> 4 ED ($2.000 ARS) | Experimento químico y su explicación interactiva usando viraje de color en vivo.
               - Pack de 3 Hojas de Papel Seed A4 [EcoPapel] -> 4 ED ($2.000 ARS) | Papel con semillas de huerta listo para plantar directamente.
               - Eco-Hidro (Vacía) [EcoIndustria] -> 6 ED ($3.000 ARS) | PET reciclado con corte de precisión industrial y mecha técnica de absorción.
               - Kit de Huertita Express Inicial [EcoIndustria] -> 8 ED ($4.000 ARS) | Incluye dispositivo Eco-Hidro, sustrato abonado y 1 bomba de semillas.
               - Pulsera de Paper Beads [EcoPapel] -> 8 ED ($4.000 ARS) | Accesorio estético de moda circular con diseño de alta resistencia al agua.
               - Eco-Carrier (x2) [EcoPapel] -> 10 ED ($5.000 ARS) | Bolsas de alta resistencia mecánica pegadas con engrudo cocido y reforzado.
               - Taller de Arte Botánico y Tintes [EcoLab] -> 12 ED ($6.000 ARS) | Clase práctica avanzada utilizando pigmentos orgánicos extraídos por los alumnos.
               - Billetera EcoWallet [EcoIndustria] -> 14 ED ($7.000 ARS) | Billetera ultra resistente de Tetra Pak, impermeable y con broche de presión metálico o plástico.
               - EcoCristal Base de Alumbre [EcoLab] -> 16 ED ($8.000 ARS) | Demostración física y química en vivo de una estructura cristalina molecular estable.
               - Certificación Impresa de Reciclador [EcoLab] -> 16 ED ($8.000 ARS) | Documento firmado en vivo con pluma técnica utilizando Carbon Ink (tinta artesanal).
               - Kit "Mi Primer Papel Reciclado" [EcoPapel] -> 18 ED ($9.000 ARS) | Caja de inicio rápido con pulpa seca, aglutinante orgánico y manual técnico de uso.
               - Disparos Experimentales Cañón Vortex [EcoIndustria] -> 20 ED ($10.000 ARS) | Demostración física de fluidos con proyección controlada de anillos de humo.
               - Collar Estético [EcoIndustria] -> 20 ED ($10.000 ARS) | Joyería sustentable premium combinada con diseño estructural y geométrico metálico.
               - EcoCristal Premium Teñido [EcoLab] -> 24 ED ($12.000 ARS) | Cristalización compleja pigmentada uniformemente con extractos biológicos de EcoCroma.
               - Frasco Concentrado de Tinte EcoCroma [EcoLab] -> 26 ED ($13.000 ARS) | Envase de 150ml de tinta biológica estable para teñir textiles o papel artesanal.
               - Organizador de Escritorio Modular (x3) [EcoIndustria] -> 30 ED ($15.000 ARS) | Latas y tubos recuperados con terminación fina perimetral de Fibropapel.
               - Kit de Cristalización Científica [EcoLab] -> 34 ED ($17.000 ARS) | Caja con reactivos pesados de laboratorio, frasco guía y protocolo analítico estandarizado.
               - EcoVoz [EcoIndustria] -> 40 ED ($20.000 ARS) | Caja de resonancia física pasiva que aumenta de forma directa los decibeles de la salida de un celular.
               - EcoTrash [EcoIndustria] -> 48 ED ($24.000 ARS) | Escoba exterior de alta durabilidad hecha con filamentos de botellas PET trenzadas.
               - Kit Completo de Encuadernación [EcoPapel] -> 50 ED ($25.000 ARS) | Bastidor pequeño de madera, punzón de seguridad, hilos encerados y tapas pesadas.
               - Set Organizador Imantado Premium (x5) [EcoIndustria] -> 56 ED ($28.000 ARS) | El tope de gama de la línea de escritorio, con acoples magnéticos e impecable estética industrial.
               - Taller sobre Uso de Tamiz y Prensa [EcoPapel] -> 60 ED ($30.000 ARS) | Clase magistral personalizada de 30 min. El participante se lleva el tamiz de madera básico.
               - Eco-Estelar [EcoIndustria] -> 60 ED ($30.000 ARS) | Farol de mesa metálico perforado milimétricamente con circuito LED autónomo incorporado.
               - Manual del Reciclador (Físico) [EcoPapel] -> 70 ED ($35.000 ARS) | Encuadernación artesanal japonesa premium que contiene todo el desarrollo científico y técnico del año.
               - Terrarios Sellados [EcoTech/Lab] -> 80 ED ($40.000 ARS) | Frascos de vidrio sellados herméticamente y equilibrados biológicamente a nivel ecosistémico.
        """,

        "20": """
        FICHA TÉCNICA #20: ECOVOLT (Sección: EcoLab)
        1. CONCEPTO: Propuesta teórica de generación de energía que aprovecha la diferencia de concentración entre el agua salada y el agua dulce (gradiente salino o energía azul) para producir electricidad mediante procesos físico-químicos.
        2. OBJETIVO: Analizar el potencial energético de los gradientes salinos. Comprender los procesos físicos y químicos involucrados en la generación de energía. Desarrollar un modelo conceptual aplicable a sistemas reales. Introducir al equipo en la investigación y validación de ideas innovadoras.
        3. MATERIALES:
           - Para investigación teórica: Fuentes bibliográficas estables (internet, libros, artículos científicos), cuaderno de campo o documento digital de registro.
           - Para prueba experimental básica (opcional): Agua destilada/corriente, sal común (NaCl), vasos o recipientes limpios, electrodos reactivos (cobre, zinc u otros metales disponibles), cables de conexión con pinzas cocodrilo y multímetro digital (tester).
        4. PROCEDIMIENTO:
           - Fase Teórica:
             Paso 1: Investigar a fondo el concepto de gradiente salino y su uso contemporáneo en generación de energía limpia.
             Paso 2: Analizar los procesos químicos microscópicos como difusión, ósmosis y el movimiento direccional de iones.
             Paso 3: Formular una hipótesis de funcionamiento físico-químico del sistema a escala elemental.
             Paso 4: Diseñar un esquema conceptual o plano digital del dispositivo teórico.
           - Fase Experimental (Opcional):
             Paso 1: Preparar soluciones acuosas con distinta concentración controlada de cloruro de sodio (sal).
             Paso 2: Colocar los electrodos metálicos seleccionados sumergidos en las soluciones correspondientes.
             Paso 3: Conectar el circuito eléctrico al multímetro y medir el voltaje y amperaje neto generado.
             Paso 4: Registrar de forma estricta los resultados y analizar el comportamiento de la celda galvánica elemental.
        5. ACTIVIDAD PARA EL EQUIPO: Investigar distintas formas experimentales de obtener energía a partir de la sal. Desarrollar una hipótesis propia y original del funcionamiento físico. Diseñar un modelo teórico robusto del sistema. Realizar una prueba de laboratorio básica (si los recursos están disponibles) y comparar críticamente los resultados entre los distintos enfoques planteados.
        6. CRITERIO DE CALIDAD: Claridad absoluta en la explicación del fenómeno molecular. Coherencia lógica entre la hipótesis formulada y el fundamento científico real. Diseño gráfico comprensible del sistema propuesto. Registro ordenado de datos, variables y conclusiones preliminares. Capacidad crítica de reconocer las limitaciones físicas del modelo escolar.
        7. IMPACTO AMBIENTAL: Potencial generación de energía 100% limpia, constante y renovable. Muy bajo impacto ambiental superficial en comparación con la quema de combustibles fósiles. Aprovechamiento de recursos naturales altamente abundantes del planeta (agua salada y agua dulce). Promoción activa de la investigación científica escolar en energías alternativas.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Diferencia neta de concentración utilizada: __ %. Voltaje total obtenido: __ mV. Tipo de electrodos metálicos utilizados: __. Tiempo total de medición continua: __ minutos. Observaciones físicas y químicas anotadas: __.
        9. COSTO Y VIABILIDAD: Costo experimental base sumamente accesible en entorno escolar: $____. Baja generación neta de energía eléctrica en pequeña escala de laboratorio. Alta complejidad tecnológica para una implementación real eficiente a gran escala debido a la necesidad de membranas de intercambio iónico específicas.
        10. MEJORAS Y PROYECCIÓN FUTURA: Investigar el uso y adquisición de membranas poliméricas especializadas en electrodiálisis inversa. Optimizar los materiales conductores de los electrodos para evitar la corrosión prematura. Analizar aplicaciones viables a mayor escala en desembocaduras de ríos y mares. Integrar modularmente con otros sistemas de energía renovable del proyecto.
        11. MARCO AMPLIADO (PLANTILLA METODOLÓGICA PARA PROYECTOS DE INVESTIGACIÓN CIENTÍFICA):
            Estructura estandarizada requerida para la validación de nuevas ideas del equipo:
            1. CONCEPTO: Propuesta teórica de solución ecológica basada en [Materia/Proceso], que busca transformar [Insumo/Residuo] en [Recurso/Energía].
            2. PROBLEMA A RESOLVER: Detallar qué problema concreto ataca (residuos, demanda de energía, contaminación química, optimización, etc.).
            3. HIPÓTESIS: Formular en formato condicional: “Si aplicamos [Variable Independiente], entonces podríamos lograr [Variable Dependiente].”
            4. FUNDAMENTO CIENTÍFICO: Explicación de las leyes físicas, químicas o biológicas involucradas, citando procesos conocidos en los que se basa el modelo.
            5. DISEÑO PROPUESTO: Esquema simple de cómo funcionaría mecánicamente el sistema, delimitando claramente qué insumos entran y qué recursos salen.
            6. VIABILIDAD: Análisis de factibilidad de realización a escala escolar, listando qué recursos faltan y qué limitaciones operativas existen.
            7. PRUEBA EXPERIMENTAL (Opcional): Guía para un mini test de campo, simulación digital o modelado simple.
            8. IMPACTO POTENCIAL: Evaluación del impacto ambiental, educativo y su sinergia dentro de la matriz económica del sistema EcoDollars.
            9. CONCLUSIÓN: Balance técnico analizando si funciona, si es viable y si se cataloga como proyecto implementable o línea de investigación futura.
            10. PROYECCIÓN FUTURA: Listado de mejoras de diseño, pasos de desarrollo real e integración a la plataforma digital del stand.
        """,

        "21": """
        FICHA TÉCNICA #21: ECOCRISTALES (Sección: EcoLab)
        1. CONCEPTO: Producción de cristales de alumbre mediante el principio físico-químico de sobresaturación. El soluto se disuelve en mayor cantidad en agua caliente y, al enfriarse paulatinamente y sin perturbaciones mecánicas, el exceso se organiza en el espacio formando estructuras cristalinas sólidas y geométricamente definidas. Permite observar en tiempo real procesos de nucleación y crecimiento cristalino.
        2. OBJETIVO: Demostrar procesos de cristalización controlada en un entorno escolar. Comprender de forma práctica el fenómeno de sobresaturación de soluciones. Aplicar de manera estricta las normas de seguridad e higiene en el laboratorio. Obtener un cristal estructuralmente definido y de alta pureza para su exhibición en el stand.
        3. MATERIALES: 500 ml de agua destilada o corriente, alumbre de potasio (sulfato doble de aluminio y potasio), frasco de vidrio grueso de boca ancha resistente al choque térmico, hilo de nylon fino (tanza), filtro de café o tela fina de filtrado, guantes de látex/nitrilo y gafas de protección ocular.
        4. PROCEDIMIENTO:
           Paso 1: Calentar el volumen de agua en un vaso de precipitados o recipiente adecuado sin llegar a ebullición intensa.
           Paso 2: Agregar el alumbre en polvo de forma gradual, agitando constantemente hasta alcanzar la sobresaturación (cuando el sólido ya no se disuelva y decante en el fondo).
           Paso 3: Filtrar cuidadosamente la solución en caliente utilizando el filtro de café para eliminar cualquier impureza o micropartícula insoluble.
           Paso 4: Verter el líquido filtrado y cristalino dentro del frasco de vidrio limpio.
           Paso 5: Amarrar un pequeño cristal "semilla" previamente seleccionado a un hilo de nylon y suspenderlo en el centro geométrico del frasco, asegurando que quede sumergido sin tocar el fondo ni las paredes laterales.
           Paso 6: Cubrir la boca del frasco con papel poroso para permitir una evaporación lenta y dejar reposar en un lugar aislado, libre de vibraciones, durante un periodo de 48 a 72 horas.
        5. ACTIVIDAD PARA EL EQUIPO: Preparar un mínimo de 3 cristales principales macroscópicos para la exhibición del stand. Registrar minuciosamente el tiempo de crecimiento y medir con calibre o regla el tamaño final de los ejes del cristal. Documentar fotográficamente el proceso de nucleación para la carpeta de campo.
        6. CRITERIO DE CALIDAD: Cristal con buen grado de transparencia u opacidad homogénea bien definida. Ausencia total de inclusiones visibles de impurezas en la red. Hilo de nylon perfectamente centrado sin contacto perimetral. Estructura geométrica clara, estable y sin fracturas internas.
        7. IMPACTO AMBIENTAL: Bajo consumo energético operativo (limitado únicamente al calentamiento térmico inicial del solvente). Uso responsable y seguro de reactivos químicos a pequeña escala. Promueve la educación científica y experimental con nula generación de efluentes tóxicos.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Temperatura inicial térmica del agua: __ °C. Masa aproximada de alumbre utilizada para saturar: __ g. Tiempo total cronometrado de crecimiento: __ h. Tamaño final del eje mayor del cristal: __ cm.
        9. COSTO Y VIABILIDAD: Costo estimado total de los insumos reactivos: $__. Tiempo de preparación inicial en laboratorio: __ h. Dificultad técnica del protocolo: Media. ¿Requiere supervisión adulta directa?: Sí / No.
        10. MEJORAS Y PROYECCIÓN FUTURA: Experimentar con el crecimiento de cristales coloreados mediante la adición controlada de extractos biológicos de EcoCroma (Ficha #6). Realizar un estudio comparativo cinético entre diferentes tasas de enfriamiento térmico. Implementar un taller demostrativo de química aplicada en vivo durante la feria. Integrar el modelo con una explicación geológica sobre las estructuras cristalinas macroscópicas en minerales reales.
        """,

        "22": """
        FICHA TÉCNICA #22: ECOGENERADOR DE METANO (Sección: EcoLab)
        1. CONCEPTO: Estudio teórico del proceso de digestión anaeróbica para la producción de biogás (principalmente metano) a partir de residuos orgánicos biodegradables. No incluye construcción ni experimentación física en esta etapa.
        2. OBJETIVO: Investigar el funcionamiento fisicoquímico de un biodigestor. Analizar los fundamentos microbiológicos y químicos de la descomposición. Evaluar de forma estricta los riesgos reales de operación. Diseñar una aplicación teórica e hipotética adaptada a las necesidades de la escuela.
        3. MATERIALES: No aplica por tratarse de un protocolo técnico puramente analítico y teórico.
        4. PROCEDIMIENTO:
           Paso 1: Realizar una investigación bibliográfica profunda en fuentes científicas y académicas confiables.
           Paso 2: Organizar la información recopilada en una carpeta técnica estructurada por fases.
           Paso 3: Elaboración de esquemas mecánicos y diagramas de flujo propios sobre el proceso biológico.
           Paso 4: Desarrollo de un análisis energético analítico básico basado en balances de masa teóricos.
        5. ACTIVIDAD PARA EL EQUIPO: Dividir los ejes temáticos de investigación por subgrupos de trabajo. Redactar el contenido técnico final con lenguaje claro y formal. Incluir gráficos comparativos de rendimiento energético. Preparar la defensa oral y la argumentación del proyecto teórico ante los evaluadores.
        6. CRITERIO DE CALIDAD: Información científica debidamente fundamentada con citas técnicas. Uso correcto y preciso de conceptos microbiológicos, termodinámicos y químicos. Diagramas explicativos legibles y claros. Conclusión crítica propia desarrollada por el equipo (prohibida la copia directa).
        7. IMPACTO AMBIENTAL: Análisis de la reducción neta de emisiones de gases de efecto invernadero a la atmósfera. Comparación analítica respecto al compostaje tradicional y al depósito en basurales a cielo abierto. Relación directa con la matriz de economía circular escolar.
        8. DATOS TÉCNICOS / EXPERIMENTALES (ESTIMACIONES TEÓRICAS): Producción total estimada de biogás: __ m³. Porcentaje promedio aproximado de CH₄ en la mezcla: __ %. Energía térmica/eléctrica estimada generada: __ kWh. Tipo de biodigestor de referencia analizado: __.
        9. COSTO Y VIABILIDAD: Costo estimado proyectado para una implementación real en planta: $__. Espacio físico e infraestructura requerida: __ m². Nivel de complejidad técnica global: Alto. ¿Viable en el entorno escolar?: Justificar críticamente con pros y contras.
        10. MEJORAS Y PROYECCIÓN FUTURA: Posible desarrollo experimental controlado en una etapa educativa superior. Integración del modelo teórico con el programa ambiental institucional. Vinculación y asesoramiento con escuelas e instituciones técnicas o universidades.
        11. MARCO AMPLIADO (ÍNDICE MÍNIMO OBLIGATORIO DE INVESTIGACIÓN):
            El documento de campo desarrollado por los alumnos debe estructurarse estrictamente bajo el siguiente temario:
            1️⃣ Introducción General: Definición formal de la digestión anaeróbica, historia del biogás (desde la China antigua hasta las plantas de codigestión modernas), fundamentos del metano como combustible y su rol en la economía circular.
            2️⃣ Microbiología del Proceso: Investigación analítica sobre bacterias anaeróbicas y desglose detallado de las 4 etapas bioquímicas consecutivas: Hidrólisis, Acidogénesis, Acetogénesis y Metanogénesis (identificando arqueas metanogénicas específicas y el rol del estiércol como inóculo biológico activo para demostrar que es un proceso microbiológico complejo).
            3️⃣ Química del Biogás: Composición promedio porcentual del biogás (CH₄, CO₂, trazas de H₂S y vapor de agua), fórmula molecular del metano (CH₄), balance de la ecuación química de combustión completa del metano y comparación de su poder calorífico neto frente al gas natural de red, Gas Licuado de Petróleo (GLP) y leña.
            4️⃣ Variables que Afectan la Producción: Parámetros operativos críticos (rangos de temperatura ideal: psicrófila, mesófila y termófila), pH óptimo del sustrato, relación óptima Carbono/Nitrógeno (C/N), tiempo de retención hidráulica y justificación de por qué la presencia de oxígeno inhibe y arruina el proceso.
            5️⃣ Diseño de Biodigestores Reales: Análisis morfológico comparativo entre biodigestores rurales e industriales, detallando las características de los modelos tipo chino, indio y tubular (con inclusión obligatoria de esquemas técnicos).
            6️⃣ Seguridad y Riesgos: Investigación técnica obligatoria sobre los límites de explosividad del metano, toxicidad del ácido sulfhídrico (H₂S), justificación de los peligros de operar sin control de ingeniería y análisis de normativas ambientales vigentes sobre biogás.
            7️⃣ Impacto Ambiental: Mecanismo de mitigación del metano libre en la atmósfera, matriz comparativa de impacto entre basural común, compostaje y biodigestión, y cálculo de reducción de huella de carbono.
            8️⃣ Aplicaciones Reales en el Mundo: Casos de estudio documentados del INTA (programas de biodigestores rurales en Argentina), proyectos energéticos a base de biogás en Alemania y el uso de tecnologías de digestión en granjas de la India.
            9️⃣ Aplicación Teórica en Proyecto Eco: Planteo de viabilidad local donde el equipo dimensione qué residuos orgánicos de la escuela (comedor, podas) podrían usarse, estimación teórica de cuánta energía útil produciría, aplicación práctica (calentar agua, pequeña hornalla de laboratorio) y dictamen final de viabilidad institucional debidamente justificado.
        """,

        "23": """
        FICHA TÉCNICA #23: ECOMOD (Sección: EcoTech)
        1. CONCEPTO: EcoMod es un mod educativo para Minecraft que integra los principios conceptuales del Proyecto Eco dentro de un entorno virtual interactivo. Transforma mecánicas nativas del juego en procesos de reciclaje, producción sustentable y economía circular, permitiendo que el jugador aprenda haciendo. No es un agregado meramente estético: es la simulación jugable integral del sistema Eco.
        2. OBJETIVO: Integrar la educación ambiental avanzada en un entorno digital interactivo. Enseñar procesos reales (reciclaje, producción industrial, eficiencia ecológica) mediante mecánicas lúdicas de juego. Generar un aprendizaje activo a través de la experimentación digital. Conectar la división de tecnología (EcoTech) de forma transversal con el resto del sistema Eco.
        3. MATERIALES: Computadora apta para desarrollo de software (Java + entorno integrado de modding tipo MCreator, Eclipse o IntelliJ), software de modelado y texturizado 3D (Blockbench o similar), base original instalada del juego Minecraft, recursos digitales multimedia (texturas de bloques, efectos de sonidos, interfaces gráficas de usuario) y documentación técnica del Proyecto Eco (fichas técnicas como base de conocimiento para algoritmos).
        4. PROCEDIMIENTO:
           - Fase de Diseño e Integración:
             Paso 1: Diseñar el sistema base del mod, definiendo matemáticamente las mecánicas principales (tasas de reciclaje, tiempos de producción, balanza económica).
             Paso 2: Programar y crear los nuevos ítems y bloques personalizados dentro del código (bloque de pulpa de papel, hojas de papel reciclado, etc.).
             Paso 3: Diseñar e implementar los bloques de maquinaria técnica funcional (procesador de fibras, secador de rodillos mecánico, etc.).
             Paso 4: Integrar el sistema económico cerrado mediante variables de puntuación digital tipo EcoCoins/EcoDollars.
             Paso 5: Testear exhaustivamente el balance general del mod, ajustando tiempos de espera, costos de crafteo y tasas de eficiencia operativa.
             Paso 6: Iterar el ciclo de desarrollo corrigiendo errores de código (bugs), optimizando el rendimiento y mejorando la interfaz de experiencia de usuario (UX).
        5. ACTIVIDAD PARA EL EQUIPO: Dividir formalmente los roles de desarrollo: Programación lógica (EcoTech), Diseño visual y Modelado 3D, Testing de rendimiento y Balanceo macroeconómico, y Redacción de Documentación técnica. Desarrollar una versión funcional estable (demo jugable para la feria). Probar el mod con usuarios externos (compañeros de otras secciones) para registrar feedback técnico, medir la curva de aprendizaje y preparar la demostración en vivo para el stand.
        6. CRITERIO DE CALIDAD: El mod se ejecuta de forma fluida y sin errores críticos (crashes). Las mecánicas lúdicas implementadas son comprensibles, intuitivas y coherentes con las leyes de conservación. Existe una progresión algorítmica clara en el juego (la automatización reduce los tiempos). Representa con fidelidad científica los conceptos del Proyecto Eco. Interfaz gráfica (GUI) limpia, clara y usable.
        7. IMPACTO AMBIENTAL: Genera una profunda conciencia ambiental en entornos nativos digitales. Reduce drásticamente las barreras de aprendizaje técnico mediante el uso de la gamificación. Amplía el alcance pedagógico del proyecto más allá de las fronteras del aula física. Permite una replicabilidad total e inmediata en otras escuelas del mundo sin necesidad de adquirir materiales físicos o reactivos de laboratorio.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Tiempo promedio de producción simulada (proceso manual vs. proceso automatizado): __. Eficiencia global en la conversión de recursos (input/output de materiales): __. Cantidad total de mecánicas ecológicas implementadas en código: __. Cantidad de usuarios y jugadores que testearon la demo: __. Nivel de comprensión conceptual del usuario tras la sesión (medido mediante encuesta digital): ____ %.
        9. COSTO Y VIABILIDAD: Costo económico directo muy bajo por el uso de herramientas de software de código abierto y plataformas gratuitas. Costo en tiempo de desarrollo lógico muy alto (requiere horas de programación y depuración). Alta viabilidad educativa institucional (solo se requiere el acceso a computadoras). Sistema infinitamente escalable mediante el lanzamiento de actualizaciones modulares del mod.
        10. MEJORAS Y PROYECCIÓN FUTURA: Integración algorítmica con la EcoIA mediante APIs para actuar como un asistente inteligente embebido dentro del juego. Habilitación de servidores multijugador (Multiplayer) con una economía circular y bolsa de valores compartida en tiempo real. Desarrollo de nuevas expansiones por división: EcoLab (simulación de reactivos químicos y viraje de pH dentro del juego) y EcoIndustria (complejos mecánicos y cadenas de montaje automatizadas). Diseño de un sistema integrado de misiones educativas con recompensas automáticas. Exportación de bases de datos internas del juego para análisis estadístico real en clase de matemáticas o ciencias.
        11. MARCO AMPLIADO:
            EcoMod representa la extensión e infraestructura digital del sistema Eco. Mientras las demás fichas técnicas trabajan directamente sobre la transformación de la materia física, este módulo opera sobre la simulación sistémica y el modelado del comportamiento del usuario final. 
            El software permite validar de manera estadística hipótesis críticas del sistema:
            - ¿El jugador optimiza los recursos naturales y minimiza el descarte cuando existe una economía regulada por EcoDollars?
            - ¿Se asimilan de forma más eficiente y duradera los conceptos termodinámicos y de reciclaje jugando e interactuando que mediante la lectura pasiva de textos?
            Esta ficha funciona como el laboratorio virtual definitivo del Proyecto Eco, alineado con el enfoque pedagógico moderno de aprendizaje basado en sistemas complejos interconectados y no en tareas o asignaciones aisladas.
        """,

        "24": """
        FICHA TÉCNICA #24: TERRARIA (Sección: EcoTech / EcoLab)
        1. CONCEPTO: Ecosistema cerrado autosustentable que reproduce el ciclo biogeoquímico natural del agua y de los nutrientes dentro de un recipiente hermético, incorporando sensores digitales de hardware abierto para el monitoreo ambiental continuo de variables físicas y biológicas.
        2. OBJETIVO: Demostrar de forma empírica el funcionamiento y el equilibrio homeostático de un sistema ecológico cerrado. Visualizar el ciclo hidrológico (evaporación, condensación, precipitación) en pequeña escala. Integrar las ciencias biológicas con el monitoreo tecnológico en tiempo real. Presentar datos analíticos procesados durante las jornadas de la feria de ciencias.
        3. MATERIALES: Frasco de vidrio grande con tapa de sellado hermético (junta de goma), piedras pequeñas, grava o leca para la base de drenaje, carbón activado en gránulos, tierra negra abonada (sustrato orgánico rico en nutrientes), musgo vivo o helechos pequeños de humedad, sensor de humedad de suelo (higrómetro analógico), sensor de temperatura y humedad ambiental (DHT11 o DHT22), microcontrolador programable (Arduino Uno, Nano o ESP32), cables de conexión (Jumpers Dupont) y fuente de energía eléctrica regulada (batería, powerbank o conexión USB).
        4. PROCEDIMIENTO:
           - Fase de Construcción del Ecosistema:
             Paso 1: Colocar una capa uniforme de piedras o leca (2 a 3 cm) en el fondo del frasco para garantizar el drenaje de los excesos de agua líquida.
             Paso 2: Añadir una capa fina de carbón activado sobre las piedras para actuar como filtro químico, previniendo la proliferación de hongos, bacterias y malos olores.
             Paso 3: Agregar una capa de tierra abonada con el espesor suficiente para albergar y fijar las raíces de las plantas seleccionadas.
             Paso 4: Plantar con cuidado el musgo o los helechos pequeños en el sustrato, asegurando un buen contacto de las raíces.
           - Fase de Integración Tecnológica y Cierre:
             Paso 5: Insertar de forma fija los sensores (humedad de suelo y ambiental) dentro del frasco, enrutando los cables de conexión hacia el exterior de forma prolija.
             Paso 6: Aplicar un riego ligero y medido (evitando la sobresaturación de la tierra) y cerrar herméticamente el recipiente.
             Paso 7: Conectar los sensores a los pines del microcontrolador (Arduino/ESP32) y energizar el sistema para iniciar el programa de lectura de datos.
             Paso 8: Ubicar el terrario en un sector con abundante luz solar indirecta (evitando la exposición directa que sobrecaliente el sistema).
        5. ACTIVIDAD PARA EL EQUIPO: Construir un mínimo de 1 terrario macroscópico totalmente funcional para el stand. Instalar y calibrar correctamente los sensores electrónicos de monitoreo. Programar el firmware del microcontrolador para realizar lecturas periódicas automatizadas de datos ambientales. Registrar y tabular el comportamiento de las variables de forma continua durante al menos una semana previa a la exposición.
        6. CRITERIO DE CALIDAD: Plantas saludables y turgentes sin signos de marchitamiento ni necrosis foliar. Presencia de condensación visible en las paredes de vidrio durante las primeras horas de la mañana, la cual debe controlarse y reabsorberse naturalmente a lo largo del día. Sensores transmitiendo datos continuos y estables sin pérdidas de señal ni lecturas erráticas. Estabilización biológica del sistema autónomo sin necesidad de intervención manual o apertura externa.
        7. IMPACTO AMBIENTAL: Representa a escala didáctica el frágil equilibrio ecológico y la biosfera natural del planeta Tierra. Refuerza de forma práctica el concepto de sistemas cerrados sostenibles y la conservación de recursos. Promueve el desarrollo y uso de tecnologías de monitoreo ambiental abierto con componentes de bajo impacto y alta accesibilidad global.
        8. DATOS TÉCNICOS / EXPERIMENTALES: Porcentaje de humedad de suelo promedio registrado: __ %. Temperatura interna promedio del ecosistema: __ °C. Cantidad total de días transcurridos sin adición de riego externo: __ días. Variación e histéresis térmica diaria registrada entre el día y la noche: __ °C.
        9. COSTO Y VIABILIDAD: Costo estimado total de los componentes electrónicos y biológicos: $__. Tiempo total requerido para el armado y calibración: __ horas. Dificultad técnica del protocolo: Media-Alta (debido al desarrollo de hardware/software). ¿Requiere conocimientos básicos de programación y electrónica por parte del equipo?: Sí / No.
        10. MEJORAS Y PROYECCIÓN FUTURA: Integración modular con sensores adicionales de última generación para medir concentración de Dióxido de Carbono (CO₂) e intensidad lumínica (Lux). Implementación de una base de datos web para almacenar el registro histórico digital de la evolución biológica. Versión modular automatizada para recrear múltiples ecosistemas y biomas. Desarrollo como un recurso interactivo y aplicación educativa transversal para las clases de ciencias naturales y tecnología.
        """,
    }
    # -----------------------------------------------------------------

    # Tarjeta de Contexto de Ingeniería de Prompts
    st.markdown("""
        <div class="glass-card" style="border-left: 5px solid #64FFDA; margin-bottom: 25px;">
            <strong style="color:#64FFDA; font-size:16px;">🤖 Auditoría por Segmentación de Contexto</strong><br>
            Este módulo interactivo detecta automáticamente mediante expresiones regulares qué ficha técnica estás consultando. 
            Extrae de forma quirúrgica el texto correspondiente de la base de datos y alimenta el pipeline de <strong>Groq Cloud</strong> 
            únicamente con ese fragmento para garantizar una respuesta exacta y libre de alucinaciones.
        </div>
    """, unsafe_allow_html=True)

    # Inicializar el historial de conversación en la sesión
    if "messages_ecoia" not in st.session_state:
        st.session_state.messages_ecoia = []

    # Bloque UI del Chat - Entrada y Salida unificada
    col_input, col_info = st.columns([7, 3])

    with col_info:
        st.markdown("""
            <div class="glass-card" style="height: 340px; font-size: 13px;">
                <p style="margin-top:0; color:#00E676; font-weight:600; margin-bottom:10px;">🎯 Sugerencias de Auditoría:</p>
                Hacé clic o inspirate en estos prompts técnicos para interrogar al núcleo cognitivo:
                <hr style="border:0; border-top:1px solid rgba(255,255,255,0.08); margin:8px 0;">
                <ul style="padding-left:15px; margin:0; display:flex; flex-direction:column; gap:8px; color:#B0BEC5;">
                    <li><i>"Explicame detalladamente la ficha 1"</i></li>
                    <li><i>"¿Cuál es el procedimiento de la ficha 14?"</i></li>
                    <li><i>"¿Qué impacto ambiental tiene la ficha 19?"</i></li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col_input:
        user_query = st.text_input("📝 Ingresá tu consulta técnica para EcoIA:", placeholder="Escribí acá tu pregunta (Ej: explicame la ficha 14)...", key="ecoia_input_text")
        btn_enviar = st.button("🚀 Procesar Inferencia", use_container_width=True)

        if btn_enviar and user_query:
            # INTERCEPCIÓN DINÁMICA DE CREDENCIALES
            api_key_groq = ""
            if "GROQ_API_KEY" in st.secrets:
                api_key_groq = st.secrets["GROQ_API_KEY"]
            elif os.getenv("GROQ_API_KEY"):
                api_key_groq = os.getenv("GROQ_API_KEY")

            # Insertar la consulta del usuario al historial visual
            st.session_state.messages_ecoia.append({"role": "user", "content": user_query})

            # Algoritmo de detección por Expresiones Regulares (Misma lógica de tu código 1.0)
            import re
            ficha_detectada_contenido = None
            numero_ficha_encontrada = None
            query_minusculas = user_query.lower()

            for numero, contenido_completo in TEXTO_COMPLETO_FICHAS.items():
                patron_exacto = rf"\bficha\s+{numero}\b"
                if re.search(patron_exacto, query_minusculas) or numero == query_minusculas.strip():
                    ficha_detectada_contenido = contenido_completo
                    numero_ficha_encontrada = numero
                    break

            # Si el algoritmo detectó una ficha en el texto, arma el System Prompt apuntado
            if ficha_detectada_contenido:
                system_prompt = (
                    "Actuás como EcoIA, la inteligencia artificial oficial de Proyecto Eco de la escuela E.E.S.T N°7.\n"
                    f"El usuario está consultando específicamente por la FICHA TÉCNICA N°{numero_ficha_encontrada}.\n"
                    "Tu tarea es responder la duda técnica basándote ÚNICAMENTE en el siguiente fragmento oficial extraído de nuestra base de datos. "
                    "No uses conocimientos externos ni inventes objetivos o componentes que no figuren en este texto:\n\n"
                    f"=== TEXTO OFICIAL CONFIGURADO PARA FICHA {numero_ficha_encontrada} ===\n"
                    f"{ficha_detectada_contenido}\n"
                    "====================================================="
                )
            else:
                system_prompt = (
                    "Actuás como EcoIA, la inteligencia artificial oficial de Proyecto Eco de la escuela E.E.S.T N°7. "
                    "Respondé con tono formal, científico y de ingeniería. Como no especificaron una ficha técnica concreta en la pregunta, "
                    "respondé usando tus conocimientos generales sobre las celdas del colegio (EcoPapel, EcoLab, EcoTech, EcoIndustria) de forma prudente y profesional."
                )

            # Enviar a Groq Cloud
            if api_key_groq != "":
                with st.spinner("🧠 Extrayendo segmento de la batea de datos y ejecutando inferencia..."):
                    try:
                        from groq import Groq
                        client = Groq(api_key=api_key_groq)
                        
                        completion = client.chat.completions.create(
                            model="llama-3.1-8b-instant",  
                            messages=[
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": user_query}
                            ],
                            temperature=0.2,
                            max_tokens=1024
                        )
                        respuesta_ia = completion.choices[0].message.content
                        respuesta_ia = re.sub(r'\n{3,}', '\n\n', respuesta_ia)
                        
                        st.session_state.messages_ecoia.append({"role": "assistant", "content": respuesta_ia})
                    except Exception as e:
                        st.error(f"Error de conexión con la infraestructura de Groq: {str(e)}")
            else:
                with st.spinner("⚙️ Ejecutando matriz cognitiva local..."):
                    import time
                    time.sleep(1.0)
                    respuesta_fallback = f"🤖 **[EcoIA - Modo Offline]:** Procesé tu consulta sobre la ficha. Activá `GROQ_API_KEY` para conectar con el modelo Llama."
                    st.session_state.messages_ecoia.append({"role": "assistant", "content": respuesta_fallback})

    # Renderizado elegante e histórico del Chat (Acá abajo es donde se rompía porque no encontraba el diccionario)
    if st.session_state.messages_ecoia:
        st.markdown('<p style="color:#A5D6A7; font-size:14px; margin-top:20px; margin-bottom:10px; font-weight:600;">📜 Flujo de la Conversación Actual:</p>', unsafe_allow_html=True)
        
        for msg in reversed(st.session_state.messages_ecoia):
            if msg["role"] == "user":
                st.markdown(f"""
                    <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.08); padding: 12px 16px; border-radius: 8px; margin-bottom: 10px;">
                        <span style="color: #64FFDA; font-weight: bold; font-size:12px; text-transform:uppercase;">👤 Tu Consulta Técnica:</span>
                        <p style="margin: 5px 0 0 0; color: #E0E6ED; font-size:14px;">{msg['content']}</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                    <div style="background: rgba(0, 230, 118, 0.03); border: 1px solid rgba(0, 230, 118, 0.15); padding: 16px; border-radius: 8px; margin-bottom: 15px; border-left: 4px solid #00E676;">
                        <span style="color: #00E676; font-weight: bold; font-size:12px; text-transform:uppercase;">🤖 Núcleo EcoIA responde:</span>
                        <div style="margin: 8px 0 0 0; color: #CFD8DC; font-size:14px; line-height:1.6; white-space: pre-wrap;">{msg['content']}</div>
                    </div>
                """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <div style="text-align: center; margin-top: 50px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Suite EcoIA Operativa v2.0 • Procesamiento de Lenguaje Natural en Escuelas Técnicas • E.E.S.T N°7
        </div>
    """, unsafe_allow_html=True)
