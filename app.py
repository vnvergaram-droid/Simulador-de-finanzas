import streamlit as st

st.title("💰 Simulador de Finanzas Personales")

st.write("Organiza tus ingresos, gastos y ahorro de forma sencilla.")

# INGRESOS
ingresos = st.number_input(
    "💵 Ingresos",
    min_value=0.0,
    value=0.0
)

st.subheader("📋 Categorías de gastos")

alimentacion = st.number_input("🍔 Alimentación", min_value=0.0)
transporte = st.number_input("🚌 Transporte", min_value=0.0)
educacion = st.number_input("📚 Educación", min_value=0.0)
ocio = st.number_input("🎮 Ocio", min_value=0.0)
otros = st.number_input("📦 Otros", min_value=0.0)

total_gastos = (
    alimentacion
    + transporte
    + educacion
    + ocio
    + otros
)

st.write(f"💸 Total gastos: ${total_gastos:,.0f}")

st.subheader("🏦 Ahorro")

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
        "Cantidad de ahorro",
        min_value=0.0,
        value=0.0
    )

if st.button("📊 Calcular"):

    if ahorro > ingresos:
        st.error("⚠️ El ahorro no puede ser mayor que los ingresos.")

    else:
        balance = ingresos - total_gastos - ahorro

        st.subheader("📈 Resultados")

        st.write(f"💵 Ingresos: ${ingresos:,.0f}")
        st.write(f"💸 Gastos: ${total_gastos:,.0f}")
        st.write(f"🏦 Ahorro: ${ahorro:,.0f}")
        st.write(f"📊 Balance final: ${balance:,.0f}")

        st.subheader("🚦 Diagnóstico financiero")

        porcentaje_restante = (
            balance / ingresos * 100
            if ingresos > 0
            else 0
        )

        if porcentaje_restante >= 30:
            st.success("🟢 Excelente manejo financiero.")
        elif porcentaje_restante >= 10:
            st.warning("🟡 Buen manejo financiero, pero puedes ahorrar más.")
        else:
            st.error("🔴 Debes mejorar el control de tus gastos.")
