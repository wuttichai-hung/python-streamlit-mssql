import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")

# url = "https://www.goldtraders.or.th/"
st.title("App: Table Scraping")
url = st.text_input("URL")
df_list = pd.read_html(url)

for i, df in enumerate(df_list):
    st.subtitle(f"Table{i}")
    st.dataframe(df)
    st.divider()


