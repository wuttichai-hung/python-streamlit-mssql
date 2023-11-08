import streamlit as st


def login(username, password):
    if username == "u" and password == "p":
        return True
    else:
        return False


st.title("App: Login1")
st.write("Please log in to access the app.")
username = st.text_input("Username")
password = st.text_input("Password", type="password")

click_login = st.button("Login")
if click_login:
    if login(username, password):
        st.success("Logged in successfully.")
    else:
        st.error("Incorrect username or password. Please try again.")