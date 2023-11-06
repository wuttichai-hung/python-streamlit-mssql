import streamlit as st

# button
clicked = st.button("Click me")
if clicked:
    st.success("Clicked")
st.divider()

# link_button
st.link_button("Go to Google", "https:/google.com")
st.divider()

# checkbox
agree = st.checkbox('I agree')
if agree:
    st.success('checkbox!')
st.divider()

# toggle
toggle_on = st.toggle('Activate feature')
if toggle_on:
    st.success('Feature activated!')
st.divider()

# radio
select_radio = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"],
    index=None,
)
if select_radio:
    st.success(select_radio)
st.divider()

# selectbox
option = st.selectbox(
   "How would you like to be contacted?",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select contact method...",
)
if option:
    st.success(option)
st.divider()

# file uploader
uploaded = st.file_uploader("Upload")
if uploaded:
    st.write("uploaded")

# Take a photo
# t = st.camera_input("Take a photo")