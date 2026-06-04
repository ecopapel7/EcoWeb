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
# INYECCIÓN DE INTERFAZ DE ALTO IMPACTO (CSS)
# ==========================================
st.markdown("""
    <style>
    /* Fondo con degradado general que combina verde profundo y azul técnico */
    .stApp {
        background: linear-gradient(135deg, #0b2310 0%, #081018 50%, #05080c 100%) !important;
        color: #E0E6ED !important;
    }
    
    /* Estilo del menú lateral */
    [data-testid="stSidebar"] {
        background-color: rgba(11, 25, 16, 0.85) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(46, 125, 50, 0.3);
    }

    /* Títulos Principales */
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
        display: flex;
        align-items: center;
    }

    /* Tarjetas con efecto Glassmorphism (Contenedores Llamativos) */
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

    /* Listas estilizadas */
    .custom-list {
        list-style-type: none;
        padding-left: 0;
    }
    .custom-list li {
        margin-bottom: 12px;
        font-size: 16px;
        display: flex;
        align-items: flex-start;
    }
    .custom-list li::before {
        content: "✦";
        color: #00E676;
        font-weight: bold;
        display: inline-block; 
        width: 25px;
        flex-shrink: 0;
    }

    /* TABLA PERSONALIZADA ESTILO CYBER-GREEN */
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
        transition: background 0.2s ease;
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
# MENÚ LATERAL (SIDEBAR)
# ==========================================
with st.sidebar:
    # Logo del proyecto
    st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/2913/2913520.png' width='80'></div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #B9F6CA; margin-bottom: 0;'>Ecosistema Eco 2026</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #81C784; font-size: 14px;'>E.E.S.T N°7 | 4° 4°</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Navegación simplificada solo con Inicio por el momento
    selected = option_menu(
        menu_title=None,
        options=["Inicio"],
        icons=["house-door-fill"],
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
# CONTENIDO CENTRAL: PÁGINA 1 — INICIO
# ==========================================
if selected == "Inicio":
    
    # Encabezado Principal Impactante
    st.markdown('<div class="main-title">PROYECTO ECO 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Infraestructura Educativa Continua y Sistema Integral de Innovación Sustentable</div>', unsafe_allow_html=True)
    
    # 1. ¿Qué es EcoWeb?
    st.markdown('<div class="section-header">🧬 ¿Qué es EcoWeb?</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card" style="font-size: 18px; line-height: 1.6; border-left: 5px solid #00E676;">
        <strong>EcoWeb</strong> es la plataforma digital oficial y el núcleo tecnológico de <strong>Proyecto Eco</strong>. 
        Fue diseñada con el propósito fundamental de centralizar información, documentación de ingeniería, fichas técnicas, 
        recursos educativos y herramientas interactivas del proyecto. De esta manera, garantizamos que los conocimientos 
        científicos y prácticos generados puedan conservarse de manera inalterable, consultarse de forma dinámica y 
        replicarse eficientemente en cualquier entorno institucional.
        </div>
        """, unsafe_allow_html=True
    )
    
    # Columnas para Distribución de Problemática vs Soluciones Operativas
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">⚠️ ¿Por qué fue creada?</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="glass-card">
                <p style="margin-top:0; color:#81C784; font-weight:600;">Respuesta a problemáticas críticas de infraestructura y gestión de conocimiento:</p>
                <ul class="custom-list">
                    <li><strong>Dispersión de información:</strong> Centraliza grandes volúmenes de datos e investigaciones que antes se encontraban fragmentados en formatos físicos o carpetas aisladas.</li>
                    <li><strong>Crecimiento exponencial del proyecto:</strong> Responde de manera elástica a la evolución constante y al nacimiento de nuevos subproyectos ecológicos dentro de la iniciativa.</li>
                    <li><strong>Conservación transgeneracional de saberes:</strong> Protege el capital intelectual del proyecto, evitando la pérdida de información clave cuando los alumnos finalizan su ciclo escolar.</li>
                    <li><strong>Facilidad de replicabilidad técnica:</strong> Provee una base sólida de manuales estandarizados listos para transferir el modelo sustentable a cualquier otra escuela.</li>
                    <li><strong>Evidencia transparente de resultados:</strong> Establece un espacio abierto al público y evaluadores para la visualización del impacto ambiental real.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True
        )
        
    with col2:
        st.markdown('<div class="section-header">⚙️ Funciones Principales</div>', unsafe_allow_html=True)
        st.markdown(
            """
            <div class="glass-card">
                <p style="margin-top:0; color:#81C784; font-weight:600;">Como motor operativo y centro operativo del ecosistema, EcoWeb permite:</p>
                <ul class="custom-list">
                    <li><strong>Organizar metódicamente</strong> y estructurar toda la arquitectura de datos e información base de la iniciativa.</li>
                    <li><strong>Almacenar y disponibilizar</strong> de forma inmediata las fichas técnicas de ingeniería y protocolos de acción de los laboratorios.</li>
                    <li><strong>Difundir activamente</strong> las campañas, experimentos aplicados y pruebas de campo sustentables.</li>
                    <li><strong>Facilitar la consulta dinámica</strong> e interactiva de contenidos científico-técnicos para toda la comunidad académica.</li>
                    <li><strong>Mostrar resultados e impacto de métricas</strong> cuantitativas de mitigación y huella ambiental de los prototipos.</li>
                    <li><strong>Favorecer la replicabilidad del ecosistema</strong> acelerando los tiempos de adopción en nuevas locaciones.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True
        )
        
    # 4. Relación con los pilares (La tabla de la imagen en formato HTML premium)
    st.markdown('<div class="section-header">📊 Relación de EcoWeb con los Pilares Fundamentales</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="glass-card" style="padding: 10px 20px 20px 20px;">
        <p style="color: #A5D6A7; margin-bottom: 15px;">La plataforma web no actúa como un elemento aislado, sino como la infraestructura digital que valida y potencia cada principio rector del Proyecto Eco:</p>
        <table class="custom-table">
            <thead>
                <tr>
                    <th style="width: 25%;">Pilar</th>
                    <th style="width: 75%;">Relación directa con el Entorno EcoWeb</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><span class="pilar-tag">Replicable</span></td>
                    <td>Permite acceder de forma global y abierta a toda la documentación técnica, planos y fichas de procesos.</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Continuo</span></td>
                    <td>Conserva la información técnica de manera perpetua, asegurando el traspaso fluido de conocimiento entre generaciones.</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Medible</span></td>
                    <td>Permite registrar de manera pública, auditable y transparente los avances históricos de las métricas y resultados.</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Interdisciplinario</span></td>
                    <td>Integra y unifica en una sola interfaz digital todas las secciones operativas, laboratorios y áreas técnicas de estudio.</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Experimental</span></td>
                    <td>Difunde de manera abierta los experimentos, bitácoras de fallos, pruebas de laboratorio y optimizaciones aplicadas.</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Circular</span></td>
                    <td>Facilita el intercambio abierto y democrático de conocimientos bajo una filosofía de código y datos abiertos (Open Source).</td>
                </tr>
                <tr>
                    <td><span class="pilar-tag">Sustentable</span></td>
                    <td>Reduce de manera drástica la necesidad de copias, carpetas e informes en soporte físico, digitalizando la gestión.</td>
                </tr>
            </tbody>
        </table>
        </div>
        """, unsafe_allow_html=True
    )

    # Footer institucional técnico al final de la página
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Escuela de Educación Secundaria Técnica N°7 • República Argentina
        </div>
        """, unsafe_allow_html=True
    )
