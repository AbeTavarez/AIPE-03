import streamlit as st


st.title("AI Chat App")

chat_history = []

user_msg = st.chat_input("type here...")

if user_msg:
    message = st.chat_message("user")
    message.write(user_msg)
    chat_history.append({"role": "user", "content": user_msg})
    
    ai_message = st.chat_message("ai")
    ai_message.write("how may i help you?")
    chat_history.append({"role": "ai", "content": "how may i help you?"})
    print(chat_history)
    
# container = st.container(border=True, height=500)