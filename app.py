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
    "1": {"titulo": "Papel Seed", "division": "EcoPapel", "https://drive.google.com/file/d/1S5sREmBrapKftJM5z8iZjtj46rLXer0t/view?usp=sharing": "#", "desc": "Papel artesanal biodegradable con semillas incorporadas."},
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
    tab_resumen, tab_carpeta = st.tabs(["Introducción", "Historia y Evolución"])
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
    st.write("Los 7 Pilares representan los principios fundamentales sobre los que se construye Proyecto Eco. No funcionan únicamente como características aisladas, sino como la base conceptual, organizativa y operativa que le da identidad al sistema.
Cada pilar define una forma específica de entender la sustentabilidad, la educación y el trabajo interdisciplinario dentro del proyecto. En conjunto, estos principios permiten que Proyecto Eco funcione como una estructura continua, organizada y capaz de evolucionar con el tiempo.
Los pilares también sirven como guía para el desarrollo de nuevas fichas, divisiones, productos y procesos, asegurando que todo lo incorporado al sistema mantenga coherencia con la filosofía general del proyecto.
Gracias a esta estructura, Proyecto Eco no se limita a realizar actividades ecológicas aisladas, sino que construye un modelo educativo basado en continuidad, experimentación, organización y transformación real de recursos.
En otras palabras, los 7 Pilares son la base que sostiene todo el ecosistema de Proyecto Eco.")
    
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
