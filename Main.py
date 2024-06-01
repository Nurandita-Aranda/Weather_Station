import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(
    page_title="Weather Station"
)

st.markdown("<h1 style='text-align: center; color: raisin black;'>Weather Station</h1>", unsafe_allow_html=True)




connection = mysql.connector.connect(
    host='http://192.168.144.41/',
    user='root',
    password='',
    database='esp_log'
)



cursor=connection.cursor()
cursor.execute("Select * from log")
data=cursor.fetchall()


st.title('Streamlit MySQL Connection')
