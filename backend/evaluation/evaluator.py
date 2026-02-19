# backend/evaluation/evaluator.py
from backend.evaluation.geval_judge import create_geval_judge
import json

def evaluate_with_geval(qa_chain, retriever, dataset):

    judge = create_geval_judge()
    results = []
    total = len(dataset)

    for sample in dataset:
        question = sample["question"]
        # Run RAG
        response = qa_chain.invoke(
            {"question": question},
            config={"configurable": {"session_id": "eval"}}
        )
        answer = response

        # get retrieved docs
        docs = retriever.get_relevant_documents(question)
        context = "\n\n".join([d.page_content for d in docs])

        judge_output = judge.invoke({
            "question": question,
            "context": context,
            "answer": answer
        })

        scores = json.loads(judge_output)
        results.append(scores)

    # aggregate
    final = {
        "geval_overall": sum(r["overall"] for r in results) / total,
        "geval_groundedness": sum(r["groundedness"] for r in results) / total,
        "geval_answer_relevance": sum(r["answer_relevance"] for r in results) / total,
        "geval_citation_faithfulness": sum(r["citation_faithfulness"] for r in results) / total,
        "avg_confidence": sum(r["confidence"] for r in results) / total,
        "evaluated_prompts": total
    }

    return final
