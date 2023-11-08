import streamlit as st
import pandas as pd
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")
st.title("Demo Streamlit App (10 lines)")
uploaded_file = st.file_uploader("Upload csv file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    selected_cols = st.multiselect('Select columns', options=df.columns, default=list(df.columns))
    values = st.slider('Select number of display rows', min_value=1, max_value=10, value=5, step=1)
    st.dataframe(df[selected_cols].head(values))