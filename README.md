# 📄 Smart Contract RAG Assistant

A Retrieval-Augmented Generation (RAG) system that allows users to upload a contract (PDF or DOCX) and ask questions about it using a conversational interface with memory.

Built with **FastAPI**, **LangChain (LCEL)**, **ChromaDB**, **Ollama (Mistral)**, and **Gradio**.

---

## 🎥 Demo

Below is a short demo of the system in action:

[🎬 Watch Demo](assets/demo.mp4)

> If the video does not preview directly on GitHub, download it from the link above.


## 🚀 Features

- 📂 Upload contract documents (PDF / DOCX)
- 🔎 Automatic document chunking & embeddings
- 🧠 Vector search using ChromaDB
- 🤖 RAG pipeline powered by Mistral (via Ollama)
- 💬 Conversational memory (chat history support)
- 🌐 REST API with FastAPI + LangServe
- 🖥 Modern Chat UI using Gradio

---

## 🏗 Architecture Overview

1. **Document Ingestion**
   - Load PDF/DOCX
   - Split into chunks
   - Generate embeddings (HuggingFace)
   - Store vectors in ChromaDB

2. **RAG Pipeline**
   - Retrieve top-k relevant chunks
   - Inject context into prompt
   - Generate answer using Mistral (Ollama)

3. **Conversation Memory**
   - Managed via `RunnableWithMessageHistory`
   - Session-based chat history

4. **Frontend**
   - Upload document
   - Chat with memory-enabled assistant

---

## 🛠 Tech Stack

- Python
- FastAPI
- LangChain (LCEL)
- ChromaDB
- Ollama (Mistral model)
- HuggingFace Embeddings
- Gradio (v6+)

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Youssef-Osama1/smart-contract-assistant.git
cd smart-contract-assistant
```
### 2️⃣ Create environment

```bash
conda create -n smart_assistant python=3.11 -y
conda activate smart_assistant
```
### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```
---

## ⚙️ Setup Ollama

Install Ollama from:

https://ollama.com

Then pull the Mistral model:
```bash
ollama pull mistral
```
Make sure Ollama is running locally.

---

## ▶️ Run the Backend
```bash
uvicorn backend.main:app --reload
```
Backend runs at:

http://localhost:8000

---

## ▶️ Run the Frontend
```bash
python frontend/app.py
```
Frontend runs at:

http://127.0.0.1:7860

---

## 💬 How It Works

1. Upload a contract
2. The system builds a vector store
3. Ask questions about the contract
4. The assistant:
   - Retrieves relevant context
   - Uses memory of previous messages
   - Generates accurate responses

---

## 📂 Project Structure
```
smart-contract-assistant/
│
├── backend/
│   ├── ingestion.py
│   ├── rag_chain.py
│   ├── main.py
│
├── frontend/
│   ├── app.py
|
├── assets/
│   └── demo.mp4
|
├── requirements.txt
└── README.md
```

---

## 🧠 Example Use Cases

- Contract review
- Clause explanation
- Obligation clarification
- Risk identification
- Legal Q&A assistance

---

## 🔮 Future Improvements

- Persistent memory storage
- User-based session IDs
- Streaming responses
- Authentication
- Docker deployment
- Cloud deployment (AWS / Azure)
