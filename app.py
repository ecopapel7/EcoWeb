import streamlit as st
from streamlit_option_menu import option_menu
from groq import Groq
import os
import re

# --------------------------------------------------
# CONFIGURACIÓN GENERAL DEL SISTEMA [cite: 1]
# --------------------------------------------------
st.set_page_config(
    page_title="Proyecto Eco 2026",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# ESTILOS REFINADOS (UI INTERNIVEL DE ALTO IMPACTO) [cite: 1]
# --------------------------------------------------
st.markdown("""
<style>
/* Fondo animado cyberpunk-ecológico */
.stApp {
    background: linear-gradient(-45deg, #09151c, #0f2a1d, #143525, #0a1e24);
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
    color: #f0fdf4;
    font-family: 'Inter', sans-serif;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Sidebar Estilizado */
section[data-testid="stSidebar"] {
    background: #070f14 !important;
    border-right: 1px solid rgba(74, 222, 128, 0.15);
}

/* Títulos con brillo de neón controlado */
h1, h2, h3 {
    color: #4ADE80 !important;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-shadow: 0 0 15px rgba(74, 222, 128, 0.2);
}

/* Tarjetas de División y Fichas */
.card {
    background: rgba(15, 32, 23, 0.45);
    padding: 24px;
    border-radius: 16px;
    backdrop-filter: blur(16px);
    border: 1px solid rgba(74, 222, 128, 0.15);
    box-shadow: 0 8px 32px rgba(0,0,0,0.5);
    transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
    margin-bottom: 20px;
    height: 100%;
}

.card:hover {
    transform: translateY(-6px);
    border: 1px solid rgba(74, 222, 128, 0.5);
    box-shadow: 0 12px 40px rgba(74, 222, 128, 0.15);
}

/* Contenedores de Siluetas SVG */
.icon-container {
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 15px;
    height: 60px;
}
.icon-shape {
    fill: #4ADE80;
    filter: drop-shadow(0px 0px 8px rgba(74, 222, 128, 0.6));
    width: 50px;
    height: 50px;
}

/* Hero Section Avanzado */
.hero {
    text-align: center;
    padding: 50px 30px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.12), rgba(16, 185, 129, 0.04));
    backdrop-filter: blur(20px);
    border: 1px solid rgba(74, 222, 128, 0.2);
    box-shadow: 0 20px 50px rgba(0,0,0,0.6);
    margin-bottom: 35px;
}

.hero h1 {
    font-size: 52px;
    margin-bottom: 12px;
    background: linear-gradient(90deg, #4ADE80, #22C55E);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Métricas del Dashboard */
[data-testid="stMetric"] {
    background: rgba(15, 32, 23, 0.6);
    padding: 18px;
    border-radius: 14px;
    border: 1px solid rgba(74, 222, 128, 0.1);
    text-align: center;
}

/* Chatbot UI Integración */
.ecoia-header {
    padding: 24px;
    border-radius: 16px;
    background: linear-gradient(135deg, #0b1c15, #0d261a);
    border: 1px solid rgba(46, 139, 87, 0.4);
    box-shadow: 0 0 25px rgba(46, 139, 87, 0.25);
    margin-bottom: 25px;
}

/* Utilidades de texto */
.mini {
    font-size: 13px;
    color: #a7f3d0;
    opacity: 0.8;
    margin-bottom: 8px;
    text-transform: uppercase;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# BASE DE DATOS MATRIZ (CONSERVADA INTEGRALMENTE) [cite: 19]
# --------------------------------------------------
FICHAS_DETALLADAS = {
    "1": {"titulo": "Papel Seed", "division": "EcoPapel", "descripcion": "Papel artesanal biodegradable con semillas incorporadas en su estructura fibrosa. Una vez utilizado, puede plantarse directamente en tierra húmeda, donde la celulosa se degrada y permite la germinacion de las semillas integradas. Integra principios de reciclaje, biologia vegetal y economia circular."}, # [cite: 20]
    "2": {"titulo": "FibroPapel", "division": "EcoPapel", "descripcion": "Material compuesto desarrollado a partir de pulpa de papel reciclado y fibras textiles de algodon. La incorporacion de refuerzos aumenta la resistencia mecanica, flexibilidad y durabilidad, permitiendo su uso estructural en tapas, carpetas y empaques."}, # [cite: 21]
    "3": {"titulo": "Manual del Reciclador", "division": "EcoPapel", "descripcion": "Documento tecnico educativo fabricado integramente con materiales reciclados. Compila procesos, fundamentos cientificos y protocolos desarrollados por el proyecto. Su construccion utiliza encuadernacion sin metales ni plasticos."}, # [cite: 22, 23, 24]
    "4": {"titulo": "Marca-Paginas", "division": "EcoPapel", "descripcion": "Producto funcional elaborado con carton recuperado y tecnicas de diseno artesanal. Incorpora sellos, grabados y barniz ecologico. Funciona como herramienta de difusion del proyecto."}, # [cite: 25]
    "5": {"titulo": "Eco-Carrier", "division": "EcoPapel", "descripcion": "Bolsa estructural fabricada con papel reciclado de gran formato y refuerzos internos. Demuestra sustitucion viable del plastico de un solo uso mediante ingenieria de pliegues y refuerzo."}, # [cite: 26]
    "6": {"titulo": "Colorantes Naturales", "division": "EcoLab", "descripcion": "Sistema de extraction de pigmentos organicos a partir de residuos vegetales. Utiliza procesos de decoccion y fijacion mediante mordientes naturales para estabilizar el color."}, # [cite: 27]
    "7": {"titulo": "EcoIA", "division": "EcoTech", "descripcion": "Sistema de documentacion inteligente basado en modelo de lenguaje. Permite consultar fichas tecnicas, clasificar residuos y centralizar el conocimiento del proyecto."}, # [cite: 28]
    "8": {"titulo": "Organizadores Eco-Modulares", "division": "EcoIndustria", "descripcion": "Sistema de almacenamiento modular construido con latas y tubos reciclados. Integra principios de diseno intercambiable mediante imanes o encastres estructurales."}, # [cite: 29]
    "9": {"titulo": "EcoReflector", "division": "EcoIndustria", "descripcion": "Dispositivo optico que amplifica luz utilizando reflexion metalica y refraccion en agua. Optimiza el rendimiento luminico con consumo minimo de combustible."}, # [cite: 30]
    "10": {"titulo": "Eco-Lamparas", "division": "EcoIndustria", "descripcion": "Faroles decorativos fabricados con latas perforadas mediante tecnica de soporte congelado. Proyectan patrones luminicos mediante perforado artistico controlado."}, # [cite: 31]
    "11": {"titulo": "Eco-Hidro", "division": "EcoIndustria", "descripcion": "Sistema de riego autonomo por capilaridad desarrollado con botellas PET. Permite mantener humedad constante sin intervencion manual prolongada."}, # [cite: 32]
    "12": {"titulo": "EcoTrash", "division": "EcoIndustria", "descripcion": "Escoba de alta resistencia construida mediante apilamiento de cerdas PET. Transforma un residuo flexible en herramienta estructural robusta."}, # [cite: 32]
    "13": {"titulo": "Tetra-Wallet", "division": "EcoIndustria", "descripcion": "Billetera impermeable creada a partir de envases multicapa Tetra Pak. Demuestra upcycling funcional de materiales de dificil reciclaje."}, # [cite: 33, 34]
    "14": {"titulo": "Carbon Ink", "division": "EcoLab", "descripcion": "Tinta negra obtenida por pirolisis controlada de papel descartado. El carbon molido se mezcla con aglutinantes para generar pigmento estable."}, # [cite: 35]
    "15": {"titulo": "Nendo Dango", "division": "EcoLab", "descripcion": "Metodo de siembra sin labranza basado en capsulas de arcilla, tierra y semillas. Protege la semilla hasta condiciones optimas de germinacion."}, # [cite: 36]
    "16": {"titulo": "Paper Beads", "division": "EcoPapel", "descripcion": "Cuentas estructurales fabricadas mediante enrollado a presion de tiras de papel. Una vez selladas adquieren rigidez comparable a materiales sinteticos."}, # [cite: 36]
    "17": {"titulo": "Eco-Voz", "division": "EcoIndustria", "descripcion": "Amplificador acustico pasivo basado en resonancia y concentracion de ondas sonoras. Incrementa volumen sin consumo electrico."}, # [cite: 37, 38]
    "18": {"titulo": "Canon Vortex", "division": "EcoIndustria", "descripcion": "Dispositivo neumatico que genera anillos de aire mediante compresion subita. Demuestra principios de dinamica de fluidos y conservacion del momento."}, # [cite: 39]
    "19": {"titulo": "Eco-Dollars", "division": "EcoPapel", "descripcion": "Sistema monetario interno basado en papel reciclado y tinta Carbon Ink. Representa economia circular aplicada dentro del stand."}, # [cite: 39, 40]
    "20": {"titulo": "Eco-Candy", "division": "EcoLab", "descripcion": "Cristales comestibles obtenidos por sobresaturacion de sacarosa. Permiten visualizar crecimiento cristalino en entorno controlado."}, # [cite: 40]
    "21": {"titulo": "EcoCristales", "division": "EcoLab", "descripcion": "Cristales de alumbre cultivados por enfriamiento de solucion sobresaturada. Forman estructuras geometricas translucidas de alto valor estetico."}, # [cite: 41, 42]
    "22": {"titulo": "EcoGenerador Metano", "division": "EcoLab", "descripcion": "Modelo teorico de digestion anaerobica para produccion de biogas. Representa conversion energetica de residuos organicos."}, # [cite: 42, 43]
    "23": {"titulo": "Reactor Joule-Carbon", "division": "EcoTech", "descripcion": "Sistema experimental que produce incandescencia mediante efecto Joule en grafito. Demuestra transformacion de energia electrica en termica y luminica."}, # # [cite: 43, 44]
    "24": {"titulo": "TerrarIA", "division": "EcoTech", "descripcion": "Ecosistema cerrado monitoreado por sensores ambientales. Integra biologia, electronica y analisis de datos en tiempo real."} # [cite: 44]
}

BASE_DE_DATOS = {
    "1": {"titulo": "Papel Seed", "claves": ["papel seed", "semillas", "germinar", "plantable", "biodegradable"], "info": "FICHA 1 - PAPEL SEED (División Celulosa): Es un papel artesanal biodegradable que lleva semillas en su interior. En lugar de tirarlo, se entierra. Materiales: Pulpa de papel viejo y semillas pequeñas (lechuga, rúcula, flores). Procedimiento: No licuar las semillas, agregarlas al final."}, # [cite: 45, 46, 47]
    "2": {"titulo": "FibroPapel", "claves": ["fibropapel", "reforzado", "tela", "resistente", "textil"], "info": "FICHA 2 - FIBROPAPEL (División Celulosa): Papel compuesto que mezcla celulosa con fibras textiles (retazos de algodón). Es mucho más flexible y resistente, ideal para tapas de libros. Se pica la tela muy fina y se mezcla con la pulpa."}, # [cite: 47, 48, 49]
    "3": {"titulo": "Manual del Reciclador", "claves": ["manual", "libro", "guía", "educativo"], "info": "FICHA 3 - MANUAL DEL RECICLADOR: Un libro educativo fabricado 100% por el equipo con tapas de Fibropapel. Recopila investigaciones y tutoriales. Encuadernación japonesa o cosida."}, # [cite: 49, 50]
    "4": {"titulo": "Marca-Páginas", "claves": ["marca", "paginas", "libros", "señalador"], "info": "FICHA 4 - MARCA-PÁGINAS: Accesorio de cartón reciclado decorado con flores prensadas o sellos. Objetivo: Entregar uno a cada juez como souvenir."}, # [cite: 50, 51]
    "5": {"titulo": "Bolsas Eco-Carrier", "claves": ["bolsas", "carrier", "empaque", "transportar"], "info": "FICHA 5 - ECO-CARRIER: Bolsas resistentes hechas con papel reciclado de gran formato o uniendo hojas A4. Reemplazan al plástico. Soportan peso gracias a un refuerzo de cartón en la base."}, # [cite: 51, 52]
    "6": {"titulo": "Colorantes Naturales", "claves": ["colorantes", "tinte", "pintura", "natural", "colores", "cebolla", "remolacha"], "info": "FICHA 6 - COLORANTES Y FIJADORES (División EcoLab): Extracción de pigmentos de residuos orgánicos. Amarillo: Cebolla/Cúrcuma. Rojo: Remolacha. Verde: Espinaca. Se usa vinagre y sal como mordiente (fijador)."}, # [cite: 52, 53]
    "7": {"titulo": "Eco-IA", "claves": ["ecoia", "eco-ia", "inteligencia", "artificial", "vision", "app", "chat"], "info": "FICHA 7 - ECO-IA (División EcoTech): Soy yo. Una aplicación que usa Visión por Computadora para clasificar residuos. Mi objetivo es eliminar el error humano al reciclar. También respondo dudas sobre el proyecto."}, # [cite: 53, 54, 55]
    "8": {"titulo": "Organizadores Eco-Modulares", "claves": ["organizador", "escritorio", "latas", "modular"], "info": "FICHA 8 - ORGANIZADORES (División EcoIndustria): Sistema de escritorio hecho con latas de conserva y tubos de cartón. Se unen con imanes o encastres para ser modulares."}, # [cite: 55, 56]
    "9": {"titulo": "EcoReflector", "claves": ["reflector", "luz", "vela", "agua", "espejo"], "info": "FICHA 9 - ECOREFLECTOR: Dispositivo que usa una lata pulida y un frasco con agua para amplificar la luz de una vela. Utiliza principios de reflexión y refracción."}, # [cite: 56, 57]
    "10": {"titulo": "Eco-Lámparas", "claves": ["lamparas", "faroles", "luz", "perforado", "estelares"], "info": "FICHA 10 - ECO-LÁMPARAS: Faroles hechos de latas grandes perforadas artísticamente. Se usa hielo dentro de la lata para martillar sin abollarla."}, # [cite: 57, 58]
    "11": {"titulo": "Eco-Hidro", "claves": ["hidro", "maceta", "riego", "agua", "capilaridad"], "info": "FICHA 11 - ECO-HIDRO: Sistema de cultivo en botellas PET que usa capilaridad. Una mecha de algodón lleva agua del depósito a la tierra automáticamente."}, # [cite: 58, 59]
    "12": {"titulo": "EcoTrash", "claves": ["ecotrash", "escoba", "barrer", "botellas", "cerdas"], "info": "FICHA 12 - ECOTRASH: Escoba de alta resistencia hecha cortando botellas PET en tiras finas. Se apilan varias botellas para dar volumen y fuerza."}, # [cite: 59, 60]
    "13": {"titulo": "Tetra-Wallet", "claves": ["billetera", "tetra", "wallet", "caja", "leche"], "info": "FICHA 13 - TETRA-WALLET: Billetera impermeable hecha reutilizando envases de Tetra Pak. Diseño plegable tipo acordeón."}, # [cite: 60, 61]
    "14": {"titulo": "Carbon Ink", "claves": ["carbon", "ink", "tinta", "negra", "hollin"], "info": "FICHA 14 - CARBON INK (División EcoLab): Tinta negra hecha quemando papel (pirólisis) para obtener carbón. Se mezcla con goma arábiga o plasticola y agua."}, # [cite: 61, 62]
    "15": {"titulo": "Nendo Dango", "claves": ["nendo", "dango", "bombas", "semillas", "arcilla"], "info": "FICHA 15 - NENDO DANGO: 'Bolas de arcilla'. Método de Masanobu Fukuoka. Mezcla de arcilla, tierra, papel y semillas para reforestación sin labranza."}, # [cite: 62, 63]
    "16": {"titulo": "Paper Beads", "claves": ["perlas", "beads", "collares", "pulseras", "joyeria"], "info": "FICHA 16 - PAPER BEADS: Cuentas de collar hechas enrollando tiras triangulares de papel y barnizándolas. Quedan duras como madera."}, # [cite: 63, 64]
    "17": {"titulo": "Eco-Voz", "claves": ["voz", "parlante", "amplificador", "musica", "celular"], "info": "FICHA 17 - ECO-VOZ: Amplificador pasivo para celular hecho con tubo de cartón y vasos. No usa electricidad, solo acústica física."}, # [cite: 64, 65]
    "18": {"titulo": "Cañon Vortex", "claves": ["canon", "vortex", "aire", "humo", "anillo"], "info": "FICHA 18 - CAÑON VORTEX: Juguete científico que dispara anillos de aire. Usa un tacho y una membrana elástica. Principio de Bernoulli."}, # [cite: 65, 66]
    "19": {"titulo": "Eco-Dollars", "claves": ["dolares", "moneda", "dinero", "billetes", "banco"], "info": "FICHA 19 - ECO-DOLLARS: Moneda interna del stand para canjear productos. 1 ED = 500 pesos (ejemplo). Hechos de papel reciclado y tinta Carbon Ink."}, # [cite: 66, 67]
    "20": {"titulo": "Eco-Candy", "claves": ["candy", "azucar", "cristales", "comestible", "dulce"], "info": "FICHA 20 - ECO-CANDY: Gemas comestibles hechas por cristalización de azúcar (sacarosa). Se saborizan con jugos en polvo."}, # [cite: 67, 68]
    "21": {"titulo": "EcoCristales", "claves": ["cristales", "alumbre", "quimica", "piedra"], "info": "FICHA 21 - ECOCRISTALES (División EcoLab): Cristales de Alumbre de Potasio cultivados por sobresaturación en agua caliente. Parecen joyas reales."}, # [cite: 68, 69]
    "22": {"titulo": "Biogás (Teórico)", "claves": ["biogas", "metano", "gas", "energia", "digestor"], "info": "FICHA 22 - ECOGENERADOR METANO: Producción de biogás mediante fermentación anaeróbica de residuos orgánicos. (Nota: Es complejo y requiere seguridad)."}, # [cite: 69, 70]
    "23": {"titulo": "Reactor Joule", "claves": ["joule", "reactor", "luz", "grafito", "electrico"], "info": "FICHA 23 - REACTOR JOULE-CARBON (División EcoTech): Generación de luz pasando electricidad por una mina de lápiz (grafito). Efecto Joule e incandescencia."}, # [cite: 70, 71]
    "24": {"titulo": "TerrarIA", "claves": ["terraria", "ecosistema", "frasco", "sensores", "arduino"], "info": "FICHA 24 - TERRARIA (División EcoTech): Ecosistema cerrado inteligente. Un frasco sellado con plantas donde la IA monitorea humedad y temperatura mediante sensores."} # [cite: 71, 72]
}

# --------------------------------------------------
# MOTOR DE DETECCIÓN INTELIGENTE [cite: 72]
# --------------------------------------------------
def detectar_contexto(prompt):
    texto = prompt.lower()
    match = re.search(r'(?:ficha|n°)\s*(\d+)', texto)
    if match and match.group(1) in BASE_DE_DATOS:
        return BASE_DE_DATOS[match.group(1)]
    for datos in BASE_DE_DATOS.values():
        for clave in datos["claves"]:
            if clave in texto:
                return datos # [cite: 73]
    return None

# Siluetas Vectoriales (SVGs optimizados para el look del proyecto)
SILUETA_PAPEL = '<svg class="icon-shape" viewBox="0 0 24 24"><path d="M17 8V5c0-1.1-.9-2-2-2H5c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h2v3c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2V9c0-1.1-.9-2-2-2h-2zm-2 9H9V5h6v12zm4 4H11v-2h4c1.1 0 2-.9 2-2V9h2v12z"/></svg>'
SILUETA_LAB = '<svg class="icon-shape" viewBox="0 0 24 24"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-9 15c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3zm3-7H7V7h6v4z"/></svg>'
SILUETA_TECH = '<svg class="icon-shape" viewBox="0 0 24 24"><path d="M21 11H19V9h2v2zm0-4h-2V5h2v2zm-2 10h2v-2h-2v2zm0 4h2v-2h-2v2zM5 13h2v-2H5v2zm0 4h2v-2H5v2zm0-8h2V7H5v2zm0-4h2V3H5v2zm8 16h2v-2h-2v2zm-4 0h2v-2H9v2zM3 11h2V9H3v2zm0-4h2V5H3v2zm11-4h-2v2h2V3zm-4 0H8v2h2V3zM7 19h10V5H7v14zm2-12h6v10H9V7z"/></svg>'
SILUETA_IND = '<svg class="icon-shape" viewBox="0 0 24 24"><path d="M22 22H2V2h20v20zM4 20h16V4H4v16zm4-3h3v-2H8v2zm5 0h3v-2h-3v2zm-5-4h3v-2H8v2zm5 0h3v-2h-3v2zm-5-4h3V7H8v2zm5 0h3V7h-3v2z"/></svg>'

# --------------------------------------------------
# MENÚ NAVEGACIÓN [cite: 74]
# --------------------------------------------------
with st.sidebar:
    st.markdown("## 🌱 Ecosistema Eco")
    selected = option_menu(
        menu_title="Navegación",
        options=["Inicio", "Fichas Técnicas", "EcoIA"], # [cite: 74]
        icons=["house-door", "grid-3x3-gap", "cpu-fill"],
        default_index=0,
        styles={
            "container": {"background-color": "#070f14"},
            "nav-link": {"color": "#f0fdf4", "font-size": "15px"},
            "nav-link-selected": {"background-color": "#16a34a", "color": "white", "font-weight": "600"},
        }
    )
    st.write("---")
    st.caption("⚡ 4°4° - E.E.S.T N°7") # [cite: 74]

# --------------------------------------------------
# RENDERIZADO: VISTA INICIO [cite: 74]
# --------------------------------------------------
if selected == "Inicio":
    st.markdown('<div class="hero"><h1>Proyecto Eco 2026</h1><p>Sistema Integral de Innovación Sustentable Escolar e Interdisciplinario</p></div>', unsafe_allow_html=True) # [cite: 74, 75]
    
    col_v, col_e = st.columns([2, 1])
    with col_v:
        st.markdown("""
        <div class="card">
            <h3>Visión Institucional y Evolución</h3>
            <p>Proyecto interdisciplinario orientado a la innovación ecológica, la educación ambiental y el desarrollo tecnológico sustentable. Integra reciclaje, biotecnología, tecnología digital e inteligencia artificial.</p>
            <p>A diferencia de un proyecto tradicional de reciclaje, Eco funciona como un ecosistema organizado en divisiones especializadas que operan de manera interconectada. Cada módulo aporta conocimiento técnico y producción material, formando un modelo de economía circular aplicada a escala educativa.</p>
            <p>Lo que comenzó en 2025 como EcoPapel hoy evolucionó hacia un sistema estructurado en cuatro divisiones especializadas que trabajan de forma integrada para competir al más alto nivel federal.</p>
        </div>
        """, unsafe_allow_html=True) # [cite: 75, 76, 77, 78]
    
    with col_e:
        st.markdown("<div style='height: 5px;'></div>", unsafe_allow_html=True)
        st.metric("Fichas Eco", "24", help="Módulos técnicos desarrollados") # [cite: 81]
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        st.metric("Secciones", "4", help="Unidades de especialización") # [cite: 81]

    st.write("---")
    st.subheader("Estructura de Divisiones Estratégicas")
    
    d1, d2, d3, d4 = st.columns(4)
    with d1:
        st.markdown(f'<div class="card"><div class="icon-container">{SILUETA_PAPEL}</div><h3>EcoPapel</h3><p class="mini">Seccion Artistica</p><p>Transformación de residuos celulósicos en distintas lineas artisticas, utiles y educativas.</p></div>', unsafe_allow_html=True) # [cite: 79]
    with d2:
        st.markdown(f'<div class="card"><div class="icon-container">{SILUETA_LAB}</div><h3>EcoLab</h3><p class="mini">Seccion Cientifica</p><p>Investigación aplicada a la obtención de pigmentos orgánicos, reactores moleculares, cristalizaciones controladas, etc.</p></div>', unsafe_allow_html=True) # [cite: 79, 80]
    with d3:
        st.markdown(f'<div class="card"><div class="icon-container">{SILUETA_TECH}</div><h3>EcoTech</h3><p class="mini">Seccion Tecnologica</p><p>Unidad de automatización basada en microcontroladores, sensado ambiental interactivo e interfaces de Inteligencia Artificial. Además del control de Marketing y redes sociales.</p></div>', unsafe_allow_html=True) # [cite: 80, 81]
    with d4:
        st.markdown(f'<div class="card"><div class="icon-container">{SILUETA_IND}</div><h3>EcoIndustria</h3><p class="mini">Seccion Industrial</p><p>Diseño y optimización mecánica que transforma residuos urbanos complejos en herramientas de uso estructural autónomo.</p></div>', unsafe_allow_html=True) # [cite: 81]

    st.write("---")
    st.subheader("Dinámica Interna: Economía Circular Real") # [cite: 81, 82]
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="card">
            <h4>1. Captura de Residuos e Incentivo</h4>
            <p>Se interceptan materiales descartados (PET, Tetra Pak, aluminio, cartón). A través de nuestro Banco de Intercambio, se fomenta el uso de los <b>EcoDollars</b> como dinamizadores de valor sustentable dentro del ecosistema escolar.</p>
        </div>
        """, unsafe_allow_html=True) # [cite: 83, 84, 85]
    with c2:
        st.markdown("""
        <div class="card">
            <h4>3. Mitigación y Residuo Cero</h4>
            <p>Los excedentes de papel irrecuperable sufren pirólisis controlada para sintetizar <b>Carbon Ink</b>, cerrando el bucle: escribir sobre papel nuevo con su propio remanente químico.</p>
            <h4>4. Tecnología y Entorno Autónomo</h4>
            <p>El ciclo biológico culmina con técnicas agrícolas como el <i>Nendo Dango</i> para reforestación acelerada, mientras que interfaces como <b>TerrarIA</b> procesan telemetría ecosistémica en tiempo real.</p>
        </div>
        """, unsafe_allow_html=True) # [cite: 85, 86, 87]

    st.write("---")
    st.subheader("Cuadro Técnico de Investigadores") # [cite: 87]
    equipo = [
        {"nombre": "Damian Medina", "rol": "EcoPapel y EcoIndustria | Colaborador"}, # [cite: 87, 88]
        {"nombre": "Dante Rodriguez", "rol": "EcoTech | Desarrollo EcoIA y TerrarIA"}, # [cite: 88]
        {"nombre": "Enzo Cuevas", "rol": "EcoPapel | Colaborador de Sección"}, # [cite: 88]
        {"nombre": "Franco Titirico", "rol": "EcoIndustria | Representante"}, # [cite: 88, 89, 90]
        {"nombre": "Jonathan Orellana", "rol": "EcoPapel | Representante"}, # [cite: 90]
        {"nombre": "Julian Tejerina", "rol": "EcoTech | Representante"}, # [cite: 90]
        {"nombre": "Tobias Ponce Castaño", "rol": "EcoLab | Representante"}, # [cite: 90, 91]
        {"nombre": "Valentino Correa", "rol": "EcoLab | Colaborador"} # [cite: 91]
    ]
    cols_eq = st.columns(4)
    for index, miembro in enumerate(equipo):
        with cols_eq[index % 4]:
            st.markdown(f'<div class="card" style="padding:15px; margin-bottom:10px; border-left: 3px solid #4ADE80;"><b>{miembro["nombre"]}</b><br><span style="font-size:12px; opacity:0.8;">{miembro["rol"]}</span></div>', unsafe_allow_html=True)

    st.write("---")
    st.caption("Proyecto Eco 2026 · Ciencia Aplicada · Innovación de Base Tecnológica") # [cite: 97, 98]

# --------------------------------------------------
# RENDERIZADO: VISTA FICHAS TÉCNICAS (DASHBOARD GRID PROFESIONAL) [cite: 98]
# --------------------------------------------------
elif selected == "Fichas Técnicas":
    st.markdown('<div class="ecoia-header"><h2>Biblioteca y Catálogo de Fichas Técnicas</h2><p>Filtro modular dinámico optimizado para revisión de jurados técnicos.</p></div>', unsafe_allow_html=True) # [cite: 98]
    
    filtro = st.selectbox(
        "Seleccione División de Estudio:",
        ["Todas", "EcoPapel", "EcoLab", "EcoTech", "EcoIndustria"] # [cite: 98]
    )
    
    # Filtrar fichas activas
    fichas_filtradas = {k: v for k, v in FICHAS_DETALLADAS.items() if filtro == "Todas" or v["division"] == filtro} # [cite: 98, 99]
    
    # Renderizado inteligente en Grid de 3 columnas para evitar scroll infinito lineal [cite: 98]
    items = list(fichas_filtradas.items())
    rows = [items[i:i + 3] for i in range(0, len(items), 3)]
    
    for row in rows:
        grid_cols = st.columns(3)
        for idx, (num, datos) in enumerate(row):
            with grid_cols[idx]:
                badge_color = "#22c55e" if datos["division"] == "EcoPapel" else "#3b82f6" if datos["division"] == "EcoTech" else "#eab308" if datos["division"] == "EcoLab" else "#a855f7"
                st.markdown(f"""
                <div class="card" style="display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                            <span style="background:{badge_color}; color:white; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:bold;">{datos["division"]}</span>
                            <b style="color:#4ADE80;">ID: #{num}</b>
                        </div>
                        <h4 style="margin-top:5px; color:white !important;">{datos["titulo"]}</h4>
                        <p style="font-size:14px; opacity:0.9; line-height:1.5;">{datos["descripcion"]}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True) # [cite: 99]

# --------------------------------------------------
# RENDERIZADO: NÚCLEO ECOIA [cite: 100]
# --------------------------------------------------
elif selected == "EcoIA":
    st.markdown("""
    <div class="ecoia-header">
        <h2>EcoIA · Asistente de Documentación Homologado</h2>
        <p class="mini">División EcoTech · Procesamiento de Lenguaje Natural</p>
        <p style="font-size:14px; opacity:0.9;">Interfaz inteligente para auditoría y consulta inmediata de la base científica del proyecto. Diseñada bajo restricciones estrictas de veracidad institucional.</p>
    </div>
    """, unsafe_allow_html=True) # [cite: 100]

    # Inicialización estable de memoria de conversación [cite: 100]
    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant", # [cite: 100, 101]
            "content": "Hola, soy EcoIA, el sistema centralizado de documentación del Proyecto Eco. ¿Qué ficha técnica o módulo específico del stand deseás auditar?" # [cite: 101, 102]
        }]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    prompt = st.chat_input("Escribí tu consulta técnica (Ej: Ficha 1, Nendo Dango, FibroPapel)...") # [cite: 102]

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt}) # [cite: 102]
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            response_container = st.empty()
            ficha = detectar_contexto(prompt) # [cite: 103]

            system_prompt = """
            Eres EcoIA, núcleo técnico del Proyecto Eco (División EcoTech).
            Actúas exclusivamente como sistema de documentación interna del stand escolar.

            Reglas obligatorias de comportamiento:
            1. SOLO puedes responder usando la INFORMACIÓN DE FICHA proporcionada.
            2. Si la información exacta no está explícita en la ficha provista, debes responder textualmente:
               "La información solicitada no está disponible en la ficha técnica correspondiente."
            3. Queda prohibido inventar, deducir o añadir conocimiento externo o comercial.
            4. Sé extremadamente directo, técnico y conciso. Evita saludos largos si ya estás respondiendo.
            """ # [cite: 103, 104, 105, 106]

            try:
                # Instanciación limpia y segura [cite: 106]
                api_key = os.environ.get("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY", "")
                if not api_key:
                    st.error("Error: Credencial de API (GROQ_API_KEY) no configurada.")
                    st.stop()
                
                client = Groq(api_key=api_key) # [cite: 106, 107]
                messages = [{"role": "system", "content": system_prompt}] # [cite: 107]

                if ficha:
                    user_content = f"Información técnica oficial:\n{ficha['info']}\n\nConsulta del visitante:\n{prompt}" # [cite: 107]
                else:
                    user_content = f"Consulta del visitante:\n{prompt}\n\nNota: Si no se refiere a una ficha explícita, recuerda la regla de denegación." # [cite: 108]

                messages.append({"role": "user", "content": user_content}) # [cite: 109]

                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant", # [cite: 109]
                    messages=messages,
                    temperature=0.05 # Menor temperatura = Menos margen de alucinación/invento [cite: 109]
                )

                respuesta = completion.choices[0].message.content # [cite: 110]
                response_container.markdown(respuesta)
                st.session_state.messages.append({"role": "assistant", "content": respuesta}) # [cite: 110]

            except Exception as e:
                st.error("Error en la llamada de inferencia local:")
                st.code(str(e)) # [cite: 111]
