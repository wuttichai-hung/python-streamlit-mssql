import streamlit as st
import numpy as np
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")

# st.title("chat_message")
# with st.chat_message("user"):
#    st.write("Hello 👋")
#    st.line_chart(np.random.randn(30, 3))
answer = "BBB"
def get_answer():
    answer = "AAA"
with st.chat_message("user"):
    st.write("Hello")
prompt = st.chat_input("Say something", on_submit=get_answer())
if prompt:
    # st.write(f"User has sent the following prompt: {prompt}")
    with st.chat_message("Me"):
        st.write(prompt)
    with st.chat_message("user"):
        st.write(answer)