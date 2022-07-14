import streamlit as st
import docx2txt
import pdfplumber 
import json
import pandas as pd
from googletrans import Translator
translator = Translator()

st.title('Transliteration')

with st.sidebar:
    st.info("Upload the file for which you want to translate - use the sample files 👉")

docx_file = st.file_uploader("Choose a file") 

if docx_file is not None:
    
    file_details = {"filename":docx_file.name, "filetype":docx_file.type, "filesize":docx_file.size}
    with st.sidebar.expander("File Info"):
        st.json(file_details)

    if docx_file.type == "text/plain":
        
        raw_text = str(docx_file.read(),"utf-8")
        st.text_area("Extracted Text", raw_text)
        translated_text = translator.translate(raw_text)
        st.write(translated_text.text)

    elif docx_file.type == "application/pdf":

            try:
                with pdfplumber.open(docx_file) as pdf:
                    pages = pdf.pages[0]
                    extract = pages.extract_text()
                    with st.expander("Extracted Text [Click to expand]", expanded=False):
                        st.write(extract)
                    translated_text = translator.translate(extract)
                    with st.expander("Translated text [Click to expand]"):
                        st.write(translated_text.text)

            except:
                st.write("None")

    else:

        raw_text = docx2txt.process(docx_file)
        
        with st.expander("Extracted Text [Click to expand]", expanded=False):
            st.text_area(raw_text)
            translated_text = translator.translate(raw_text)
            st.write(translated_text.text)
        
with st.expander("Sample files"):
    file_url = "https://raw.githubusercontent.com/dotaadarsh/FIR/main/Sample-FIR.csv"
    data = pd.read_csv(file_url)
    st.dataframe(data)
