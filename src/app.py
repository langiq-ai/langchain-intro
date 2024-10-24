from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM

import streamlit as st
import os
from dotenv import load_dotenv
from openai import models

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a language model assistant helping a user with a question."),
        ("user", "Question {question}"),
    ]
)

# streamlit framework
st.title("Langchain Ollama Chat")
input_text = st.text_input("Enter your question here:")

model = OllamaLLM(model="llama3.2")

if input_text:
    formatted_prompt = prompt.format(question=input_text)
    response = model.invoke(formatted_prompt)
    st.write(response)