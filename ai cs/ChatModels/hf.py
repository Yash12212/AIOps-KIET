from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint #importing the ChatHuggingFace class from the langchain_huggingface module
from dotenv import load_dotenv #using the load_dotenv function from the dotenv module to load environment variables from a .env file

load_dotenv()  # Load environment variables from .env file

llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task= "text-generation"
)

model=ChatHuggingFace(llm=llm)

#continue with invoke things