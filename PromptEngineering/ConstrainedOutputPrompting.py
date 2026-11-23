import os
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM, ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain


# Load environment varaibel from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] = api_key

# Initialize the LLM
llm =ChatOllama(temperature=0.7,model="llama3.2:latest")


constrained_template = """
You are a helpful, accurate, and professional AI assistant.

Follow these instructions strictly:

1. Answer the user's question clearly and accurately.
2. Stay focused on the user's actual question.
3. Do not provide irrelevant information.
4. If you do not know the answer, clearly say "I don't know."
5. Do not make up facts, statistics, or references.
6. Use simple and understandable language.
7. Break complex explanations into smaller steps.
8. Use bullet points or numbered lists when appropriate.
9. Keep answers concise but informative.
10. Follow the requested output format strictly.
11. Do not include unnecessary introductions or conclusions.
12. If the user asks for code, provide properly formatted and executable code.
13. Explain code briefly when necessary.

Customer message: {customer_message}

"""


constrained_prompt = PromptTemplate(
    input_variables=["customer_message"],
    template=constrained_template
)

constrained_chain = LLMChain(llm=llm,prompt=constrained_prompt)

customer_message="""
    I've been waiting for 2hours for your delievery and it still hasn't arrived!
    This is absolutely unacceptable! I paid extra for express delivery adn this is
    what I get? I want my money back immediately!
"""


print(constrained_chain.run(customer_message))