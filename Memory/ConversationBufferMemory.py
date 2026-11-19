# from langchain_anthropic import ChatAnthropic
# from langchain_classic.chains import ConversationChain
# from langchain_classic.memory import ConversationBufferMemory

# from dotenv import load_dotenv
# import os

# load_dotenv()

# llm = ChatAnthropic(
#     model="claude-sonnet-4-5",
#     api_key=os.getenv("ANTHROPIC_API_KEY"),
#     temperature=0
# )

# memory = ConversationBufferMemory()

# conversation = ConversationChain(
#     llm=llm,
#     memory=memory,
#     verbose=True
# )

# response = conversation.predict(
#     input="Hello, my name is Bibek"
# )

# print(response)

# response = conversation.predict(
#     input="What is my name?"
# )

# print(response)

from langchain_ollama import ChatOllama
from langchain_classic.chains import ConversationChain
from langchain_classic.memory import ConversationBufferMemory

llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0.7
)

memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm = llm,
    memory = memory,
    verbose = True
)

print(conversation.predict(input="Hi, my name is Ram"))

print(conversation.predict(input="I'm doing well! Just having a conversation with an AI"))

print(conversation.predict(input="What is AI"))