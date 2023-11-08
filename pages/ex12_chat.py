import streamlit as st
import numpy as np
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")

with st.chat_message("A"):
    st.write("Hello")
prompt = st.chat_input("Say something")
if prompt:
    # st.write(f"User has sent the following prompt: {prompt}")
    with st.chat_message("B"):
        st.write(prompt)