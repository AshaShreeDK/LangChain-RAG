from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.ingestion import load_documents


def split_with(chunk_size, overlap):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )
    docs = load_documents()
    return splitter.split_documents(docs)


def compare():
    strategies = [
        (500, 50),
        (800, 100),
        (1000, 150)
    ]

    for size, overlap in strategies:
        chunks = split_with(size, overlap)
        print(f"chunk_size={size}, overlap={overlap} → chunks={len(chunks)}")


if __name__ == "__main__":
    compare()

