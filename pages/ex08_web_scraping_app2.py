import streamlit as st
import pandas as pd
import numpy as np
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")

# url = "https://www.goldtraders.or.th/"
st.title("App: Table Scraping")
st.text("Sample url: https://www.goldtraders.or.th/")
url = st.text_input("URL")
click_scrape = st.button("Scrape it!!")
if click_scrape:
    df_list = pd.read_html(url)
    tab_names = [f"tbl{i}" for i in range(len(df_list))]
    tabs = st.tabs(tab_names)
    for i, tab in enumerate(tabs):
        with tabs[i]:
            st.dataframe(df_list[i])


