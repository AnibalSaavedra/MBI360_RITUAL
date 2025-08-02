
import streamlit as st

st.set_page_config(page_title="MBI 360° | RITUAL", layout="centered")

st.title("🌀 MBI 360° – Evaluación Integral del Ser")
st.markdown("""
Bienvenido al sistema **MBI 360°**, una herramienta única para conocer en profundidad tu estado emocional, epigenético, físico y energético.

Selecciona el módulo que deseas evaluar:
- Puedes elegir uno o varios, según tu interés.
- Al finalizar, recibirás un informe PDF y podrás contactar directamente para iniciar tu proceso terapéutico.

**Marca:** RITUAL  
**Creador:** Aníbal Saavedra – Biotecnólogo MIB
""")

modulos = {
    "Test de disociación o trauma": "🔹 Evaluar desconexión emocional y fragmentación del yo.",
    "Estado epigenético emocional (materno/paterno)": "🔹 Analizar heridas heredadas y patrones repetitivos.",
    "Condiciones clínicas opcionales": "🔹 Identificar posibles desequilibrios físicos que acompañan tu estado emocional."
}

seleccion = st.multiselect("Selecciona los módulos que deseas realizar:", options=list(modulos.keys()))

if seleccion:
    st.success("Has seleccionado los siguientes módulos:")
    for s in seleccion:
        st.markdown(f"- {s}: {modulos[s]}")
    st.markdown("👉 Presiona el botón inferior para comenzar con los módulos.")
    if st.button("Iniciar Evaluación"):
        st.info("⚙️ Esta función estará disponible en la próxima versión. Estamos preparando cada módulo.")
else:
    st.info("Selecciona al menos un módulo para comenzar.")
