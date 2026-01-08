import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq

ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)

def get_llm():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY not found")

    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0,
        api_key=api_key
    )
