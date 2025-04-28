# 🚀 QUANTUM Dashboard Setup v1.1 - Live Auto-Loader

import pandas as pd
import streamlit as st

# 1. Titel & Design
st.set_page_config(page_title="QUANTUM Dashboard", layout="wide")
st.title("🚀 QUANTUM Stock Forecast Dashboard")

# 2. Daten automatisch laden (immer aktuelle Forecasts)
try:
    forecast_df = pd.read_csv('forecast_results.csv')
except FileNotFoundError:
    st.error("❌ Fehler: Forecast-Datei nicht gefunden!")
    st.stop()

# 3. Tabelle sortieren
forecast_df = forecast_df.sort_values(by='Confidence', ascending=False)

# 4. Übersicht anzeigen
st.subheader("🔍 Asset Forecast Übersicht")
for idx, row in forecast_df.iterrows():
    col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 2])
    
    with col1:
        st.markdown(f"**Asset:** {row['Asset']}")
    with col2:
        st.markdown(f"**Trend:** {'📈 Steigt' if row['Trend'] == 'Steigt' else '📉 Fällt'}")
    with col3:
        st.markdown(f"**Confidence:** {round(row['Confidence'] * 100, 1)}%")
    with col4:
        st.markdown(f"**Hochzeit:** 🕒 --:--")
    with col5:
        st.markdown(f"**Tiefzeit:** 🕒 --:--")

# 5. Erfolgreich-Info
st.success("✅ QUANTUM Dashboard v1.1 läuft mit Live-Daten!")
