import streamlit as st
import requests
import json
import subprocess

st.title("Turing Solution.pvt.ltd",)

DB_schema = st.text_input("Enter Database Schema")
addition_promt = '''consider and understand this schema, its structure and answer accordingly and reject any out of context questions.
Important Note: Never answer out of the context and not beyond sql query. Note : If any query refers to any attribute which is not in given schema then reject that question.'''


Quary = st.text_input("Enter Your Queation")

Final_prompt = DB_schema + addition_promt + Quary

url = 'http://localhost:11434/api/generate'

# Define the header and body of your POST request
headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive', 'User-Agent' : 'PostmanRuntime/7.37.3'}
data = {"model": "gemma:7b", "prompt": Final_prompt}

# Send the POST request
response = requests.post(url, headers=headers, json=data)

json_objects = response.text.split('\n')

# Parse each JSON object individually
ans = ''
for json_str in json_objects:
    if json_str:  # Check if the string is not empty
        json_obj = json.loads(json_str)
        ans += json_obj['response']

if DB_schema != '' and Quary != '':
    st.write(ans)
