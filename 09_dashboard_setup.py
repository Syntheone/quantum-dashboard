import streamlit as st
import pandas as pd

# Lade Forecast Daten
st.set_page_config(page_title="QUANTUM Forecast Dashboard", layout="wide")

st.title("🚀 QUANTUM Stock Forecast Dashboard")

forecast_df = pd.read_csv('outputs/forecasts/forecast_results.csv')

st.subheader("🔍 Asset Forecast Übersicht")

for index, row in forecast_df.iterrows():
    with st.container():
        cols = st.columns(5)
        cols[0].markdown(f"**Asset:** {row['Asset']}")
        trend_icon = "📈" if row['Trend'] == "Steigt" else "📉"
        cols[1].markdown(f"**Trend:** {trend_icon} {row['Trend']}")
        confidence_percent = round(row['Confidence'] * 100, 2)
        cols[2].markdown(f"**Confidence:** {confidence_percent}%")
        cols[3].markdown("**Hochzeit:** 🕐 --:--")
        cols[4].markdown("**Tiefzeit:** 🕐 --:--")

st.success("✅ QUANTUM Dashboard v1.0 erfolgreich gestartet!")