# 🚀 QUANTUM Dashboard Setup v1.0 🚀

import streamlit as st
import pandas as pd

# 1. Forecast Ergebnisse laden
forecast_df = pd.read_csv('outputs/forecasts/forecast_results.csv')

# 2. Dashboard Layout
st.set_page_config(page_title="QUANTUM Forecast Dashboard", layout="wide")

st.title("🚀 QUANTUM Stock Forecast Dashboard")

# 3. Übersicht: Aktuelle Analyse-Ergebnisse
st.subheader("🔍 Asset Forecast Übersicht")

# 4. Dynamische Anzeige für jedes Asset
for index, row in forecast_df.iterrows():
    with st.container():
        cols = st.columns(5)
        
        # Asset Name
        cols[0].markdown(f"**Asset:** {row['Asset']}")
        
        # Trend
        trend_icon = "📈" if row['Trend'] == "Steigt" else "📉"
        cols[1].markdown(f"**Trend:** {trend_icon} {row['Trend']}")
        
        # Confidence
        confidence_percent = round(row['Confidence'] * 100, 2)
        cols[2].markdown(f"**Confidence:** {confidence_percent}%")
        
        # Platzhalter für Hoch/Tief Zeiten (fügen wir später dynamisch hinzu)
        cols[3].markdown("**Hochzeit:** 🕐  --:--")
        cols[4].markdown("**Tiefzeit:** 🕐  --:--")

st.success("✅ QUANTUM Dashboard v1.0 erfolgreich gestartet!")
