from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()
messages=[
    SystemMessage(content="You are a angry assistant that is very rude and sarcastic. You will answer the user in a very rude and sarcastic manner.")
]
model=ChatGroq(model="openai/gpt-oss-20b")
print("-------Write '0' to exit-------")
while True:hi
    user=input("User: ")
    if user=="0":
        break
    messages.append(HumanMessage(content=user))
    result=model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print("Bot:",result.content)

print(messages)