import xlrd
import xlwt
from pandas import read_excel
import streamlit as st
import docx2txt
import pdfplumber 
import json
import xlsxwriter
import pandas as pd
from openpyxl import load_workbook, Workbook
from googletrans import Translator
translator = Translator()

st.title('Transliteration_round-1')

workbook = xlsxwriter.Workbook('/workspace/FIR/round1/t.xlsx')
worksheet = workbook.add_worksheet()

my_sheet = 'Sheet1'
file_name = '/workspace/FIR/round1/t.xlsx'
df = read_excel(file_name, sheet_name = my_sheet)
st.dataframe(df)

my_list = []
my_val = []


df = pd.read_excel('/workspace/FIR/round1/t.xlsx')
my_list = df['word'].tolist()
my_val = df['transliterated'].tolist()

index = 0
for column in df[['word']]:
    columnSeriesObj = df[column]
    st.write(columnSeriesObj.values)

    for values in columnSeriesObj.values:
        translated_text = translator.translate(values)
        my_val[index] = translated_text.text
        index += 1


st.write(my_list)
st.write(my_val)

columns=['word', 'transliterated']

df = pd.DataFrame(list(zip(my_list, my_val)), columns=columns )
st.dataframe(df)
df.to_excel('output.xlsx', columns=['word', 'transliterated'], index = False)

st.download_button('Output', data='/workspace/FIR/output.xlsx',file_name='Output')