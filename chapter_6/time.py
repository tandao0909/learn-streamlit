import datetime
import streamlit as st

st.title("Time")

st.time_input("Select Your Time")

st.title("Date")

st.date_input("Select Date")

st.title("Date with limit")

st.date_input("Select Date",
              value=datetime.date(1989, 12, 25),
              min_value=datetime.date(1987, 1, 1),
              max_value=datetime.date(2005, 12, 31))
