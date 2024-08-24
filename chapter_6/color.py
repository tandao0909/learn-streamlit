import streamlit as st

st.title("Select color")

color_code = st.color_picker("Select your color")

st.header(color_code)
