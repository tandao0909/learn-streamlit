import streamlit as st
import pandas as pd

st.title("CSV data")
data_file = st.file_uploader("Upload your CSV file", type=["csv"])

details = st.button("View details")

if details:
    if data_file is not None:
        file_details = {
            "filename": data_file.name,
            "filetype": data_file.type,
            "filesize": data_file.size
        }
        st.write(file_details)
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No csv is uploaded")