from langchain_ollama import ChatOllama
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationSummaryMemory

from dotenv import load_dotenv
import os

# load environment variables from the .env files
load_dotenv()



# Read the key
anthropic_api_key = os.getenv('API_KEY')

os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key

# Initialize the LLM
llm = ChatOllama(
    model = "llama3.2:latest",
    temperature=0.7
)

# create a long string
schedule = "There is a meeting at 8am with product team.\
    You will need your powerpoint presentation prepared.\
    9am-12pm have time to work on your LangChain \
    project which will go quickly because LangChain is such a powerful tool.\
    At Noon,lunch at the Italian resturant with a customer who is driving \
    from over an hour away to meet you to understand the latest in AI. \
    Be sure to bring your laptop to show the latest LLM demo." 

memory = ConversationSummaryMemory(llm = llm)

# memory = ConversationSummaryMemory(llm = llm,max_token_llm = 100)

memory.save_context({"input" : "Hello"},{"output": "what's up"})

memory.save_context({"input" : "Not Much , just hnaging"},{"output" : "Cool"})
memory.save_context({"input" : "what is on the schedule today"},{"output" : f"{schedule}"})

memory.load_memory_variables({})

conversation = ConversationChain(memory=memory,
                                llm=llm,
                                verbose=True)

# print(memory.load_memory_variables({}))

print(conversation.predict(input="9am-12pm what will you do?"))

print(conversation.predict(input="What is deep learning?"))

print(conversation.predict(input="What is AI?"))
print(conversation.predict(input="which weather is now and temperature??"))