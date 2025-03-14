from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddingModel=OpenAIEmbeddings(model='text-embedding-3-large',dimensions=32)

documents = [
    "Delhi is the capital of India.",
    "Gandhinagar is the capital of Gujarat."
    "Paris is the capital of France."
]

result = embeddingModel.embed_documents(documents)

print(str(result))