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

    with st.expander("Show table data"):
        cols = st.columns(3)
        for i, df in enumerate(df_list):
            with cols[i % 3]:
                st.title(f"Table {i}")
                st.dataframe(df_list[i], height=200, hide_index=True)


