from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# displays some text in the app
st.title("AI App with Langchain")
st.divider()

# Sidebar
with st.sidebar:
    st.markdown("### Settings")
    
    temp = st.slider("Temperature", min_value=0.0, max_value=1.0)
    
    stream = st.toggle("Stream")

# displays a text input
user_prompt = st.text_input("Write your prompt...")

if user_prompt:
    # create the model
    model = ChatGroq(model="openai/gpt-oss-20b")

    # create parser
    parser = StrOutputParser()

    # create a chain
    chain = model | parser

    # invoke the chain with the user prompt
    completion = chain.invoke(user_prompt)

    print(completion)
    st.write(completion)