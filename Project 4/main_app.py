import streamlit as st
from vukta_odhikar import create_vector_db, get_qa_chain

st.title("⚖️ Consumer Rights Assistant")
if st.sidebar.button("Create Database"):
    create_vector_db()
    st.sidebar.success("Ready!")

q = st.text_input("Your Question")
if q:
    chain = get_qa_chain()
    ans = chain.invoke({"query": q})['result']
    st.write(ans)

#streamlit run main_app.py
