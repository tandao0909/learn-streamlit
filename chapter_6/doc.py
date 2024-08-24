import streamlit as st
import docx2txt
import inspect

st.title("DOC and Text documents")

text_file = st.file_uploader("Upload Document", type=["docx", "txt"])

details = st.button("Check details")

if details:
    if text_file is not None:
        doc_details = {
            "file_name": text_file.name,
            "file_type": text_file.type,
            "file_size": text_file.size
        }
        st.write(doc_details)
        if text_file.type == "text/plain":
            raw_text = str(text_file.read(), "utf-8")
            st.write(raw_text)
        else:
            docx_text = docx2txt.process(text_file)
            st.write(docx_text)