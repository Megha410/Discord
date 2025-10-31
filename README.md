# Discord
This is an interactive AI-powered chatbot built with Streamlit and LangChain that allows users to upload PDF documents and ask questions about their content. 
# 🧠 PDF Question Answering Chatbot

## 📘 Overview
This project is an **AI-powered chatbot** built using **Streamlit** and **LangChain** that enables users to **upload PDF documents and ask questions** related to their content.  
The chatbot reads and processes the text from uploaded PDFs, splits it into smaller chunks, and generates **vector embeddings** using **OpenAI’s Embedding API**.  
These embeddings are stored in a **FAISS vector database** to allow efficient semantic search, and **GPT-3.5 Turbo** is used to generate accurate and context-aware responses.

---

## ⚙️ Tech Stack
- **Frontend:** Streamlit  
- **Backend:** Python  
- **AI Frameworks:** LangChain, OpenAI API  
- **Vector Database:** FAISS  
- **Libraries:** PyPDF2, RecursiveCharacterTextSplitter  

---

## 🚀 Features
✅ Upload and process PDF files  
✅ Ask natural language questions  
✅ Retrieve context-based answers  
✅ Secure API key management with Streamlit Secrets  
✅ Clean and interactive user interface  

---

## 🧩 How It Works
1. User uploads a PDF through the Streamlit sidebar  
2. The system extracts text using **PyPDF2**  
3. Text is split into chunks using **RecursiveCharacterTextSplitter**  
4. Each chunk is converted into vector embeddings using **OpenAIEmbeddings**  
5. Embeddings are stored in a **FAISS vector store**  
6. When a user asks a question, similar chunks are retrieved  
7. **ChatOpenAI** (GPT-3.5 Turbo) generates a natural language response  

---

