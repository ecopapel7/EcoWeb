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
# INYECCIÓN DE INTERFAZ DE ALTO IMPACTO (CSS CORREGIDO)
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

    /* CONTENEDOR FLUIDO COHESIVO (Solución al desorden de la lista) */
    .info-item {
        margin-bottom: 16px;
        line-height: 1.5;
        font-size: 15.5px;
    }
    .info-bullet {
        color: #00E676;
        font-weight: bold;
        margin-right: 8px;
        display: inline-block;
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
# MENÚ LATERAL (SIDEBAR MODULAR)
# ==========================================
with st.sidebar:
    st.markdown("<div style='text-align: center;'><img src='https://cdn-icons-png.flaticon.com/512/2913/2913520.png' width='80'></div>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #B9F6CA; margin-bottom: 0;'>Ecosistema Eco 2026</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #81C784; font-size: 14px;'>E.E.S.T N°7 | 4° 4°</p>", unsafe_allow_html=True)
    st.write("---")
    
    # Menú dinámico: quitamos las páginas viejas, listo para la reconstrucción
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
# PÁGINA 1 — INICIO (RECONSTRUCCIÓN COMPLETADA)
# ==========================================
if selected == "Inicio":
    
    # Encabezado de la Plataforma Principal
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
    
    # Contenedores organizados en Columnas en paralelo (Corregido sin bugs de espaciado)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">⚠️ ¿Por qué fue creada?</div>', unsafe_allow_html=True)
        st.markdown(
            """
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
            """, unsafe_allow_html=True
        )
        
    with col2:
        st.markdown('<div class="section-header">⚙️ Funciones de EcoWeb</div>', unsafe_allow_html=True)
        st.markdown(
            """
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
            """, unsafe_allow_html=True
        )
        
    # 4. Relación con los pilares (Cuadro final de cierre)
    st.markdown('<div class="section-header">📊 Relación con los Pilares</div>', unsafe_allow_html=True)
    st.markdown(
        """
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
        """, unsafe_allow_html=True
    )

    # Footer institucional 
    st.markdown(
        """
        <div style="text-align: center; margin-top: 50px; padding: 20px; color: #81C784; font-size: 14px; border-top: 1px solid rgba(165,214,167,0.1);">
            Proyecto Eco 2026 • Escuela de Educación Secundaria Técnica N°7 • República Argentina
        </div>
        """, unsafe_allow_html=True
    )
