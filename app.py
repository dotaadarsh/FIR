import streamlit as st 

st.title("FIR")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.info("File uploaded sucessfully")
    