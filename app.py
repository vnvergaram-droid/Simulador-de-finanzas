import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Simulador de Finanzas",
    page_icon=""
)

# HISTORIAL

if "historial" not in st.session_state:
    st.session_state.historial = []

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

        st.error(
            " El ahorro no puede ser mayor que los ingresos."
        )

    else:

        balance = ingresos - total_gastos - ahorro

        # GUARDAR EN HISTORIAL

        registro = {
            "Fecha": datetime.now().strftime("%H:%M:%S"),
            "Ingresos": ingresos,
            "Gastos": total_gastos,
            "Ahorro": ahorro,
            "Balance": balance
        }

        st.session_state.historial.append(registro)

        st.subheader(" Resumen financiero")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Ingresos",
                f"${ingresos:,.0f}"
            )

        with col2:
            st.metric(
                "Balance",
                f"${balance:,.0f}"
            )

        st.metric(
            "Gastos",
            f"${total_gastos:,.0f}"
        )

        st.metric(
            "Ahorro",
            f"${ahorro:,.0f}"
        )

        # DIAGNÓSTICO

        st.subheader("🚦 Diagnóstico financiero")

        porcentaje_restante = (
            (balance / ingresos) * 100
            if ingresos > 0 else 0
        )

        if porcentaje_restante >= 30:

            st.success(
                "🟢 Excelente manejo financiero."
            )

        elif porcentaje_restante >= 10:

            st.warning(
                "🟡 Buen manejo financiero."
            )

        else:

            st.error(
                "🔴 Debes mejorar el control de tus gastos."
            )

        # RECOMENDACIONES

        st.subheader(" Recomendaciones")

        if total_gastos > ingresos:

            st.warning(
                "Tus gastos son mayores que tus ingresos."
            )

        elif ahorro >= ingresos * 0.2:

            st.success(
                "Excelente hábito de ahorro."
            )

        else:

            st.info(
                "Puedes plantearte una meta de ahorro mayor."
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

# HISTORIAL

if len(st.session_state.historial) > 0:

    st.subheader(" Historial de registros")

    historial_df = pd.DataFrame(
        st.session_state.historial
    )

    st.dataframe(historial_df)

    if len(historial_df) >= 2:

        st.subheader(" Comparación con registro anterior")

        ultimo = historial_df.iloc[-1]
        anterior = historial_df.iloc[-2]

        st.write(
            f" Diferencia de ingresos: ${ultimo['Ingresos'] - anterior['Ingresos']:,.0f}"
        )

        st.write(
            f" Diferencia de gastos: ${ultimo['Gastos'] - anterior['Gastos']:,.0f}"
        )

        st.write(
            f" Diferencia de ahorro: ${ultimo['Ahorro'] - anterior['Ahorro']:,.0f}"
        )

        st.write(
            f" Diferencia de balance: ${ultimo['Balance'] - anterior['Balance']:,.0f}"
        )
