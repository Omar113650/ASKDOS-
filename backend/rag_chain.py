from operator import itemgetter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

def create_qa_chain(retriever):

    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.2,
         groq_api_key=os.environ.get("GROQ_API_KEY"),

    )
    

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You answer questions about the contract using ONLY the provided context."),
            MessagesPlaceholder(variable_name="history"),
            ("system", "Context:\n{context}"),
            ("human", "{question}")
        ]
    )

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {
            "context": itemgetter("question") | retriever | format_docs,
            "question": itemgetter("question"),
            "history": itemgetter("history"),   
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    chain_with_memory = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="question",
        history_messages_key="history",
    )

    return chain_with_memory
































