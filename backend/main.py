from fastapi import FastAPI, UploadFile
from langserve import add_routes
from langchain_core.runnables import RunnableLambda
from backend.ingestion import load_document, create_vector_store
from backend.rag_chain import create_qa_chain
# from backend.evaluation.evaluator import evaluate
from backend.evaluation.evaluator import evaluate_with_geval

import shutil
import os

app = FastAPI(title="Smart Contract RAG API")

os.makedirs("data", exist_ok=True)

qa_chain = None
retriever = None


def build_chain(file_path: str):
    global retriever
    docs = load_document(file_path)
    vectorstore = create_vector_store(docs)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    return create_qa_chain(retriever)


@app.post("/upload")
async def upload_file(file: UploadFile):
    global qa_chain

    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    qa_chain = build_chain(file_path)

    return {"message": "Document processed successfully"}


def invoke_chain(inputs: dict):
    if qa_chain is None:
        return "Please upload a document first."

    return qa_chain.invoke(
        {"question": inputs["question"]},
        config={"configurable": {"session_id": "default"}}
    )


rag_runnable = RunnableLambda(invoke_chain)

add_routes(app, rag_runnable, path="/rag")

@app.get("/evaluate-geval")
async def run_geval():
    if qa_chain is None:
        return {"error": "Upload document first."}
    if retriever is None:
        return {"error": "Please upload a document first."}
    results = evaluate_with_geval(qa_chain, retriever)

    return results




@app.get("/health")
async def health():
    return {"status": "ok"}






