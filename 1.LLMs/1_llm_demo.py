from langchain_openai import OpenAI
from dotenv import load_dotenv

# Load .env file 
load_dotenv()

# Load model from openAI 
llm = OpenAI(model='gpt-3.5-turbo-instruct')

# Invoke Model 
result = llm.invoke("What is the capital of India ?")

print("result : ", result)