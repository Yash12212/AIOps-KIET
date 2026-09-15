from langchain_groq import ChatGroq #importing the ChatGroq class from the langchain_groq module

from dotenv import load_dotenv #using the load_dotenv function from the dotenv module to load environment variables from a .env file

load_dotenv()  # Load environment variables from .env file

model= ChatGroq(model="qwen/qwen3.8-27b", temperature=0.9, max_tokens=20) #creating an instance of the ChatGroq class and assigning it to the variable model

prompt="write a poem on sky" 

result=model.invoke(prompt)

print(result.content) #printing the result of the model's response to the prompt