# pip install langhchain-openai

from langchain_ollama import OllamaLLM, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPEN_API_KEY"] =api_key

# Initialize LLM
llm = ChatOllama(model="llama3.2:latest")

# Define prompt template
first_template = "Give me a simple bullet point outline for a blog post on {topic}"

topic = "AI"

# Create prompt
first_prompt = ChatPromptTemplate.from_template(first_template)


# Create chain one
chain_one = first_prompt | llm

# print('Chain one -------->', chain_one)

chain_one_result = chain_one.invoke(topic)


print("\n\033[1m Give me a simple bullet point outline for a blog post ")
print("-" * 50)
print('\033[0m' + chain_one_result.content)

# Define prompt template
second_template = "Write a blog post using this outline : {abc}"

# Create prompt
second_prompt = ChatPromptTemplate.from_template(second_template)

# Create chain two
chain_two = second_prompt | llm

print("Chain two ----------->", chain_two)


full_chain = chain_one | chain_two

result = full_chain.invoke(topic)

print("\n\033[1m Write a blog post using the outline")
print("-" * 50)
print('\033[0m' + result.content)