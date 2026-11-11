import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Simulador de Finanzas",
    page_icon=""
)

st.title(" Simulador de Finanzas Personales")

st.write(
    "Esta herramienta permite organizar ingresos, gastos y ahorro para conocer tu situación financiera."
)

# INGRESOS

ingresos = st.number_input(
    " Ingresos",
    min_value=0.0,
    value=0.0
)

st.subheader(" Categorías de gastos")

alimentacion = st.number_input(" Alimentación", min_value=0.0)
transporte = st.number_input(" Transporte", min_value=0.0)
educacion = st.number_input(" Educación", min_value=0.0)
ocio = st.number_input(" Ocio", min_value=0.0)
otros = st.number_input(" Otros", min_value=0.0)

total_gastos = (
    alimentacion +
    transporte +
    educacion +
    ocio +
    otros
)

st.info(f" Gastos totales: ${total_gastos:,.0f}")

# AHORRO

st.subheader(" Ahorro")

tipo_ahorro = st.radio(
    "Selecciona el tipo de ahorro",
    ["Por porcentaje", "Cantidad fija"]
)

ahorro = 0

if tipo_ahorro == "Por porcentaje":
    porcentaje = st.slider(
        "Porcentaje de ahorro (%)",
        min_value=0,
        max_value=100,
        value=10
    )

    ahorro = ingresos * (porcentaje / 100)

else:
    ahorro = st.number_input(
        " Cantidad fija de ahorro",
        min_value=0.0
    )

# BOTÓN

if st.button(" Calcular"):

    if ahorro > ingresos:
        st.error(" El ahorro no puede ser mayor que los ingresos.")

    else:

        balance = ingresos - total_gastos - ahorro

        st.subheader(" Resumen financiero")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Ingresos", f"${ingresos:,.0f}")

        with col2:
            st.metric("Balance", f"${balance:,.0f}")

        st.metric("Gastos", f"${total_gastos:,.0f}")
        st.metric("Ahorro", f"${ahorro:,.0f}")

        # DIAGNÓSTICO

        st.subheader("🚦 Diagnóstico financiero")

        porcentaje_restante = (
            (balance / ingresos) * 100
            if ingresos > 0 else 0
        )

        if porcentaje_restante >= 30:
            st.success(
                "🟢 Excelente manejo financiero. Mantienes un buen equilibrio entre gasto y ahorro."
            )

        elif porcentaje_restante >= 10:
            st.warning(
                "🟡 Buen manejo financiero, aunque podrías aumentar tu ahorro."
            )

        else:
            st.error(
                "🔴 Debes mejorar el control de tus gastos."
            )

        # RECOMENDACIONES

        st.subheader(" Recomendaciones")

        if total_gastos > ingresos:
            st.warning(
                "Tus gastos son mayores que tus ingresos. Intenta reducir gastos innecesarios."
            )

        elif ahorro >= ingresos * 0.2:
            st.success(
                "Excelente hábito de ahorro. Estás destinando más del 20% de tus ingresos."
            )

        else:
            st.info(
                "Puedes plantearte una meta de ahorro mayor para mejorar tu planificación financiera."
            )

        # TABLA

        st.subheader(" Distribución de gastos")

        tabla = pd.DataFrame({
            "Categoría": [
                "Alimentación",
                "Transporte",
                "Educación",
                "Ocio",
                "Otros"
            ],
            "Valor": [
                alimentacion,
                transporte,
                educacion,
                ocio,
                otros
            ]
        })

        st.dataframe(tabla)

        # GRÁFICO

        st.subheader(" Gráfico de gastos")

        st.bar_chart(
            tabla.set_index("Categoría")
        )
