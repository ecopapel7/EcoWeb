import streamlit as st
from streamlit_option_menu import option_menu

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="EcoWeb 1.0 - Proyecto Eco",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# INYECCIÓN DE INTERFAZ DE ALTO IMPACTO (CSS BLINDADO)
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
        background: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(165, 214, 167, 0.15);
        border-radius: 16px;
        padding: 24px;
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

# === REEMPLAZAR EL BLOQUE OPTION_MENU POR ESTE ===
    selected = option_menu(
        menu_title=None,
        options=[
            "Inicio", "Objetivo Eco", "Fundamentos Eco", "Cronología Eco", 
            "Fichas Técnicas", "Explorador Eco", "Impacto Eco", 
            "Sistema Reconocidos", "Replicar Eco", "Galería Eco", "Preguntas Frecuentes"
        ], # Agregadas Páginas 11 y 12
        icons=[
            "house-door-fill", "target", "diagram-3-fill", "clock-history", 
            "file-earmark-text-fill", "search-heart-fill", "activity", 
            "award-fill", "share-fill", "images", "patch-question-fill"
        ], # Íconos correspondientes para Galería y FAQs
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#00E676", "font-size": "18px"}, 
            "nav-link": {"font-size": "15px", "color": "#E0E6ED", "text-align": "left", "margin":"3px 0px", "--hover-color": "rgba(0, 230, 118, 0.1)"},
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
    st.markdown('<div class="subtitle">Infraestructura Educativa Continua y Sistema Integral de Innovación Sustentable</div>', unsafe_allow_html=True)
    
    # 1. ¿Qué es EcoWeb?
    st.markdown('<div class="section-header">🧬 ¿Qué es EcoWeb?</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card" style="font-size: 18px; line-height: 1.6; border-left: 5px solid #00E676;">
        <strong>EcoWeb</strong> es la plataforma digital oficial de <strong>Proyecto Eco</strong>. 
        Fue desarrollada para centralizar información, documentación, fichas técnicas, recursos educativos y 
        herramientas relacionadas con el proyecto, permitiendo que los conocimientos generados puedan conservarse, 
        consultarse y replicarse con mayor facilidad.
        </div>
        """, unsafe_allow_html=True
    )
    
    # Columnas centrales solucionadas sin fugas de string
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">⚠️ ¿Por qué fue creada?</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:18px;">Necesitábamos resolver un problema:</p>
                <div class="info-item">
                    <span class="info-bullet">✦</span><span class="info-tag">Gran cantidad de información dispersa:</span> Centraliza datos fragmentados de investigaciones anteriores.
                </div>
                <div class="info-item">
                    <span class="info-bullet">✦</span><span class="info-tag">Crecimiento del proyecto:</span> Soporta de forma escalable la evolución continua del ecosistema.
                </div>
                <div class="info-item">
                    <span class="info-bullet">✦</span><span class="info-tag">Necesidad de conservar conocimientos:</span> Evita la pérdida del capital intelectual al egresar los estudiantes.
                </div>
                <div class="info-item">
                    <span class="info-bullet">✦</span><span class="info-tag">Necesidad de facilitar la replicabilidad:</span> Prepara manuales listos para exportar el modelo a otras escuelas.
                </div>
                <div class="info-item">
                    <span class="info-bullet">✦</span><span class="info-tag">Necesidad de mostrar resultados:</span> Crea una ventana pública y auditable de mitigación ambiental real.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="section-header">⚙️ Funciones de EcoWeb</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:18px;">Para qué sirve nuestra plataforma digital:</p>
                <div class="info-item">
                    <span class="info-bullet">✦</span><span class="info-tag">Organizar información:</span> Sistematiza el árbol de subproyectos e iniciativas del equipo.
                </div>
                <div class="info-item">
                    <span class="info-bullet">✦</span><span class="info-tag">Almacenar fichas técnicas:</span> Ofrece descarga y lectura inmediata de los protocolos de ingeniería.
                </div>
                <div class="info-item">
                    <span class="info-bullet">✦</span><span class="info-tag">Difundir iniciativas ecológicas:</span> Comunica las campañas aplicadas y las bitácoras experimentales.
                </div>
                <div class="info-item">
                    <span class="info-bullet">✦</span><span class="info-tag">Facilitar la consulta de contenidos:</span> Optimiza la búsqueda de material educativo de base científica.
                </div>
                <div class="info-item">
                    <span class="info-bullet">✦</span><span class="info-tag">Mostrar resultados e impacto:</span> Muestra de forma transparente las métricas logradas por los dispositivos.
                </div>
                <div class="info-item">
                    <span class="info-bullet">✦</span><span class="info-tag">Favorecer la replicabilidad:</span> Agiliza la transferencia metodológica del ecosistema escolar.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    # 4. Relación con los pilares (Cuadro final de cierre)
    st.markdown('<div class="section-header">📊 Relación con los Pilares</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="padding: 10px 20px 20px 20px;">
        <table class="custom-table">
            <thead>
                <tr>
                    <th style="width: 25%;">Pilar</th>
                    <th style="width: 75%;">Relación con EcoWeb</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><span class="pilar-tag">Replicable</span></td>
                    <td>Permite acceder a documentación y fichas técnicas desde cualquier lugar.</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Continuo</span></td>
                    <td>Conserva la información y el conocimiento técnico entre generaciones de estudiantes.</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Medible</span></td>
                    <td>Permite registrar de manera pública y transparente los avances y resultados.</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Interdisciplinario</span></td>
                    <td>Integra y unifica todas las secciones, áreas y divisiones tecnológicas.</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Experimental</span></td>
                    <td>Difunde los experimentos, pruebas, fallos y optimizaciones de las fichas.</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Circular</span></td>
                    <td>Facilita el intercambio abierto de conocimientos bajo una filosofía Open Source.</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Sustentable</span></td>
                    <td>Reduce la necesidad de copias impresas y digitaliza la infraestructura de auditoría.</td>
                </tr>
            </tbody>
        </table>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# PÁGINA 2 — OBJETIVO ECO
# ==========================================
elif selected == "Objetivo Eco":
    
    st.markdown('<div class="main-title">OBJETIVO ECO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Análisis Crítico del Problema Ambiental Escolar y Nuestra Solución Sistémica</div>', unsafe_allow_html=True)
    
    # SECCIÓN 5: OBJETIVO GENERAL (Ubicado estratégicamente arriba como introducción)
    st.markdown('<div class="section-header">🎯 Objetivo General: ¿Qué intenta conseguir Proyecto Eco?</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="font-size: 18px; line-height: 1.6; border-left: 5px solid #00E676;">
        El propósito definitivo de <strong>Proyecto Eco</strong> es estructurar un sistema integral y replicable que mitigue el impacto ambiental institucional mediante la creación de tecnologías sustentables, beneficiando directamente a la comunidad educativa y sentando las bases operativas para que el conocimiento técnico no se pierda entre ciclos lectivos.
        </div>
    """, unsafe_allow_html=True)

    # Columnas para Sección 1 y Sección 2 (Problema vs Consecuencias)
    col_prob, col_cons = st.columns(2)
    
    with col_prob:
        st.markdown('<div class="section-header">❌ 1. Problema Identificado</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card">
                <p style="margin-top:0; color:#FF5252; font-weight:600; margin-bottom:18px;">¿Qué problema observó Proyecto Eco?</p>
                <div class="info-item">
                    <span class="info-bullet" style="color:#FF5252;">✦</span><span class="info-tag">Dependencia personalista:</span> Proyectos ecológicos escolares que caen bajo la responsabilidad de muy pocas personas.
                </div>
                <div class="info-item">
                    <span class="info-bullet" style="color:#FF5252;">✦</span><span class="info-tag">Fuga de conocimiento:</span> Pérdida masiva de los saberes prácticos avanzados al finalizar cada ciclo lectivo.
                </div>
                <div class="info-item">
                    <span class="info-bullet" style="color:#FF5252;">✦</span><span class="info-tag">Ausencia de documentación:</span> Falta extrema de registros organizados, planos o memorias técnicas descriptivas.
                </div>
                <div class="info-item">
                    <span class="info-bullet" style="color:#FF5252;">✦</span><span class="info-tag">Brecha intergeneracional:</span> Alta dificultad para transmitir experiencias de forma fluida entre diferentes camadas de alumnos.
                </div>
                <div class="info-item">
                    <span class="info-bullet" style="color:#FF5252;">✦</span><span class="info-tag">Fragilidad operativa:</span> Escasa o nula continuidad a largo plazo de las iniciativas ambientales escolares.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_cons:
        st.markdown('<div class="section-header">📉 2. Consecuencias del Problema</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card">
                <p style="margin-top:0; color:#FF8A80; font-weight:600; margin-bottom:18px;">¿Por qué es crítico e importante resolverlo?</p>
                <div class="info-item">
                    <span class="info-bullet" style="color:#FF8A80;">✦</span><span class="info-tag">Reinicio constante:</span> Las dinámicas ambientales sufren un bucle donde cada año se arranca desde cero.
                </div>
                <div class="info-item">
                    <span class="info-bullet" style="color:#FF8A80;">✦</span><span class="info-tag">Desperdicio de recursos:</span> Pérdida material de prototipos y desvanecimiento de la documentación previa.
                </div>
                <div class="info-item">
                    <span class="info-bullet" style="color:#FF8A80;">✦</span><span class="info-tag">Desmotivación del alumnado:</span> Disminución progresiva de la participación activa por falta de rumbo claro.
                </div>
                <div class="info-item">
                    <span class="info-bullet" style="color:#FF8A80;">✦</span><span class="info-tag">Impacto diluido:</span> Reducción severa del verdadero impacto ecológico y comunitario proyectado.
                </div>
                <div class="info-item">
                    <span class="info-bullet" style="color:#FF8A80;">✦</span><span class="info-tag">Cuellos de botella:</span> El sistema colapsa si un docente o alumno líder específico abandona la institución.
                </div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 3: SOLUCIÓN PROPUESTA
    st.markdown('<div class="section-header">🛠️ 3. Solución Propuesta: El Sistema Eco</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
            <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:18px;">¿Cómo intenta resolver el problema Proyecto Eco mediante una infraestructura sistémica?</p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
                <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;">
                    <span style="color:#00E676; font-weight:bold;">🏢 Organización por Secciones:</span> Divisiones técnicas de trabajo especializado (EcoPapel, EcoLab, EcoTech, EcoIndustria) para atomizar tareas.
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;">
                    <span style="color:#00E676; font-weight:bold;">🏆 Sistema de Reconocidos:</span> Un esquema de incentivo basado en mérito y auditoría semanal para mantener activa la participación constante.
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;">
                    <span style="color:#00E676; font-weight:bold;">📋 Fichas Técnicas:</span> Protocolos de ingeniería estandarizados y manuales de desarrollo rápido para asegurar la transferencia científica.
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;">
                    <span style="color:#00E676; font-weight:bold;">🔄 Flujo Eco:</span> Dinámica metodológica de retroalimentación donde un subproyecto nutre directamente la producción del siguiente.
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;">
                    <span style="color:#00E676; font-weight:bold;">⭐ Pilares Eco:</span> Los 7 vectores conceptuales irrenunciables que rigen y validan cada línea de investigación y desarrollo.
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border-left: 3px solid #00E676;">
                    <span style="color:#00E676; font-weight:bold;">🌐 Herramientas Digitales:</span> El uso de software interactivo y de EcoWeb como el repositorio unificado de libre acceso.
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 4 & SECCIÓN 6: PRINCIPIOS Y VISIÓN FUTURA
    col_pila, col_vis = st.columns([4, 6])
    
    with col_pila:
        st.markdown('<div class="section-header">⚖️ 4. Principios de la Solución</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 290px;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:15px;">¿Sobre qué pilares inquebrantables se construye?</p>
                <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                    <span class="pilar-tag">♻️ Replicable</span>
                    <span class="pilar-tag">🌿 Sustentable</span>
                    <span class="pilar-tag">🔄 Circular</span>
                    <span class="pilar-tag">⏳ Continuo</span>
                    <span class="pilar-tag">🧪 Experimental</span>
                    <span class="pilar-tag">📊 Medible</span>
                    <span class="pilar-tag">🤝 Interdisciplinario</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_vis:
        st.markdown('<div class="section-header">🚀 6. Visión Futura</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 290px;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:15px;">¿Hacia dónde está creciendo el sistema?</p>
                <div class="info-item"><span class="info-bullet">🚀</span><strong>Masificación participativa:</strong> Escalar la cantidad de alumnos e investigadores activos en los laboratorios.</div>
                <div class="info-item"><span class="info-bullet">📚</span><strong>Expansión técnica:</strong> Generar e indexar un número cada vez mayor de fichas técnicas normalizadas.</div>
                <div class="info-item"><span class="info-bullet">⚡</span><strong>Desarrollo de proyectos:</strong> Diseñar nuevos dispositivos ecológicos complejos interconectados.</div>
                <div class="info-item"><span class="info-bullet">🏫</span><strong>Exportación del modelo:</strong> Lograr la replicación efectiva del ecosistema Eco en otras escuelas de la región.</div>
                <div class="info-item"><span class="info-bullet">🤖</span><strong>Evolución digital:</strong> Potenciar las capacidades de EcoWeb mediante integraciones de IA avanzada.</div>
            </div>
        """, unsafe_allow_html=True)

    # Cierre de la página
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Filosofía de Infraestructura Continua • E.E.S.T N°7
        </div>
    """, unsafe_allow_html=True)
    
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
        El éxito y la trascendencia de <strong>Proyecto Eco</strong> no radican únicamente en la ejecución de actividades aisladas o en el armado de fichas técnicas. El núcleo operativo se sostiene sobre una <strong>infraestructura de fundamentos organizativos interconectados</strong>. Estos pilares, flujos de procesos y conceptos científicos garantizan que el proyecto se mantenga activo, perfectamente estructurado y listo para ser replicado en cualquier institución educativa.
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 2: LOS 7 PILARES (Desplegable interactivo premium para feria)
    st.markdown('<div class="section-header">🏛️ 1. Los 7 Pilares: ¿Qué características debe cumplir el proyecto?</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A5D6A7; margin-bottom:15px;">Haz clic en cada pilar para auditar sus definiciones, funciones y aplicaciones prácticas en el mundo real:</p>', unsafe_allow_html=True)
    
    pilares_data = {
        "♻️ Replicable": {
            "def": "Capacidad de ser adaptado e implementado en otras instituciones educativas sin depender de infraestructura compleja.",
            "fun": "Estandariza los procesos para que cualquier escuela técnica o secundaria pueda adoptar el modelo rápidamente.",
            "ej": "Fichas técnicas en formato abierto y manuales paso a paso de libre acceso en EcoWeb."
        },
        "🌿 Sustentable": {
            "def": "Desarrollo que equilibra el impacto ambiental, social y el uso racional de recursos disponibles.",
            "fun": "Garantiza que cada dispositivo o recurso creado reduzca de forma real la huella ecológica institucional.",
            "ej": "Construcción del Módulo Eco-Hidro utilizando exclusivamente botellas PET recuperadas y descarte escolar."
        },
        "🔄 Circular": {
            "def": "Modelo de diseño enfocado en la eliminación de residuos mediante el upcycling y el aprovechamiento continuo.",
            "fun": "Cierra los ciclos de vida de los materiales de descarte, convirtiendo la salida de un proceso en la entrada de otro.",
            "ej": "Producción de Carbon Ink (tinta premium) procesando el descarte y sobrantes inservibles de EcoPapel."
        },
        "⏳ Continuo": {
            "def": "Garantía de preservación y avance del proyecto a través del tiempo, mitigando el recambio generacional.",
            "fun": "Evita la pérdida de conocimiento crítico cuando las camadas de estudiantes egresan de la institución.",
            "ej": "La centralización histórica de planos, códigos y bitácoras experimentales dentro de esta plataforma."
        },
        "🧪 Experimental": {
            "def": "Metodología basada en el ensayo, el error documentado, el análisis empírico y la optimización constante.",
            "fun": "Fomenta el pensamiento científico y técnico, permitiendo aprender de los fallos de los prototipos.",
            "ej": "Pruebas de congelado y perforación en el desarrollo de luminarias Eco-Estelar hasta dar con el espesor óptimo."
        },
        "📊 Medible": {
            "def": "Capacidad de cuantificar y auditar los resultados, el rendimiento y el impacto ambiental directo.",
            "fun": "Aporta rigor matemático y científico a las iniciativas mediante indicadores claros y tangibles.",
            "ej": "Cálculo del volumen de agua optimizado por capilaridad o pesaje de kg de celulosa recuperada mensualmente."
        },
        "🤝 Interdisciplinario": {
            "def": "Integración y convergencia de múltiples áreas del conocimiento (química, electrónica, informática, diseño).",
            "fun": "Rompe el aislamiento de las materias escolares tradicionales, unificando saberes en pos de un desarrollo común.",
            "ej": "El desarrollo de TerrarIA, donde interactúan programación de sensores, química del suelo y diseño estructural."
        }
    }

    for name, info in pilares_data.items():
        with st.expander(name):
            st.markdown(f"""
                <div style="padding: 10px; line-height: 1.6;">
                    <p style="color:#B9F6CA; margin-bottom:5px;"><strong>Definition:</strong> {info['def']}</p>
                    <p style="color:#E0E6ED; margin-bottom:5px;"><strong>Función en el Sistema:</strong> {info['fun']}</p>
                    <p style="color:#81C784; margin-bottom:0;"><strong>⚡ Aplicación Práctica:</strong> {info['ej']}</p>
                </div>
            """, unsafe_allow_html=True)

    # SECCIÓN 3: FLUJO ECO (Línea de proceso secuencial visualmente impactante)
    st.markdown('<div class="section-header">🔄 2. El Flujo Eco: ¿Cómo circulan las ideas y actividades?</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
            <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:20px;">Ciclo de Vida del Desarrollo Sustentable (Línea de Proceso):</p>
            <div style="display: flex; flex-direction: column; gap: 12px;">
                <div style="background: rgba(255,255,255,0.02); padding: 12px 18px; border-radius: 8px; border-left: 4px solid #64FFDA;">
                    <span style="color:#64FFDA; font-weight:bold; font-size:16px;">Fase 1: Identificación y Captura 🎯</span><br>
                    <span style="font-size:14.5px; color:#E0E6ED;">Se detecta un residuo institucional o una necesidad energética/ambiental. <strong>Función:</strong> Filtrar problemas reales bajo la óptica de los pilares ecológicos.</span>
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 12px 18px; border-radius: 8px; border-left: 4px solid #00E676;">
                    <span style="color:#00E676; font-weight:bold; font-size:16px;">Fase 2: Investigación y Laboratorio Experimental 🧪</span><br>
                    <span style="font-size:14.5px; color:#E0E6ED;">Los estudiantes realizan ensayos químicos, físicos o lógicos de los materiales. <strong>Función:</strong> Validar la viabilidad técnica de la idea mediante prototipado rápido.</span>
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 12px 18px; border-radius: 8px; border-left: 4px solid #B9F6CA;">
                    <span style="color:#B9F6CA; font-weight:bold; font-size:16px;">Fase 3: Estandarización y Ficha Técnica 📋</span><br>
                    <span style="font-size:14.5px; color:#E0E6ED;">Se redactan de forma rigurosa los pasos, herramientas y medidas de seguridad. <strong>Función:</strong> Traducir el experimento exitoso en un documento técnico auditable y replicable.</span>
                </div>
                <div style="background: rgba(255,255,255,0.02); padding: 12px 18px; border-radius: 8px; border-left: 4px solid #69F0AE;">
                    <span style="color:#69F0AE; font-weight:bold; font-size:16px;">Fase 4: Integración al Flujo Circular 🔄</span><br>
                    <span style="font-size:14.5px; color:#E0E6ED;">El subproyecto resultante se vincula con el resto de las secciones. <strong>Función:</strong> Asegurar que los subproductos (como la moneda EcoDollars o las tintas) nutran el engranaje de otras divisiones.</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 4 & SECCIÓN 5: CONCEPTOS Y RELACIÓN DE FUNDAMENTOS
    col_con, col_rel = st.columns([6, 4])
    
    with col_con:
        st.markdown('<div class="section-header">🧪 3. Conceptos Eco: Marcos de Conocimiento</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 380px; overflow-y: auto;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:15px;">Conocimientos científicos aplicados por el sistema:</p>
                <div class="info-item">
                    <span class="info-bullet">📘</span><span class="info-tag">Upcycling (Reciclaje Avanzado):</span> Transformación de residuos en productos de mayor valor técnico o estético. <em>Área: Ecología / Diseño.</em>
                </div>
                <div class="info-item">
                    <span class="info-bullet">📘</span><span class="info-tag">Pirólisis Controlada:</span> Degradación térmica de materiales orgánicos en ausencia de oxígeno. <em>Área: Química Aplicada.</em>
                </div>
                <div class="info-item">
                    <span class="info-bullet">📘</span><span class="info-tag">Gradiente Salino:</span> Aprovechamiento de la diferencia de concentración de sal para generar energía teórica. <em>Área: Energías Limpias.</em>
                </div>
                <div class="info-item">
                    <span class="info-bullet">📘</span><span class="info-tag">Automatización Ecosistémica:</span> Uso de matrices de sensores de hardware para controlar variables biológicas. <em>Área: Tecnología / IoT.</em>
                </div>
                <div class="info-item">
                    <span class="info-bullet">📘</span><span class="info-tag">Economía de Circulación Abierta:</span> Sistemas monetarios propios impresos sobre recursos internos. <em>Área: Educación Ambiental / Economía Circular.</em>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
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
                    <span style="font-size:13.5px; color:#E0E6ED;">Aportan los <strong>conocimientos científicos y técnicos</strong> base utilizados.</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 6: APLICACIÓN EN LAS SECCIONES TÉCNICAS
    st.markdown('<div class="section-header">🏢 5. Aplicación Práctica en las Secciones Técnicas del Ecosistema</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="padding: 10px 20px 20px 20px;">
        <p style="color: #A5D6A7; margin-bottom: 15px;">Cómo se materializan transversalmente los fundamentos dentro de cada rama operativa de Proyecto Eco:</p>
        <table class="custom-table">
            <thead>
                <tr>
                    <th style="width: 20%;">Sección Técnica</th>
                    <th style="width: 30%;">¿Qué hace?</th>
                    <th style="width: 25%;">Aplicación de Pilares y Flujo</th>
                    <th style="width: 25%;">Conceptos Clave Aplicados</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong style="color:#B9F6CA;">EcoPapel</strong></td>
                    <td>Procesamiento y manufactura de papel artesanal reciclado y elementos derivados de la celulosa recuperada.</td>
                    <td>Sustentable e Interdisciplinario. Estandariza su producción mediante fichas de secado y granulometría.</td>
                    <td>Fibras vegetales, Celulosa recuperada, Biodegradabilidad, Inclusión de semillas nativas.</td>
                </tr>
                <tr>
                    <td><strong style="color:#B9F6CA;">EcoLab</strong></td>
                    <td>Área de experimentación química avanzada, obtención de insumos biológicos y análisis de energías alternativas.</td>
                    <td>Experimental y Medible. Valida empíricamente la viabilidad científica antes de redactar manuales.</td>
                    <td>Pirólisis, Extracción de pigmentos, Digestión anaeróbica, Gradiente salino, Cristalización.</td>
                </tr>
                <tr>
                    <td><strong style="color:#B9F6CA;">EcoTech</strong></td>
                    <td>División de desarrollo informático, algoritmia de Inteligencia Artificial, simulación virtual y hardware de monitoreo.</td>
                    <td>Replicable y Continuo. Digitaliza el conocimiento del proyecto y crea interfaces interactivas accesibles.</td>
                    <td>Modelado LLM (EcoIA), Internet de las Cosas (IoT), Matrices de sensores, Simulación interactiva (Minecraft).</td>
                </tr>
                <tr>
                    <td><strong style="color:#B9F6CA;">EcoIndustria</strong></td>
                    <td>Sección orientada al diseño y fabricación de dispositivos mecánicos, mobiliario modular y soluciones físicas a base de PET/Cartón.</td>
                    <td>Circular y Sustentable. Transforma descartes estructurales duros en herramientas ergonómicas operativas.</td>
                    <td>Upcycling estructural, Dinámica de fluidos, Amplificación acústica pasiva, Termofusión controlada.</td>
                </tr>
            </tbody>
        </table>
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
        Escribir la historia de <strong>Proyecto Eco</strong> es fundamental para validar su <strong>continuidad</strong> y mejora constante. El ecosistema actual no surgió de un día para el otro; es el resultado de un proceso orgánico de <strong>evolución</strong>, aprendizaje institucional y resiliencia técnica, donde los errores de fases previas se transformaron en la ingeniería del presente.
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 2: COMPARATIVA DE EVOLUCIÓN (Tabla Premium de Transformación estructural)
    st.markdown('<div class="section-header">📊 1. Matriz de Transformación Institucional</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="padding: 10px 20px 20px 20px;">
        <table class="custom-table">
            <thead>
                <tr>
                    <th style="width: 20%;">Variable Operativa</th>
                    <th style="width: 40%; background: rgba(239, 83, 80, 0.2); color: #FFCDD2;">Fase Origen: EcoPapel (2025)</th>
                    <th style="width: 40%; background: rgba(76, 175, 80, 0.2); color: #C8E6C9;">Fase Actual: Proyecto Eco (2026)</th>
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
                    <td><span style="color:#00E676; font-weight:bold;">24 Fichas Técnicas</span> normalizadas de ingeniería.</td>
                </tr>
                <tr>
                    <td><strong>Gestión del Alumnado</strong></td>
                    <td>Participación voluntaria informal y dispersa.</td>
                    <td><span style="color:#00E676; font-weight:bold;">Sistema de Reconocidos</span> con auditoría y puntaje semanal.</td>
                </tr>
                <tr>
                    <td><strong>Infraestructura Digital</strong></td>
                    <td>Inexistente (Registros en formato papel/físico).</td>
                    <td><span style="color:#00E676; font-weight:bold;">Ecosistema Digital</span> (EcoWeb, Modelado IA, Servidores de consulta).</td>
                </tr>
                <tr>
                    <td><strong>Alcance Científico</strong></td>
                    <td>Reciclaje básico y concientización interna.</td>
                    <td>Desarrollo de hardware IoT, pirólisis química y economía circular activa.</td>
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
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:12px;">El chispazo inicial del proyecto:</p>
                <div class="info-item"><strong>Año de Nacimiento:</strong> Marz-Nov 2025.</div>
                <div class="info-item"><strong>Contexto y Problema:</strong> Se detectó un desperdicio masivo de hojas, carpetas y cartones en los cestos de la escuela técnica, sin ningún tratamiento de reciclado.</div>
                <div class="info-item"><strong>Objetivo Inicial:</strong> Recuperar esa celulosa escolar para fabricar hojas artesanales e incorporarles semillas nativas (Papel Seed).</div>
                <div class="info-item"><strong>Características:</strong> Un grupo reducido de alumnos experimentando con licuadoras caseras y bastidores de madera rústicos.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_trans:
        st.markdown('<div class="section-header">🔄 3. La Gran Ruptura y Evolución</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 330px;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:12px;">¿Por qué dejamos de ser solo "EcoPapel"?</p>
                <div class="info-item"><span style="color:#FFD54F; font-weight:bold;">⚠️ El Quiebre:</span> Al cerrar el ciclo lectivo 2025, se vio que si los alumnos clave se egresaban, las técnicas se perdían y las licuadoras quedaban arrumbadas.</div>
                <div class="info-item"><span style="color:#00E676; font-weight:bold;">🧠 Mutación Sistémica:</span> Nace la necesidad imperiosa de crear los <strong>7 Pilares Eco</strong> (Continuo, Replicable, Medible...) para que el proyecto trascienda a las personas.</div>
                <div class="info-item"><span style="color:#00E676; font-weight:bold;">🏢 Expansión de Fronteras:</span> Al querer optimizar el papel, se requirió química (EcoLab), automatización (EcoTech) y moldes mecánicos complejos (EcoIndustria). El residuo se volvió engranaje.</div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 5: LÍNEA TEMPORAL SECUENCIAL CRONOLÓGICA
    st.markdown('<div class="section-header">📅 4. Línea de Tiempo Histórica Oficial</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
            <div style="display: flex; flex-direction: column; gap: 15px;">
                <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #81C784;">
                    <span style="color:#81C784; font-weight:bold;">Marzo 2025 • Fundación de EcoPapel 🧪</span><br>
                    <span style="font-size:14px; color:#E0E6ED;">Primeros ensayos de reciclado de celulosa en contraturno. <strong>Importancia:</strong> Estableció la viabilidad del upcycling escolar.</span>
                </div>
                <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #A5D6A7;">
                    <span style="color:#A5D6A7; font-weight:bold;">Noviembre 2025 • Primera Muestra Técnica 📑</span><br>
                    <span style="font-size:14px; color:#E0E6ED;">Presentación del "Manual del Reciclador" físico. <strong>Importancia:</strong> Se detectó el peligro de perder el conocimiento si no se digitalizaba el avance.</span>
                </div>
                <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #4CAF50;">
                    <span style="color:#4CAF50; font-weight:bold;">Marzo 2026 • Redacción de los 7 Pilares ⚖️</span><br>
                    <span style="font-size:14px; color:#E0E6ED;">Se decreta la matriz conceptual obligatoria. Nace formalmente el concepto de "Proyecto Eco". <strong>Importancia:</strong> Blindaje metodológico transgeneracional.</span>
                </div>
                <div style="background: rgba(255,255,255,0.01); padding: 14px; border-radius: 8px; border-left: 4px solid #00E676;">
                    <span style="color:#00E676; font-weight:bold;">Mayo 2026 • Despliegue de la Arquitectura Digital y EcoWeb 🌐</span><br>
                    <span style="font-size:14px; color:#E0E6ED;">Desarrollo de las interfaces en Streamlit, codificación de las 24 fichas de ingeniería y lanzamiento de los primeros prompts de EcoIA. <strong>Importancia:</strong> Democratización total del acceso técnico.</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 6: HITOS CRÍTICOS (Los 3 momentos clave de quiebre técnico)
    st.markdown('<div class="section-header">🏆 5. Hitos de Mayor Impacto Tecnológico</div>', unsafe_allow_html=True)
    st.markdown("""
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 15px; margin-bottom: 25px;">
            <div style="background: rgba(0, 230, 118, 0.03); border: 1px solid rgba(0, 230, 118, 0.2); padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                <span style="font-size: 24px;">🚀</span> <h4 style="margin: 10px 0 5px 0; color:#B9F6CA;">Paso de Taller a Sistema</h4>
                <p style="font-size:14px; margin:0; color:#E0E6ED;">La creación de las 4 divisiones paralelas interconectadas mediante el <em>Flujo Eco</em>, rompiendo la linealidad del reciclaje tradicional.</p>
            </div>
            <div style="background: rgba(0, 230, 118, 0.03); border: 1px solid rgba(0, 230, 118, 0.2); padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                <span style="font-size: 24px;">📋</span> <h4 style="margin: 10px 0 5px 0; color:#B9F6CA;">Estandarización de 24 Fichas</h4>
                <p style="font-size:14px; margin:0; color:#E0E6ED;">La conversión de simples ideas en protocolos científicos rígidos de ingeniería, asegurando el pilar <strong>Replicable</strong> de la solución.</p>
            </div>
            <div style="background: rgba(0, 230, 118, 0.03); border: 1px solid rgba(0, 230, 118, 0.2); padding: 20px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.2);">
                <span style="font-size: 24px;">💎</span> <h4 style="margin: 10px 0 5px 0; color:#B9F6CA;">El Algoritmo de Control</h4>
                <p style="font-size:14px; margin:0; color:#E0E6ED;">La implementación de software interactivo (EcoWeb) y simulación analítica de datos como centro neurálgico del Proyecto.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 7 & SECCIÓN 8: SITUACIÓN ACTUAL VS PROYECCIÓN FUTURA
    col_act, col_fut = st.columns(2)
    
    with col_act:
        st.markdown('<div class="section-header">📍 6. Estado y Situación Actual</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 310px; border-left: 4px solid #00E676;">
                <p style="margin-top:0; color:#B9F6CA; font-weight:600; margin-bottom:15px;">Métricas consolidadas en tiempo real (2026):</p>
                <ul class="custom-list">
                    <li><strong>4 Secciones Técnicas</strong> operando en sincronía en las aulas-taller.</li>
                    <li><strong>7 Pilares Rectores</strong> auditando el 100% de los desarrollos.</li>
                    <li><strong>24 Fichas Estructurales</strong> completadas y subidas a la nube de EcoWeb.</li>
                    <li><strong>Herramientas Activas:</strong> Interfaz Streamlit, Base documental en la nube, Módulo de prompts EcoIA.</li>
                    <li><strong>Equipo Estable:</strong> Alumnos de 4° 4° encuadrados en el esquema riguroso de Reconocidos.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with col_fut:
        st.markdown('<div class="section-header">🔮 7. Visión de Crecimiento y Proyecciones</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 310px; border-left: 4px solid #64FFDA;">
                <p style="margin-top:0; color:#64FFDA; font-weight:600; margin-bottom:15px;">Hacia dónde se proyecta el engranaje sistémico:</p>
                <ul class="custom-list">
                    <li><strong>Nuevas Fichas:</strong> Indexar hasta 40 protocolos técnicos abarcando biodigestores complejos.</li>
                    <li><strong>Replicación Institucional:</strong> Exportar los manuales empaquetados para implementarlos en otras escuelas técnicas del distrito.</li>
                    <li><strong>Expansión Digital:</strong> Evolucionar la plataforma hacia una aplicación móvil de monitoreo IoT nativa.</li>
                    <li><strong>EcoCommunity:</strong> Lanzar de forma oficial la división de extensión e impacto en barrios y comedores de la zona.</li>
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
# PÁGINA 6 — FICHAS TÉCNICAS
# ==========================================
elif selected == "Fichas Técnicas":
    
    st.markdown('<div class="main-title">FICHAS TÉCNICAS</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Biblioteca de Conocimiento Estandarizado y Protocolos de Ingeniería Sustentable</div>', unsafe_allow_html=True)
    
    # Diccionario Oficial de Fichas del Proyecto
    FICHAS = {
        "1": {"titulo": "Papel Seed", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1S5sREmBrapKftJM5z8iZjtj46rLXer0t/view?usp=sharing", "desc": "Papel artesanal biodegradable con semillas incorporadas."},
        "2": {"titulo": "FibroPapel", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1JV_LZ_25r-gyqP27gndXCKweqzovfaiN/view?usp=sharing", "desc": "Papel compuesto reforzado con fibras textiles de algodón."},
        "3": {"titulo": "Manual del Reciclador", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1icRZmLchhPNXkbqHRKe3rsGF2yQdsXHq/view?usp=sharing", "desc": "Documento técnico educativo 100% sustentable."},
        "4": {"titulo": "Marca-Páginas", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1LVUYPIBTA6mY61HVtQn7f15ud1sw-3Rv/view?usp=sharing", "desc": "Souvenir funcional de cartón recuperado."},
        "5": {"titulo": "Eco-Carrier", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1q2m3efrr3WPZtJ_a__8YZ6m42nK-3y31/view?usp=sharing", "desc": "Bolsas estructurales que reemplazan el plástico de un solo uso."},
        "6": {"titulo": "Colorantes Naturales", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1EGy35MOOpkKR3-ksINjzhkurokfqwdWz/view?usp=sharing", "desc": "Extracción de pigmentos puros de residuos vegetales y cáscaras."},
        "7": {"titulo": "EcoIA", "division": "EcoTech", "drive_url": "https://drive.google.com/file/d/1H0seDIImClVjA5UrHELyucapO9DzXrHH/view?usp=sharing", "desc": "Asistente inteligente de documentación técnica y auditoría sustentable."},
        "8": {"titulo": "Organizadores Ecomodulares", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1sJP_u9-UgqRWkXk3f3PsvUVzLCa93Uow/view?usp=sharing", "desc": "Sistemas de ordenamiento de escritorio mediante latas y tubos."},
        "9": {"titulo": "Eco-Estelar", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/15qlgSz3v6YOLmHTWVmubTMknKM0WVUNS/view?usp=sharing", "desc": "Lámparas decorativas perforadas mediante técnica avanzada de congelado."},
        "10": {"titulo": "EcoChallenge", "division": "Transversal", "drive_url": "https://drive.google.com/file/d/1n6C2rPadtw662DZfogxJagQrbVvhem90/view?usp=sharing", "desc": "Sistema transversal de desafíos interactivos aplicable a todas las áreas."},
        "11": {"titulo": "Eco-Hidro", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1q5ImtWBOhHfztDthNQs1yPdmIiK3zZYJ/view?usp=sharing", "desc": "Módulo de riego autónomo por capilaridad optimizado en botellas PET."},
        "12": {"titulo": "EcoTrash", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1XdaHhW7Z5nzfBHBr3dj7I-N0HNQuLp8k/view?usp=sharing", "desc": "Escoba técnica de alta resistencia construida con cerdas de PET alineadas."},
        "13": {"titulo": "EcoWallet", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1xWXIx2TAa1QJU2izv0KwqhtEiZSo4GvW/view?usp=sharing", "desc": "Billetera impermeable mediante upcycling estructurado de Tetra Pak."},
        "14": {"titulo": "Carbon Ink", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1njzGFWQbRuRo-_ucORzZMYceuOE6uoOt/view?usp=sharing", "desc": "Tinta negra premium obtenida por pirólisis controlada de papel sucio."},
        "15": {"titulo": "Nendo Dango", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1NO2FaJdNvlYZA9X8PKMSUAZ8gXJ4PzG8/view?usp=sharing", "desc": "Bolas de arcilla, sustrato y semillas para reforestación masiva guiada."},
        "16": {"titulo": "EcoWear", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1tDOsmBio3hPoLzTVGfHzaauTz-wmhEtf/view?usp=sharing", "desc": "Cuentas estructurales y elementos decorativos de papel enrollado."},
        "17": {"titulo": "Eco-Voz", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1xh5hOjk_HXqaMcFr431Od3z15norhe1q/view?usp=sharing", "desc": "Amplificador acústico pasivo diseñado en cartón corrugado."},
        "18": {"titulo": "Cañón Vortex", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1h8tS94N0edR9Tw7GU94dummpULnt32zi/view?usp=sharing", "desc": "Generador físico de anillos de aire para demostración de dinámica de fluidos."},
        "19": {"titulo": "Eco-Dollars", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1xQSQpyuVH-YSgtjWZYahVeterC99rX70/view?usp=sharing", "desc": "Sistema monetario de economía circular impreso sobre papel reciclado propio."},
        "20": {"titulo": "EcoVolt", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1OmhWYiMxZvxMxHFRO7slATfgt_Brwhui/view?usp=sharing", "desc": "Generación teórica de energía limpia aprovechando el gradiente salino (agua dulce y salada)."},
        "21": {"titulo": "EcoCristales", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1jQwwWbwoUoq3xlcBYY5aVB1WoOieLQ30/view?usp=sharing", "desc": "Cristalización de alumbre orientada al estudio de la geometría química."},
        "22": {"titulo": "Biogás", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1m4l9L2Y5sXrWz2KlmgfjfDii76ZwBtS6/view?usp=sharing", "desc": "Investigación avanzada sobre digestión anaeróbica y captura de metano."},
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
                <span style="color:#FFD54F; font-weight:bold;">⚠️ Ruptura de conceptos tradicionales:</span>
                <ul style="margin-top:5px; padding-left:20px; font-size:14px; color:#E0E6ED;">
                    <li><strong>No es un apunte:</strong> No contiene anotaciones informales o fragmentadas.</li>
                    <li><strong>No es un informe:</strong> No narra un suceso pasado; es una guía de ejecución viva.</li>
                    <li><strong>No es una presentación:</strong> No resume ideas superficiales para exposición visual.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
    with col_por:
        st.markdown('<div class="section-header">🛡️ 2. ¿Por qué usamos Fichas Técnicas?</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 330px;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:15px;">Problemas de la educación tradicional que soluciona:</p>
                <div class="info-item"><span style="color:#64FFDA;">✦</span> <strong>Mitiga la fuga de cerebros:</strong> Evita la pérdida del conocimiento acumulado cuando los alumnos de último año egresan.</div>
                <div class="info-item"><span style="color:#64FFDA;">✦</span> <strong>Destruye personalismos:</strong> El proyecto ya no depende de un alumno o docente líder específico; la ficha empodera a cualquiera.</div>
                <div class="info-item"><span style="color:#64FFDA;">✦</span> <strong>Garantiza Continuidad:</strong> Permite retomar un desarrollo exactamente en el mismo punto técnico donde se dejó el ciclo anterior.</div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 3: ESTRUCTURA OFICIAL (Desplegables de anatomía de una ficha)
    st.markdown('<div class="section-header">📐 3. Anatomía Estructural de los Documentos</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A5D6A7; margin-bottom:12px;">Cada una de las 24 fichas del sistema se redacta bajo la misma matriz de campos obligatorios:</p>', unsafe_allow_html=True)
    
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
        st.markdown('<div class="section-header">🔄 5. Ciclo de Vida de una Ficha</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 340px; display:flex; flex-direction:column; justify-content:center;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:15px; text-align:center;">Flujo Evolutivo del Documento:</p>
                <div style="display:flex; justify-content:space-between; align-items:center; text-align:center; font-size:12.5px;">
                    <div style="background:rgba(255,255,255,0.03); padding:8px; border-radius:6px; width:15%;"><strong>Idea</strong><br><span style="color:#64FFDA;">Captura</span></div>
                    <div style="color:#00E676;">➔</div>
                    <div style="background:rgba(255,255,255,0.03); padding:8px; border-radius:6px; width:16%;"><strong>Desarrollo</strong><br><span style="color:#00E676;">Laboratorio</span></div>
                    <div style="color:#00E676;">➔</div>
                    <div style="background:rgba(255,255,255,0.03); padding:8px; border-radius:6px; width:15%;"><strong>Prueba</strong><br><span style="color:#B9F6CA;">Ensayo</span></div>
                    <div style="color:#00E676;">➔</div>
                    <div style="background:rgba(255,255,255,0.03); padding:8px; border-radius:6px; width:18%;"><strong>Documentación</strong><br><span style="color:#69F0AE;">Ficha</span></div>
                    <div style="color:#00E676;">➔</div>
                    <div style="background:rgba(255,255,255,0.03); padding:8px; border-radius:6px; width:15%;"><strong>Mejora</strong><br><span style="color:#A5D6A7;">Optimización</span></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 4 & SECCIÓN 7: BIBLIOTECA DE CONOCIMIENTO (La base interactiva con tus links)
    st.markdown('<div class="section-header">📚 6. Biblioteca Interactiva: Base Documental del Ecosistema</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A5D6A7; margin-bottom:15px;">Filtra y accede directamente a los documentos de ingeniería alojados de forma segura en Google Drive:</p>', unsafe_allow_html=True)
    
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

    # DICCIONARIO OPTIMIZADO CON METADATOS TÉCNICOS PARA FILTRADO AVANZADO
    FICHAS_AVANZADAS = {
        "1": {"titulo": "Papel Seed", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1S5sREmBrapKftJM5z8iZjtj46rLXer0t/view?usp=sharing", "desc": "Papel artesanal biodegradable con semillas incorporadas.", "dificultad": "Inicial", "concepto": "Sustentabilidad", "estado": "Producción Estable", "siguiente": "2"},
        "2": {"titulo": "FibroPapel", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1JV_LZ_25r-gyqP27gndXCKweqzovfaiN/view?usp=sharing", "desc": "Papel compuesto reforzado con fibras textiles de algodón.", "dificultad": "Básico", "concepto": "Reciclaje", "estado": "Producción Estable", "siguiente": "5"},
        "3": {"titulo": "Manual del Reciclador", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1icRZmLchhPNXkbqHRKe3rsGF2yQdsXHq/view?usp=sharing", "desc": "Documento técnico educativo 100% sustentable.", "dificultad": "Inicial", "concepto": "Sustentabilidad", "estado": "Completado", "siguiente": "10"},
        "4": {"titulo": "Marca-Páginas", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1LVUYPIBTA6mY61HVtQn7f15ud1sw-3Rv/view?usp=sharing", "desc": "Souvenir funcional de cartón recuperado.", "dificultad": "Inicial", "concepto": "Reciclaje", "estado": "Producción Estable", "siguiente": "3"},
        "5": {"titulo": "Eco-Carrier", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1q2m3efrr3WPZtJ_a__8YZ6m42nK-3y31/view?usp=sharing", "desc": "Bolsas estructurales que reemplazan el plástico de un solo uso.", "dificultad": "Básico", "concepto": "Sustentabilidad", "estado": "Optimización", "siguiente": "13"},
        "6": {"titulo": "Colorantes Naturales", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1EGy35MOOpkKR3-ksINjzhkurokfqwdWz/view?usp=sharing", "desc": "Extracción de pigmentos puros de residuos vegetales.", "dificultad": "Intermedio", "concepto": "Química", "estado": "Ensayos Clínicos", "siguiente": "14"},
        "7": {"titulo": "EcoIA", "division": "EcoTech", "drive_url": "https://drive.google.com/file/d/1H0seDIImClVjA5UrHELyucapO9DzXrHH/view?usp=sharing", "desc": "Asistente inteligente de documentación técnica y auditoría.", "dificultad": "Avanzado", "concepto": "Tecnología", "estado": "Fase Beta", "siguiente": "23"},
        "8": {"titulo": "Organizadores Ecomodulares", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1sJP_u9-UgqRWkXk3f3PsvUVzLCa93Uow/view?usp=sharing", "desc": "Sistemas de ordenamiento mediante latas y tubos.", "dificultad": "Inicial", "concepto": "Reciclaje", "estado": "Producción Estable", "siguiente": "9"},
        "9": {"titulo": "Eco-Estelar", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/15qlgSz3v6YOLmHTWVmubTMknKM0WVUNS/view?usp=sharing", "desc": "Lámparas decorativas perforadas mediante técnica avanzada de congelado.", "dificultad": "Intermedio", "concepto": "Tecnología", "estado": "Optimización", "siguiente": "17"},
        "10": {"titulo": "EcoChallenge", "division": "Transversal", "drive_url": "https://drive.google.com/file/d/1n6C2rPadtw662DZfogxJagQrbVvhem90/view?usp=sharing", "desc": "Sistema transversal de desafíos interactivos inter-áreas.", "dificultad": "Básico", "concepto": "Sustentabilidad", "estado": "Completado", "siguiente": "19"},
        "11": {"titulo": "Eco-Hidro", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1q5ImtWBOhHfztDthNQs1yPdmIiK3zZYJ/view?usp=sharing", "desc": "Módulo de riego autónomo por capilaridad optimizado en botellas PET.", "dificultad": "Básico", "concepto": "Tecnología", "estado": "Producción Estable", "siguiente": "24"},
        "12": {"titulo": "EcoTrash", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1XdaHhW7Z5nzfBHBr3dj7I-N0HNQuLp8k/view?usp=sharing", "desc": "Escoba técnica de alta resistencia construida con cerdas de PET.", "dificultad": "Básico", "concepto": "Reciclaje", "estado": "Producción Estable", "siguiente": "8"},
        "13": {"titulo": "EcoWallet", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1xWXIx2TAa1QJU2izv0KwqhtEiZSo4GvW/view?usp=sharing", "desc": "Billetera impermeable mediante upcycling estructurado de Tetra Pak.", "dificultad": "Inicial", "concepto": "Reciclaje", "estado": "Producción Estable", "siguiente": "4"},
        "14": {"titulo": "Carbon Ink", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1njzGFWQbRuRo-_ucORzZMYceuOE6uoOt/view?usp=sharing", "desc": "Tinta negra premium obtenida por pirólisis controlada.", "dificultad": "Avanzado", "concepto": "Química", "estado": "Ensayos Clínicos", "siguiente": "21"},
        "15": {"titulo": "Nendo Dango", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1NO2FaJdNvlYZA9X8PKMSUAZ8gXJ4PzG8/view?usp=sharing", "desc": "Bolas de arcilla, sustrato y semillas para reforestación guiada.", "dificultad": "Inicial", "concepto": "Sustentabilidad", "estado": "Producción Estable", "siguiente": "1"},
        "16": {"titulo": "EcoWear", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1tDOsmBio3hPoLzTVGfHzaauTz-wmhEtf/view?usp=sharing", "desc": "Cuentas estructurales y elementos decorativos de papel enrollado.", "dificultad": "Inicial", "concepto": "Reciclaje", "estado": "Producción Estable", "siguiente": "13"},
        "17": {"titulo": "Eco-Voz", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1xh5hOjk_HXqaMcFr431Od3z15norhe1q/view?usp=sharing", "desc": "Amplificador acústico pasivo diseñado en cartón corrugado.", "dificultad": "Básico", "concepto": "Tecnología", "estado": "Producción Estable", "siguiente": "18"},
        "18": {"titulo": "Cañón Vortex", "division": "EcoIndustria", "drive_url": "https://drive.google.com/file/d/1h8tS94N0edR9Tw7GU94dummpULnt32zi/view?usp=sharing", "desc": "Generador físico de anillos de aire para dinámica de fluidos.", "dificultad": "Intermedio", "concepto": "Tecnología", "estado": "Optimización", "siguiente": "7"},
        "19": {"titulo": "Eco-Dollars", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1xQSQpyuVH-YSgtjWZYahVeterC99rX70/view?usp=sharing", "desc": "Sistema monetario de economía circular impreso sobre papel reciclado.", "dificultad": "Intermedio", "concepto": "Sustentabilidad", "estado": "Completado", "siguiente": "23"},
        "20": {"titulo": "EcoVolt", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1OmhWYiMxZvxMxHFRO7slATfgt_Brwhui/view?usp=sharing", "desc": "Generación teórica de energía limpia aprovechando el gradiente salino.", "dificultad": "Avanzado", "concepto": "Energía", "estado": "Investigación", "siguiente": "22"},
        "21": {"titulo": "EcoCristales", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1jQwwWbwoUoq3xlcBYY5aVB1WoOieLQ30/view?usp=sharing", "desc": "Cristalización de alumbre orientada al estudio de la geometría química.", "dificultad": "Intermedio", "concepto": "Química", "estado": "Ensayos Clínicos", "siguiente": "20"},
        "22": {"titulo": "Biogás", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1m4l9L2Y5sXrWz2KlmgfjfDii76ZwBtS6/view?usp=sharing", "desc": "Investigación avanzada sobre digestión anaeróbica y captura de metano.", "dificultad": "Avanzado", "concepto": "Energía", "estado": "Investigación", "siguiente": "24"},
        "23": {"titulo": "EcoMod", "division": "EcoTech", "drive_url": "https://drive.google.com/file/d/13qfQNtrsH1iAjTEAck-LrFfluuHgZZGf/view?usp=sharing", "desc": "Módulo interactivo de reciclaje y economía circular en entornos virtuales.", "dificultad": "Intermedio", "concepto": "Tecnología", "estado": "Fase Beta", "siguiente": "7"},
        "24": {"titulo": "TerrarIA", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1P3r5UlcdPS4KWDcuYPN45qJWmD_KTBDu/view?usp=sharing", "desc": "Ecosistema cerrado automatizado y monitoreado por sensores.", "dificultad": "Avanzado", "concepto": "Tecnología", "estado": "Optimización", "siguiente": "11"},
    }

    # SECCIÓN 1: INTRODUCCIÓN
    st.markdown('<div class="section-header">🔍 ¿Para qué sirve el Explorador Eco?</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="font-size: 16px; border-left: 5px solid #00E676;">
        Debido a que el volumen documental de <strong>Proyecto Eco</strong> cuenta con múltiples vertientes de ingeniería, esta central inteligente permite realizar consultas analíticas cruzadas. El usuario puede mapear y filtrar el conocimiento según la división responsable, la complejidad de ejecución o el eje conceptual científico, garantizando que la información justa llegue al operador adecuado.
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 2: ESTADÍSTICAS GENERALES (Cálculos automáticos en base al diccionario)
    st.markdown('<div class="section-header">📈 1. Auditoría Automatizada de la Biblioteca</div>', unsafe_allow_html=True)
    
    # Procesamiento de variables en background
    tot_fichas = len(FICHAS_AVANZADAS)
    secciones = set(f["division"] for f in FICHAS_AVANZADAS.values())
    conceptos = set(f["concepto"] for f in FICHAS_AVANZADAS.values())
    niveles = set(f["dificultad"] for f in FICHAS_AVANZADAS.values())
    
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:28px; font-weight:bold; color:#00E676;">{tot_fichas}</span><br><span style="font-size:13px; color:#B0BEC5;">Fichas Totales</span></div>', unsafe_allow_html=True)
    with col_m2:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:28px; font-weight:bold; color:#64FFDA;">{len(secciones)}</span><br><span style="font-size:13px; color:#B0BEC5;">Secciones Eco</span></div>', unsafe_allow_html=True)
    with col_m3:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:28px; font-weight:bold; color:#FFD54F;">{len(conceptos)}</span><br><span style="font-size:13px; color:#B0BEC5;">Ejes Científicos</span></div>', unsafe_allow_html=True)
    with col_m4:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:28px; font-weight:bold; color:#A5D6A7;">{len(niveles)}</span><br><span style="font-size:13px; color:#B0BEC5;">Niveles Complejidad</span></div>', unsafe_allow_html=True)

    # SECCIÓN 3, 4 & 5: PANEL DE FILTROS CRUZADOS EN COLUMNAS (Interactivos)
    st.markdown('<div class="section-header">🎛️ 2. Panel de Segmentación de Conocimiento</div>', unsafe_allow_html=True)
    
    col_f1, col_f2, col_f3 = st.columns(3)
    
    with col_f1:
        filtro_sec = st.selectbox("📂 Filtrar por División Responsable:", ["Todas"] + sorted(list(secciones)))
    with col_f2:
        filtro_dif = st.selectbox("⚡ Filtrar por Nivel de Dificultad:", ["Todas", "Inicial", "Básico", "Intermedio", "Avanzado"])
    with col_f3:
        filtro_con = st.selectbox("🔬 Filtrar por Concepto / Eje Base:", ["Todas"] + sorted(list(conceptos)))

    # SECCIÓN 6: RENDERIZADO DE FILTRADO EN MATRIZ DE TARJETAS PREMIUN
    st.markdown('<div class="section-header">📋 3. Fichas Técnicas Encontradas</div>', unsafe_allow_html=True)
    
    tarjetas_renderizadas = 0
    
    # Grid de ejecución lógica
    for k, f in FICHAS_AVANZADAS.items():
        # Lógica cruzada de discriminación de filtros
        if filtro_sec != "Todas" and f["division"] != filtro_sec:
            continue
        if filtro_dif != "Todas" and f["dificultad"] != filtro_dif:
            continue
        if filtro_con != "Todas" and f["concepto"] != filtro_con:
            continue
            
        tarjetas_renderizadas += 1
        
        # Color del badge por dificultad
        color_dif = "#81C784" if f["dificultad"] == "Inicial" else "#4CAF50" if f["dificultad"] == "Básico" else "#FFD54F" if f["dificultad"] == "Intermedio" else "#EF5350"
        
        # Tarjeta HTML Premium
        st.markdown(f"""
            <div class="glass-card" style="margin-bottom: 15px; border-left: 5px solid {color_dif};">
                <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px;">
                    <div>
                        <span style="font-size: 12px; font-weight: bold; text-transform: uppercase; color: #64FFDA; letter-spacing: 0.5px;">[{f['division']}]</span>
                        <h3 style="margin: 3px 0; color: #FFFFFF; font-size: 19px;">Ficha N°{k}: {f['titulo']}</h3>
                    </div>
                    <div style="text-align: right;">
                        <span style="background: rgba(255,255,255,0.05); color: {color_dif}; border: 1px solid {color_dif}; padding: 2px 8px; border-radius: 4px; font-size: 11px; font-weight: bold;">{f['dificultad']}</span>
                        <br><span style="font-size: 11px; color: #90A4AE; display:block; margin-top:4px;">{f['estado']}</span>
                    </div>
                </div>
                <p style="margin: 0 0 12px 0; color: #CFD8DC; font-size: 14.5px; line-height:1.4;">{f['desc']}</p>
                <div style="display: flex; justify-content: space-between; align-items: center; background: rgba(0,0,0,0.15); padding: 8px 12px; border-radius: 6px;">
                    <span style="font-size: 13px; color: #A5D6A7;">🧬 Concepto Clave: <strong>{f['concepto']}</strong></span>
                    <a href="{f['drive_url']}" target="_blank" style="text-decoration: none; font-weight: bold; color: #00E676; font-size: 13px;">Ver Manual Técnico Completo ↗</a>
                </div>
            </div>
        """, unsafe_allow_html=True)

    if tarjetas_renderizadas == 0:
        st.info("Ninguna ficha técnica cumple simultáneamente con los tres criterios seleccionados en el panel.")

    # SECCIÓN 7: RUTA DE APRENDIZAJE SUGERIDA (Lógica de grafos y secuencias lineales recomendadas)
    st.markdown('<div class="section-header">🛤️ 4. Rutas de Aprendizaje Sugeridas</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A5D6A7; font-size:14px; margin-bottom:12px;">Sistemas encadenados por correlatividad de ingeniería:</p>', unsafe_allow_html=True)
    
    st.markdown("""
        <div class="glass-card" style="padding: 15px;">
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px;">
                <div style="background: rgba(0,0,0,0.15); padding: 12px; border-radius: 8px; border-left: 3px solid #64FFDA;">
                    <span style="color:#64FFDA; font-weight:bold; font-size:14px;">🌱 Línea Celulosa Sostenible</span><br>
                    <span style="font-size:13px; color:#E0E6ED;">Comenzar con <strong>Ficha 3 (Manual)</strong> ➔ Continuar con <strong>Ficha 1 (Papel Seed)</strong> ➔ Escalar a <strong>Ficha 2 (FibroPapel)</strong>.</span>
                </div>
                <div style="background: rgba(0,0,0,0.15); padding: 12px; border-radius: 8px; border-left: 3px solid #FFD54F;">
                    <span style="color:#FFD54F; font-weight:bold; font-size:14px;">🧪 Línea Química Aplicada</span><br>
                    <span style="font-size:13px; color:#E0E6ED;">Iniciar en <strong>Ficha 6 (Colorantes)</strong> ➔ Avanzar a <strong>Ficha 14 (Carbon Ink)</strong> ➔ Consolidar en <strong>Ficha 21 (EcoCristales)</strong>.</span>
                </div>
                <div style="background: rgba(0,0,0,0.15); padding: 12px; border-radius: 8px; border-left: 3px solid #EF5350;">
                    <span style="color:#EF5350; font-weight:bold; font-size:14px;">💻 Ecosistema IoT y Automatización</span><br>
                    <span style="font-size:13px; color:#E0E6ED;">Comprender <strong>Ficha 7 (EcoIA)</strong> ➔ Integrar con <strong>Ficha 23 (EcoMod Minecraft)</strong> ➔ Desplegar en <strong>Ficha 24 (TerrarIA)</strong>.</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 8: EXPLORACIÓN ALEATORIA (Botón dinámico interactivo con Session State)
    st.markdown('<div class="section-header">🎲 5. Descubrimiento de Conocimiento Aleatorio</div>', unsafe_allow_html=True)
    
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
# PÁGINA 8 — IMPACTO ECO
# ==========================================
elif selected == "Impacto Eco":
    
    st.markdown('<div class="main-title">IMPACTO ECO</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Auditoría de Resultados Metodológicos, Alcance de Infraestructura y Métricas de Evolución</div>', unsafe_allow_html=True)

    # Base de datos local para cálculos analíticos de impacto (Sincronizada con Fichas Avanzadas)
    FICHAS_IMPACTO = {
        "1": {"division": "EcoPaper", "concepto": "Sustentabilidad", "tipo": "Producto"},
        "2": {"division": "EcoPaper", "concepto": "Reciclaje", "tipo": "Producto"},
        "3": {"division": "EcoPaper", "concepto": "Sustentabilidad", "tipo": "Manual"},
        "4": {"division": "EcoPaper", "concepto": "Reciclaje", "tipo": "Producto"},
        "5": {"division": "EcoPaper", "concepto": "Sustentabilidad", "tipo": "Producto"},
        "6": {"division": "EcoLab", "concepto": "Química", "tipo": "Experimento"},
        "7": {"division": "EcoTech", "concepto": "Tecnología", "tipo": "Sistema Digital"},
        "8": {"division": "EcoIndustria", "concepto": "Reciclaje", "tipo": "Producto"},
        "9": {"division": "EcoIndustria", "concepto": "Tecnología", "tipo": "Producto"},
        "10": {"division": "Transversal", "concepto": "Sustentabilidad", "tipo": "Sistema"},
        "11": {"division": "EcoIndustria", "concepto": "Tecnología", "tipo": "Producto"},
        "12": {"division": "EcoIndustria", "concepto": "Reciclaje", "tipo": "Producto"},
        "13": {"division": "EcoIndustria", "concepto": "Reciclaje", "tipo": "Producto"},
        "14": {"division": "EcoLab", "concepto": "Química", "tipo": "Experimento"},
        "15": {"division": "EcoLab", "concepto": "Sustentabilidad", "tipo": "Experimento"},
        "16": {"division": "EcoPaper", "concepto": "Reciclaje", "tipo": "Producto"},
        "17": {"division": "EcoIndustria", "concepto": "Tecnología", "tipo": "Producto"},
        "18": {"division": "EcoIndustria", "concepto": "Tecnología", "tipo": "Experimento"},
        "19": {"division": "EcoPaper", "concepto": "Sustentabilidad", "tipo": "Sistema"},
        "20": {"division": "EcoLab", "concepto": "Energía", "tipo": "Investigación"},
        "21": {"division": "EcoLab", "concepto": "Química", "tipo": "Experimento"},
        "22": {"division": "EcoLab", "concepto": "Energía", "tipo": "Investigación"},
        "23": {"division": "EcoTech", "concepto": "Tecnología", "tipo": "Sistema Digital"},
        "24": {"division": "EcoLab", "concepto": "Tecnología", "tipo": "Sistema"},
    }

    # SECCIÓN 1: INTRODUCCIÓN AL IMPACTO ECO
    st.markdown('<div class="section-header">🌍 ¿Qué significa "Impacto" para Proyecto Eco?</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card" style="font-size: 16px; border-left: 5px solid #64FFDA; line-height:1.6;">
        Para nuestra comunidad técnica, el <strong>Impacto Eco</strong> no es una simple métrica de kilos de papel acumulados en un depósito. Entendemos el impacto como una <strong>matriz sistémica e interdisciplinaria</strong>. Una verdadera solución ambiental es aquella que transforma la cultura de una institución, automatiza el acceso al conocimiento, promueve la regularidad del alumnado mediante incentivos de gestión y blinda los procesos para que trasciendan el ciclo lectivo vigente.
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 8: INDICADORES GENERALES (Panel de Control Analítico Inicial)
    st.markdown('<div class="section-header">📊 1. Panel Global de Indicadores de Gestión (KPIs)</div>', unsafe_allow_html=True)
    
    # Pre-cálculos analíticos automáticos sobre el diccionario
    num_fichas = len(FICHAS_IMPACTO)
    num_conceptos = len(set(f["concepto"] for f in FICHAS_IMPACTO.values()))
    num_experimentos = len([f for f in FICHAS_IMPACTO.values() if f["tipo"] in ["Experimento", "Investigación"]])
    
    col_k1, col_k2, col_k3, col_k4 = st.columns(4)
    with col_k1:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:26px; font-weight:bold; color:#00E676;">{num_fichas}</span><br><span style="font-size:12px; color:#CFD8DC;">Fichas de Ingeniería</span></div>', unsafe_allow_html=True)
    with col_k2:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:26px; font-weight:bold; color:#64FFDA;">{num_conceptos}</span><br><span style="font-size:12px; color:#CFD8DC;">Ejes Científicos</span></div>', unsafe_allow_html=True)
    with col_k3:
        st.markdown(f'<div class="glass-card" style="text-align:center;"><span style="font-size:26px; font-weight:bold; color:#FFD54F;">{num_experimentos}</span><br><span style="font-size:12px; color:#CFD8DC;">Ensayos de Lab</span></div>', unsafe_allow_html=True)
    with col_k4:
        st.markdown('<div class="glass-card" style="text-align:center;"><span style="font-size:26px; font-weight:bold; color:#B9F6CA;">4</span><br><span style="font-size:12px; color:#CFD8DC;">Divisiones Activas</span></div>', unsafe_allow_html=True)

    # SECCIÓN 2 & SECCIÓN 3: IMPACTO EN PARTICIPANTES Y CONOCIMIENTO
    col_part, col_cono = st.columns(2)
    
    with col_part:
        st.markdown('<div class="section-header">👥 2. Transformación Humana y Alumnado</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 310px;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:12px;">Métricas del Capital Humano Estructurado (4° 4°):</p>
                <div class="info-item"><strong>Participantes Operativos Activos:</strong> El 100% de la división técnica involucrada en laboratorios.</div>
                <div class="info-item"><strong>Alumnos Reconocidos Auditados:</strong> Sistema cerrado con asignación de puntaje por mérito técnico semanal.</div>
                <div class="info-item"><strong>Estructura de Líderes de Celda:</strong> 4 Jefes de Sección encargados de velar por la seguridad y calidad en contraturno.</div>
                <div class="info-item"><strong>Evolución Histórica:</strong> De una participación informal y fragmentada en 2025 a un organigrama de ingeniería industrial en 2026.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_cono:
        st.markdown('<div class="section-header">🧠 3. Capital Intelectual Producido</div>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="glass-card" style="height: 310px;">
                <p style="margin-top:0; color:#81C784; font-weight:600; margin-bottom:12px;">Resultados de la Producción Científica Acumulada:</p>
                <ul class="custom-list" style="font-size:14px; line-height:1.6;">
                    <li><strong>Estandarización Absoluta:</strong> {num_fichas} protocolos subidos a la infraestructura de la nube.</li>
                    <li><strong>Transferencia de Experiencia:</strong> Rompe la dependencia del personalismo docente; la información le pertenece al taller.</li>
                    <li><strong>Recursos Libres Desarrollos:</strong> Repositorio abierto para que cursos entrantes sigan los manuales de procedimientos paso a paso.</li>
                    <li><strong>Marcos Epistemológicos:</strong> Vinculación directa con papers de pirólisis, termodinámica y ciencias químicas básicas.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 4: IMPACTO ORGANIZATIVO (Herramientas y Sistemas Propios)
    st.markdown('<div class="section-header">🏗️ 4. Infraestructura Organizativa y Herramientas Creadas</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="glass-card">
        <p style="margin-top:0; color:#A5D6A7; font-weight:600;">Sistemas de control lógico desarrollados desde cero para el soporte institucional:</p>
        <table class="custom-table" style="font-size:14px;">
            <thead>
                <tr>
                    <th style="width: 25%;">Sistema / Herramienta</th>
                    <th style="width: 75%;">Función Operativa y Aporte Organizacional</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Los 7 Pilares Eco</strong></td>
                    <td>La constitución dogmática técnica que audita que todo proyecto sea Continuo, Replicable y Medible.</td>
                </tr>
                <tr>
                    <td><strong>Sistema de Reconocidos</strong></td>
                    <td>Algoritmo de gamificación conductual que premia la regularidad, el orden de banco y los hitos de laboratorio.</td>
                </tr>
                <tr>
                    <td><strong>El Flujo Eco</strong></td>
                    <td>Protocolo logístico interno que conecta los residuos plásticos y de celulosa del colegio con las celdas de refinamiento.</td>
                </tr>
                <tr>
                    <td><strong>Plataforma EcoWeb</strong></td>
                    <td>Interfaz de software interactiva (Streamlit) utilizada para centralizar los indicadores ante entes evaluadores.</td>
                </tr>
                <tr>
                    <td><strong>Módulo EcoIA</strong></td>
                    <td>Entrenamiento de matrices de prompts para la asistencia automática en el diseño formal de nuevas fichas de ingeniería.</td>
                </tr>
            </tbody>
        </table>
        </div>
    """, unsafe_allow_html=True)

    # SECCIÓN 5: IMPACTO POR SECCIÓN (Distribución analítica automatizada de cargas técnicas)
    st.markdown('<div class="section-header">🏢 5. Rendimiento Operativo Descentralizado por División</div>', unsafe_allow_html=True)
    
    col_s1, col_s2, col_s3, col_s4 = st.columns(4)
    
    with col_s1:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(0, 230, 118, 0.2); padding: 15px; border-radius: 10px; height: 260px;">
                <h4 style="margin:0 0 8px 0; color:#00E676; text-align:center;">EcoPapel</h4>
                <p style="font-size:13px; color:#CFD8DC; line-height:1.4; margin:0;">
                <strong>Fichas:</strong> N°1 al N°5, N°16, N°19.<br><br>
                <strong>Eje:</strong> Recuperación de celulosa, Papel Seed de germinación y acuñación de Eco-Dollars.<br><br>
                <strong>Resultado:</strong> Sustitución total de hojas en desuso de preceptoría.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_s2:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(100, 255, 218, 0.2); padding: 15px; border-radius: 10px; height: 260px;">
                <h4 style="margin:0 0 8px 0; color:#64FFDA; text-align:center;">EcoLab</h4>
                <p style="font-size:13px; color:#CFD8DC; line-height:1.4; margin:0;">
                <strong>Fichas:</strong> N°6, N°14, N°15, N°20, N°21, N°22, N°24.<br><br>
                <strong>Eje:</strong> Pirólisis de Carbon Ink, ensayos de biogás metanogénico y soluciones salinas.<br><br>
                <strong>Resultado:</strong> Validación química y control físico de tolerancias.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_s3:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(255, 213, 79, 0.2); padding: 15px; border-radius: 10px; height: 260px;">
                <h4 style="margin:0 0 8px 0; color:#FFD54F; text-align:center;">EcoTech</h4>
                <p style="font-size:13px; color:#CFD8DC; line-height:1.4; margin:0;">
                <strong>Fichas:</strong> N°7, N°23.<br><br>
                <strong>Eje:</strong> Algoritmia computacional, programación de la arquitectura digital y modelado de entornos virtuales en Minecraft (EcoMod).<br><br>
                <strong>Resultado:</strong> Digitalización total del conocimiento operativo.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_s4:
        st.markdown("""
            <div style="background: rgba(255,255,255,0.02); border: 1px solid rgba(165, 214, 167, 0.2); padding: 15px; border-radius: 10px; height: 260px;">
                <h4 style="margin:0 0 8px 0; color:#A5D6A7; text-align:center;">EcoIndustria</h4>
                <p style="font-size:13px; color:#CFD8DC; line-height:1.4; margin:0;">
                <strong>Fichas:</strong> N°8, N°9, N°11, N°12, N°13, N°17, N°18.<br><br>
                <strong>Eje:</strong> Matricería mecánica, upcycling estructural de TetraPak/PET y amplificadores acústicos.<br><br>
                <strong>Resultado:</strong> Productos físicos de alta resistencia y utilidad escolar.
                </p>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 6 & SECCIÓN 7: IMPACTO AMBIENTAL Y EDUCATIVO
    col_amb, col_edu = st.columns(2)
    
    with col_amb:
        st.markdown('<div class="section-header">🍃 6. Vector e Impacto Ambiental Real</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 330px; border-left: 4px solid #00E676;">
                <p style="margin-top:0; color:#B9F6CA; font-weight:600; margin-bottom:12px;">Efectos Directos en Sustentabilidad y Reciclaje Técnico:</p>
                <div class="info-item">♻️ <strong>Mitigación de Desperdicio Rígido:</strong> Reciclado activo de botellas PET (cerdas para EcoTrash) y envases de TetraPak (EcoWallet impermeables).</div>
                <div class="info-item">♻️ <strong>Tratamiento Térmico Controlado:</strong> Reutilización de celulosa residual sucia mediante pirólisis confinada para la generación de tinta escolar (Carbon Ink).</div>
                <div class="info-item">♻️ <strong>Prácticas Promovidas:</strong> Concientización activa en la separación en origen dentro de los talleres y laboratorios de la E.E.S.T N°7.</div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_edu:
        st.markdown('<div class="section-header">🎓 7. Impacto Educativo e Interdisciplinar</div>', unsafe_allow_html=True)
        st.markdown("""
            <div class="glass-card" style="height: 330px; border-left: 4px solid #64FFDA;">
                <p style="margin-top:0; color:#64FFDA; font-weight:600; margin-bottom:12px;">Habilidades Profesionales y Fusión de Saberes:</p>
                <div class="info-item">🧠 <strong>Interdisciplinaridad Nativa:</strong> Amalgama orgánica de conceptos de Química Orgánica (EcoLab), Programación Estructurada (EcoTech), y Diseño de Procesos Industriales (EcoIndustria).</div>
                <div class="info-item">🧠 <strong>Habilidades Técnicas Clave:</strong> Redacción de protocolos normalizados, manejo riguroso de variables experimentales y pensamiento crítico orientado a fallos.</div>
                <div class="info-item">🧠 <strong>Aprendizaje Basado en Proyectos:</strong> El alumno deja de ser un receptor pasivo; se transforma en un diseñador activo de soluciones para su propia institución.</div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 9: PROYECCIÓN DE IMPACTO (Logrado vs Proyectado)
    st.markdown('<div class="section-header">🔮 8. Matriz de Proyección Temática y Escalabilidad</div>', unsafe_allow_html=True)
    
    col_log, col_proy = st.columns(2)
    with col_log:
        st.markdown("""
            <div style="background: rgba(76, 175, 80, 0.05); border: 1px solid #4CAF50; padding: 18px; border-radius: 12px; height: 180px;">
                <h4 style="margin: 0 0 10px 0; color:#81C784;">✅ Impacto Logrado (Consolidado 2026)</h4>
                <span style="font-size:14px; color:#E0E6ED; line-height:1.5;">
                • Estructuración matemática de 24 fichas de ingeniería.<br>
                • Lanzamiento funcional de la suite interactiva EcoWeb.<br>
                • Sistema de control conductual y académico por Reconocidos operando.
                </span>
            </div>
        """, unsafe_allow_html=True)
        
    with col_proy:
        st.markdown("""
            <div style="background: rgba(33, 150, 243, 0.05); border: 1px solid #2196F3; padding: 18px; border-radius: 12px; height: 180px;">
                <h4 style="margin: 0 0 10px 0; color:#64B5F6;">🚀 Impacto Proyectado (Escalabilidad Futura)</h4>
                <span style="font-size:14px; color:#E0E6ED; line-height:1.5;">
                • Exportación de la base documental empaquetada a otras escuelas técnicas del distrito.<br>
                • Migración del backend analítico hacia sensores IoT reales en tiempo de ejecución.<br>
                • Expansión formal de la división EcoCommunity para inserción en comedores barriales.
                </span>
            </div>
        """, unsafe_allow_html=True)

    # Footer institucional
    st.markdown("""
        <div style="text-align: center; margin-top: 40px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Auditoría General de Calidad y Resultados de Impacto • E.E.S.T N°7
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
                El Sistema de Reconocidos <strong>no es un concurso</strong>, una competencia meritocrática ni un esquema de exclusión jerárquica. Su diseño persigue un fin puramente humano y profesional: <strong>hacer visible el trabajo silencioso y constante</strong>.
                <br><br>
                <span style="color:#64FFDA; font-weight:bold;">Declaración de principios:</span>
                <ul style="margin-top:5px; padding-left:18px; font-size:13.5px; color:#E0E6ED; line-height:1.4;">
                    <li>No determina quién vale más o menos en los laboratorios.</li>
                    <li>No otorga privilegios de autoridad técnica arbitraria.</li>
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
                <div class="info-item"><strong>Invisibilidad de Contribuciones:</strong> Soluciona el clásico problema donde el trabajo técnico minucioso queda opacado por perfiles puramente expositores.</div>
                <div class="info-item"><strong>Desmotivación por Falta de Seguimiento:</strong> Rompe la apatía escolar al registrar formalmente cada hito, validando el tiempo invertido por el operador.</div>
            </div>
        """, unsafe_allow_html=True)

    # SECCIÓN 3 & SECCIÓN 4: FUNCIONAMIENTO GENERAL Y CRITERIOS OFICIALES
    st.markdown('<div class="section-header">⚙️ 3. Protocolo de Funcionamiento y Criterios de Evaluación</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:#A5D6A7; font-size:14px; margin-bottom:12px;">Mapeo claro y auditable del proceso de ponderación semanal:</p>', unsafe_allow_html=True)
    
    col_func, col_crit = st.columns([6, 4])
    
    with col_func:
        st.markdown("""
            <div class="glass-card" style="height: 330px; display:flex; flex-direction:column; justify-content:center;">
                <p style="margin-top:0; color:#A5D6A7; font-weight:600; margin-bottom:15px;">Las 4 Etapas del Registro Operativo:</p>
                <div style="font-size:13.5px; line-height:1.6; color:#E0E6ED;">
                    <strong>1. Bitácora de Asiento:</strong> Cada jefe de celda anota diariamente las tareas cumplidas en su sección.<br>
                    <strong>2. Evaluación Periódica:</strong> Reunión semanal inter-áreas para analizar la constancia y el mantenimiento del orden.<br>
                    <strong>3. Consolidación de Datos:</strong> Se cruzan las métricas conductuales con los objetivos de las fichas técnicas asignadas.<br>
                    <strong>4. Publicación en EcoWeb:</strong> Se formaliza el reconocimiento en la cartelera digital para conocimiento de toda la institución.
                </div>
            </div>
        """, unsafe_allow_html=True)
        
    with col_crit:
        st.markdown("""
            <div class="glass-card" style="height: 330px;">
                <p style="margin-top:0; color:#A5D6A7; font-weight:600; margin-bottom:12px;">Criterios Técnicos Evaluados:</p>
                <span style="font-size:13px; color:#CFD8DC;">Solo se consideran variables documentadas:</span>
                <div style="margin-top:8px; display:flex; flex-direction:column; gap:8px; font-size:13px;">
                    <div style="background:rgba(0,230,118,0.05); padding:6px; border-radius:4px; border-left:3px solid #00E676;">🤝 <strong>Colaboración Transversal</strong></div>
                    <div style="background:rgba(0,230,118,0.05); padding:6px; border-radius:4px; border-left:3px solid #00E676;">⏱️ <strong>Compromiso y Puntualidad</strong></div>
                    <div style="background:rgba(0,230,118,0.05); padding:6px; border-radius:4px; border-left:3px solid #00E676;">🧹 <strong>Responsabilidad y Seguridad</strong></div>
                    <div style="background:rgba(0,230,118,0.05); padding:6px; border-radius:4px; border-left:3px solid #00E676;">🔧 <strong>Cumplimiento Absoluto de Fichas</strong></div>
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
