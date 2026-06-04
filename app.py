import streamlit as st
from streamlit_option_menu import option_menu

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="EcoWeb 1.0 - Feria Tecnológica",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# ARQUITECTURA DE DISEÑO CSS AVANZADO (UI/UX)
# ==========================================
st.markdown("""
    <style>
    /* Importación de tipografía moderna */
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;700&family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
    
    * {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Fondo general y scroll personalizado */
    .stApp {
        background-color: #0B0F12;
    }
    
    /* Título Principal Neo-Glow */
    .hero-title {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 52px !important;
        font-weight: 800;
        background: linear-gradient(135deg, #A5D6A7 0%, #2E7D32 50%, #1B5E20 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -1px;
        margin-bottom: 0px;
        line-height: 1.2;
    }
    
    .hero-subtitle {
        font-family: 'JetBrains Mono', monospace;
        font-size: 16px !important;
        color: #81C784;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 30px;
    }
    
    /* Encabezados de Sección */
    .section-glow {
        font-size: 26px !important;
        font-weight: 700;
        color: #FFFFFF;
        border-left: 4px solid #4CAF50;
        padding-left: 15px;
        margin-top: 40px;
        margin-bottom: 20px;
    }
    
    /* Tarjeta Principal Interactiva (¿Qué es EcoWeb?) */
    .main-card {
        background: linear-gradient(145deg, #11181C 0%, #161F24 100%);
        border: 1px solid #233038;
        border-radius: 16px;
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .main-card:hover {
        transform: translateY(-3px);
        border-color: #4CAF50;
    }
    
    /* Tarjetas de Contenido Cuadrículas (Grid Cards) */
    .grid-card {
        background: #12181D;
        border: 1px solid #1C262C;
        border-radius: 12px;
        padding: 24px;
        height: 100%;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .grid-card:hover {
        background: #161F25;
        border-color: #388E3C;
        box-shadow: 0 10px 20px rgba(0,0,0,0.4);
    }
    
    /* Estilización de Listas con Iconos Tech */
    .tech-list-item {
        display: flex;
        align-items: flex-start;
        margin-bottom: 14px;
        font-size: 15px;
        color: #E2E8F0;
        line-height: 1.5;
    }
    .tech-icon {
        color: #4CAF50;
        margin-right: 12px;
        font-weight: bold;
        font-family: 'JetBrains Mono', monospace;
    }
    
    /* Tabla de Pilares Futurista mediante HTML puro */
    .custom-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0 8px;
        margin-top: 15px;
    }
    .custom-table th {
        background-color: #161F24;
        color: #81C784;
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        text-transform: uppercase;
        font-size: 13px;
        letter-spacing: 1px;
        padding: 16px;
        text-align: left;
        border-bottom: 2px solid #2E7D32;
    }
    .custom-table td {
        background-color: #11181C;
        color: #E2E8F0;
        padding: 16px;
        font-size: 15px;
        border-top: 1px solid #1C262C;
        border-bottom: 1px solid #1C262C;
    }
    .custom-table td:first-child {
        border-left: 1px solid #1C262C;
        border-radius: 8px 0 0 8px;
        font-weight: 600;
        color: #FFFFFF;
    }
    .custom-table td:last-child {
        border-right: 1px solid #1C262C;
        border-radius: 0 8px 8px 0;
    }
    .custom-table tr:hover td {
        background-color: #161F24;
        border-color: #4CAF50;
        color: #FFFFFF;
    }
    
    /* Métricas del Ecosistema Inferior */
    .metric-container {
        background: linear-gradient(180deg, #11181C 0%, #0D1316 100%);
        border: 1px solid #1C262C;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        transition: all 0.2s ease;
    }
    .metric-container:hover {
        border-color: #2E7D32;
    }
    .metric-num {
        font-family: 'JetBrains Mono', monospace;
        font-size: 32px;
        font-weight: 700;
        color: #4CAF50;
    }
    .metric-title {
        font-size: 16px;
        font-weight: 600;
        color: #FFFFFF;
        margin-top: 4px;
    }
    .metric-delta {
        font-size: 13px;
        color: #81C784;
        margin-top: 2px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# MENÚ LATERAL (SIDEBAR TÉCNICO)
# ==========================================
with st.sidebar:
    # Logo del proyecto (puedes cambiar la URL por tu logo oficial si lo deseas)
    st.image("https://cdn-icons-png.flaticon.com/512/2913/2913520.png", width=75)
    st.markdown("<h2 style='color:white; margin-bottom:0;'>EcoWeb 1.0</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#81C784; font-family:\"JetBrains Mono\"; font-size:13px; margin-top:0;'>E.E.S.T N°7 | 4° 4°</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Menú simplificado enfocado temporalmente en Inicio por requerimiento de la feria
    selected = option_menu(
        menu_title="NAVEGACIÓN PRINCIPAL",
        options=["Inicio"],
        icons=["house-rocket"],
        menu_icon="layers",
        default_index=0,
        styles={
            "container": {"padding": "5px!important", "background-color": "#0B0F12"},
            "icon": {"color": "#4CAF50", "font-size": "18px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"5px", "color": "#A0AEC0", "--hover-color": "#161F24"},
            "nav-link-selected": {"background-color": "#2E7D32", "color": "white", "font-weight": "600"},
            "menu-title": {"color": "#4A5568", "font-size": "11px", "font-weight": "700", "letter-spacing": "1px"}
        }
    )
    
    st.write("---")
    st.caption("⚡ Foco de Proyecto Activo - Feria de Innovación y Tecnología 2026")

# ==========================================
# DESARROLLO DE LA PÁGINA: INICIO
# ==========================================
if selected == "Inicio":
    
    # --- BLOQUE HERO (CABECERA) ---
    st.markdown('<h1 class="hero-title">PROYECTO ECO 2026</h1>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Infraestructura Educativa Continua y Sistema Integral de Innovación Sustentable</p>', unsafe_allow_html=True)
    
    # --- SECCIÓN 1: ¿QUÉ ES ECOWEB? ---
    st.markdown('<div class="section-glow">¿Qué es EcoWeb?</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="main-card">
            <p style="font-size: 17px; line-height: 1.7; color: #E2E8F0; margin: 0;">
                <b style="color: #4CAF50; font-size: 19px;">EcoWeb</b> es la plataforma digital oficial y el 
                núcleo tecnológico de <strong>Proyecto Eco</strong>. Fue desarrollada con el fin estratégico de 
                centralizar información, documentación de ingeniería, fichas técnicas, recursos educativos y herramientas 
                avanzadas de auditoría. Su estructura permite que los conocimientos generados por los estudiantes puedan 
                <strong>conservarse a través de las generaciones, consultarse dinámicamente y replicarse</strong> de manera libre en cualquier entorno institucional.
            </p>
        </div>
        """, unsafe_allow_html=True
    )
    
    # --- SECCIÓN 2 y 3: COLUMNAS DE RESOLUCIÓN DE PROBLEMAS Y FUNCIONES ---
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown('<div class="section-glow">¿Por qué fue creada?</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="grid-card">
                <p style="color: #A0AEC0; font-size: 14px; margin-bottom: 20px; font-family: 'JetBrains Mono', monospace;">// RESOLUCIÓN DE PROBLEMÁTICAS CRÍTICAS</p>
                <div class="tech-list-item"><span class="tech-icon">[⚡]</span><div><b>Dispersión de información:</b> Centraliza grandes volúmenes de datos científico-técnicos que antes se encontraban fragmentados.</div></div>
                <div class="tech-list-item"><span class="tech-icon">[⚡]</span><div><b>Crecimiento exponencial:</b> Responde a la evolución y expansión constante de los nuevos subproyectos de la iniciativa.</div></div>
                <div class="tech-list-item"><span class="tech-icon">[⚡]</span><div><b>Conservación del conocimiento:</b> Protege el capital intelectual para que trascienda la rotación de los ciclos escolares.</div></div>
                <div class="tech-list-item"><span class="tech-icon">[⚡]</span><div><b>Facilidad de replicabilidad:</b> Provee las herramientas metodológicas limpias para transferir el modelo a otras escuelas.</div></div>
                <div class="tech-list-item"><span class="tech-icon">[⚡]</span><div><b>Evidencia de impacto:</b> Establece un canal abierto y transparente para la exposición de métricas y resultados reales.</div></div>
            </div>
            """, unsafe_allow_html=True
        )
        
    with col2:
        st.markdown('<div class="section-glow">Funciones Principales</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="grid-card">
                <p style="color: #A0AEC0; font-size: 14px; margin-bottom: 20px; font-family: 'JetBrains Mono', monospace;">// ARQUITECTURA OPERATIVA DEL SITIO</p>
                <div class="tech-list-item"><span class="tech-icon">{✓}</span><div><b>Organizar metódicamente</b> toda la información conceptual y estructural del proyecto general.</div></div>
                <div class="tech-list-item"><span class="tech-icon">{✓}</span><div><b>Almacenar y disponibilizar</b> las fichas técnicas normalizadas de desarrollo y sus protocolos.</div></div>
                <div class="tech-list-item"><span class="tech-icon">{✓}</span><div><b>Difundir activamente</b> las iniciativas tecnológicas, laboratorios y experimentos ecológicos realizados.</div></div>
                <div class="tech-list-item"><span class="tech-icon">{✓}</span><div><b>Facilitar la consulta dinámica</b> e interactiva de contenidos académicos esenciales para la comunidad.</div></div>
                <div class="tech-list-item"><span class="tech-icon">{✓}</span><div><b>Mostrar resultados e impacto</b> directo de manera pública, combatiendo prácticas de lavado de imagen verde.</div></div>
                <div class="tech-list-item"><span class="tech-icon">{✓}</span><div><b>Favorecer la replicabilidad del ecosistema</b> mediante licencias abiertas y guías paso a paso.</div></div>
            </div>
            """, unsafe_allow_html=True
        )
        
    # --- SECCIÓN 4: RELACIÓN CON LOS PILARES (TABLA DISEÑADA CON HTML) ---
    st.markdown('<div class="section-glow">Relación de EcoWeb con los Pilares Fundamentales</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <table class="custom-table">
            <thead>
                <tr>
                    <th style="width: 25%;">Pilar del Proyecto</th>
                    <th style="width: 75%;">Relación e Integración con EcoWeb</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Replicable</td>
                    <td>Permite acceder a documentación, diagramas de flujo y fichas desde cualquier lugar del mundo de manera libre.</td>
                </tr>
                <tr>
                    <td>Continuo</td>
                    <td>Conserva la información técnica e histórica entre generaciones de estudiantes, evitando la pérdida de conocimiento.</td>
                </tr>
                <tr>
                    <td>Medible</td>
                    <td>Permite registrar de forma pública y auditable los avances, métricas, analíticas de impacto y resultados reales.</td>
                </tr>
                <tr>
                    <td>Interdisciplinario</td>
                    <td>Integra y unifica todas las secciones técnicas (EcoPapel, EcoLab, EcoTech, EcoIndustria) en un solo software unificado.</td>
                </tr>
                <tr>
                    <td>Experimental</td>
                    <td>Difunde los experimentos, bitácoras de fallos, matrices de pruebas y optimizaciones de diseño de cada ficha.</td>
                </tr>
                <tr>
                    <td>Circular</td>
                    <td>Facilita el intercambio abierto y descentralizado de conocimientos técnicos bajo la filosofía de código abierto.</td>
                </tr>
                <tr>
                    <td>Sustentable</td>
                    <td>Reduce de manera absoluta la necesidad de copias físicas en papel y digitaliza la infraestructura administrativa.</td>
                </tr>
            </tbody>
        </table>
        """, unsafe_allow_html=True
    )
    
    # --- SECCIÓN 5: VISTA PREVIA DEL DESPLIEGUE ARQUITECTÓNICO (METRICS) ---
    st.markdown('<div class="section-glow">Estructura General del Ecosistema Integrado</div>', unsafe_allow_html=True)
    
    m_col1, m_col2, m_col3, m_col4, m_col5 = st.columns(5)
    
    with m_col1:
        st.markdown('<div class="metric-container"><div class="metric-num">01</div><div class="metric-title">Inicio</div><div class="metric-delta">Introducción General</div></div>', unsafe_allow_html=True)
    with m_col2:
        st.markdown('<div class="metric-container"><div class="metric-num">02</div><div class="metric-title">Los 7 Pilares</div><div class="metric-delta">Bases Conceptuales</div></div>', unsafe_allow_html=True)
    with m_col3:
        st.markdown('<div class="metric-container"><div class="metric-num">24</div><div class="metric-title">Fichas Técnicas</div><div class="metric-delta">Biblioteca de Protocolos</div></div>', unsafe_allow_html=True)
    with m_col4:
        st.markdown('<div class="metric-container"><div class="metric-num">🤖</div><div class="metric-title">EcoIA</div><div class="metric-delta">Consultor Científico</div></div>', unsafe_allow_html=True)
    with m_col5:
        st.markdown('<div class="metric-container"><div class="metric-num">4°4°</div><div class="metric-title">Equipo Eco</div><div class="metric-delta">Investigadores E.E.S.T N°7</div></div>', unsafe_allow_html=True)

    # Footer institucional discreto y elegante
    st.write("<br><br><p style='text-align: center; color: #4A5568; font-family: \"JetBrains Mono\", monospace; font-size: 12px;'>Proyecto Eco 2026 · E.E.S.T N°7 · República Argentina · Open Source Platform</p>", unsafe_allow_html=True)
