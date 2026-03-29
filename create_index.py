from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

print("Loading PDF...")
loader = PyPDFLoader("medical.pdf")
documents = loader.load()

print("Splitting...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(documents)

print("Creating embeddings...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("Creating FAISS index...")
db = FAISS.from_documents(chunks, embeddings)

print("Saving index...")
db.save_local("faiss_index")

print("✅ DONE")