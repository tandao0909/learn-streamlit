import streamlit as st
from PIL import Image

st.write("Displaying an image")

st.image("./turtle.jpg")

st.image("https://tinyurl.com/322vu3ab")

original_image = Image.open("./turtle.jpg")
st.title("original image")
st.image(original_image)

resized_image = original_image.resize((400, 300))

st.title("resized image")
st.image(resized_image)
