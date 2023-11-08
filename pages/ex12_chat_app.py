import streamlit as st
from datetime import datetime
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="auto")

with st.sidebar:
    clear_session_click = st.button("Clear session")
    if clear_session_click:
        st.session_state["messages"] = []
if "messages" not in st.session_state:
    st.session_state["messages"] = []

def chat_bot_response(question):
    answer = str(datetime.now()) + "  " + question
    return answer

question = st.chat_input("Say something")
if question:
    answer = chat_bot_response(question)
    st.session_state["messages"].append({"q": question, "a": answer})
# st.session_state["messages"]

if "messages" in st.session_state:
    for msg in st.session_state["messages"]:
        with st.chat_message("human"):
            st.write(msg['q'])
        with st.chat_message("ai"):
            st.write(msg['a'])
