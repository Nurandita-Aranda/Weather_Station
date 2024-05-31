import streamlit as st
import mysql.connector

st.set_page_config(
    page_title="Weather Station"
)

st.markdown("<h1 style='text-align: center; color: raisin black;'>Weather Station</h1>", unsafe_allow_html=True)


db_config = {
    'user': 'root',
    'password': '',
    'host': '192.168.144.41',
    'database': 'esp_log'
}

# Establishing a connection
try:
    conn = mysql.connector.connect(**db_config)
    st.success('Connected to the database successfully!')
except mysql.connector.Error as err:
    st.error(f"Error: {err}")
conn = st.connection('esp_log', type='sql')
df = conn.query('SELECT Humidity, Temperature, LDR_Value  from log', ttl=600)

for row in df.itertuples():
    st.write(f"{Humidity}, {Temperature}, {row.pet}:")
