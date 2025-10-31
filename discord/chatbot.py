import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]

st.header("📘 My First Chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Upload a PDF file and start asking questions", type="pdf")

if file is not None:
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # ---- Break Text into Chunks ----
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # ---- Generate Embeddings ----
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    # ---- Create FAISS Vector Store ----
    vector_store = FAISS.from_texts(chunks, embeddings)

    user_question = st.text_input("💬 Type your question here:")

    if user_question:
        match = vector_store.similarity_search(user_question)
        llm = ChatOpenAI(
            openai_api_key=OPENAI_API_KEY,
            temperature=0,
            max_tokens=1000,
            model_name="gpt-3.5-turbo"
        )
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=match, question=user_question)

        st.subheader("🧠 Answer:")
        st.write(response)
else:
    st.info("👆 Please upload a PDF file to begin.")