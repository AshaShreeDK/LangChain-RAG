from pathlib import Path
from langchain_community.vectorstores import FAISS
from app.embeddings import get_embeddings

# Base directories
FAISS_BASE_DIR = Path("faiss_index")
VERSIONS_DIR = FAISS_BASE_DIR / "versions"
CURRENT_LINK = FAISS_BASE_DIR / "CURRENT"


def create_faiss_index(chunks):
    """
    Explicit indexing function.
    Creates a NEW versioned FAISS index and updates CURRENT pointer.
    Must be called only via index.py.
    """
    VERSIONS_DIR.mkdir(parents=True, exist_ok=True)

    # Determine next version number
    existing_versions = sorted(
        [d for d in VERSIONS_DIR.iterdir() if d.is_dir() and d.name.startswith("v")]
    )
    next_version = f"v{len(existing_versions) + 1}"
    index_dir = VERSIONS_DIR / next_version

    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(index_dir)

    # Update CURRENT symlink atomically
    if CURRENT_LINK.exists() or CURRENT_LINK.is_symlink():
        CURRENT_LINK.unlink()
    CURRENT_LINK.symlink_to(index_dir)

    print(f"[INDEX] FAISS index {next_version} created and activated.")


def load_faiss_index():
    """
    Load FAISS index from CURRENT pointer.
    Fail fast if index is missing.
    """
    if not CURRENT_LINK.exists():
        raise RuntimeError(
            "FAISS index not found. Run `python index.py` before querying."
        )

    embeddings = get_embeddings()
    return FAISS.load_local(
        CURRENT_LINK,
        embeddings,
        allow_dangerous_deserialization=True
    )
