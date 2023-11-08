import pandas as pd
import streamlit as st
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")

df = pd.read_csv("./data/housing.csv", sep=",")

st.title("Metric")
st.metric(label="Temperature", value="60 C", delta="3 C")

st.title("Dataframe")
st.dataframe(df)

st.title("Data eitor")
st.data_editor(df)

st.title("Bar Chart")
st.bar_chart(df, x="housing_median_age", y="median_house_value")
st.line_chart(df, x="housing_median_age", y="population")
st.scatter_chart(df, x="housing_median_age", y="median_house_value")
# st.pyplot
# st.altair_chart
# st.vega_lite_chart
# st.plotly_chart
# st.bokeh_chart
# st.pydeck_chart
# st.graphviz_chart
st.map(df, latitude="latitude", longitude="longitude", color=None, size=None)
st.table(df)