import streamlit as st
import pandas as pd
import mysql.connector
from mysql.connector import Error

st.set_page_config(
    page_title="Weather Station"
)

st.markdown("<h1 style='text-align: center; color: raisin black;'>Weather Station</h1>", unsafe_allow_html=True)

try:
    # Establish connection to MySQL
    connection = mysql.connector.connect(
        host='192.168.144.41',  # Use the IP address directly
        user='root',
        password='',
        database='esp_log'
    )

    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM log")
        data = cursor.fetchall()

        # Convert data to a DataFrame
        df = pd.DataFrame(data, columns=[i[0] for i in cursor.description])

        # Display the data in Streamlit
        st.title('Streamlit MySQL Connection')
        st.dataframe(df)

except Error as e:
    st.error(f"Error while connecting to MySQL: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        st.write("MySQL connection is closed")
