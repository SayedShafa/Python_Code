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
