import streamlit as st
import mysql.connector
import pandas as pd

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
        try:
            conn = mysql.connector.connect(**db_config)
            return conn
        except mysql.connector.Error as err:
            st.error(f"Error: {err}")
            return None
    else:
        st.error("Invalid connection type or name.")
        return None

st.connection = connection
conn = st.connection('esp_log', type='sql')

if conn:
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT Humidity, Temperature, LDR_Value FROM log')
        result = cursor.fetchall()

        # Convert the result to a pandas DataFrame
        df = pd.DataFrame(result)

        # Display the DataFrame in Streamlit
        st.dataframe(df)

        # Display individual rows
        for row in df.itertuples():
            st.write(f"Humidity: {row.Humidity}, Temperature: {row.Temperature}, LDR Value: {row.LDR_Value}")

    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()
else:
    st.error("Failed to connect to the database.")

