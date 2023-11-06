import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
from pygwalker.api.streamlit import init_streamlit_comm, get_streamlit_html

st.set_page_config(
    page_title="My App",
    layout="wide"
)
init_streamlit_comm()

@st.cache_resource
def get_pyg_html(df: pd.DataFrame) -> str:
    html = get_streamlit_html(df, spec="./gw0.json", use_kernel_calc=True, debug=False)
    return html

@st.cache_data
def get_df() -> pd.DataFrame:
    # https://raw.githubusercontent.com/justmarkham/DAT8/master/data/bikeshare.csv
    return pd.read_csv("https://raw.githubusercontent.com/sonarsushant/California-House-Price-Prediction/master/housing.csv")


df = get_df()
components.html(get_pyg_html(df), height=2000, scrolling=True) # width=1300, height=1000
st.write(st.get_container_width)