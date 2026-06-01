import streamlit as st
from streamlit_option_menu import option_menu
from groq import Groq
import os
import re

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
        options=["Inicio", "Los 7 Pilares", "Fichas Técnicas", "EcoIA", "Equipo"],
        icons=["house", "heptagon", "file-earmark-text", "cpu", "people"],
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
    tab_resumen, tab_carpeta = st.tabs(["Introducción", "Historia y Evolución"])
    with tab_resumen:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            <div class="card">
                <h3>¿Que es el Proyecto Eco?</h3>
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
        st.markdown("### Registro Documental de 2025")
        
        # 1. Introducción
        with st.expander("1. Introducción", expanded=True):
            st.write("""
            El presente documento describe el desarrollo y evolución de nuestro Proyecto Eco, desde nuestros inicios en el año 2025 bajo el nombre de EcoPapel, hasta su transformación en un systema integral en 2026.
            
            El objetivo de esta carpeta de campo es registrar el proceso real de nuestro proyecto, incluyendo su origen, desarrollo, dificultades y evolución. A diferencia de un trabajo teórico, este documento se basa en la experiencia práctica de nuestro equipo, mostrando cómo una idea inicial fue modificándose hasta convertirse en una propuesta más compleja y estructurada.
            
            Además, buscamos evidenciar no solo los resultados obtenidos, sino también nuestro proceso de aprendizaje, los errores y las decisiones que nos llevaron a la evolución del proyecto.
            """)
        
        # 2. Origen
        with st.expander("2. Origen del Proyecto (2025)"):
            st.write("""
            Nuestro proyecto comenzó en el año 2025 a partir de una propuesta de trabajo anual planteada por el docente. Frente a esta consigna, iniciamos una etapa de ideas iniciales, donde planteamos múltiples posibles proyectos que abarcaban distintas áreas.
            
            Entre las ideas que consideramos se encontraban la construcción de una guitarra hecha a mano, un tren eléctrico de madera y el desarrollo de herramientas destinadas a personas con discapacidad. Estas propuestas demostraban nuestro interés por la innovación y la creación de objetos funcionales, pero presentaban diferentes niveles de complejidad y viabilidad.
            
            A medida que analizamos las opciones, buscamos una idea que no solo fuera realizable, sino que también tuviera un impacto concreto dentro del entorno escolar. Fue en este proceso donde nos surgió la propuesta de trabajar con el reciclaje de papel.
            
            La elección de esta idea no fue aleatoria, sino que la basamos en la identificación de una problemática presente en la comunidad: el manejo de los residuos y, en particular, la falta de aprovechamiento del papel descartado. De esta manera, decidimos enfocar el proyecto en la recuperación y transformación del papel, dando origen a EcoPapel, que se convertiría en el eje central de nuestro trabajo durante todo el ciclo 2025.
            """)
        
        # 3. Problema
        with st.expander("3. Problema Detectado en 2025"):
            st.write("""
            Durante la etapa inicial del proyecto, identificamos una situación particular dentro del entorno escolar: si bien la mayoría de las personas reconoce la importancia del reciclaje, en la práctica no sabe cómo llevarlo a cabo.
            
            Es decir, notamos que existe una conciencia general sobre el reciclaje como concepto, pero no un conocimiento real sobre sus procesos. Los estudiantes saben que reciclar es “algo bueno”, pero desconocen cómo se transforma un residuo en un nuevo material, especialmente en el caso del papel.
            
            Esta falta de conocimiento práctico genera que el reciclaje sea minimizado o ignorado. Observamos que, al no comprender el proceso, las personas no se involucran activamente ni lo incorporan como un hábito. A partir de esta observación, definimos un enfoque claro: no centrarse únicamente en promover el reciclaje mediante mensajes teóricos, sino en mostrar el proceso de forma concreta. Nuestro objetivo dejó de ser decir “hay que reciclar” y pasó a ser demostrar “cómo se recicla”.
            
            De esta manera, orientamos el proyecto a la concientización a través de la práctica, utilizando la transformación real de materiales como herramienta principal para generar aprendizaje e interés en la comunidad.
            """)
        
        # 4. Desarrollo EcoPapel 2025
        with st.expander("4. Desarrollo de EcoPapel 2025"):
            st.write("""
            Una vez definido el enfoque del proyecto, comenzamos el desarrollo práctico de EcoPapel, centrado en la producción de papel reciclado y la demostración de nuestro proceso.
            
            Para llevar a cabo este trabajo, tomamos como referencia contenido educativo del canal de YouTube *Papel en Coma*, el cual nos sirvió como guía inicial para comprender las técnicas básicas de reciclaje artesanal. A partir de esta base, adaptamos los procedimientos a los recursos disponibles y fuimos mejorando los resultados mediante la práctica.
            
            El eje principal del desarrollo fue la fabricación de papel reciclado, proceso que implicó la recolección de papel en desuso, su tratamiento con agua para generar pulpa y el posterior formado de nuevas hojas utilizando un tamiz que construimos con madera recuperada.
            """)
            
            st.markdown("<div class='history-block'><b>Líneas de Productos desarrolladas en el ciclo anterior:</b>", unsafe_allow_html=True)
            st.markdown("""
            * Nuestra producción de papel reciclado como material base.
            * Fabricación de cartón reciclado y construcción de herramientas propias (tamiz).
            * Elaboración de piezas artísticas de origami y libretas con cubiertas recuperadas.
            * Diseño de cartelería institucional mediante papel maché e impresión directa sobre soporte reciclado.
            * Desarrollo experimental de tintes a partir de materiales accesibles.
            * Investigación formal sobre la historia cronológica del reciclaje de papel.
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.write("""
            Además del trabajo técnico, el proyecto incluyó una dimensión comunicacional. Utilizamos redes sociales y la creación de souvenirs como estrategias para difundir nuestro proyecto, generar interés y ampliar su alcance dentro de la comunidad.
            
            Durante el desarrollo, enfrentamos dificultades principalmente relacionadas con nuestra falta de experiencia. En las primeras pruebas, el papel que obteníamos presentaba problemas de calidad, como hojas demasiado finas o bordes irregulares. Sin embargo, superamos estos inconvenientes a través de la repetición del proceso y el ajuste de las técnicas utilizadas. Este proceso de prueba y error nos permitió mejorar progresivamente los resultados, logrando productos más consistentes y estéticamente más cuidados.
            """)
        
        # 5. Resultados
        with st.expander("5. Resultados y Aprendizajes"):
            st.write("""
            A lo largo del desarrollo de EcoPapel 2025, logramos obtener resultados concretos tanto a nivel técnico como en nuestro proceso de aprendizaje. En primer lugar, consolidamos la producción de papel reciclado como eje principal del proyecto. A través de la práctica constante, logramos mejorar la calidad de las hojas, corrigiendo problemas iniciales como el espesor irregular y los bordes poco definidos. Este avance nos permitió obtener un material más resistente y estéticamente más prolijo.
            
            Además, desarrollamos distintos productos a partir del papel reciclado, como libretas, carteles y figuras de origami. Entre estos, los origamis se destacaron especialmente por su calidad visual, demostrándonos el potencial del material no solo desde lo funcional, sino también desde lo estético.
            
            Por otro lado, adquirimos conocimientos prácticos sobre el proceso de reciclaje, comprendiendo cada una de sus etapas: desde la recolección del material hasta la obtención del producto final. Este aprendizaje nos permitió pasar de un conocimiento teórico general a una comprensión real del proceso. También logramos avanzar en la comunicación del proyecto, utilizando redes sociales y estrategias de difusión para generar interés en otras personas. Esto reforzó nuestro objetivo inicial de no solo reciclar, sino también enseñar cómo hacerlo.
            
            Sin embargo, uno de los resultados más importantes no fue un producto físico, sino el aprendizaje obtenido a partir de la experiencia. Entendimos la importancia de la práctica, la repetición y la mejora progresiva, así como la necesidad de adaptar los procesos según los errores que detectamos. En este sentido, el proyecto no solo nos permitió aprender a reciclar papel, sino también desarrollar una forma de trabajo basada en la experimentación y la resolución de problemas.
            """)
        
        # 6. Limitaciones
        with st.expander("6. Limitaciones del Proyecto"):
            st.write("""
            A pesar de los resultados que obtuvimos durante el desarrollo de EcoPapel 2025, nuestro proyecto presentó diversas limitaciones, principalmente relacionadas con nuestra inexperiencia inicial y la falta de una estructura definida.
            
            En el aspect técnico, una de las principales dificultades que enfrentamos fue la calidad del papel reciclado en las primeras etapas. Las hojas tendían a ser demasiado finas y con bordes irregulares, lo que afectaba tanto su resistencia como su presentación. Estas limitaciones se debieron, en gran parte, a nuestra falta de práctica y de conocimiento previo sobre el proceso. Si bien fuimos mejorando estos problemas con el tiempo, evidenciaron nuestra necesidad de mayor precisión en las técnicas y de un control más claro sobre las variables del proceso.
            
            Por otro lado, el proyecto no contaba con una organización estructurada. Desarrollábamos las actividades sin una división clara de roles ni un sistema que nos permitiera ordenar el trabajo de forma eficiente. Esto generaba cierta dependencia del esfuerzo individual y nos dificultaba la continuidad del proyecto más allá del grupo que lo llevaba adelante. Además, nuestro enfoque estaba centrado principalmente en la producción y demostración, sin un sistema que asegurara su crecimiento o sostenibilidad en el tiempo. Es decir, el proyecto funcionaba, pero no estábamos preparados para mantenerlo o escalarlo de manera organizada.
            
            Estas limitaciones no impidieron el desarrollo de EcoPapel, pero sí nos marcaron un punto importante: la necesidad de evolucionar hacia un modelo más estructurado, que nos permitiera mejorar la calidad, organizar el trabajo y asegurar la continuidad del proyecto.
            """)
        
        # 7. Punto de Evolución
        with st.expander("7. Punto de Evolución"):
            st.write("""
            A medida que avanzaba el desarrollo de EcoPapel 2025, empezamos a notar que el proyecto tenía un potencial mayor al esperado inicialmente. Lo que en un principio era una propuesta enfocada en el reciclaje de papel empezó a mostrar posibilidades de crecimiento más amplias.
            
            Este punto de evolución no surgió de un momento único, sino de una acumulación de experiencias a lo largo de nuestro proceso. Al mejorar las técnicas, obtener resultados más consistentes y lograr productos funcionales, comprendimos que el proyecto podía ir más allá de una actividad puntual. Sin embargo, esta misma evolución nos permitió identificar una limitación más profunda: el proyecto funcionaba, pero no teníamos una estructura que le permitiera sostenerse en el tiempo o expandirse de manera organizada.
            
            A partir de esta reflexión, detectamos un problema más general: muchos proyectos ecológicos surgen con buenas ideas, pero terminan desapareciendo con el tiempo. No logran mantenerse activos ni generar un impacto duradero, ya sea por falta de organización, continuidad o integración con otros procesos. Este análisis nos llevó a replantear el enfoque del proyecto. Ya no se trataba únicamente de mejorar lo que estábamos haciendo, sino de cambiar la lógica del proyecto en sí. Nuestro objetivo pasó de desarrollar un proyecto funcional a diseñar un sistema capaz de mantenerse, crecer y adaptarse con el tiempo. Este cambio de perspectiva marcó el punto de evolución entre nuestro EcoPapel 2025 y lo que posteriormente se convertiría en nuestro Proyecto Eco 2026.
            """)
        
        # 8. Nacimiento del Proyecto Eco 2026
        with st.expander("8. Nacimiento del Proyecto Eco 2026"):
            st.write("""
            A partir del punto de evolución alcanzado en 2025, decidimos transformar el enfoque de nuestro proyecto para el nuevo ciclo lectivo. De esta manera, EcoPapel deja de ser nuestro proyecto principal y pasa a formar parte de una estructura más amplia: el Proyecto Eco 2026.
            
            Este cambio no implicó descartar lo que habíamos trabajado anteriormente, sino utilizarlo como base para construir una propuesta más completa. EcoPapel se mantiene como nuestro núcleo inicial, pero ahora integrado dentro de un sistema con mayor organización y proyección.
            
            El Proyecto Eco surge con el objetivo de resolver una problemática más amplia: la falta de continuidad y sostenibilidad en los proyectos ecológicos. En lugar de desarrollar una iniciativa aislada, nos propusimos la creación de un sistema capaz de mantenerse en el tiempo y generar un impacto real. Para lograrlo, adoptamos un enfoque diferente. Pasamos de un modelo basado en actividades a un modelo estructurado, con una lógica de funcionamiento más cercana a una organización.
            """)
            
            st.markdown("<div class='history-block'><b>Esta reestructuración nos implica de manera directa:</b>", unsafe_allow_html=True)
            st.markdown("""
            * Mayor orden metodológico en nuestro trabajo diario.
            * Definición explícita de roles y liderazgos dentro del equipo.
            * Integración transversal de distintas áreas de estudio y materias.
            * Proyección y escalabilidad a largo plazo.
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
            st.write("""
            Además, ampliamos el alcance del proyecto, incorporando nuevas ideas y líneas de trabajo que van más allá del reciclaje de papel, lo que nos permite abordar el problema ambiental desde múltiples enfoques. De esta manera, el nacimiento de nuestro Proyecto Eco 2026 representa un cambio de escala: de un proyecto puntual a un sistema en desarrollo, con intención de continuidad, crecimiento y mejora constante.
            """)
        
        # 9. Nuevo Enfoque y Objetivos
        with st.expander("9. Nuevo Enfoque y Objetivos"):
            st.write("""
            A partir de la creación de nuestro Proyecto Eco 2026, adoptamos un nuevo enfoque basado en la organización, la integración de áreas y la proyección a largo plazo. El cambio principal radica en dejar atrás un modelo centrado en actividades aisladas para pasar a un sistema estructurado, donde cada parte de nuestro proyecto cumple una función específica dentro de un conjunto mayor.
            
            En este nuevo esquema, organizamos el proyecto en distintas áreas o divisiones, cada una con un rol definido:
            * **EcoPapel:** encargada de la recuperación y transformación del papel, funcionando como base material de nuestro sistema.
            * **EcoLab:** orientada a la experimentación, donde desarrollamos procesos relacionados con química y materiales.
            * **EcoTech:** centrada en la tecnología, la organización de la información y el desarrollo de herramientas digitales.
            * **EcoIndustria:** enfocada en la creación de productos funcionales a partir de materiales reciclados.
            
            Esta división nos permite distribuir el trabajo, mejorar la organización y abordar el proyecto desde diferentes enfoques de manera simultánea. Además, el Proyecto Eco incorpora una lógica de funcionamiento basada en la continuidad. No se trata de realizar actividades puntuales, sino de sostener un sistema en el tiempo, capaz de adaptarse, mejorar y crecer.
            """)
            
            st.markdown("<div class='history-block'><b>Nuestros Principales Objetivos para 2026:</b>", unsafe_allow_html=True)
            st.markdown("""
            1. Consolidar un sistema organizado de trabajo.
            2. Mejorar la calidad medible de nuestros procesos y productos finales.
            3. Integrar distintas áreas del conocimiento práctico (tecnología, ciencia, producción).
            4. Generar un impacto real y cuantificable dentro de nuestra comunidad escolar.
            5. Lograr que el proyecto pueda mantenerse, transferirse y evolucionar autónomamente en el tiempo.
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        # 10. Conclusión
        with st.expander("10. Conclusión"):
            st.write("""
            El desarrollo de nuestro proyecto a lo largo de 2025 y su evolución en 2026 permite evidenciar un cambio significativo tanto en el enfoque como en la forma de trabajo de nuestro equipo.
            
            EcoPapel comenzó como una propuesta centrada en el reciclaje de papel y la concientización práctica, logrando demostrar que es posible transformar residuos en nuevos materiales mediante procesos accesibles. A través de la experiencia, no solo adquirimos conocimientos técnicos, sino que también desarrollamos una forma de trabajo basada en la prueba, el error y la mejora continua.
            
            Sin embargo, el aspecto más importante del proceso fue nuestra capacidad de identificar nuestras propias limitaciones y, a partir de ellas, replantear el proyecto. Este análisis dio lugar al nacimiento del Proyecto Eco 2026, que representa una evolución hacia un modelo más complejo, organizado y con proyección a largo plazo. El paso de un conjunto de actividades a un sistema estructurado marca una diferencia fundamental en términos de impacto y continuidad para nosotros.
            
            De esta manera, el proyecto deja de ser una experiencia aislada para convertirse en una propuesta con intención de permanencia, capaz de adaptarse, crecer y mantenerse en el tiempo. En síntesis, más allá de los productos obtenidos, el verdadero resultado de nuestro proyecto es la construcción de una base sólida sobre la cual seguiremos desarrollando soluciones sustentables en el futuro.
            """)
            
elif selected == "Los 7 Pilares":
    st.markdown("## ¿Que son los 7 Pilares?")
    st.write("Los 7 Pilares representan los principios fundamentales sobre los que se construye Proyecto Eco. No funcionan únicamente como características aisladas, sino como la base conceptual, organizativa y operativa que le da identidad al sistema. Cada pilar define una forma específica de entender la sustentabilidad, la educación y el trabajo interdisciplinario dentro del proyecto. En conjunto, estos principios permiten que Proyecto Eco funcione como una estructura continua, organizada y capaz de evolucionar con el tiempo. Los pilares también sirven como guía para el desarrollo de nuevas fichas, divisiones, productos y procesos, asegurando que todo lo incorporado al sistema mantenga coherencia con la filosofía general del proyecto. Gracias a esta estructura, Proyecto Eco no se limita a realizar actividades ecológicas aisladas, sino que construye un modelo educativo basado en continuidad, experimentación, organización y transformación real de recursos. En otras palabras, los 7 Pilares son la base que sostiene todo el ecosistema de Proyecto Eco.")
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
# VISTA 2: BIBLIOTECA DE FICHAS TÉCNICAS (CON ESTRUCTURA DE 11 PUNTOS)
# --------------------------------------------------
elif selected == "Fichas Técnicas":
    st.markdown("## Biblioteca de Fichas 2026")
    st.write("Las 24 Fichas constituyen el núcleo técnico y organizativo de Proyecto Eco. Cada ficha funciona como un protocolo documentado que explica, estructura y estandariza un proceso, experimento, sistema o actividad dentro del proyecto. Su función principal es transformar ideas aisladas en conocimiento organizado, permitiendo que los procesos puedan repetirse, mejorarse, enseñarse y mantenerse en el tiempo. Gracias a esta sistematización, Proyecto Eco deja de depender únicamente de la memoria o experiencia de sus integrantes y se convierte en una infraestructura educativa continua.")
    
    # Expander con el diseño oficial de la estructura interna
    with st.expander("Ver Estructura Estándar de las Fichas (11 Puntos)"):
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
# --------------------------------------------------
# VISTA 3: ECOIA (CON INYECCIÓN AUTOMÁTICA DE LAS 24 FICHAS)
# --------------------------------------------------
# --------------------------------------------------
# VISTA 3: ECOIA (DETECCIÓN E INYECCIÓN DE FICHA COMPLETA)
# --------------------------------------------------
elif selected == "EcoIA":
    st.markdown("""
        <div class="card">
            <h3>🤖 EcoIA: Consultor de Procesos Sustentables</h3>
            <p>Módulo de Inteligencia Artificial integrado para auditar y responder de forma científico-técnica sobre las 24 fichas estructurales del Proyecto Eco.</p>
        </div>
    """, unsafe_allow_html=True)

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
    # Autenticación automática por Secrets o Variable de entorno ambiental
    api_key = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", "")
    
    if not api_key:
        st.warning("⚠️ El sistema requiere la configuración de la clave 'GROQ_API_KEY' en los secretos de la plataforma.")
    else:
        client = Groq(api_key=api_key)
    
    # Inicializar el historial de mensajes
        if "messages" not in st.session_state:
            st.session_state.messages = []

    # MUESTRA EL HISTORIAL COMPLETO CON AVATARES PERSONALIZADOS
        for message in st.session_state.messages:
            avatar_actual = "👤" if message["role"] == "user" else "🌱"
            with st.chat_message(message["role"], avatar=avatar_actual):
                st.markdown(message["content"])

        if prompt := st.chat_input("Escribe tu consulta de investigación sobre el sistema Eco..."):
        
        # 1. Guardar el mensaje del usuario en el historial
            st.session_state.messages.append({"role": "user", "content": prompt})
        
        # 2. Mostrar el mensaje del usuario en la interfaz actual
            with st.chat_message("user", avatar="👤"):
                st.markdown(prompt)

        # 3. GENERACIÓN DE LA RESPUESTA EN VIVO
            with st.chat_message("assistant", avatar="🌱"):
                with st.spinner("Analizando matriz de datos científico-técnicos..."):
                
                # 🔍 DETECTOR INTELIGENTE DE FICHAS (CON REGEX)
                    ficha_detectada_contenido = None
                    numero_ficha_encontrada = None
                    prompt_en_minusculas = prompt.lower()

                    for numero, info in FICHAS.items():
                        termino_busqueda_nombre = info['titulo'].lower()
                        patron_exacto = rf"\bficha\s+{numero}\b"
  
                        if (re.search(patron_exacto, prompt_en_minusculas) or 
                            numero == prompt_en_minusculas.strip() or 
                            termino_busqueda_nombre in prompt_en_minusculas):
                        
                            numero_ficha_encontrada = numero
                            if numero in TEXTO_COMPLETO_FICHAS:
                                ficha_detectada_contenido = TEXTO_COMPLETO_FICHAS[numero]
                            break
                
                # 🧠 ARMADO DEL SYSTEM PROMPT PERSONALIZADO
                    sys_prompt = (
                        "Eres EcoIA, el núcleo de inteligencia computacional de Proyecto Eco 2026 (E.E.S.T N°7).\n"
                        "Tu rol es responder preguntas técnicas sobre sustentabilidad basados en los protocolos del colegio.\n\n"
                    )
                
                    if f_contenido := ficha_detectada_contenido:
                        sys_prompt += (
                            f"¡ALERTA DE CONTEXTO! El usuario está preguntando específicamente por la Ficha #{numero_ficha_encontrada}. "
                            "A continuación tienes el DOCUMENTO COMPLETO E INTEGRAL de esa ficha (con sus 11 puntos oficiales). "
                            "Usa esta información detallada para responder de forma extremadamente precisa, técnica y completa a lo que te pidan.\n\n"
                            f"DOCUMENTO DE LA FICHA DETECTADA:\n{f_contenido}"
                        )
                    else:
                        contexto_resumido = ""
                        for numero, info in FICHAS.items():
                            contexto_resumido += f"- Ficha #{numero} [{info['division']}]: {info['titulo']} -> {info['desc']}\n"
                    
                        sys_prompt += (
                            "El usuario está haciendo una pregunta general. Aquí tienes el índice resumido de las 24 fichas para guiarte.\n"
                            "Si el usuario menciona una ficha que no está cargada detalladamente, responde con lo que sepas del resumen y "
                            "sugiérele revisar el Drive.\n\n"
                            f"ÍNDICE DE FICHAS:\n{contexto_resumido}"
                        )

                # Unimos el prompt del sistema con el historial de mensajes
                    full_messages = [{"role": "system", "content": sys_prompt}] + st.session_state.messages
                
                    completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=full_messages,
                        temperature=0.3
                    )
                    response = completion.choices[0].message.content
                    st.markdown(response)
                
        # 4. Guardar la respuesta de la IA en el historial
            st.session_state.messages.append({"role": "assistant", "content": response})
# --------------------------------------------------
# VISTA 4: EQUIPO (CUADRO DE INVESTIGADORES)
# --------------------------------------------------
elif selected == "Equipo":
    st.markdown("## Equipo Eco")

    st.write("""
**Sistema de Reconocidos**

Proyecto Eco utiliza un sistema de participación mensual llamado **Reconocidos**.

Cada semana los participantes acumulan puntos según su participación, asistencia,
trabajo en fichas, aporte de materiales, documentación fotográfica y comprensión
de los proyectos.

Al finalizar cada mes se calcula un promedio general.

Promedio superior a 5 → Participante Reconocido.

Promedio inferior a 5 → Colaborador No Reconocido.

Los integrantes mostrados a continuación corresponden al equipo oficial reconocido
del mes actual. Esta lista puede modificarse mensualmente según la participación.
""")

    equipo = [
        {"nombre": "Jonathan Orellana", "rol": "Líder de EcoIndustria"},
        {"nombre": "Facundo Rodriguez", "rol": "Participante de EcoIndustria, EcoLab y EcoPapel"},
        {"nombre": "Tobias Ponce", "rol": "Líder de EcoLab"},
        {"nombre": "Franco Titirico", "rol": "Líder de EcoPapel"},
        {"nombre": "Octavio Vidal", "rol": "Participante de EcoPapel"},
        {"nombre": "Taina Pral", "rol": "Particpante de EcoPapel y EcoLab"},
        {"nombre": "Romina Colque", "rol": "Participante de EcoLab"},
        {"nombre": "Julian Tejerina", "rol": "Líder de EcoTech"},
    ]

    st.markdown("### Reconocidos del Mes")

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

    st.markdown("---")

    st.markdown("""
### ¿Por qué existe este sistema?

El Sistema de Reconocidos busca:

- Reconocer el compromiso real.
- Mantener la participación constante.
- Evitar grupos pasivos.
- Organizar el crecimiento del proyecto.
- Construir un sistema sostenible en el tiempo.

Cualquier estudiante puede colaborar con Proyecto Eco, pero únicamente los
participantes reconocidos forman parte del equipo oficial del mes y aparecen en la
Página Web, Redes Sociales y documentación institucional.
""")

# --------------------------------------------------
# FOOTER UNIVERSAL INSTITUCIONAL
# --------------------------------------------------
st.markdown("<br><br><p style='text-align: center; opacity: 0.45; font-size:0.8rem;'>Proyecto Eco 2026 · E.E.S.T N°7 · República Argentina</p>", unsafe_allow_html=True)
