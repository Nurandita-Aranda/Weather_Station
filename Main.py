import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(
    page_title="Weather Station"
)

st.markdown("<h1 style='text-align: center; color: raisin black;'>Weather Station</h1>", unsafe_allow_html=True)

connection = mysql.connector.connect(
    host = "192.168.144.41"
    port = 3306
    database = "esp_log"
    username = "root"
    password = ""
)

st.write('connected')
cursor = connection.cursor()
cursor.execute('select * from log')
st.write(cursor.fetchall())
