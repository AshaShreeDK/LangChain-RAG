from app.ingestion import load_documents, split_documents


def inspect_chunks(preview_len=150):
    documents = load_documents()
    chunks = split_documents(documents)

    print(f"\nDocuments: {len(documents)}")
    print(f"Chunks: {len(chunks)}\n")

    for i, chunk in enumerate(chunks, start=1):
        print(f"--- CHUNK {i} ---")
        print(chunk.page_content[:preview_len].replace("\n", " ") + "...")
        print("Metadata:", chunk.metadata)
        print()


if __name__ == "__main__":
    inspect_chunks()
