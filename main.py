# pip install langchain
# pip install langchain-text-splitter
# pip install langchain-community
# pip install langchain-anthropic
# pip install sentence-transformers
# pip install chromadb
# pip install langchain langchain-text-splitters langchain-community langchain-anthropic sentence-transformers chromadb

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_anthropic import ChatAnthropic
from langchain_classic.chains import RetrievalQA
from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os

# load environment variable from .env file
load_dotenv()

# Read the key
api_key = os.getenv('API_KEY')

os.environ["ANTHROPIC_API_KEY"] = api_key

# Step 1 : Sample document
print("\nStep 1 : Preparing our document:")
print("-" * 50)
document = """
    1. Artificial Intelligence (AI)
    Artificial Intelligence (AI) enables machines to perform tasks that normally require 
    human intelligence, such as learning, reasoning, and decision-making. It helps automate 
    processes and solve complex problems efficiently.

    2. Natural Language Processing (NLP)
    Natural Language Processing (NLP) allows computers to understand, interpret, and 
    generate human language. It is used in chatbots, language translation, voice assistants, 
    and text analysis.

    3. Computer Vision
    Computer Vision enables computers to interpret and understand visual information from 
    images and videos. It is widely used in facial recognition, object detection, medical 
    imaging, and self-driving vehicles.

    4. Reinforcement Learning
    Reinforcement Learning is a type of machine learning in which an agent learns by interacting
    with its environment and receiving rewards or penalties. It helps systems improve their 
    decisions through experience and is used in robotics, gaming, and autonomous systems.
"""

print("Document loaded. Length:",len(document),"characters")
print("\nPreview of the document.")
print(document[:200],"...\n")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50,
    length_function = len,
    separators=["\n\n","\n",". "," "]
)

chunks = text_splitter.split_text(document)

print(f"Document has been split into {len(chunks)} chunks.")
print("\nExample chunks:")
for i , chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print(chunk)
    print("-" * 30)




# Step 3 : Initialize Embeddings
print("\nStep 3: Creating embeddings")
print("-" * 50)

embeddings = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

print("Embedding model loaded:",embeddings.model_name)

# OpenAI embeddings:
# embeddings = OpenAIEmbeddings()

# Step 4 : Create and populate vector store
print("\nStep 4 : Creating vector store")
print("-" * 50)

# Create vector store
vectorstore = Chroma.from_texts(
    texts = chunks,
    embedding = embeddings,
    persist_directory= "./chroma_db"
)

print("Vector store created with followng details:")
print(f"- Number of texts : {len(chunks)}")
print(f"- Embedding dimension: {len(embeddings.embed_query('test'))}")
print(f"- Database location: ./chroma_db")

query = "What is reinforcment learning?"
results = vectorstore.similarity_search(query, k=2)

print(f"Query: {query}")
print("\nTop 2 most relevant chunks:")
for i, doc in enumerate(results):
    print(f"\nResult {i+1}:")
    print(doc.page_content)
    print("-" * 30)


# Step 6: Set up RAG with Anthropic Claude
print("\nStep 6: Setting up RAG pipline")
print("-" * 50)


print("Using Anthropoic Claude mode with the provided API key")

# Initialze the LLM with Anthropic Claude
# llm = ChatAnthropic(
#     model="claude-3-5-soonet-20240620",
#     temperature=0.5
# )

# OpenAI
# if "OPENAI_API_KEY" in os.environ:
#     llm = OpenAI(
#         model="gpt-4",
#         temperature=0.5
#     )
# HuggingFace:
# if "HUGGINGFACEHUB_API_TOKEN" in os.environ:
# llm = HuggingFaceHub(
# repo_id="google/flan-t5-small",
# model_kwagrs = {"temperature":0.5,"max_length":512})
llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0.5
)
# response = llm.invoke("What is Artificial Intellgience?")
# print(response.content)

# Create the RAG pipeline
qa_chain = RetrievalQA.from_chain_type(
    llm = llm,
    chain_type = "stuff",
    retriever = vectorstore.as_retriever()
)

# Examples question to ask
questions = [
    "What is reinfrocement learining and how does it works?",
    "What are the main applications of computer vision?",
    "How is NLP used in real-world applications?"
]

print("\nAsking qustiions to our RAG system:")

for question in questions:
    print("\nQuestion:",question)
    try:
        answer = qa_chain.invoke(question)
        print("Answer: ",answer)
    except Exception as e:
        print("Error getting answer:",str(e))
