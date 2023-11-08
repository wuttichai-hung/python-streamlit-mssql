import streamlit as st
from PIL import Image
st.set_page_config(page_title="Demo Streamlit App", page_icon="🧊", layout="wide", initial_sidebar_state="collapsed")
# https://docs.streamlit.io/library/api-reference/media/st.image
st.title("Image")
image = Image.open('./data/ex_image.png')
st.image(image, caption='My Caption')
st.divider()

st.title("Audio")
audio_file = open('./data/ex_audio.ogg', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')
st.divider()

st.title("Video")
video_file = open('./data/ex_video.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)