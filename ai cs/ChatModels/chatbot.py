from langchain_groq import ChatGroq #importing the ChatGroq class from the langchain_groq module

from dotenv import load_dotenv #using the load_dotenv function from the dotenv module to load environment variables from a .env file

load_dotenv()  # Load environment variables from .env file

model= ChatGroq(model="qwen/qwen3.8-27b", temperature=0.9) #creating an instance of the ChatGroq class and assigning it to the variable model
memory=[] #initializing an empty list to store the conversation history
print("-------------Chatbot ------------------")
print("Press 0 if you dont want chatbot to run")
while True: #starting an infinite loop to continuously take user input and generate responses
    user=input("Enter the prompt: ") #taking user input for the prompt
    if user == "0":
        break
    memory.append(user) #appending the user input to the memory list to keep track of the conversation history
    result=model.invoke(user) #invoking the model object with the user input prompt to generate a response
    memory.append(result.content) #appending the generated response to the memory list
    print(result.content) #printing the generated response to the console
