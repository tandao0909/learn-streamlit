import streamlit as st

sample_video = open("./video.mp4", "rb")

st.video(sample_video, start_time=10)

st.video("https://www.youtube.com/watch?v=OMkEVX23BdM")
