# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser

# from app.vector_store import load_faiss_index
# from app.llm import get_llm
# from app.config import TOP_K


# def build_rag_chain():
#     """
#     Build a pure LCEL-based RAG chain (LangChain 1.x compatible).
#     """

#     vectorstore = load_faiss_index()
#     retriever = vectorstore.as_retriever(search_kwargs={"k": TOP_K})

#     prompt = ChatPromptTemplate.from_template(
#         """
# You are an internal enterprise assistant.
# Answer the question using ONLY the context provided.
# If the answer is not in the context, say "I don't know".

# Context:
# {context}

# Question:
# {question}

# Answer:
# """
#     )

#     llm = get_llm()

#     rag_chain = (
#         {
#             "context": retriever,
#             "question": RunnablePassthrough()
#         }
#         | prompt
#         | llm
#         | StrOutputParser()
#     )

#     return rag_chain, retriever
# def build_rag_chain(k=20):
#     vectorstore = load_faiss_index()
#     retriever = vectorstore.as_retriever(
#         search_kwargs={"k": k}
#     )
    
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from app.vector_store import load_faiss_index
from app.llm import get_llm
from app.config import TOP_K


def build_rag_chain(k: int = TOP_K):
    """
    Build a pure LCEL-based RAG chain (LangChain 1.x compatible).
    """

    vectorstore = load_faiss_index()

    # Retriever (still top-k, but now configurable)
    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an internal enterprise assistant.
Answer the question using ONLY the context provided.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
    )

    llm = get_llm()

    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return rag_chain, retriever
