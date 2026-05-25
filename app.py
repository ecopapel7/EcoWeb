import streamlit as st
from streamlit_option_menu import option_menu
from groq import Groq
import os

# --------------------------------------------------
# CONFIGURACIÓN DE PÁGINA
# --------------------------------------------------
st.set_page_config(
    page_title="EcoWeb",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# ESTILOS CSS (UI ECO-TECH PREMIUM)
# --------------------------------------------------
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    :root {
        --primary: #10b981;
        --primary-glow: rgba(16, 185, 129, 0.25);
        --bg-dark: #090f0c;
        --card-bg: rgba(15, 23, 20, 0.75);
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
        border: 1px solid rgba(16, 185, 129, 0.18);
        border-radius: 16px;
        padding: 24px;
        backdrop-filter: blur(12px);
        transition: all 0.35s ease-in-out;
        height: 100%;
        margin-bottom: 16px;
    }

    .card:hover {
        transform: translateY(-6px);
        border-color: var(--primary);
        box-shadow: 0 12px 24px var(--primary-glow);
    }

    /* Cuadros históricos especiales */
    .history-block {
        background: rgba(255, 255, 255, 0.02);
        border-left: 4px solid var(--primary);
        padding: 15px 20px;
        margin: 15px 0;
        border-radius: 0 12px 12px 0;
    }

    /* Hero Section */
    .hero {
        text-align: center;
        padding: 50px 20px;
        background: linear-gradient(180deg, rgba(16, 185, 129, 0.12) 0%, rgba(9, 15, 12, 0) 100%);
        border-radius: 24px;
        margin-bottom: 30px;
    }

    h1, h2, h3, h4 {
        font-family: 'Inter', sans-serif;
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    .highlight {
        color: var(--primary);
    }

    /* Botones y Enlaces Drive */
    .drive-link {
        display: inline-block;
        padding: 8px 18px;
        background: rgba(16, 185, 129, 0.15);
        color: var(--primary) !important;
        text-decoration: none;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 600;
        margin-top: 12px;
        border: 1px solid rgba(16, 185, 129, 0.4);
        transition: all 0.3s ease;
    }

    .drive-link:hover {
        background: var(--primary);
        color: #090f0c !important;
        box-shadow: 0 0 12px var(--primary);
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# BASE DE DATOS MATRIZ: 24 FICHAS TÉCNICAS
# --------------------------------------------------
# Espacio 'drive_url' listo para colocar los enlaces de descarga de Google Drive.
FICHAS = {
    "1": {"titulo": "Papel Seed", "division": "EcoPapel", "drive_url": "#", "desc": "Papel artesanal biodegradable con semillas incorporadas."},
    "2": {"titulo": "FibroPapel", "division": "EcoPapel", "drive_url": "#", "desc": "Papel compuesto reforzado con fibras textiles de algodón."},
    "3": {"titulo": "Manual del Reciclador", "division": "EcoPapel", "drive_url": "#", "desc": "Documento técnico educativo 100% sustentable."},
    "4": {"titulo": "Marca-Páginas", "division": "EcoPapel", "drive_url": "#", "desc": "Souvenir funcional de cartón recuperado."},
    "5": {"titulo": "Eco-Carrier", "division": "EcoPapel", "drive_url": "#", "desc": "Bolsas estructurales que reemplazan el plástico de un solo uso."},
    "6": {"titulo": "Colorantes Naturales", "division": "EcoLab", "drive_url": "#", "desc": "Extracción de pigmentos puros de residuos vegetales y cáscaras."},
    "7": {"titulo": "EcoIA", "division": "EcoTech", "drive_url": "#", "desc": "Asistente inteligente de documentación técnica y auditoría sustentable."},
    "8": {"titulo": "Organizadores Modulares", "division": "EcoIndustria", "drive_url": "#", "desc": "Sistemas de ordenamiento de escritorio mediante latas y tubos."},
    "9": {"titulo": "Eco-Estelar", "division": "EcoIndustria", "drive_url": "#", "desc": "Lámparas decorativas perforadas mediante técnica avanzada de congelado."},
    "10": {"titulo": "EcoChallenge", "division": "Transversal", "drive_url": "#", "desc": "Sistema transversal de desafíos interactivos aplicable a todas las áreas."},
    "11": {"titulo": "Eco-Hidro", "division": "EcoIndustria", "drive_url": "#", "desc": "Módulo de riego autónomo por capilaridad optimizado en botellas PET."},
    "12": {"titulo": "EcoTrash", "division": "EcoIndustria", "drive_url": "#", "desc": "Escoba técnica de alta resistencia construida con cerdas de PET alineadas."},
    "13": {"titulo": "EcoWallet", "division": "EcoIndustria", "drive_url": "#", "desc": "Billetera impermeable mediante upcycling estructurado de Tetra Pak."},
    "14": {"titulo": "Carbon Ink", "division": "EcoLab", "drive_url": "#", "desc": "Tinta negra premium obtenida por pirólisis controlada de papel sucio."},
    "15": {"titulo": "Nendo Dango", "division": "EcoLab", "drive_url": "#", "desc": "Bolas de arcilla, sustrato y semillas para reforestación masiva guiada."},
    "16": {"titulo": "Paper Beads", "division": "EcoPapel", "drive_url": "#", "desc": "Cuentas estructurales y elementos decorativos de papel enrollado."},
    "17": {"titulo": "Eco-Voz", "division": "EcoIndustria", "drive_url": "#", "desc": "Amplificador acústico pasivo diseñado en cartón corrugado."},
    "18": {"titulo": "Cañón Vortex", "division": "EcoIndustria", "drive_url": "#", "desc": "Generador físico de anillos de aire para demostración de dinámica de fluidos."},
    "19": {"titulo": "Eco-Dollars", "division": "EcoPapel", "drive_url": "#", "desc": "Sistema monetario de economía circular impreso sobre papel reciclado propio."},
    "20": {"titulo": "EcoVolt", "division": "EcoLab", "drive_url": "#", "desc": "Generación teórica de energía limpia aprovechando el gradiente salino (agua dulce y salada)."},
    "21": {"titulo": "EcoCristales", "division": "EcoLab", "drive_url": "#", "desc": "Cristalización de alumbre orientada al estudio de la geometría química."},
    "22": {"titulo": "Biogás (Teórico)", "division": "EcoLab", "drive_url": "#", "desc": "Investigación avanzada sobre digestión anaeróbica y captura de metano."},
    "23": {"titulo": "Reactor Joule", "division": "EcoTech", "drive_url": "#", "desc": "Generación de luz incandescente mediante grafito escolar (Efecto Joule)."},
    "24": {"titulo": "TerrarIA", "division": "EcoTech", "drive_url": "#", "desc": "Ecosistema cerrado automatizado y monitoreado por matrices de sensores."},
}

# --------------------------------------------------
# MENÚ DE NAVEGACIÓN LATERAL
# --------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2913/2913520.png", width=70)
    st.markdown("### Ecosistema Eco 2026")
    st.caption("E.E.S.T N°7 | 4° 4°")
    st.write("---")
    
    selected = option_menu(
        menu_title=None,
        options=["Inicio", "Fichas Técnicas", "EcoIA", "Equipo"],
        icons=["house", "file-earmark-text", "cpu", "people"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#10b981", "font-size": "17px"}, 
            "nav-link": {"font-size": "14px", "text-align": "left", "margin":"4px", "color":"#ecfdf4"},
            "nav-link-selected": {"background-color": "rgba(16, 185, 129, 0.18)", "border-left": "4px solid #10b981"},
        }
    )

# --------------------------------------------------
# VISTA 1: INICIO (CON INTERFAZ DE TABS E HISTORIA COMPLETA)
# --------------------------------------------------
if selected == "Inicio":
    st.markdown("""
        <div class="hero">
            <h1 style='font-size: 3.2rem; margin-bottom:0;'>PROYECTO <span class='highlight'>ECO</span> 2026</h1>
            <p style='font-size: 1.1rem; opacity: 0.85;'>Infraestructura Educativa Continua y Sistema Integral de Innovación Sustentable</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Navegación por pestañas internas para balancear el contenido
    tab_resumen, tab_carpeta = st.tabs(["📊 Resumen del Ecosistema", "📖 Carpeta de Campo: Historia y Evolución"])
    
    with tab_resumen:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="card">
                <h3>Nuestra Visión Estratégica</h3>
                <p><b>Proyecto Eco</b> no constituye simplemente un taller aislado de reciclaje; representa una auténtica <b>infraestructura de conocimiento</b> instalada y arraigada dentro de la institución escolar.</p>
                <p>Buscamos transformar de manera práctica los residuos convencionales en recursos de alto valor técnico y pedagógico a través de una red interconectada de cuatro áreas del saber, asegurando que el conocimiento trascienda a las personas y se preserve en protocolos institucionales continuos.</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.metric("Divisiones Operativas", "4", delta="Estructuradas")
            st.metric("Protocolos Documentados", "24 Fichas", delta="Metodología Científica")
            
        st.write("<br>", unsafe_allow_html=True)
        st.subheader("Divisiones Técnicas del Sistema")
        
        c1, c2, c3, c4 = st.columns(4)
        divs_data = [
            ("EcoPapel", "Sección Artística", "🌱", "Recuperación de fibras, soportes orgánicos y el circuito de acuñación de los Eco-Dollars."),
            ("EcoLab", "Sección Científica", "🧪", "Investigación analítica, procesos químicos moleculares, extracciones y cristalización."),
            ("EcoTech", "Sección Tecnológica", "💻", "Inteligencia Artificial, Marketing, Diseño Gráfico y Desarrollo."),
            ("EcoIndustria", "Sección de Ingeniería", "🏗️", "Diseño estructural avanzado, leyes de física de fluidos, upcycling a escala y ergonomía.")
        ]
        for idx, (name, sub, icon, text) in enumerate(divs_data):
            with [c1, c2, c3, c4][idx]:
                st.markdown(f"""
                <div class="card">
                    <span style='font-size: 1.8rem;'>{icon}</span>
                    <h4 style='margin-top:5px; margin-bottom:2px;'>{name}</h4>
                    <p style='font-size: 0.8rem; color: #10b981; font-weight:600;'>{sub}</p>
                    <p style='font-size: 0.85rem; opacity: 0.8; line-height:1.4;'>{text}</p>
                </div>
                """, unsafe_allow_html=True)

    with tab_carpeta:
        st.markdown("### 📝 Registro Documental Completo de la Carpeta de Campo")
        st.caption("Lectura oficial y cronológica del proceso de investigación práctica del equipo.")
        
        # Usamos expanders para que no sea un bloque de texto infinito
        with st.expander("1. Introducción & 2. Origen del Proyecto (2025)", expanded=True):
            st.markdown("""
            <div class="history-block">
                El presente documento describe el desarrollo y evolución de nuestro Proyecto Eco, desde nuestros inicios en el año 2025 bajo el nombre de <b>EcoPapel</b>, hasta su transformación en un sistema integral en 2026.
            </div>
            """, unsafe_allow_html=True)
            
            st.write("""
            Nuestro proyecto comenzó en el año 2025 a partir de una propuesta de trabajo anual. Entre las ideas consideramos construir herramientas o instrumentos, pero buscamos una idea que tuviera un impacto concreto dentro del entorno escolar: **trabajar con el reciclaje de papel**.
            
            De esta manera, decidimos enfocar el proyecto en la recuperación y transformación del papel, dando origen a EcoPapel.
            """)

        with st.expander("3. Problema Detectado en 2025"):
            st.info("💡 **Dato clave:** Notamos que existe una conciencia general sobre el reciclaje como concepto, pero no un conocimiento real sobre sus procesos.")
            st.write("""
            Esta falta de conocimiento práctico genera que el reciclaje sea minimizado o ignorado. Nuestro objetivo dejó de ser decir “hay que reciclar” y pasó a ser demostrar **“cómo se recicla”**.
            """)

        with st.expander("4. Desarrollo de EcoPapel 2025"):
            st.write("""
            Comenzamos el desarrollo práctico centrado en la producción de papel reciclado. El eje principal fue la fabricación, implicando recolección, tratamiento con agua, y formado de nuevas hojas utilizando un tamiz propio.
            """)
            
            st.markdown("<div class='card' style='margin-top:10px;'><b>Líneas de Productos desarrolladas en el ciclo anterior:</b><br><br>", unsafe_allow_html=True)
            st.markdown("""
            * Producción de papel reciclado como material base.
            * Fabricación de cartón reciclado y herramientas propias.
            * Elaboración de piezas artísticas de origami.
            * Desarrollo experimental de tintes.
            </div>
            """, unsafe_allow_html=True)

        with st.expander("5. Resultados y Aprendizajes"):
            st.success("A lo largo del desarrollo de EcoPapel 2025, logramos consolidar la producción de papel como eje principal, corrigiendo problemas iniciales como el espesor irregular.")
            st.write("""
            El resultado más importante no fue un producto físico, sino el aprendizaje. Entendimos la importancia de la práctica, la repetición y la mejora progresiva.
            """)

        with st.expander("6. Limitaciones & 7. Punto de Evolución"):
            st.warning("Las principales dificultades que enfrentamos fueron la calidad inicial del papel y la falta de una organización estructurada de roles.")
            st.write("""
            El proyecto funcionaba, pero no estábamos preparados para mantenerlo o escalarlo de manera organizada. Detectamos que muchos proyectos ecológicos desaparecen por falta de continuidad. 
            
            **Nuestro objetivo pasó de desarrollar un proyecto funcional a diseñar un sistema capaz de mantenerse, crecer y adaptarse con el tiempo.**
            """)

        with st.expander("8. Nacimiento y Objetivos de Proyecto Eco 2026"):
            st.write("""
            EcoPapel dejó de ser nuestro proyecto principal y pasó a formar parte de una estructura más amplia: el **Proyecto Eco 2026**. Pasamos de un modelo basado en actividades a un modelo estructurado.
            """)
            
            st.markdown("<div class='history-block'><b>Nuestros Principales Objetivos para 2026:</b>", unsafe_allow_html=True)
            st.markdown("""
            1. Consolidar un sistema organizado de trabajo.
            2. Mejorar la calidad medible de nuestros procesos y productos finales.
            3. Integrar distintas áreas del conocimiento práctico (tecnología, ciencia, producción).
            4. Generar un impacto real y cuantificable dentro de nuestra comunidad escolar.
            5. Lograr que el proyecto pueda mantenerse y evolucionar autónomamente en el tiempo.
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
# --------------------------------------------------
# VISTA 2: BIBLIOTECA DE FICHAS TÉCNICAS (CON ESTRUCTURA DE 11 PUNTOS)
# --------------------------------------------------
elif selected == "Fichas Técnicas":
    st.markdown("## 📄 Biblioteca de Fichas 2026")
    st.write("Las 24 Fichas constituyen el núcleo técnico y organizativo de Proyecto Eco. Cada ficha funciona como un protocolo documentado que explica, estructura y estandariza un proceso, experimento, sistema o actividad dentro del proyecto. Su función principal es transformar ideas aisladas en conocimiento organizado, permitiendo que los procesos puedan repetirse, mejorarse, enseñarse y mantenerse en el tiempo. Gracias a esta sistematización, Proyecto Eco deja de depender únicamente de la memoria o experiencia de sus integrantes y se convierte en una infraestructura educativa continua.")
    
    # Expander con el diseño oficial de la estructura interna
    with st.expander("📋 Ver Estructura Oficial Estándar de las Fichas (11 Puntos)"):
        st.markdown("""
        <div style='background: rgba(16, 185, 129, 0.04); padding: 20px; border-radius: 12px; border-left: 4px solid #10b981; line-height: 1.5;'>
            <p style='margin-bottom:10px;'><b>1. Concepto:</b> Define qué es el sistema, producto o proceso desarrollado. Explica su función principal dentro de Proyecto Eco y establece el marco general de la ficha.</p>
            <p style='margin-bottom:10px;'><b>2. Objetivo:</b> Describe los propósitos concretos del desarrollo. Aquí se establecen las metas educativas, técnicas, ambientales, organizativas o experimentales que busca cumplir la ficha.</p>
            <p style='margin-bottom:10px;'><b>3. Materiales:</b> Detalla todos los recursos necesarios para realizar el proceso o construir el sistema. Incluye herramientas, materiales reciclados, insumos técnicos y conexiones con otras fichas del proyecto.</p>
            <p style='margin-bottom:10px;'><b>4. Procedimiento:</b> Explica paso a paso cómo desarrollar el proceso de manera ordenada y replicable. Esta sección transforma ideas generales en protocolos prácticos capaces de repetirse y enseñarse.</p>
            <p style='margin-bottom:10px;'><b>5. Actividad para el Equipo:</b> Establece tareas específicas para los integrantes del proyecto. Permite distribuir responsabilidades, organizar el trabajo grupal y asegurar participación activa dentro del sistema.</p>
            <p style='margin-bottom:10px;'><b>6. Criterio de Calidad:</b> Define las condiciones mínimas necesarias para considerar que el proceso o producto fue realizado correctamente. Funciona como sistema interno de control y mejora continua.</p>
            <p style='margin-bottom:10px;'><b>7. Impacto Ambiental:</b> Analiza cómo el desarrollo contribuye a la sustentabilidad, reutilización de recursos, reducción de residuos o concientización ecológica dentro del proyecto.</p>
            <p style='margin-bottom:10px;'><b>8. Datos Técnicos / Experimentales:</b> Registra mediciones, resultados, estadísticas o variables obtenidas durante el proceso. Esta sección permite evaluar resultados reales y desarrollar una metodología basada en evidencia y experimentación.</p>
            <p style='margin-bottom:10px;'><b>9. Costo y Viabilidad:</b> Evalúa el costo de producción, accesibilidad de materiales y posibilidad de mantener el sistema funcionando a largo plazo. Busca garantizar que los desarrollos sean sostenibles y aplicables en contextos reales.</p>
            <p style='margin-bottom:10px;'><b>10. Proyección Futura:</b> Explora posibles mejoras, expansiones o evoluciones del sistema. Esta sección permite que cada ficha permanezca abierta a nuevas ideas, tecnologías y adaptaciones futuras.</p>
            <p style='margin-bottom:0;'><b>11. Marco Ampliado:</b> Es la sección más extensa y flexible de la ficha. Aquí se desarrolla el contexto completo del sistema mediante tablas, reglamentos, conversiones, estrategias, estructuras complementarias, aplicaciones avanzadas y documentación ampliada. El Marco Ampliado permite transformar una ficha básica en un sistema complejo, integrando información técnica, organizativa y conceptual dentro de una misma estructura documental.</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.write("---")
    
    # Filtro del Selectbox actualizado correctamente sin "Estrategia" y sumando "Transversal"
    f_cat = st.selectbox("Filtrar por División o Eje:", ["Todas", "EcoPapel", "EcoLab", "EcoTech", "EcoIndustria", "Transversal"])
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Filtrado lógico
    filtered_items = {k: v for k, v in FICHAS.items() if f_cat == "Todas" or v["division"] == f_cat}
    
    # Despliegue en Grid de 3 columnas
    cols = st.columns(3)
    for index, (idx, data) in enumerate(filtered_items.items()):
        with cols[index % 3]:
            # Badge de color condicional rápido
            badge_color = "#10b981" if data['division'] != "Transversal" else "#34d399"
            st.markdown(f"""
            <div class="card">
                <small style='color: {badge_color}; font-weight: 700; letter-spacing:0.5px;'>FICHA #{idx} | {data['division'].upper()}</small>
                <h4 style='margin-top: 4px; margin-bottom: 8px;'>{data['titulo']}</h4>
                <p style='font-size: 0.85rem; opacity: 0.85; line-height:1.4;'>{data['desc']}</p>
                <a href='{data['drive_url']}' target='_blank' class='drive-link'>📄 Ver Documento Drive</a>
            </div>
            """, unsafe_allow_html=True)

# --------------------------------------------------
# VISTA 3: ECOIA (SISTEMA DE INTELIGENCIA ARTIFICIAL)
# --------------------------------------------------
elif selected == "EcoIA":
    st.markdown("""
        <div class="card">
            <h3>🤖 EcoIA: Consultor de Procesos Sustentables</h3>
            <p>Módulo de Inteligencia Artificial integrado para auditar y responder de forma científico-técnica sobre las 24 fichas estructurales del Proyecto Eco.</p>
        </div>
    """, unsafe_allow_html=True)

    # Autenticación automática por Secrets o Variable de entorno ambiental
    api_key = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", "")
    
    if not api_key:
        st.warning("⚠️ El sistema requiere la configuración de la clave 'GROQ_API_KEY' en los secretos de la plataforma.")
    else:
        client = Groq(api_key=api_key)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # Historial persistente en pantalla
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("Escribe tu consulta de investigación sobre el sistema Eco..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                # System prompt ultra preciso para evitar alucinaciones
                sys_prompt = (
                    "Eres EcoIA, el núcleo de inteligencia computacional de Proyecto Eco 2026. "
                    "Tu escuela es la E.E.S.T N°7. Tienes 4 divisiones: EcoPapel, EcoLab, EcoTech y EcoIndustria. "
                    "Tu rol es responder preguntas técnicas sobre sustentabilidad, reciclaje y los 24 protocolos "
                    "institucionales de las fichas del proyecto de manera clara, rigurosa y experta."
                )
                full_messages = [{"role": "system", "content": sys_prompt}] + st.session_state.messages
                
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=full_messages,
                    temperature=0.25
                )
                response = completion.choices[0].message.content
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# --------------------------------------------------
# VISTA 4: EQUIPO (CUADRO DE INVESTIGADORES)
# --------------------------------------------------
elif selected == "Equipo":
    st.markdown("## 👥 Cuadro de Investigadores")
    st.write("Estructura de roles y responsabilidades del grupo de investigadores de la E.E.S.T N°7 (4° 4°).")
    
    equipo = [
        {"nombre": "Damian Medina", "rol": "EcoPapel / EcoIndustria"},
        {"nombre": "Dante Rodriguez", "rol": "EcoTech"},
        {"nombre": "Enzo Cuevas", "rol": "EcoPapel"},
        {"nombre": "Franco Titirico", "rol": "EcoIndustria (Representante)"},
        {"nombre": "Jonathan Orellana", "rol": "EcoPapel (Representante)"},
        {"nombre": "Julian Tejerina", "rol": "EcoTech (Representante)"},
        {"nombre": "Tobias Ponce Castaño", "rol": "EcoLab (Representante)"},
        {"nombre": "Valentino Correa", "rol": "EcoLab"},
    ]
    
    # Cuadrícula limpia de 4 columnas para los integrantes
    cols = st.columns(4)
    for index, persona in enumerate(equipo):
        with cols[index % 4]:
            st.markdown(f"""
            <div class="card" style='text-align: center; padding: 20px 15px;'>
                <div style='background: var(--primary); width: 44px; height: 44px; border-radius: 50%; margin: 0 auto 12px; display: flex; align-items: center; justify-content: center; color: #090f0c; font-weight: 700; font-size:1.1rem;'>
                    {persona['nombre'][0]}
                </div>
                <b style='font-size: 0.95rem; display:block; margin-bottom:4px;'>{persona['nombre']}</b>
                <small style='opacity: 0.75; font-size:0.8rem; color:#a7f3d0;'>{persona['rol']}</small>
            </div>
            """, unsafe_allow_html=True)

# --------------------------------------------------
# FOOTER UNIVERSAL INSTITUCIONAL
# --------------------------------------------------
st.markdown("<br><br><p style='text-align: center; opacity: 0.45; font-size:0.8rem;'>Proyecto Eco 2026 · E.E.S.T N°7 · República Argentina</p>", unsafe_allow_html=True)
