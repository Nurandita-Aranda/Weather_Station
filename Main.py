import streamlit as st
import mysql.connector

st.set_page_config(
    page_title="Weather Station"
)

st.markdown("<h1 style='text-align: center; color: raisin black;'>Weather Station</h1>", unsafe_allow_html=True)

def connection(name, type):
    if type == 'sql' and name == 'esp_log':
        db_config = {
            'user': 'root',
            'password': '',
            'host': 'localhost',
            'database': 'esp_log'
        }

st.connection = connection
conn = st.connection('esp_log', type='sql')
df = connection.query('SELECT Humidity, Temperature, LDR_Value  from log', ttl=600)

for row in df.itertuples():
    st.write(f"{Humidity}, {Temperature}, {row.pet}:")
