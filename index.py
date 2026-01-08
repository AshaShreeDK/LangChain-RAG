"""
Explicit indexing entry point.
This script is responsible ONLY for:
- loading documents
- chunking
- building FAISS index
"""

from app.ingestion import load_documents, split_documents
from app.vector_store import create_faiss_index

def run_indexing():
    print("[INDEX] Loading documents...")
    documents = load_documents()

    print("[INDEX] Splitting documents into chunks...")
    chunks = split_documents(documents)

    print(f"[INDEX] Total documents: {len(documents)}")
    print(f"[INDEX] Total chunks: {len(chunks)}")

    print("[INDEX] Building FAISS index...")
    create_faiss_index(chunks)

    print("[INDEX] Indexing completed successfully.")

if __name__ == "__main__":
    run_indexing()

