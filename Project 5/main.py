import streamlit as st
from ecommerce import get_qa_chain, create_vector_db

st.title("KENAKATA Q&A 🛍️")
btn = st.button("Create Knowledgebase")
if btn:
    create_vector_db()

question = st.text_input("Question: ")

if question:
    chain = get_qa_chain()
    response = chain(question)

    st.header("Answer")
    st.write(response["result"])
    
    #streamlit run main.py
    