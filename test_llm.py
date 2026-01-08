from app.llm import get_llm

llm = get_llm()
response = llm.invoke("Say only the word READY")
print(response.content)
