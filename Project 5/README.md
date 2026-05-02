#### 🛍️ Kenakata Q&A – E‑commerce FAQ Chatbot

This is an end‑to‑end LLM project  built with **Ollama + LangChain**.  
We are building a Q&A system for an e‑commerce store called **Kenakata** (fictional name).  
Kenakata sells a wide range of products online and has thousands of customers who frequently ask questions about orders, payments, shipping, returns, and warranties. This system provides a Streamlit‑based user interface where customers can ask questions and get instant, accurate answers.





---

##  Quick Setup (3 steps)

1. **Install Ollama** and pull the model  
   ```bash
   ollama pull llama3.2:1b
   
2. **Install Python dependencies**

bash
pip install langchain-community langchain-core langchain-classic langchain-ollama faiss-cpu streamlit

3. **Run the app**

bash
streamlit run main.py

- First launch: click “Create Knowledgebase” – this builds the FAISS index (takes 1‑2 minutes).
- Then type any question (e.g., “How long does shipping take?”).
  




**Sample Questions**
- How can I track my order?
- What is your return policy?
- What should I do if my package is lost or damaged?
- How long does shipping take?
- Do you offer international shipping?
  
**Tech Stack**
Component       -------	Technology
LLM & Embeddings-------	Ollama (llama3.2:1b)
Vector Database	-----FAISS
RAG Framework	  -----LangChain (community, classic, Ollama support)
Frontend	      -----Streamlit
Data Source	CSV -----(mainecommerce.csv, 40+ Q&A pairs)
  
  
**Project Structure**
- main.py: The main Streamlit application script.
- ecommerce.py: This has all the langchain code.


