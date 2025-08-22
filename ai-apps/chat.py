import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Prompt Template
prompt_template = PromptTemplate.from_template("""
You're a helpful assistant at AI Products Inc. Your task is to respond to customers' inquiries about our products. 
Use a friendly and polite tone. Ask the customer for any clarification or more information before answering the customer's request.

Examples:
---
user: where is my product?
assistant: Hello, how are you today? I can help you track your product, can you please provide your order number?
user: P1234
assistant: Great, thank you! Let me check the status of your order.
---

USER QUESTION: {question}
You can only answer questions about the following inquiries: tracking, availability, shipping, return policy.
If you're not about to help the customer, provide the following customer service number: 123-345-7890 
""")



model = ChatGroq(model="openai/gpt-oss-20b")
parser = StrOutputParser()
chain = prompt_template | model | parser


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
    
    
    # Create the prompt
    # prompt = prompt_template.invoke({"question": user_msg})
    # print(prompt)
    
    # Invoke Model
    result = chain.invoke({"question": st.session_state.chat_history})

    # add the AI message to the chat history list
    st.session_state.chat_history.append({"role": "ai", "content": result})
    
    with st.chat_message("ai"):
        st.write(result)
    print(st.session_state.chat_history)
    