from langchain_ollama import OllamaLLM, ChatOllama
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] = api_key

# Initialize LLM
llm = ChatOllama(model="llama3.2:latest")

employee_review = """
Employee Name: John Smith
Position: Software Developer
Department: IT

Performance Review:

John has demonstrated excellent performance throughout the review period.
He consistently completes assigned tasks on time and maintains high-quality
work standards.

Strengths:
- Strong problem-solving and analytical skills.
- Good knowledge of Python and software development.
- Works effectively with team members.
- Takes responsibility for assigned tasks.
- Shows willingness to learn new technologies.

Areas for Improvement:
- Should improve communication during team meetings.
- Needs to focus more on project documentation.
- Should work on time management when handling multiple tasks.

Overall Performance:
John is a dedicated and hardworking employee who contributes positively
to the organization. His overall performance has been satisfactory,
and he has shown good potential for professional growth.

Recommendation:
Continue developing technical skills and take more responsibility
for upcoming projects.
"""

# Define prompt template
template1 = "Give a summary of this employee's performance review:\n{review}"


prompt1 = ChatPromptTemplate.from_template(template1)

chain_1 = prompt1 | llm

print("\n\033[1m Summary of employee's performance review")
print("-" * 50)
print('\033[0m' + chain_1.invoke(employee_review).content)

template2 = "Identify key employee weakness in this review summary:\n{review_summary}"

prompt2 = ChatPromptTemplate.from_template(template2)

chain_2 = prompt2 | llm
print("\n\033[1m Identify key employee weakness in the performance review summary")
print("-" * 50)
print('\033[0m' + (chain_1 | chain_2).invoke(employee_review).content)

template3 = "Create a personalized plan to help address and fix these waknesses:\n{weaknesses}"

prompt3 = ChatPromptTemplate.from_template(template3)

chain_3 = prompt3 | llm

seq_chain = chain_1 | chain_2 | chain_3

results = seq_chain.invoke(employee_review)