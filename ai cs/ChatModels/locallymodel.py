from langchain_huggingface import HuggingFacePipeline #importing the HuggingFacePipeline class from the langchain_huggingface module

llm=HuggingFacePipeline(
    model_id="HuggingFaceTB/SmolLM2-135M",
    task="text-generation",
    pipeline_kwargs={"temperature":0.7}
)

prompt="Hello, how are you?"
result=llm.invoke(prompt) #invoking the llm object with the prompt string to generate a response
print(result.content) #printing the content of the result object which contains the generated response