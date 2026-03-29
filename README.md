
# 🏥 Medical RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot that answers medical questions using a medical textbook dataset.
The system uses FAISS for vector search and Google Gemini for generating responses.

---

## 🚀 Features

* 📚 Retrieval-Augmented Generation (RAG)
* 🔍 FAISS vector similarity search
* 🤖 Google Gemini (2.5 Flash) for response generation
* ⚡ Fast response using precomputed embeddings
* 🌐 Streamlit web interface

---

## 🧠 How It Works

1. Medical PDF is split into chunks
2. Embeddings are created using HuggingFace model
3. Stored in FAISS vector database
4. User query → similar chunks retrieved
5. Gemini generates answer based on context

---

## 📂 Project Structure

```
medical-rag/
│
├── app.py                # Streamlit application
├── faiss_index/          # Precomputed vector database
├── requirements.txt      # Dependencies
├── README.md             # Documentation
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/medical-rag.git
cd medical-rag
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set API Key

Get your API key from:
👉 https://aistudio.google.com

Set environment variable:

```bash
set GOOGLE_API_KEY=your_api_key
```

---

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

## 🌐 Live Demo

👉 https://your-app-link

---

## 📊 Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* HuggingFace Embeddings
* Google Gemini API

---

## ⚠️ Notes

* The original PDF dataset is not included due to size constraints
* Precomputed FAISS index is used for fast retrieval
* Do not expose your API key publicly



