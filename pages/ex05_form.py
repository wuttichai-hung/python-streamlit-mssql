import streamlit as st
from sqlalchemy.sql import text
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")

with st.form("my_form"):
    st.write("abd")
    submitted = st.form_submit_button('Submit')
    if submitted:
        st.success("Submit Done!")