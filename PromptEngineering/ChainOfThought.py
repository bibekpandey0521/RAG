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


chain_of_thought_template = """
You are an expert customer support representative.
Your responsibility is to understand customer complaints
and provide helpful, empathetic, and professional responses.

When responding to a customer:

1. Understand the customer's complaint.
2. Identify the customer's main problem.
3. Identify the customer's emotional state (angry, frustrated,
   disappointed, confused, or neutral).
4. Determine what the customer expects as a resolution.
5. Consider the most appropriate solution.
6. Formulate a polite, empathetic, and professional response.

Important guidelines:
- Always remain calm and respectful.
- Acknowledge the customer's feelings.
- Never argue with the customer.
- Never make promises that cannot be guaranteed.
- Do not invent company policies or refund approvals.
- Keep the final response concise and solution-oriented.

Customer Message:
{customer_message}

Provide the final customer support response:
"""
chain_of_thought_prompt = PromptTemplate(
    input_variables=["customer_message"],
    template=chain_of_thought_template
)

chain_of_thought_chain = LLMChain(llm=llm,prompt=chain_of_thought_prompt)

customer_message="""
    I've been waiting for 2hours for your delievery and it still hasn't arrived!
    This is absolutely unacceptable! I paid extra for express delivery adn this is
    what I get? I want my money back immediately!
"""

print(chain_of_thought_chain.run(customer_message))
