import streamlit as st
# hint: create table -> add input widget -> connect db
with st.form("my_form"):
    uid = st.number_input("Employee ID", min_value=0, 
                          max_value=99999, value=30, step=1)
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    age = st.slider('Age', 0, 120, 30, step=1)
    gender = st.selectbox("Gender", ["M", "F", "Other"])
    ##### Select, Insert
    # emp_id
    # first_name
    # last_name
    # address
    # gender: male / female
    # age
    ####
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success("Submit Done!!")
        # insert to db