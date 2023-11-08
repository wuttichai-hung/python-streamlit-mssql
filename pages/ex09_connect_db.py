import streamlit as st
from sqlalchemy.sql import text
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")

TABLE_NAME = "mytable"

conn = st.connection("sqlite", type="sql", autocommit=True)
click_create = st.button("Create table")
if click_create:
    with conn.session as s:
        sql = f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id int, 
            fname text
            )
        """
        s.execute(text(sql))
    st.success("Create table  successfully!")

click_insert = st.button("Insert value")
if click_insert:
    with conn.session as s:
        sql = f"""
        INSERT INTO {TABLE_NAME} (id, fname)
        VALUES (1, 'A')
        """
        s.execute(text(sql))
    st.success("INSERT successfully!")

click_read = st.button("Read data")
if click_read:
    st.cache_data.clear()
    df = conn.query(f'SELECT * from {TABLE_NAME}')
    print(len(df))
    st.dataframe(df)
