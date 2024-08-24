import time
import streamlit as st

st.title("Creating a button")

button = st.button("Click here")

if button:
    st.write("You have clicked the button")
else:
    st.write("You haven't clicked the button yet")

st.title("Creating Radio buttons")

number = st.radio("select the number", [1, 2, 3], key=1)

number2 = st.radio("select the number", [1, 2, 3], key=2)

st.write("The sum of two number is", number+number2)

st.title("Creating checkboxes")

st.write("What are your hobbies?")

check_1 = st.checkbox("Books")
check_2 = st.checkbox("Movies")
check_3 = st.checkbox("Sports")

st.title("Drop downs")

hobby = st.selectbox("Choose your hobby", 
                     ["Books", "Movies", "Sports"])

st.title("Multiselect")

hobbies = st.multiselect(
    "What are your hobbies?",
    ["Reading", "Cooking", "Coding"]
)

st.title("Download Button")

st.download_button(
    label="Download Image",
    data=open("fam.jpg", "rb"),
    file_name="lion.jpg",
    mime="image/jpg"
)

st.title("Download csv file")

st.download_button(
    label="Downland csv",
    data=open("avocado.csv", "rb"),
    file_name="data.csv",
    mime="csv"
)

st.title("Progress Bar")

download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage+1)

st.write("Download complete")

st.title("Spinner")

with st.spinner("Loading..."):
    time.sleep(3)
st.write("Done Spinner")