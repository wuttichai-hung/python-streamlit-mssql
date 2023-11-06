import streamlit as st

cols = st.columns(3)
with cols[0]:
    pass
with cols[1]:
    pass
with cols[2]:
    pass

with st.expander("Read more"):
    st.write("BBB")