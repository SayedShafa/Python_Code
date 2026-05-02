# Import required libraries
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CSVLoader
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
#import os

# =================== CONFIGURATION ===================
# Path of CSV file (update if needed)

CSV_FILE_PATH = r'D:\pythoncode\Gitcode\Project10\engvuktaodikar.csv'

# Folder where FAISS vector database will be saved
FAISS_INDEX_PATH = "faiss_index_vukta"

# Local Ollama model name (already downloaded,offline model)
OLLAMA_MODEL =  "llama3.2:1b"     # for my pc use "llama3.2:1b"/ "qwen2.5:0.5b"
TEMPERATURE = 0.1

# =====================================================

# 1. Initialize the local LLM using Ollama
llm = ChatOllama(model=OLLAMA_MODEL, temperature=TEMPERATURE)

# 2. Initialize embeddings using the same local model
embeddings = OllamaEmbeddings(model=OLLAMA_MODEL)

def create_vector_db():
    """
    Load questions and answers from CSV, create a FAISS vector database,
    and save it locally.
    """
    # Load CSV with 'question' as the source column
    loader = CSVLoader(file_path=CSV_FILE_PATH,
                       source_column="question",
                       encoding='utf-8-sig')
    documents = loader.load()
    print(f" Loaded {len(documents)} documents.")
    
    # Create FAISS vector store
    vectordb = FAISS.from_documents(documents=documents, embedding=embeddings)
    
    # Save to disk
    vectordb.save_local(FAISS_INDEX_PATH)
    print(f" FAISS index saved to folder: '{FAISS_INDEX_PATH}'")

def get_qa_chain():
    """
    Load the saved FAISS index and create a RetrievalQA chain.
    """

    # Load vector database (allow deserialization for local trusted files)
    vectordb = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
    
    # Create retriever (returns top 3 relevant documents)
    retriever = vectordb.as_retriever(search_kwargs={"k": 3, "score_threshold": 0.5})
    
    # Define prompt template
    prompt_template = """You are an assistant specializing in consumer rights in Bangladesh.
Based only on the context below, provide a detailed answer. Do not go outside the context.
If the answer is not found in the context, clearly say: "Sorry, I cannot provide accurate information on this matter. Please contact the Consumer Rights Directorate hotline at 16125."
Keep the answer short, accurate, and relevant.

Context: {context}

Question: {question}

Answer:"""
    
    PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    
    # Build the QA chain
    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=False,   # Set to True if you want to see sources
                                        chain_type_kwargs={"prompt": PROMPT})
    return chain

if __name__ == "__main__":
     
    # Uncomment the next line only ONCE at time of first run to create the vector database.after running succesfully do comment of it
    create_vector_db()
    
    # After the index is created, you can comment the above line and run the chain directly
    chain = get_qa_chain()
    
    # Ask a question
    question = "What is the warranty period for a mobile phone??"
    answer = chain.invoke({"query": question})
    
    print(f"\n Question: {question}")
    print(f" Answer: {answer['result']}")
