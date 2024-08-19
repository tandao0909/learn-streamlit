import streamlit as st
import base64

SCORE = 0
NORMAL = 0
ANGRY = -1
HAPPY = 1

def add_local_backgound_image_(image):
    with open(image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Calling Image in function
add_local_backgound_image_('./maydie.jpg')

st.title("Web để dỗ Kiều")
st.write("website này được Đào Xuân Tân viết ra để giúp Kiều nói lên tâm tư của mình.")

mood_list = ["Bình thường", "Vui lắm anh :smile:", "Đập bỏ m* mày giờ :angry:"]
mood = st.radio("Bạn Kiều hôm nay có một ngày như thế nào", 
                mood_list
         )

if mood == mood_list[0]:
    SCORE += NORMAL
if mood == mood_list[1]:
    SCORE += HAPPY
if mood == mood_list[2]:
    SCORE += ANGRY

reject_list = [0, 1, 2, 3]
reject = st.radio("Hôm nay bạn Kiều bị Tân \"say no\" mấy lần?", reject_list)

SCORE += reject * ANGRY

energy_list = ["Mệt mỏi:cry:", "Bình thường", "Đầy Năng Lượng:rocket:"]
energy = st.radio("Còn mức năng lượng của em iu thì sao?", energy_list)

if energy == energy_list[0]:
    SCORE += ANGRY
if energy == energy_list[1]:
    SCORE += NORMAL
if energy == energy_list[2]:
    SCORE += HAPPY

if SCORE > 0:
    st.write("Có vẻ Kiều khá vui :smiley:, có thể liên hệ anh qua mess để kể anh nghe ngày hôm nay của em được chứ?")
if SCORE < 0:
    st.write("Anh xin lỗi Kiều :cry:, sao em không vui vậy, nói anh nghe nha")
