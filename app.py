import streamlit as st
from streamlit_option_menu import option_menu

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(
    page_title="EcoWeb",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados para mejorar la estética de la interfaz
st.markdown("""
    <style>
    .main-title {
        font-size: 42px !important;
        font-weight: 700;
        color: #2E7D32;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 18px !important;
        color: #558B2F;
        margin-bottom: 25px;
    }
    .section-header {
        font-size: 24px !important;
        font-weight: 600;
        color: #1B5E20;
        border-bottom: 2px solid #A5D6A7;
        padding-bottom: 8px;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .highlight-box {
        background-color: #F1F8E9;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #7CB342;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# BASE DE DATOS DE FICHAS TÉCNICAS
# ==========================================
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
    "19": {"titulo": "Eco-Dollars", "division": "EcoPapel", "drive_url": "https://drive.google.com/file/d/1xQSQpyuVH-YSgtjWZYahVeterC99r70/view?usp=sharing", "desc": "Sistema monetario de economía circular impreso sobre papel reciclado propio."},
    "20": {"titulo": "EcoVolt", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1OmhWYiMxZvxMxHFRO7slATfgt_Brwhui/view?usp=sharing", "desc": "Generación teórica de energía limpia aprovechando el gradiente salino (agua dulce y salada)."},
    "21": {"titulo": "EcoCristales", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1jQwwWbwoUoq3xlcBYY5aVB1WoOieLQ30/view?usp=sharing", "desc": "Cristalización de alumbre orientada al estudio de la geometría química."},
    "22": {"titulo": "Biogás", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1m4l9L2Y5sXrWz2KlmgfjfDii76ZwBtS6/view?usp=sharing", "desc": "Investigación avanzada sobre digestión anaeróbica y captura de metano."},
    "23": {"titulo": "EcoMod", "division": "EcoTech", "drive_url": "https://drive.google.com/file/d/13qfQNtrsH1iAjTEAck-LrFfluuHgZZGf/view?usp=sharing", "desc": "Transforma mecánicas de juego en procesos interactivos de reciclaje, producción sustentable y economía circular (EcoDollars) para un aprendizaje activo en Minecraft."},
    "24": {"titulo": "TerrarIA", "division": "EcoLab", "drive_url": "https://drive.google.com/file/d/1P3r5UlcdPS4KWDcuYPN45qJWmD_KTBDu/view?usp=sharing", "desc": "Ecosistema cerrado automatizado y monitoreado por matrices de sensores."}
}

# ==========================================
# MENÚ LATERAL (SIDEBAR)
# ==========================================
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2913/2913520.png", width=70)
    st.markdown("### Ecosistema Eco 2026")
    st.caption("E.E.S.T N°7 | 4° 4°")
    st.write("---")
    
    # Menú de navegación
    selected = option_menu(
        menu_title=None,
        options=["Inicio", "Los 7 Pilares", "Fichas Técnicas", "EcoIA", "Equipo"],
        icons=["house", "bookmark-star", "collection", "robot", "people"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#558B2F", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#E8F5E9"},
            "nav-link-selected": {"background-color": "#2E7D32", "color": "white"},
        }
    )

# ==========================================
# CONTENIDO DE LAS PÁGINAS
# ==========================================

# --- PÁGINA 1: INICIO (INTRODUCCIÓN A ECOWEB) ---
if selected == "Inicio":
    st.markdown('<div class="main-title">PROYECTO ECO 2026</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Infraestructura Educativa Continua y Sistema Integral de Innovación Sustentable</div>', unsafe_allow_html=True)
    st.write("---")
    
    # 1. ¿Qué es EcoWeb?
    st.markdown('<div class="section-header">¿Qué es EcoWeb?</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="highlight-box">
        <strong>EcoWeb</strong> es la plataforma digital oficial de <strong>Proyecto Eco</strong>. 
        Fue desarrollada para centralizar información, documentación, fichas técnicas, recursos educativos y 
        herramientas relacionadas con el proyecto, permitiendo que los conocimientos generados puedan conservarse, 
        consultarse y replicarse con mayor facilidad.
        </div>
        """, unsafe_allow_html=True
    )
    
    # 2. ¿Por qué fue creada? & 3. Funciones principales
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="section-header">¿Por qué fue creada?</div>', unsafe_allow_html=True)
        st.write("EcoWeb surge de la necesidad real de resolver problemáticas críticas de gestión e infraestructura:")
        st.markdown("""
        * 📉 **Dispersión de información:** Centraliza grandes volúmenes de datos que antes se encontraban fragmentados.
        * 📈 **Crecimiento exponencial:** Responde a la evolución y expansión constante de los subproyectos de la iniciativa.
        * 🧠 **Conservación del conocimiento:** Protege el capital intelectual del proyecto para que trascienda los ciclos escolares.
        * 🔄 **Facilidad de replicabilidad:** Provee las herramientas metodológicas para transferir el modelo a otras instituciones.
        * 📊 **Evidencia de impacto:** Establece un espacio transparente para la exposición de resultados medibles.
        """)
        
    with col2:
        st.markdown('<div class="section-header">Funciones Principales</div>', unsafe_allow_html=True)
        st.write("Como núcleo operativo y tecnológico de la iniciativa, EcoWeb está diseñada para:")
        st.markdown("""
        * 🗂️ **Organizar metódicamente** toda la información estructural del proyecto.
        * 📥 **Almacenar y disponibilizar** las fichas técnicas y protocolos de trabajo.
        * 📢 **Difundir activamente** las iniciativas y experimentos ecológicos realizados.
        * 🔍 **Facilitar la consulta dinámica** de contenidos científico-técnicos esenciales.
        * 📈 **Visibilizar los resultados cuantitativos** y el impacto real en el entorno.
        * 🚀 **Favorecer la replicabilidad del ecosistema** en nuevos entornos educativos.
        """)
        
    # 4. Relación con los pilares
    st.markdown('<div class="section-header">Relación con los Pilares Fundamentales</div>', unsafe_allow_html=True)
    st.write("La plataforma web no es solo un sitio informativo; es la materialización tecnológica de los principios del proyecto:")
    
    # Construcción de la tabla estética de pilares utilizando st.dataframe para un look moderno
    tabla_pilares = {
        "Pilar": ["Replicable", "Continuo", "Medible", "Interdisciplinario", "Experimental", "Circular", "Sustentable"],
        "Relación con EcoWeb": [
            "Permite acceder a documentación y fichas técnicas desde cualquier lugar.",
            "Conserva la información y el conocimiento técnico entre generaciones de estudiantes.",
            "Permite registrar de manera pública y transparente los avances y resultados.",
            "Integra y unifica todas las secciones, áreas y divisiones tecnológicas.",
            "Difunde los experimentos, pruebas, fallos y optimizaciones de las fichas.",
            "Facilita el intercambio abierto de conocimientos bajo una filosofía Open Source.",
            "Reduce la necesidad de copias impresas y digitaliza la infraestructura de auditoría."
        ]
    }
    st.dataframe(tabla_pilares, use_container_width=True, hide_index=True)
    
    # 5. Estructura general de la plataforma
    st.markdown('<div class="section-header">Estructura General del Ecosistema</div>', unsafe_allow_html=True)
    st.write("A través del menú de navegación lateral, se puede explorar la arquitectura completa de nuestra solución sustentable:")
    
    step_col1, step_col2, step_col3, step_col4, step_col5 = st.columns(5)
    step_col1.metric(label="01", value="Inicio", delta="Introducción")
    step_col2.metric(label="02", value="Fundamentos", delta="7 Pilares Eco")
    step_col3.metric(label="03", value="Biblioteca", delta="24 Fichas Técnicas")
    step_col4.metric(label="04", value="EcoIA", delta="Consultor de IA")
    step_col5.metric(label="05", value="Equipo", delta="Reconocidos 2026")

# --- PÁGINA 2: LOS 7 PILARES ---
elif selected == "Los 7 Pilares":
    st.markdown("## ¿Qué son los 7 Pilares?")
    st.write("Los 7 Pilares representan los principios fundamentales sobre los que se construye Proyecto Eco...")
    # (Aquí irá el desarrollo extendido de la Página 2 en los siguientes pasos)

# --- PÁGINA 3: FICHAS TÉCNICAS ---
elif selected == "Fichas Técnicas":
    st.markdown("## Biblioteca de Fichas 2026")
    st.write("Las 24 Fichas constituyen el núcleo técnico y organizativo de Proyecto Eco...")
    # (Aquí irá el desarrollo extendido de la Página 3 en los siguientes pasos)

# --- PÁGINA 4: ECOIA ---
elif selected == "EcoIA":
    st.markdown("## 🤖 EcoIA: Consultor de Procesos Sustentables")
    st.write("Módulo de Inteligencia Artificial integrado para auditar y responder...")
    # (Aquí irá el desarrollo extendido de la Página 4 en los siguientes pasos)

# --- PÁGINA 5: EQUIPO ---
elif selected == "Equipo":
    st.markdown("## Equipo Eco")
    st.write("Sistema de Reconocidos Proyecto Eco...")
    # (Aquí irá el desarrollo extendido de la Página 5 en los siguientes pasos)
