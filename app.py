import streamlit as st
from streamlit_option_menu import option_menu
from groq import Groq
import os
import re

# --------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# --------------------------------------------------
st.set_page_config(
    page_title="Proyecto Eco 2026 | Sistema Integral",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# ESTILOS CSS (UI ECO-TECH PREMIUM)
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    :root {
        --primary: #10b981;
        --primary-glow: rgba(16, 185, 129, 0.3);
        --bg-dark: #090f0c;
        --card-bg: rgba(15, 23, 20, 0.7);
        --text-main: #ecfdf5;
    }

    .stApp {
        background: radial-gradient(circle at top right, #0d2e1f, #090f0c);
        color: var(--text-main);
        font-family: 'Inter', sans-serif;
    }

    /* Tarjetas Glassmorphism */
    .card {
        background: var(--card-bg);
        border: 1px solid rgba(16, 185, 129, 0.2);
        border-radius: 20px;
        padding: 25px;
        backdrop-filter: blur(10px);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        height: 100%;
        margin-bottom: 15px;
    }

    .card:hover {
        transform: translateY(-8px);
        border-color: var(--primary);
        box-shadow: 0 10px 30px var(--primary-glow);
    }

    /* Hero Section */
    .hero {
        text-align: center;
        padding: 60px 20px;
        background: linear-gradient(180deg, rgba(16, 185, 129, 0.1) 0%, rgba(9, 15, 12, 0) 100%);
        border-radius: 30px;
        margin-bottom: 40px;
    }

    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    .highlight {
        color: var(--primary);
    }

    /* Botones y Links */
    .drive-link {
        display: inline-block;
        padding: 8px 16px;
        background: rgba(16, 185, 129, 0.2);
        color: var(--primary) !important;
        text-decoration: none;
        border-radius: 10px;
        font-size: 14px;
        font-weight: 600;
        margin-top: 10px;
        border: 1px solid var(--primary);
    }

    .drive-link:hover {
        background: var(--primary);
        color: #000 !important;
    }

    /* Status Badges */
    .badge {
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# BASE DE DATOS (FICHAS ACTUALIZADAS)
# --------------------------------------------------
# Nota: "drive_url" es el espacio para poner tus links de Google Drive
FICHAS = {
    "1": {"titulo": "Papel Seed", "division": "EcoPapel", "drive_url": "#", "desc": "Papel artesanal biodegradable con semillas incorporadas."},
    "2": {"titulo": "FibroPapel", "division": "EcoPapel", "drive_url": "#", "desc": "Papel compuesto reforzado con fibras textiles de algodón."},
    "3": {"titulo": "Manual del Reciclador", "division": "EcoPapel", "drive_url": "#", "desc": "Documento técnico educativo 100% sustentable."},
    "4": {"titulo": "Marca-Páginas", "division": "EcoPapel", "drive_url": "#", "desc": "Souvenir funcional de cartón recuperado."},
    "5": {"titulo": "Eco-Carrier", "division": "EcoPapel", "drive_url": "#", "desc": "Bolsas estructurales que reemplazan el plástico."},
    "6": {"titulo": "Colorantes Naturales", "division": "EcoLab", "drive_url": "#", "desc": "Extracción de pigmentos de residuos vegetales."},
    "7": {"titulo": "EcoIA", "division": "EcoTech", "drive_url": "#", "desc": "Asistente inteligente de documentación técnica."},
    "8": {"titulo": "Organizadores Modulares", "division": "EcoIndustria", "drive_url": "#", "desc": "Sistemas de escritorio de latas y tubos."},
    "9": {"titulo": "Eco-Estelar", "division": "EcoIndustria", "drive_url": "#", "desc": "Lámparas perforadas mediante técnica de congelado."},
    "10": {"titulo": "EcoChallenge", "division": "Estrategia", "drive_url": "#", "desc": "Sistema de desafíos interactivos para ganar EcoDollars."},
    "11": {"titulo": "Eco-Hidro", "division": "EcoIndustria", "drive_url": "#", "desc": "Riego autónomo por capilaridad en botellas PET."},
    "12": {"titulo": "EcoTrash", "division": "EcoIndustria", "drive_url": "#", "desc": "Escoba de alta resistencia construida con cerdas PET."},
    "13": {"titulo": "EcoWallet", "division": "EcoIndustria", "drive_url": "#", "desc": "Billetera impermeable upcycling de Tetra Pak."},
    "14": {"titulo": "Carbon Ink", "division": "EcoLab", "drive_url": "#", "desc": "Tinta negra obtenida por pirólisis de papel sucio."},
    "15": {"titulo": "Nendo Dango", "division": "EcoLab", "drive_url": "#", "desc": "Bolas de arcilla y semillas para reforestación."},
    "16": {"titulo": "Paper Beads", "division": "EcoPapel", "drive_url": "#", "desc": "Cuentas estructurales decorativas de papel enrollado."},
    "17": {"titulo": "Eco-Voz", "division": "EcoIndustria", "drive_url": "#", "desc": "Amplificador acústico pasivo de cartón."},
    "18": {"titulo": "Cañón Vortex", "division": "EcoIndustria", "drive_url": "#", "desc": "Generador de anillos de aire (Dinámica de fluidos)."},
    "19": {"titulo": "Eco-Dollars", "division": "Estrategia", "drive_url": "#", "desc": "Sistema monetario de economía circular interna."},
    "20": {"titulo": "Eco-Candy", "division": "EcoLab", "drive_url": "#", "desc": "Cristalización de sacarosa saborizada (Ciencia dulce)."},
    "21": {"titulo": "EcoCristales", "division": "EcoLab", "drive_url": "#", "desc": "Cristalización de alumbre (Geometría química)."},
    "22": {"titulo": "Biogás (Teórico)", "division": "EcoLab", "drive_url": "#", "desc": "Investigación en digestión anaeróbica."},
    "23": {"titulo": "Reactor Joule", "division": "EcoTech", "drive_url": "#", "desc": "Generación de luz mediante grafito (Efecto Joule)."},
    "24": {"titulo": "TerrarIA", "division": "EcoTech", "drive_url": "#", "desc": "Ecosistema cerrado monitoreado por sensores."},
}

# --------------------------------------------------
# BARRA LATERAL
# --------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2913/2913520.png", width=80)
    st.markdown("### Ecosistema Eco")
    st.markdown("Feria Regional 2026")
    
    selected = option_menu(
        menu_title=None,
        options=["Inicio", "Estrategia", "Fichas Técnicas", "EcoIA", "Equipo"],
        icons=["house", "diagram-3", "file-earmark-text", "cpu", "people"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#10b981", "font-size": "18px"}, 
            "nav-link": {"font-size": "15px", "text-align": "left", "margin":"5px", "color":"#ecfdf4"},
            "nav-link-selected": {"background-color": "rgba(16, 185, 129, 0.2)", "border-left": "4px solid #10b981"},
        }
    )
    
    st.write("---")
    st.caption("⚡ E.E.S.T N°7 | 4°4°")

# --------------------------------------------------
# SECCIÓN: INICIO
# --------------------------------------------------
if selected == "Inicio":
    st.markdown("""
        <div class="hero">
            <h1 style='font-size: 3.5rem;'>PROYECTO <span class='highlight'>ECO</span> 2026</h1>
            <p style='font-size: 1.2rem; opacity: 0.8;'>Sistema Integral de Innovación Sustentable e Interdisciplinario</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        <div class="card">
            <h3>Nuestra Visión</h3>
            <p>Proyecto Eco no es solo reciclaje; es una <b>infraestructura de conocimiento</b> instalada dentro de la escuela. Transformamos residuos en recursos mediante un sistema interconectado de cuatro divisiones.</p>
            <p>Nacido en 2025 como EcoPapel, hoy evolucionamos hacia un ecosistema que integra ciencia aplicada, tecnología de punta y procesos industriales para competir en la Feria Regional 2026.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.metric("Divisiones", "4", delta="Estables")
        st.metric("Fichas Técnicas", "24", delta="Documentadas")

    st.write("---")
    st.subheader("Divisiones del Sistema")
    c1, c2, c3, c4 = st.columns(4)
    
    divs = [
        ("EcoPapel", "División Celulosa", "🌱", "Recuperación de fibras y economía de soporte."),
        ("EcoLab", "División Científica", "🧪", "Investigación química y biológica aplicada."),
        ("EcoTech", "División Tecnológica", "💻", "IA, sensado IoT y automatización digital."),
        ("EcoIndustria", "División de Ingeniería", "🏗️", "Física aplicada y diseño estructural.")
    ]
    
    for i, (name, sub, icon, text) in enumerate(divs):
        with [c1, c2, c3, c4][i]:
            st.markdown(f"""
            <div class="card">
                <h1 style='font-size: 2rem;'>{icon}</h1>
                <h4>{name}</h4>
                <p style='font-size: 0.8rem; color: #10b981;'>{sub}</p>
                <p style='font-size: 0.9rem; opacity: 0.8;'>{text}</p>
            </div>
            """, unsafe_allow_html=True)

# --------------------------------------------------
# SECCIÓN: ESTRATEGIA (NUEVO)
# --------------------------------------------------
elif selected == "Estrategia":
    st.markdown("## 🎯 Estrategia y Características Nucleares")
    st.write("¿Por qué el Proyecto Eco es un sistema de alto impacto?")
    
    char_list = [
        ("Replicable", "Diseñado para ser recreado en cualquier escuela con materiales accesibles."),
        ("Sustentable", "Equilibrio real entre uso de recursos y regeneración ambiental."),
        ("Interdisciplinario", "Integración de Química, Física, Tecnología y Arte en un solo flujo."),
        ("Circular", "El residuo no desaparece, cambia de función (Economía Circular)."),
        ("Continuo", "Protocolos documentados que permiten la trascendencia del equipo."),
        ("Experimental", "Metodología basada en prueba, error y optimización técnica."),
        ("Medible", "Evitamos el greenwashing mediante métricas de impacto real.")
    ]
    
    rows = [char_list[i:i + 3] for i in range(0, len(char_list), 3)]
    for row in rows:
        cols = st.columns(3)
        for j, (title, desc) in enumerate(row):
            with cols[j]:
                st.markdown(f"""
                <div class="card">
                    <h4 style='color: #10b981;'>{title}</h4>
                    <p style='font-size: 0.9rem;'>{desc}</p>
                </div>
                """, unsafe_allow_html=True)

# --------------------------------------------------
# SECCIÓN: FICHAS TÉCNICAS
# --------------------------------------------------
elif selected == "Fichas Técnicas":
    st.markdown("## 📄 Biblioteca Técnica 2026")
    
    f_cat = st.selectbox("Filtrar por División:", ["Todas", "EcoPapel", "EcoLab", "EcoTech", "EcoIndustria", "Estrategia"])
    
    items = {k: v for k, v in FICHAS.items() if f_cat == "Todas" or v["division"] == f_cat}
    
    # Grid de 3 columnas
    cols = st.columns(3)
    for i, (idx, data) in enumerate(items.items()):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card">
                <small style='color: #10b981;'>FICHA #{idx} | {data['division']}</small>
                <h4>{data['titulo']}</h4>
                <p style='font-size: 0.85rem; opacity: 0.8;'>{data['desc']}</p>
                <a href='{data['drive_url']}' class='drive-link'>📄 Ver Ficha Drive</a>
            </div>
            """, unsafe_allow_html=True)

# --------------------------------------------------
# SECCIÓN: ECOIA
# --------------------------------------------------
elif selected == "EcoIA":
    st.markdown("""
        <div class="card">
            <h3>🤖 EcoIA: Núcleo de Inteligencia</h3>
            <p>Asistente técnico basado en el modelo Llama 3 para auditoría de procesos sustentables.</p>
        </div>
    """, unsafe_allow_html=True)

    # Configuración de Groq
    api_key = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", "")
    
    if not api_key:
        st.warning("Configura la API Key de Groq para chatear.")
    else:
        client = Groq(api_key=api_key)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Consulta sobre el sistema Eco..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                sys_prompt = "Eres EcoIA, el sistema central del Proyecto Eco. Responde de forma técnica y profesional sobre sustentabilidad y las 24 fichas del proyecto."
                full_messages = [{"role": "system", "content": sys_prompt}] + st.session_state.messages
                
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=full_messages,
                    temperature=0.3
                )
                response = completion.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# --------------------------------------------------
# SECCIÓN: EQUIPO
# --------------------------------------------------
elif selected == "Equipo":
    st.markdown("## 👥 Cuadro de Investigadores")
    
    equipo = [
        {"nombre": "Damian Medina", "rol": "EcoPapel / EcoIndustria"},
        {"nombre": "Dante Rodriguez", "rol": "EcoTech (Desarrollo EcoIA)"},
        {"nombre": "Enzo Cuevas", "rol": "EcoPapel"},
        {"nombre": "Franco Titirico", "rol": "EcoIndustria (Representante)"},
        {"nombre": "Jonathan Orellana", "rol": "EcoPapel (Representante)"},
        {"nombre": "Julian Tejerina", "rol": "EcoTech (Representante)"},
        {"nombre": "Tobias Ponce Castaño", "rol": "EcoLab (Representante)"},
        {"nombre": "Valentino Correa", "rol": "EcoLab"},
    ]
    
    cols = st.columns(4)
    for i, persona in enumerate(equipo):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="card" style='text-align: center;'>
                <div style='background: var(--primary); width: 50px; height: 50px; border-radius: 50%; margin: 0 auto 10px; display: flex; align-items: center; justify-content: center; color: black; font-weight: bold;'>
                    {persona['nombre'][0]}
                </div>
                <b style='font-size: 0.9rem;'>{persona['nombre']}</b><br>
                <small style='opacity: 0.7;'>{persona['rol']}</small>
            </div>
            """, unsafe_allow_html=True)

# Footer universal
st.markdown("<br><br><p style='text-align: center; opacity: 0.5;'>Proyecto Eco 2026 · E.E.S.T N°7 · República Argentina</p>", unsafe_allow_html=True)
