# BD Consumer Rights Assistant: An Offline RAG Chatbot for Bangladesh
A local, offline RAG chatbot that answers consumer rights queries based on Bangladeshi laws. It uses Ollama (LLaMA 3.2) for language understanding, FAISS for fast similarity search, and a simple Streamlit interface. No internet, no API keys, no data leaves your computer – just reliable answers from a curated Q&A dataset.

## Project Overview

Ever needed to quickly check a consumer right but found legal texts overwhelming? This project solves that by combining a local LLM with a focused FAQ dataset. 

The **Consumer Rights Assistant** loads a CSV file containing hundreds of common questions and official answers about consumer rights in Bangladesh. It then builds a FAISS vector index (just once) and uses Ollama's `llama3.2:1b` to retrieve and generate precise answers. 

All processing happens offline – no API calls, no trackers, no sudden costs. The Streamlit interface keeps interaction simple: you ask, the system finds the closest matching question, and the LLM returns a clear, context‑based answer. Perfect for developers learning RAG, privacy‑conscious users, or anyone needing a reliable consumer rights reference tool.


## Tech Stack 

| Component        | Technology Used                              |
|------------------|----------------------------------------------|
| **Language**     | Python 3.10+                                 |
| **LLM & Embeddings** | Ollama (`llama3.2:1b` – local, no API)   |
| **Vector Database** | FAISS (Facebook AI Similarity Search)        |
| **RAG Framework**   | LangChain (community, classic, Ollama)       |
| **Frontend**     | Streamlit (clean, one‑file UI)               |
| **Data**         | CSV (question/answer pairs, 400+ entries)    |





##  Quick Setup (3 steps)

1. **Install Ollama** and pull the model:
   ```bash
   ollama pull llama3.2:1b
2. **Install Python packages** (run in project folder):

   pip install langchain-community langchain-core langchain-classic langchain-ollama faiss-cpu streamlit
   
4. **Run the app:**

   ```bash
   streamlit run mainapp.py
   
- First time: click "Create Database" in sidebar (1-2 min to build FAISS index)
- Then ask any question (English )

### Sample Question:
1.What should I do if the seller does not give a cash memo?
2.What is the warranty period for a mobile phone?
3.What should a consumer do if expired food is sold?
4.What should I do if a shopkeeper charges more than the listed price?
5.What should I do if I receive a fake or damaged product?


### Project Files
- vukta_odhikar.py – backend (create DB, QA chain)
- vuktaapp.py – Streamlit frontend
- vuktaodikar.csv – Q&A dataset (400+ English entries)











  
