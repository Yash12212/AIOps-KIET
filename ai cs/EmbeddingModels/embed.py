from langchain_huggingface import HuggingFaceEmbeddings #importing the HuggingFaceEmbeddings class from the langchain_huggingface module
from dotenv import load_dotenv #using the load_dotenv function from the dotenv module to load environment variables from a .env file

load_dotenv()  # Load environment variables from .env file

embedding=HuggingFaceEmbeddings(
    model_name="Qwen/Qwen3-Embedding-4B", #specifying the model name for the embeddings
)

vector=embedding.embed_query("Hello, how are you?") #embedding a query string into a vector representation using the embed_query method of the embedding object

print(vector) #printing the resulting vector representation of the query string