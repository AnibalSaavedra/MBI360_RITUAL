
import streamlit as st
from fpdf import FPDF
import datetime

def modulo_disociacion():
    st.header("🧠 Test de Disociación o Trauma – DES-II")
    st.markdown("Este test evalúa experiencias disociativas. Responde con sinceridad cuánto te ocurren estas experiencias (0 a 100%).")

    afirmaciones = [
        "Pérdidas de tiempo (no recordar lo que hizo).",
        "Recordar cosas que no hizo.",
        "Encontrar objetos que no recuerda haber comprado.",
        "Sentirse fuera de su cuerpo.",
        "Escuchar voces internas con opiniones distintas.",
        "Cambios bruscos de humor sin causa aparente.",
        "Sentir que actúa como si fuera otra persona.",
        "Ver cosas que otros no ven.",
        "Falta de conexión con el entorno.",
        "Automatismo en tareas cotidianas (manejar sin recordar el trayecto).",
        "Sentirse como si observara una película de sí mismo.",
        "No reconocer lugares conocidos.",
        "Sentirse desconectado emocionalmente.",
        "No recordar eventos importantes.",
        "Sentirse controlado por fuerzas externas.",
        "Olvidar lo que acaba de decir o hacer.",
        "Tener nombres distintos para diferentes contextos.",
        "Conversaciones sin recordar su inicio.",
        "Soñar despierto en exceso.",
        "Sentirse ajeno a su cuerpo.",
        "Bloqueos de memoria frecuentes.",
        "Confusión sobre quién es.",
        "Sentir que hay 'otra parte de sí mismo'.",
        "Despersonalización.",
        "Desrealización.",
        "Cambiar la letra al escribir sin darse cuenta.",
        "Sentirse como niño/a en situaciones cotidianas.",
        "Experimentar recuerdos como si estuviera viviéndolos nuevamente."
    ]

    respuestas = []
    for i, af in enumerate(afirmaciones):
        val = st.slider(f"{i+1}. {af}", 0, 100, 0, 5, key=f"af_{i}")
        respuestas.append(val)

    if st.button("Finalizar y generar informe"):
        puntaje_total = round(sum(respuestas) / len(respuestas), 2)
        st.subheader("📊 Resultado:")
        if puntaje_total < 30:
            estado = "bajo"
            mensaje = "No se observan signos relevantes de disociación."
        elif 30 <= puntaje_total < 60:
            estado = "moderado"
            mensaje = "Se observan rasgos disociativos moderados. Sería recomendable explorar posibles experiencias traumáticas pasadas."
        else:
            estado = "alto"
            mensaje = "Alto nivel de disociación. Es probable que existan traumas no integrados que requieren acompañamiento terapéutico."

        st.success(f"Puntaje promedio: {puntaje_total}% ({estado.upper()})")
        st.markdown(f"**Interpretación:** {mensaje}")

        # Recomendaciones
        st.markdown("### 🧭 Recomendaciones:")
        st.markdown("- Considera iniciar un proceso terapéutico de integración.")
        st.markdown("- Técnicas como EMDR, hipnosis, PNL y constelaciones familiares pueden ser útiles.")
        st.markdown("- Si lo deseas, puedes agendar una consulta personalizada.")

        # PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "Informe de Evaluación – MBI 360°", ln=True, align="C")
        pdf.ln(10)
        pdf.set_font("Arial", "", 12)
        pdf.cell(0, 10, "Módulo: Test de Disociación o Trauma (DES-II)", ln=True)
        pdf.cell(0, 10, f"Puntaje promedio: {puntaje_total}%", ln=True)
        pdf.cell(0, 10, f"Estado: {estado.upper()}", ln=True)
        pdf.multi_cell(0, 10, f"Interpretación: {mensaje}")
        pdf.ln(10)
        pdf.cell(0, 10, "Fecha: " + datetime.datetime.now().strftime("%d-%m-%Y"), ln=True)
        pdf.ln(20)
        pdf.cell(0, 10, "Firma: Aníbal Saavedra – Biotecnólogo MIB", ln=True)

        pdf_output = str(modulo_dir / "informe_disociacion.pdf")
        pdf.output(pdf_output)

        with open(pdf_output, "rb") as file:
            btn = st.download_button(
                label="📥 Descargar Informe PDF",
                data=file,
                file_name="Informe_DISOCIACION_MBI360.pdf",
                mime="application/pdf"
            )

        # WhatsApp contacto
        st.markdown("📲 ¿Quieres conversar tu resultado o agendar? [Haz clic aquí para contactar por WhatsApp](https://wa.me/56967010107)")
