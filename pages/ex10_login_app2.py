import streamlit as st

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

def login(username, password):
    if username == "u" and password == "p":
        return True
    else:
        return False
    
def logout():
    st.session_state["logged_in"] = False
    st.rerun()


st.title("App: Login")
if not st.session_state["logged_in"]:
    st.write("Please log in to access the app.")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    click_login = st.button("Login")
    if click_login:
        if login(username, password):
            st.session_state["logged_in"] = True
            st.rerun()
            st.write("Logged in successfully.")
        else:
            st.write("Incorrect username or password. Please try again.")
else:
    click_logout = st.button("Logout")
    if click_logout:
        logout()
    st.write("Welcome to the main app!")