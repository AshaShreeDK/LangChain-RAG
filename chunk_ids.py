import hashlib
from app.ingestion import load_documents, split_documents


def generate_chunk_id(text: str) -> str:
    """
    Generate a stable, deterministic ID for a chunk.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]


def attach_chunk_ids():
    documents = load_documents()
    chunks = split_documents(documents)

    for chunk in chunks:
        chunk.metadata["chunk_id"] = generate_chunk_id(chunk.page_content)

    return chunks


if __name__ == "__main__":
    chunks = attach_chunk_ids()
    print(f"Assigned chunk IDs to {len(chunks)} chunks")
    print("Sample metadata:", chunks[0].metadata)

