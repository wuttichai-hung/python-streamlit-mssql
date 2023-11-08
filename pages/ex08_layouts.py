import streamlit as st
import time
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")
with st.sidebar:
    st.title("Sidebar")
    value = st.slider("Value", value=5, min_value=1, max_value=10, step=1)
    st.write(value)

# Columns
st.title("Columns")
with st.expander("More"):
   col1, col2, col3 = st.columns((1, 2, 1))

   # Column 1: Left Sidebar
   with st.echo():
      with col1:
         st.write("## Left Sidebar")
         st.image("https://via.placeholder.com/150")

      # Column 2: Main Content
      with col2:
         st.write("## Main Content")
         st.image("https://via.placeholder.com/350")

      # Column 3: Right Sidebar
      with col3:
         st.write("## Right Sidebar")
         st.image("https://via.placeholder.com/150")

   cols = st.columns(3)
   with cols[0]:
      st.header("A cat")
      st.image("https://static.streamlit.io/examples/cat.jpg")

   with cols[1]:
      st.header("A dog")
      st.image("https://static.streamlit.io/examples/dog.jpg")

   with cols[2]:
      st.header("An owl")
      st.image("https://static.streamlit.io/examples/owl.jpg")
   st.divider()

st.title("Container")
with st.container():
   import numpy as np
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))
st.write("This is outside the container")

st.title("Tab")
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

with st.expander("See more"):
    st.write("hidden information")

st.title("Empty")
with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 1 minute over!")
    time.sleep(3)
    st.success("Empty Done!!")


