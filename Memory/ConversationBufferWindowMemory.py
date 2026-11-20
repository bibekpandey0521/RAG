from langchain_ollama import ChatOllama
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv
import os

load_dotenv()

# Read the key
anthropic_api_key = os.getenv('API_KEY')

os.environ["ANTHROPIC_API_KEY"] = anthropic_api_key

# Initialize the LLM
llm = ChatOllama(
    model = "llama3.2:latest",
    temperature=0.7
)

# Memory to LLM
memory = ConversationBufferWindowMemory(k=1,return_messages=True)

memory.save_context({"input" : "hi"},{"output" : "whas up"})
memory.save_context({"input" : "not much you"},{"output" : "not much"})

memory.load_memory_variables({})

memory = ConversationBufferWindowMemory(k=3)

conversation = ConversationChain(memory=memory,
                                 llm = llm,
                                 verbose = True)

print(conversation.predict(input="Hi, this is Ram?"))
print(conversation.predict(input="2*2 is 4"))
print(conversation.predict(input="what is my name"))