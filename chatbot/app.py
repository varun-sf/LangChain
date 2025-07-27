from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
 
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user's query."),
    ("human", "{input}"),
])

st.title("LangChain Ollama Chatbot")
input_text = st.text_input("Search the topic you want to know about:")

llm = OllamaLLM(model="llama3.2:1b")

# Output parser
output_parser = StrOutputParser()


chain = prompt | llm | output_parser

if input_text:
    result = chain.invoke({"input": input_text})  
    st.write(result)
