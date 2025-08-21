import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b")
parser = StrOutputParser()
chain = model | parser


st.title("AI Chat App")

# Application state that will be available after the app refresh
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Iterate over the chat history and show each message
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])


user_msg = st.chat_input("type here...")

if user_msg:
    # add the user message to the chat history list
    st.session_state.chat_history.append({"role": "user", "content": user_msg})
    
    with st.chat_message("user"):
        st.write(user_msg)
    
    
    # Invoke Model
    result = chain.invoke(st.session_state.chat_history)

    # add the AI message to the chat history list
    st.session_state.chat_history.append({"role": "ai", "content": result})
    
    with st.chat_message("ai"):
        st.write(result)
    print(st.session_state.chat_history)
    