import streamlit as st
import json
st.title("json extractor")
  
filename = '/workspace/pdf-parser/data.txt'
  

dict1 = {}

with open(filename) as fh:
  
    for line in fh:
  
        # reads each line and trims of extra the spaces 
        # and gives only the valid words
        command, description = line.strip().split(None, 1)
  
        dict1[command] = description.strip()
  
# creating json file
# the JSON file is named as test1
out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()

st.json("/workspace/pdf-parser/my_app/test1.json")