import streamlit as st

st.set_page_config(
    page_title="Weather Station"
)

st.markdown("<h1 style='text-align: center; color: raisin black;'>Weather Station</h1>", unsafe_allow_html=True)

conn = st.connection('esp_log', type='sql')
df = conn.query('SELECT Humidity, Temperature, LDR_Value  from log', ttl=600)

for row in df.itertuples():
    st.write(f"{Humidity}, {Temperature}, {row.pet}:")
