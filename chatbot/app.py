from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.outputs import StrOutputParser
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os
import streamlit as st

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")


#Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user's query."),
        ("human", "{input}"),
    ]
)

# streamlit framework
st.title("LangChain OpenAI Chatbot")
input_text = st.text_input("Search the topic u want to know about:")

# llm model
llm = Ollama(model='llama3')

output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))