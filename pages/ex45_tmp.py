import streamlit as st
import time
# Set the app width to be wider for better responsiveness
st.set_page_config(layout="wide")

with st.status('Authenticating...') as s:
  time.sleep(2)
  st.write('Some long response.')
  s.update(label='Response')