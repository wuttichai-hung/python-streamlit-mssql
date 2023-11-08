import streamlit as st
import datetime
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")


username = st.text_input("Username")
password = st.text_input("Password", type="password")


txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
    )
st.write(f'You wrote {len(txt)} characters.')

number = st.number_input('Insert a number')
st.write('The current number is ', number)


# button
clicked = st.button("Click me")
if clicked:
    st.success("Clicked")
    st.session_state.runpage = "main"
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


options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

# file uploader
uploaded = st.file_uploader("Upload")
if uploaded:
    st.write("uploaded")

# Take a photo
# t = st.camera_input("Take a photo")
values = st.slider('Select a range of values', 0, 100, step=1)
st.write('Values:', values)

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

# date
d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)

# time
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)

# color
color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)