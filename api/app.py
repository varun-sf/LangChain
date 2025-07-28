from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="LangChain Ollama Chatbot API",
              version="1.0.0",
              description="A simple API for a LangChain chatbot using Ollama.")

# add_routes(app, ChatOpenAI(), path="/chat")

model = OllamaLLM(model="llama3.2:1b")
prompt = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")
add_routes(app, prompt|model, path="/essay")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)