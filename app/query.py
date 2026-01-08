from app.rag_chain import build_rag_chain
from app.vector_store import load_faiss_index
# def search_all_matches(
#     question: str,
#     k: int = 50,
#     score_threshold: float = 0.35,
# ):
def search_all_matches(
    question: str,
    k: int = 50,
    score_threshold: float = 1.2,  # <-- changed
):

    """
    Return all matching chunks above a similarity threshold.
    No LLM involved.
    """

    vectorstore = load_faiss_index()

    docs_with_scores = vectorstore.similarity_search_with_score(
        question,
        k=k
    )

    matches = []

    for doc, score in docs_with_scores:
        if score <= score_threshold:
            matches.append({
                "content": doc.page_content,
                "metadata": doc.metadata,
                "score": score
            })

    return matches

def search_by_domain(
    question: str,
    domain: str,
    k: int = 50,
    score_threshold: float = 1.2,
):
    """
    Return all matching chunks for a given domain.
    """

    all_matches = search_all_matches(
        question=question,
        k=k,
        score_threshold=score_threshold
    )

    filtered = [
        m for m in all_matches
        if m["metadata"].get("domain") == domain
    ]

    return filtered

def ask(question: str):
    rag_chain, retriever = build_rag_chain()

    answer = rag_chain.invoke(question)
    sources = retriever.invoke(question)

    return answer, sources


if __name__ == "__main__":
    while True:
        q = input("\nAsk a question (or type 'exit'): ")
        if q.lower() == "exit":
            break

        answer, sources = ask(q)

        print("\nAnswer:\n", answer)

        print("\nSources:")
        for doc in sources:
            print(f"- {doc.metadata}")
