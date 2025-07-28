import requests
import streamlit as st

def get_essay(input_text):
    url = "http://localhost:8000/essay/invoke"
    payload = {"input":{"topic": input_text}}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    print(response)
    if response.status_code == 200:
        return response.json()['output']
    else:
        return f"Error: {response.status_code} - {response.text}"
    
st.title("LangChain Ollama Essay Generator")
input_text = st.text_input("Enter a topic for your essay:")

if input_text:
    st.write(get_essay(input_text))