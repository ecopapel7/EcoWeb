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

    selected = option_menu(
        menu_title=None,
        options=["Inicio", "Objetivo Eco", "Fundamentos Eco"],  # Agregamos la Página 3
        icons=["house-door-fill", "target", "diagram-3-fill"],   # Ícono de red/diagrama para fundamentos
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#00E676", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "color": "#E0E6ED", "text-align": "left", "margin":"5px 0px", "--hover-color": "rgba(0, 230, 118, 0.1)"},
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
    
    # Footer institucional 
    st.markdown("""
        <div style="text-align: center; margin-top: 50px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Escuela de Educación Secundaria Técnica N°7 • República Argentina
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
