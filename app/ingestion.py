# from pathlib import Path
# from langchain_community.document_loaders import TextLoader, PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# from app.config import DATA_DIR, DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP


# def load_documents():
#     """
#     Load all documents from data/documents directory.
#     Returns a list of LangChain Document objects.
#     """
#     documents = []

#     for domain_dir in DATA_DIR.iterdir():
#         if domain_dir.is_dir():
#             domain = domain_dir.name

#             for file_path in domain_dir.iterdir():
#                 if file_path.suffix == ".txt":
#                     loader = TextLoader(str(file_path))
#                     docs = loader.load()

#                 elif file_path.suffix == ".pdf":
#                     loader = PyPDFLoader(str(file_path))
#                     docs = loader.load()

#                 else:
#                     continue

#                 for doc in docs:
#                     doc.metadata["domain"] = domain
#                     doc.metadata["source"] = file_path.name

#                 documents.extend(docs)

#     return documents


# def split_documents(documents):
#     """
#     Split documents into chunks.
#     """
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=DEFAULT_CHUNK_SIZE,
#         chunk_overlap=DEFAULT_CHUNK_OVERLAP
#     )

#     return splitter.split_documents(documents)
#==============================================================
# from pathlib import Path
# from langchain_community.document_loaders import TextLoader, PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from app.config import DATA_DIR, DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP


# def load_documents():
#     """
#     Recursively load all documents from data/documents directory.
#     """
#     documents = []

#     for file_path in DATA_DIR.rglob("*"):
#         if file_path.suffix == ".txt":
#             loader = TextLoader(str(file_path))
#             docs = loader.load()

#         elif file_path.suffix == ".pdf":
#             loader = PyPDFLoader(str(file_path))
#             docs = loader.load()

#         else:
#             continue

#         # Metadata enrichment
#         for doc in docs:
#             doc.metadata["source"] = file_path.name
#             doc.metadata["path"] = str(file_path.relative_to(DATA_DIR))
#             doc.metadata["domain"] = file_path.relative_to(DATA_DIR).parts[0]
            
#     if len(file_path.parts) >= 3 else "unknown"

#         documents.extend(docs)

#     return documents


# def split_documents(documents):
#     splitter = RecursiveCharacterTextSplitter(
#         chunk_size=DEFAULT_CHUNK_SIZE,
#         chunk_overlap=DEFAULT_CHUNK_OVERLAP
#     )
#     return splitter.split_documents(documents)

from pathlib import Path
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config import DATA_DIR, DEFAULT_CHUNK_SIZE, DEFAULT_CHUNK_OVERLAP


def load_documents():
    """
    Recursively load all documents from data/documents directory
    and attach correct metadata.
    """
    documents = []

    for file_path in DATA_DIR.rglob("*"):
        if file_path.suffix == ".txt":
            loader = TextLoader(str(file_path))
            docs = loader.load()

        elif file_path.suffix == ".pdf":
            loader = PyPDFLoader(str(file_path))
            docs = loader.load()

        else:
            continue

        # Metadata enrichment (CRITICAL)
        for doc in docs:
            doc.metadata["source"] = file_path.name
            doc.metadata["path"] = str(file_path.relative_to(DATA_DIR))
            doc.metadata["domain"] = file_path.relative_to(DATA_DIR).parts[0]

        documents.extend(docs)

    return documents


def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=DEFAULT_CHUNK_SIZE,
        chunk_overlap=DEFAULT_CHUNK_OVERLAP
    )
    return splitter.split_documents(documents)
