import streamlit as st
from streamlit_option_menu import option_menu
from groq import Groq
import os
import re

# --------------------------------------------------
# CONFIGURACIÓN GENERAL
# --------------------------------------------------

st.set_page_config(
    page_title="Proyecto Eco 2026",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
div[data-testid="stMetric"] {
    background-color: #172d43;
    border-radius: 12px;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# BASE DE DATOS (MANTENÉ LA TUYA COMPLETA)
# --------------------------------------------------

BASE_DE_DATOS = {
    "1": {
        "titulo": "Papel Seed",
        "claves": ["papel seed", "semillas", "germinar", "plantable", "biodegradable"],
        "info": "FICHA 1 - PAPEL SEED (División Celulosa): Es un papel artesanal biodegradable que lleva semillas en su interior[cite: 23]. En lugar de tirarlo, se entierra. Materiales: Pulpa de papel viejo y semillas pequeñas (lechuga, rúcula, flores). Procedimiento: No licuar las semillas, agregarlas al final."
    },
    "2": {
        "titulo": "FibroPapel",
        "claves": ["fibropapel", "reforzado", "tela", "resistente", "textil"],
        "info": "FICHA 2 - FIBROPAPEL (División Celulosa): Papel compuesto que mezcla celulosa con fibras textiles (retazos de algodón)[cite: 51]. Es mucho más flexible y resistente, ideal para tapas de libros. Se pica la tela muy fina y se mezcla con la pulpa."
    },
    "3": {
        "titulo": "Manual del Reciclador",
        "claves": ["manual", "libro", "guía", "educativo"],
        "info": "FICHA 3 - MANUAL DEL RECICLADOR: Un libro educativo fabricado 100% por el equipo con tapas de Fibropapel[cite: 67]. Recopila investigaciones y tutoriales. Encuadernación japonesa o cosida."
    },
    "4": {
        "titulo": "Marca-Páginas",
        "claves": ["marca", "paginas", "libros", "señalador"],
        "info": "FICHA 4 - MARCA-PÁGINAS: Accesorio de cartón reciclado decorado con flores prensadas o sellos[cite: 74]. Objetivo: Entregar uno a cada juez como souvenir."
    },
    "5": {
        "titulo": "Bolsas Eco-Carrier",
        "claves": ["bolsas", "carrier", "empaque", "transportar"],
        "info": "FICHA 5 - ECO-CARRIER: Bolsas resistentes hechas con papel reciclado de gran formato o uniendo hojas A4[cite: 87]. Reemplazan al plástico. Soportan peso gracias a un refuerzo de cartón en la base."
    },
    "6": {
        "titulo": "Colorantes Naturales",
        "claves": ["colorantes", "tinte", "pintura", "natural", "colores", "cebolla", "remolacha"],
        "info": "FICHA 6 - COLORANTES Y FIJADORES (División EcoLab): Extracción de pigmentos de residuos orgánicos[cite: 99]. Amarillo: Cebolla/Cúrcuma. Rojo: Remolacha. Verde: Espinaca. Se usa vinagre y sal como mordiente (fijador)."
    },
    "7": {
        "titulo": "Eco-IA",
        "claves": ["ecoia", "eco-ia", "inteligencia", "artificial", "vision", "app", "chat"],
        "info": "FICHA 7 - ECO-IA (División EcoTech): Soy yo. Una aplicación que usa Visión por Computadora para clasificar residuos[cite: 110]. Mi objetivo es eliminar el error humano al reciclar. También respondo dudas sobre el proyecto."
    },
    "8": {
        "titulo": "Organizadores Eco-Modulares",
        "claves": ["organizador", "escritorio", "latas", "modular"],
        "info": "FICHA 8 - ORGANIZADORES (División EcoIndustria): Sistema de escritorio hecho con latas de conserva y tubos de cartón[cite: 119]. Se unen con imanes o encastres para ser modulares."
    },
    "9": {
        "titulo": "EcoReflector",
        "claves": ["reflector", "luz", "vela", "agua", "espejo"],
        "info": "FICHA 9 - ECOREFLECTOR: Dispositivo que usa una lata pulida y un frasco con agua para amplificar la luz de una vela[cite: 147]. Utiliza principios de reflexión y refracción."
    },
    "10": {
        "titulo": "Eco-Lámparas",
        "claves": ["lamparas", "faroles", "luz", "perforado", "estelares"],
        "info": "FICHA 10 - ECO-LÁMPARAS: Faroles hechos de latas grandes perforadas artísticamente[cite: 131]. Se usa hielo dentro de la lata para martillar sin abollarla."
    },
    "11": {
        "titulo": "Eco-Hidro",
        "claves": ["hidro", "maceta", "riego", "agua", "capilaridad"],
        "info": "FICHA 11 - ECO-HIDRO: Sistema de cultivo en botellas PET que usa capilaridad[cite: 158]. Una mecha de algodón lleva agua del depósito a la tierra automáticamente."
    },
    "12": {
        "titulo": "EcoTrash",
        "claves": ["ecotrash", "escoba", "barrer", "botellas", "cerdas"],
        "info": "FICHA 12 - ECOTRASH: Escoba de alta resistencia hecha cortando botellas PET en tiras finas[cite: 172]. Se apilan varias botellas para dar volumen y fuerza."
    },
    "13": {
        "titulo": "Tetra-Wallet",
        "claves": ["billetera", "tetra", "wallet", "caja", "leche"],
        "info": "FICHA 13 - TETRA-WALLET: Billetera impermeable hecha reutilizando envases de Tetra Pak[cite: 185]. Diseño plegable tipo acordeón."
    },
    "14": {
        "titulo": "Carbon Ink",
        "claves": ["carbon", "ink", "tinta", "negra", "hollin"],
        "info": "FICHA 14 - CARBON INK (División EcoLab): Tinta negra hecha quemando papel (pirólisis) para obtener carbón[cite: 198]. Se mezcla con goma arábiga o plasticola y agua."
    },
    "15": {
        "titulo": "Nendo Dango",
        "claves": ["nendo", "dango", "bombas", "semillas", "arcilla"],
        "info": "FICHA 15 - NENDO DANGO: 'Bolas de arcilla'. Método de Masanobu Fukuoka[cite: 214]. Mezcla de arcilla, tierra, papel y semillas para reforestación sin labranza."
    },
    "16": {
        "titulo": "Paper Beads",
        "claves": ["perlas", "beads", "collares", "pulseras", "joyeria"],
        "info": "FICHA 16 - PAPER BEADS: Cuentas de collar hechas enrollando tiras triangulares de papel y barnizándolas[cite: 228]. Quedan duras como madera."
    },
    "17": {
        "titulo": "Eco-Voz",
        "claves": ["voz", "parlante", "amplificador", "musica", "celular"],
        "info": "FICHA 17 - ECO-VOZ: Amplificador pasivo para celular hecho con tubo de cartón y vasos[cite: 241]. No usa electricidad, solo acústica física."
    },
    "18": {
        "titulo": "Cañon Vortex",
        "claves": ["canon", "vortex", "aire", "humo", "anillo"],
        "info": "FICHA 18 - CAÑON VORTEX: Juguete científico que dispara anillos de aire[cite: 253]. Usa un tacho y una membrana elástica. Principio de Bernoulli."
    },
    "19": {
        "titulo": "Eco-Dollars",
        "claves": ["dolares", "moneda", "dinero", "billetes", "banco"],
        "info": "FICHA 19 - ECO-DOLLARS: Moneda interna del stand para canjear productos[cite: 269]. 1 ED = 500 pesos (ejemplo). Hechos de papel reciclado y tinta Carbon Ink."
    },
    "20": {
        "titulo": "Eco-Candy",
        "claves": ["candy", "azucar", "cristales", "comestible", "dulce"],
        "info": "FICHA 20 - ECO-CANDY: Gemas comestibles hechas por cristalización de azúcar (sacarosa)[cite: 293]. Se saborizan con jugos en polvo."
    },
    "21": {
        "titulo": "EcoCristales",
        "claves": ["cristales", "alumbre", "quimica", "piedra"],
        "info": "FICHA 21 - ECOCRISTALES (División EcoLab): Cristales de Alumbre de Potasio cultivados por sobresaturación en agua caliente[cite: 305]. Parecen joyas reales."
    },
    "22": {
        "titulo": "Biogás (Teórico)",
        "claves": ["biogas", "metano", "gas", "energia", "digestor"],
        "info": "FICHA 22 - ECOGENERADOR METANO: Producción de biogás mediante fermentación anaeróbica de residuos orgánicos[cite: 341]. (Nota: Es complejo y requiere seguridad)."
    },
    "23": {
        "titulo": "Reactor Joule",
        "claves": ["joule", "reactor", "luz", "grafito", "electrico"],
        "info": "FICHA 23 - REACTOR JOULE-CARBON (División EcoTech): Generación de luz pasando electricidad por una mina de lápiz (grafito)[cite: 357]. Efecto Joule e incandescencia."
    },
    "24": {
        "titulo": "TerrarIA",
        "claves": ["terraria", "ecosistema", "frasco", "sensores", "arduino"],
        "info": "FICHA 24 - TERRARIA (División EcoTech): Ecosistema cerrado inteligente[cite: 376]. Un frasco sellado con plantas donde la IA monitorea humedad y temperatura mediante sensores."
    }
}

# --------------------------------------------------
# FUNCIÓN DETECCIÓN CONTEXTO
# --------------------------------------------------

def detectar_contexto(prompt):
    texto = prompt.lower()

    match = re.search(r'(?:ficha|n°)\s*(\d+)', texto)
    if match and match.group(1) in BASE_DE_DATOS:
        return BASE_DE_DATOS[match.group(1)]

    for datos in BASE_DE_DATOS.values():
        for clave in datos["claves"]:
            if clave in texto:
                return datos

    return None

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.markdown("## Proyecto Eco")

    selected = option_menu(
        menu_title="Menú Principal",
        options=["Inicio", "Fichas Técnicas", "EcoIA"],
        icons=["house", "book", "cpu"],
        default_index=0,
        styles={
            "nav-link-selected": {"background-color": "#2E8B57"},
        }
    )

    st.write("---")
    st.caption("4°4° - E.E.S.T N°7")

# --------------------------------------------------
# INICIO
# --------------------------------------------------

if selected == "Inicio":

    st.title("Proyecto Eco 2026")
    st.markdown("### Ciencia · Tecnología · Economía Circular Aplicada")

    st.write("""
Proyecto Eco es un sistema integral de innovación sustentable
que transforma residuos en recursos mediante ciencia,
ingeniería y tecnología aplicada.
""")

    c1, c2, c3 = st.columns(3)
    c1.metric("Fichas Técnicas", "24")
    c2.metric("Divisiones", "4")
    c3.metric("Instancia", "Regional 2026")

# --------------------------------------------------
# FICHAS
# --------------------------------------------------

elif selected == "Fichas Técnicas":

    st.title("Biblioteca Técnica Eco")
    st.write("Explorá las fichas desarrolladas por cada división.")

    for num, datos in BASE_DE_DATOS.items():
        with st.expander(f"Ficha {num} - {datos['titulo']}"):
            st.write(datos["info"])

# --------------------------------------------------
# ECOIA (VERSIÓN NUBE ESTABLE)
# --------------------------------------------------

elif selected == "EcoIA":

    st.title("EcoIA · Núcleo de Conocimiento")
    st.caption("División EcoTech | Sistema de Documentación Inteligente")

    st.info(
        "EcoIA permite consultar en tiempo real cualquier ficha técnica "
        "del Proyecto Eco mediante un modelo de lenguaje optimizado "
        "para documentación científica educativa."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Hola. Soy EcoIA. Podés consultarme cualquier ficha técnica del proyecto."
        }]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Escribí tu consulta técnica..."):

        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("assistant"):

            response_container = st.empty()

            ficha = detectar_contexto(prompt)

            system = """
Eres EcoIA, núcleo técnico del Proyecto Eco (División EcoTech).
Actúas exclusivamente como sistema de documentación interna.

Reglas obligatorias:
1. SOLO puedes responder usando la INFORMACIÓN DE FICHA proporcionada.
2. Si la información no está en la ficha, debes decir:
   "La información solicitada no está disponible en la ficha técnica correspondiente."
3. No agregues conocimiento externo.
4. No generalices.
5. No recomiendes productos comerciales.
6. Mantén tono técnico y conciso.
"""


            try:
                client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


                messages = [{"role": "system", "content": system}]

                if ficha:
                    user_content = f"""
Información técnica:
{ficha['info']}

Consulta del visitante:
{prompt}
"""
                else:
                    user_content = f"""
Consulta del visitante:
{prompt}

Relaciona la respuesta con sustentabilidad o ciencia.
"""

                messages.append({"role": "user", "content": user_content})

                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=messages,
                    temperature=0.1,
                )

                respuesta = completion.choices[0].message.content

                response_container.markdown(respuesta)

                st.session_state.messages.append(
                    {"role": "assistant", "content": respuesta}
                )

            except Exception as e:
                st.error("Error real:")
                st.code(str(e))
