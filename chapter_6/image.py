import io

import streamlit as st
from PIL import Image

st.title("Upload Image")
image_file = st.file_uploader("Upload images", type=["png", "jpg", "jpeg"])

check_details = st.button("View details")

if check_details:
    if image_file is not None:
        image_details = {
            "filename": image_file.name,
            "filetype": image_file.type,
            "filesize": image_file.size
        }
        st.write(image_details)

        image_data = image_file.read()
        image = Image.open(io.BytesIO(image_data))
        st.image(image)
    else:
        st.write("No image uploaded")
