from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

def create_geval_judge():

    judge_llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        groq_api_key=os.environ.get("GROQ_API_KEY"),
    )

    prompt = ChatPromptTemplate.from_template("""
You are an expert evaluator for RAG systems.

Given:

Question:
{question}

Retrieved Context:
{context}

Assistant Answer:
{answer}

Evaluate the answer on a 0-100 scale for:

1. groundedness
2. answer_relevance
3. citation_faithfulness
4. overall_quality

Also provide:
confidence score (0-100)

Return ONLY valid JSON in this format:

{{
  "groundedness": number,
  "answer_relevance": number,
  "citation_faithfulness": number,
  "overall": number,
  "confidence": number
}}
""")

    return prompt | judge_llm | StrOutputParser()
