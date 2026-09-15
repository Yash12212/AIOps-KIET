from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline 

llm=HuggingFacePipeline(
    model_id="Qwen/Qwen2.5-0.5B-Instruct"
)

prompt="hi!!! how are you?"
model=ChatHuggingFace(llm=llm)
result=model.invoke(prompt)
print(result.content)