from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

messages=[
    SystemMessage(content="You are a angry assistant.")
    ]

chat = ChatGroq(model_name="openai/gpt-oss-20b", temperature=0.7)
while True:
    user_input = input("User: ")
    if user_input=="0":
        break
    messages.append(HumanMessage(content=user_input))
    response = chat.invoke(messages)
    print(f"AI: {response.content}")
    messages.append(AIMessage(content=response.content))

print(messages)