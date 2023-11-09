import streamlit as st
st.title("Title")
st.header("Header")
st.subheader("subheader")
st.text("text")

# st.markdown("<script><script>", unsafe_allow_html=True)
st.markdown("# Title")
style = """
<stlye>
#title {
  text-align: center
}
</stlye>
"""
st.markdown(style, unsafe_allow_html=True)