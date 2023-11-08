import streamlit as st
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")
st.title("State page2")
if 'key' not in st.session_state:
    st.session_state['key'] = 'value'
    st.write("Not in state")
else:
    st.write("In tate")