"""
Chunk inspection utility.
This file is used ONLY for debugging and auditing chunks.
It does NOT touch FAISS or indexing.
"""

from app.ingestion import load_documents, split_documents


def inspect_chunks(preview_only=True, preview_len=150):
    documents = load_documents()
    chunks = split_documents(documents)

    print(f"\nTotal documents loaded: {len(documents)}")
    print(f"Total chunks created: {len(chunks)}\n")

    for i, chunk in enumerate(chunks, start=1):
        print(f"--- CHUNK {i} ---")

        if preview_only:
            text = chunk.page_content[:preview_len].replace("\n", " ")
            print(text + "...")
        else:
            print(chunk.page_content)

        print("Metadata:", chunk.metadata)
        print()


if __name__ == "__main__":
    # Change preview_only=False to print full chunks
    inspect_chunks(preview_only=True)

