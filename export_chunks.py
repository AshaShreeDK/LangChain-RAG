import json
from app.ingestion import load_documents, split_documents
from chunk_ids import generate_chunk_id


OUTPUT_FILE = "chunks.jsonl"


def export_chunks():
    chunks = split_documents(load_documents())

    with open(OUTPUT_FILE, "w") as f:
        for chunk in chunks:
            record = {
                "chunk_id": generate_chunk_id(chunk.page_content),
                "content": chunk.page_content,
                "metadata": chunk.metadata
            }
            f.write(json.dumps(record) + "\n")

    print(f"Exported {len(chunks)} chunks to {OUTPUT_FILE}")


if __name__ == "__main__":
    export_chunks()

