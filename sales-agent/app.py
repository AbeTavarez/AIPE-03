from langchain_tavily import TavilySearch
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-20b")
search_tool = TavilySearch(topic="general", max_results=2)

user_question = "whats the current weather in NYC"
results = search_tool.invoke({"query": user_question})
print("Result: ", results)

messages = [
    SystemMessage(f"You're a helpful assistant. answer the user question using the provided content: {results}"),
    HumanMessage(user_question)
]

model_response = llm.invoke(messages)
print("\n Model Response: ", model_response.content)
