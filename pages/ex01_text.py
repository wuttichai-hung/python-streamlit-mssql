import streamlit as st
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")

a = 5
a

b = a + 5
b

c = {"a": a, "b": b}
c
st.json(c)


st.title("My Title")
st.header("My Header")
st.subheader("My Subheader")
st.caption("My Caption")
st.code("""
import streamlit as st
""")
st.text("My Text")
st.latex("E = mc^2") # https://katex.org/docs/supported.html
st.divider()

st.markdown("# My Title with Markdown")
st.markdown("## My Header")
st.markdown("### My Subheader")
st.markdown("*My Caption*")
st.markdown("""
```python
import streamlit as st
```
""")
st.markdown("My Text")
st.markdown("$$ E = mc^2 $$")
st.markdown("---")

# CSS Zone
st.write("This is :blue[test]")

st.markdown(":blue[$$ E = mc^2 $$]")

new_title = '<p style="font-family:sans-serif; color:blue; font-size: 42px;">Text Colors</p>'
st.markdown(new_title, unsafe_allow_html=True)

title_alignment="""
<style>
#my-title-with-markdown {
  text-align: center
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

st.write("### My Subheader")
st.markdown("### My Subheader")