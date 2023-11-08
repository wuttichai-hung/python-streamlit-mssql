import streamlit as st
import numpy as np
import pandas as pd
import time
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")


@st.cache_data
def get_data():
    df = pd.read_csv("https://raw.githubusercontent.com/ywchiu/riii/master/data/house-prices.csv", sep=",")


click_load_data = st.button("Load data")
if click_load_data:
    s = time.time()
    df = get_data()
    e = time.time()
    st.dataframe(df)
    st.write(f"Load duration: {e-s} sec.")

click_clear_cache = st.button("Clear cache data")
if click_clear_cache:
    get_data.clear()