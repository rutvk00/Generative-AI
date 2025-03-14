from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_HOME'] = 'F:/huggingface_cache-embedding'
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# text = "Delhi is the capital of India."
documents = [
    "Delhi is the capital of India.",
    "Gandhinagar is the capital of Gujarat."
    "Paris is the capital of France."
]

vectors = embedding.embed_documents(documents)
# vector = embedding.embed_query(text)

print(str(vectors))