from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

model=ChatGroq(model="openai/gpt-oss-20b",temperature=0.5,max_tokens=100)

result=model.invoke("provide me a sarcastic answer to the question: 'What is the machine learning")

print(result.content)

