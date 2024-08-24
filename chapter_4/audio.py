import streamlit as st

sample_audio = open("./audio.wav", "rb")

audio_bytes = sample_audio.read()

st.audio(sample_audio, start_time=2)

sample_url = st.audio("https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3")
