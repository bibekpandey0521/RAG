# pip install langchain-openai

# from langchain_openai import ChatOpenAI

from langchain_ollama import OllamaLLM, ChatOllama

from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate
)

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPEN_API_KEY"] = api_key


# Create a simple prompt by using Human MessagePromptTemplate
human_message_prompt = HumanMessagePromptTemplate.from_template(
    "Make up a funny company name for a company that produces {product}"
)

# Chat prompt template
chat_prompt_template = ChatPromptTemplate.from_messages([human_message_prompt])


# Initailze LLM
llm = ChatOllama(model="llama3.2:latest")


# bind LLM and Chat prompt template
chain = chat_prompt_template | llm

# print(llm)

topic="C#"
funnyCompanyName = chain.invoke(input=topic).content


print(funnyCompanyName)


print("\n\033[1m Make up a funny company name for the topic " + topic)
print("-" * 50)

print('\033[0m' + funnyCompanyName)