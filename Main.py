import streamlit as st

st.set_page_config(
    page_title="Weather Station"
)

st.markdown("<h1 style='text-align: center; color: raisin black;'>Weather Station</h1>", unsafe_allow_html=True)

conn = st.connection('my sql', type='sql')
df = conn.query('SELECT * from mytable', ttl=600)

for row in df.itertuples():
    st.write(f"
