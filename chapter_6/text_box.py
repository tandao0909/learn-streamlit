import streamlit as st

st.title("Text Box")

name = st.text_input("Enter Your Name")

st.write("Your name is ", name)

st.title("Text box as password")

password = st.text_input("Enter your password", type="password")

st.write("Your password is ", password)

st.title("Text Area")

input_text = st.text_area("Enter your Review")

st.write("""You entered: \n""", input_text)