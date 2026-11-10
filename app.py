import streamlit as st

st.title("💰 Simulador de Finanzas Personales")

st.write("Ingresa tus datos para conocer tu balance financiero.")

ingresos = st.number_input("Ingresos", min_value=0.0)

gastos = st.number_input("Gastos totales", min_value=0.0)

ahorro_porcentaje = st.slider(
    "Porcentaje de ahorro (%)",
    min_value=0,
    max_value=100,
    value=10
)

if st.button("Calcular"):
    ahorro = ingresos * (ahorro_porcentaje / 100)
    balance = ingresos - gastos - ahorro

    st.subheader("Resultados")

    st.write(f"💵 Ingresos: ${ingresos:,.0f}")
    st.write(f"💸 Gastos: ${gastos:,.0f}")
    st.write(f"🏦 Ahorro: ${ahorro:,.0f}")
    st.write(f"📊 Balance final: ${balance:,.0f}")

    if balance > 0:
        st.success("✅ Balance positivo")
    elif balance < 0:
        st.error("⚠️ Balance negativo")
    else:
        st.warning("➖ Balance neutro")
