import streamlit as st
import docx2txt
import pdfplumber
import os 
import json

st.title("FIR")

docx_file = st.file_uploader("Choose a file")

if docx_file is not None:
    file_details = {"filename":docx_file.name, "filetype":docx_file.type,
                    "filesize":docx_file.size}
    with st.sidebar.expander("File Info"):
        st.json(file_details)

    if docx_file.type == "text/plain":
        # Read as string (decode bytes to string)
        raw_text = str(docx_file.read(),"utf-8")
        st.text_area("Extracted Text", raw_text)

    elif docx_file.type == "application/pdf":

        try:
            with pdfplumber.open(docx_file) as pdf:
                pages = pdf.pages[0]
                extract = pages.extract_text()
                st.text_area("Extracted Text", extract)
                summarizer(extract)

        except:
            st.write("None")

    else:   
        raw_text = docx2txt.process(docx_file)
        st.text_area("Extracted Text", raw_text)