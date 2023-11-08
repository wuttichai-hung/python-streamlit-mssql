import streamlit as st
from sqlalchemy.sql import text
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")

SCHEMA = "dbo"
TABLE_NAME = "mytable"

conn = st.connection("sqlite", type="sql", autocommit=True)
click_create = st.button("Create table")
if click_create:
    with conn.session as s:
        # IF OBJECT_ID(N'{SCHEMA}.{TABLE_NAME}', N'U') IS NULL
        sql = f"""
        CREATE TABLE {TABLE_NAME} (
            id int, 
            fname text
            )
        """
        s.execute(text(sql))
        st.success("Create table  successfully!")

with st.form("my_form"):
    user_id = st.number_input("ID", step=1, min_value=0, max_value=999)
    username = st.text_input("Name")
    submitted = st.form_submit_button("Submit")
    if submitted:
        with conn.session as s:
            sql = f"""
            INSERT INTO {TABLE_NAME} (id, fname)
            VALUES ({user_id}, '{username}')
            """
            s.execute(text(sql))
        st.success("Submit successfully!")

click_show = st.button("Show value")
if click_show:
    st.cache_data.clear()
    df = conn.query(f'SELECT * from {TABLE_NAME}', ttl=600)
    print(len(df))
    st.dataframe(df)
