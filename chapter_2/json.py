import streamlit as st

st.json(
    {
        "Books": [
            {
                "BookName": "Python Testing with Selenium",
                "BookID": "1",
                "Publisher": "Apress",
                "Year": "2021",
                "Edition": "First",
                "Language": "Python"
            },
            {
                "BookName": "Beginners Guide to Streamlit with Python",
                "BookID": "2",
                "Publisher": "Apress",
                "Year": "2022",
                "Edition": "First",
                "Language": "Python"
            }
        ]
    }
)