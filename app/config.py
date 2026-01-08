from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Data paths
DATA_DIR = BASE_DIR / "data" / "documents"
FAISS_INDEX_DIR = BASE_DIR / "faiss_index"

# Embedding model (Hugging Face)
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

# Chunking defaults
DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 200

# Retrieval
TOP_K = 4
