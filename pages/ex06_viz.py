import pandas as pd
import streamlit as st
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")

load_df = pd.read_csv("./data/housing.csv", sep=",")
value = st.slider('Select a range of values', 0, 50, step=1)
st.write('Values:', value)
df = load_df.head(value)

st.title("Map")
st.map(df, latitude="latitude", longitude="longitude", color=None, size=None)

st.title("Metric")
st.metric(label="Temperature", value="60", delta="3 C")

st.title("Table")
st.table(df)

st.title("Dataframe")
st.dataframe(df)

st.title("Data eitor")
st.data_editor(df)

st.title("Chart")
st.bar_chart(df, x="housing_median_age", y="median_house_value")
st.line_chart(df, x="housing_median_age", y="population")
st.scatter_chart(df, x="housing_median_age", y="median_house_value")
# st.pyplot
# st.altair_chart
# st.vega_lite_chart
# st.plotly_chart
# st.bokeh_chart
# st.pydeck_chart
st.title("Plotly")
import plotly.express as px
df = px.data.iris()
fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="sepal_length",
    color_continuous_scale="reds",
)
st.plotly_chart(fig, use_container_width=True)

st.title("Graphviz")
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
    }
''')
