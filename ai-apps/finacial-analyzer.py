from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders.csv_loader import CSVLoader
import streamlit as st

from dotenv import load_dotenv
load_dotenv()

# ======= UI with Streamlit =====================
# Displays some text in the app
st.title("AI Financial Analyzer")
st.subheader("Upload and analyze your financial data.")
st.divider()
st.markdown("##### Open the sidebar to upload CSV file.")


# Sidebar
csv_file = None
with st.sidebar:
    st.markdown("### Options:")
    csv_file_path = st.file_uploader("Upload a CSV file", type="csv")

    if csv_file_path is not None:
        # https://python.langchain.com/docs/how_to/document_loader_csv/
        
        csv_loader = CSVLoader(file_path=csv_file_path.name)
        csv_file = csv_loader.load()
        print("FILE UPLOADED: ", csv_file[:1])
# ==============================================

# Prompt Template
prompt_template = PromptTemplate.from_template(
    """
    Answer this question: {question} 
    based on the context: {context}
    """
)


# document loader
llama_llm = ChatGroq(model="llama-3.1-8b-instant")
gpt_llm = ChatGroq(model="openai/gpt-oss-20b")

llama_chain = prompt_template | llama_llm | StrOutputParser()
gpt_chain = prompt_template | gpt_llm | StrOutputParser()

question = st.text_input("Ask a question about your data", key="question_input")

if st.button("Submit"):
    if csv_file is not None:
        with st.spinner("Processing..."):
            llama_response = llama_chain.invoke(
                {"question": question, "context": csv_file}
            )
            gpt_response = gpt_chain.invoke({"question": question, "context": csv_file})

            st.markdown("#### Llama Response")
            st.write(llama_response)

            st.divider()

            st.markdown("#### GPT Response")
            st.write(gpt_response)

    else:
        st.warning("Please upload a CSV file first.")
