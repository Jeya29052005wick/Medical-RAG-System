import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import google.generativeai as genai
import os

st.title("🏥 Medical RAG Chatbot")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# NEW - Active Model
model = genai.GenerativeModel("gemini-2.5-flash")

@st.cache_resource
def load_db():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)

db = load_db()

query = st.text_input("Ask a medical question:")

if query:
    docs = db.similarity_search(query, k=3)
    context = "\n\n".join([d.page_content for d in docs])

    try:
        response = model.generate_content(
            f"Answer using only this context:\n{context}\n\nQuestion: {query}"
        )
        # Check if the response was blocked by safety filters
        if response.text:
            st.write(response.text)
        else:
            st.warning("The model returned an empty response. It may have been blocked by safety filters.")
            
    except Exception as e:
        st.error(f"An error occurred: {e}")