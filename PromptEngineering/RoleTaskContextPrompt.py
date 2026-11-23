# pip install langchain-community
# pip install openai

# import os
# from dotenv import load_dotenv
# from langchain.llms import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain
# from langchain.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM, ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import LLMChain

# load environment variables from .env file
load_dotenv()

api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"]=api_key

# Initialize the LLM
llm =ChatOllama(temperature=0.7,model="llama3.2:latest")

# Define prompt template
role_context_template = """
You are a highly professional customer support specialist at a premium tech company.
You goal is to address the customer's concerns while maintaining a calm and helpful demenaor.


Cusomter Message : {customer_message}

Please provide a response that:
1. Acknowldeges the csutomer's feelings
2. Addressed their concerns professionally
3. Offers concerete solutions
4. Ends with a positive note

"""

role_context_prompt = PromptTemplate(
    input_variables=["customer_message"],
    template=role_context_template
)

role_context_chain = LLMChain(llm=llm,prompt=role_context_prompt)

customer_message="""
    I've been waiting for 2hours for your delievery and it still hasn't arrived!
    This is absolutely unacceptable! I paid extra for express delivery adn this is
    what I get? I want my money back immediately!
"""

print(role_context_chain.run(customer_message))