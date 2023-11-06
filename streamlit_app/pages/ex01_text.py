import streamlit as st
conn = st.connection("sqlite", type="sql", autocommit=True)
conn.driver
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