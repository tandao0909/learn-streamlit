import streamlit as st
import pdfplumber

st.title("PDF file")
pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

details = st.button("View details")

if details:
    if pdf_file is not None:
        pdf_details = {
            "filename": pdf_file.name,
            "filetype": pdf_file.type,
            "filesize": pdf_file.size
        }
        st.write(pdf_details)
        pdf = pdfplumber.open(pdf_file)
        page = pdf.pages[0]
        st.write(page.extract_text())
    else:
        st.write("No PDF file is uploaded")
