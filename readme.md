🤖 Local RAG System using Llama 3.2, Ollama, LangChain & ChromaDB

!Python !LangChain !Ollama !HuggingFace !ChromaDB

A Retrieval-Augmented Generation (RAG) application built using Llama 3.2, Ollama, LangChain, Hugging Face Embeddings, and ChromaDB.

This project allows users to ask questions about custom documents and receive relevant, context-aware answers using a locally running Large Language Model (LLM).

📌 Project Overview

Retrieval-Augmented Generation (RAG) combines information retrieval with generative AI.

Instead of relying only on the knowledge stored in an LLM, RAG retrieves relevant information from a custom knowledge base and provides that information to the LLM to generate more relevant responses.

This project implements a complete RAG pipeline using locally executed Llama 3.2.

🎯 Project Objectives
Understand the working principles of RAG.
Load different types of documents.
Convert documents into smaller text chunks.
Generate embeddings using Hugging Face.
Store embeddings in ChromaDB.
Retrieve relevant documents using similarity search.
Generate answers using Llama 3.2 through Ollama.
Build a locally running question-answering system.
🏗️ System Architecture

The following diagram illustrates the complete RAG architecture.

mermaid
flowchart TD

    A["📄 Input Document"] --> B["Text Splitter"]

    B --> C["Text Chunks"]

    C --> D["Hugging Face Embeddings"]

    D --> E["Vector Embeddings"]

    E --> F[("ChromaDB Vector Database")]

    G["👤 User Question"] --> H["Similarity Search"]

    F --> H

    H --> I["Relevant Document Chunks"]

    I --> J["LangChain RetrievalQA"]

    G --> J

    J --> K["Llama 3.2 via Ollama"]

    K --> L["💬 Generated Answer"]

    style A fill:#dbeafe,stroke:#2563eb,color:#111827
    style F fill:#dcfce7,stroke:#16a34a,color:#111827
    style K fill:#fef3c7,stroke:#d97706,color:#111827
    style L fill:#d1fae5,stroke:#059669,color:#111827

Architecture Explanation
Document Loading: Loads the input document containing information.
Text Splitting: Divides the document into smaller chunks.
Embedding Generation: Hugging Face converts text chunks into numerical vectors.
Vector Storage: ChromaDB stores the generated embeddings.
User Query: The user submits a question.
Similarity Search: ChromaDB retrieves the most relevant document chunks.
RetrievalQA: LangChain passes the retrieved context to the LLM.
Answer Generation: Llama 3.2 generates the final answer using retrieved context.
🛠️ Technologies Used
Technology	Purpose
Python 3.14	Programming language
LangChain	RAG framework
LangChain Core	Prompts, messages and runnable components
LangChain Community	Document loaders
LangChain Classic	Legacy chains such as RetrievalQA
LangChain Ollama	Ollama model integration
LangChain Hugging Face	Hugging Face embedding integration
LangChain Chroma	Chroma vector database integration
LangChain Text Splitters	Document splitting
Llama 3.2	Large Language Model
Ollama	Local LLM execution
Hugging Face	Text embeddings
all-MiniLM-L6-v2	Embedding model
ChromaDB	Vector database
Sentence Transformers	Embedding generation
📂 Project Structure
text
RAG/
│
├── main.py
│
├── chroma_db/
│   └── Vector database files
│
├── README.md
│
├── requirements.txt
│
├── .env
│
└── .gitignore

⚙️ Installation and Setup

Follow these steps to set up the complete RAG project on your local machine.

🗺️ Installation Workflow

The following diagram illustrates the complete installation and execution process.

mermaid
flowchart TD

    A["🐍 Install Python"] --> B["📁 Clone GitHub Repository"]

    B --> C["Create Virtual Environment"]

    C --> D["Install LangChain Packages"]

    D --> E["Install Document Loaders & Splitters"]

    E --> F["Install ChromaDB & Hugging Face"]

    F --> G["⚙️ Install Ollama"]

    G --> H["Download Llama 3.2"]

    H --> I["Load Hugging Face Embedding Model"]

    I --> J["Run main.py"]

    J --> K["📄 Load Documents"]

    K --> L["Generate Embeddings"]

    L --> M["Store Vectors in ChromaDB"]

    M --> N["💬 Ask Questions"]

    N --> O["Retrieve Relevant Context"]

    O --> P["Generate Answer using Llama 3.2"]

    style A fill:#dbeafe,stroke:#2563eb,color:#111827
    style G fill:#fef3c7,stroke:#d97706,color:#111827
    style M fill:#dcfce7,stroke:#16a34a,color:#111827
    style P fill:#d1fae5,stroke:#059669,color:#111827

1. Clone the Repository
bash
git clone https://github.com/bibekpandey0521/RAG.git


Navigate to the project directory:

bash
cd RAG

2. Install Python

Download Python:

https://www.python.org/downloads/

Check the installed Python version:

bash
python --version


This project was developed using Python 3.14.

3. Create a Virtual Environment
bash
python -m venv venv


Activate the environment on Windows:

bash
venv\Scripts\activate

4. Install LangChain Packages

This project uses the LangChain 1.x package architecture.

Install the main LangChain packages:

bash
python -m pip install -U langchain langchain-core langchain-classic langchain-community


Install model integrations:

bash
python -m pip install -U langchain-ollama langchain-huggingface


Install ChromaDB and text processing packages:

bash
python -m pip install -U langchain-chroma langchain-text-splitters chromadb sentence-transformers


Install document loader dependencies:

bash
python -m pip install -U pypdf beautifulsoup4 pymupdf4llm


Install additional utilities:

bash
python -m pip install -U python-dotenv


Optional: Install Anthropic integration if you want to use Claude:

bash
python -m pip install -U langchain-anthropic

5. Install Everything Using requirements.txt

Create a requirements.txt file in your project directory.

Add the following dependencies:

text
langchain
langchain-core
langchain-classic
langchain-community
langchain-ollama
langchain-huggingface
langchain-chroma
langchain-text-splitters
chromadb
sentence-transformers
pypdf
beautifulsoup4
pymupdf4llm
python-dotenv


Install all dependencies using one command:

bash
python -m pip install -r requirements.txt


Optional Anthropic integration:

bash
python -m pip install langchain-anthropic

6. Verify LangChain Installation

Check all installed LangChain packages:

bash
python -m pip list | findstr langchain


Check individual package versions:

bash
python -m pip show langchain
python -m pip show langchain-core
python -m pip show langchain-classic
python -m pip show langchain-community
python -m pip show langchain-ollama
python -m pip show langchain-huggingface
python -m pip show langchain-chroma
python -m pip show langchain-text-splitters

7. Install Ollama

Download and install Ollama:

https://ollama.com/download

Verify installation:

bash
ollama --version

8. Download Llama 3.2

Download the Llama 3.2 model:

bash
ollama pull llama3.2


Check installed models:

bash
ollama list


Expected output:

text
NAME              ID              SIZE
llama3.2:latest   <model-id>      2.0 GB


Test the model:

bash
ollama run llama3.2


Ask a simple question:

text
Hello, how are you?

9. Configure Hugging Face Embeddings

This project uses the following embedding model:

text
sentence-transformers/all-MiniLM-L6-v2


Install the embedding integration:

bash
python -m pip install -U langchain-huggingface sentence-transformers


Example:

python
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


The model will download automatically when initialized for the first time.

An internet connection is required for the initial download unless the model is already cached locally.

10. Configure Environment Variables (Optional)

If you want to use Anthropic Claude, create a .env file:

env
ANTHROPIC_API_KEY=your_anthropic_api_key


Load the API key:

python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("ANTHROPIC_API_KEY")


Note: Anthropic is optional. The main RAG project uses Ollama and does not require an Anthropic API key.

11. Run the Project

Make sure Ollama is running and the Llama model is available.

Execute:

bash
python main.py


The application will:

Load the input document.
Split the document into chunks.
Generate embeddings using Hugging Face.
Store vectors in ChromaDB.
Retrieve relevant information.
Generate answers using Llama 3.2 through Ollama.
🧠 Models Used
1. Llama 3.2

Llama 3.2 is used as the Large Language Model (LLM).

Purpose:

Understand user questions.
Process retrieved document context.
Generate natural language answers.
Run locally using Ollama.

Model:

text
llama3.2:latest


Initialize using LangChain:

python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2:latest",
    temperature=0.7
)

2. Hugging Face Embedding Model

Model:

text
sentence-transformers/all-MiniLM-L6-v2


Purpose:

Convert text into numerical vector representations.
Identify semantically similar documents.
Support efficient similarity searching.

Initialize using LangChain:

python
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

📄 Document Loading

LangChain Community provides different document loaders for extracting information from various file formats.

This project can use different document loaders depending on the input file.

Document Type	Loader	Import
PDF	PyPDFLoader	langchain_community.document_loaders
CSV	CSVLoader	langchain_community.document_loaders
HTML	BSHTMLLoader	langchain_community.document_loaders
Text	TextLoader	langchain_community.document_loaders
Website	WebBaseLoader	langchain_community.document_loaders

Example PDF loader:

python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Docker.pdf")

pages = loader.load()

print(pages[0].page_content)


Example CSV loader:

python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("data.csv")

documents = loader.load()

print(documents[0].page_content)


Example HTML loader:

python
from langchain_community.document_loaders import BSHTMLLoader

loader = BSHTMLLoader("test.html")

documents = loader.load()

print(documents[0].page_content)

🔄 RAG Workflow

The application follows two major stages.

Stage 1: Document Indexing
Load the document.
Split the document into smaller chunks.
Generate embeddings for each chunk.
Store embeddings in ChromaDB.
Stage 2: Retrieval and Generation
Accept a user question.
Search for relevant document chunks.
Retrieve the most relevant context.
Pass the context to Llama 3.2.
Generate the final answer.
💬 Example Questions

The RAG system can answer questions such as:

What is reinforcement learning and how does it work?
What are the main applications of computer vision?
How is NLP used in real-world applications?
What is Artificial Intelligence?
How does a machine learning agent learn?
What is Docker and how does containerization work?
Example Output

Question:

What is reinforcement learning and how does it work?

Answer:

Reinforcement Learning is a type of machine learning in which an agent learns by interacting with its environment and receiving rewards or penalties. It improves its decisions through experience and is commonly used in robotics, gaming, and autonomous systems.

✨ Key Features
Local LLM execution using Ollama.
Document-based question answering.
Multiple document loader support.
Semantic search using vector embeddings.
Persistent vector storage with ChromaDB.
Context-aware answer generation.
Hugging Face embedding integration.
No OpenAI or Anthropic API key required for the local setup.
Retrieval of relevant source documents.
🚀 Future Improvements
Support PDF and DOCX document uploads.
Build an interactive chatbot interface using Streamlit.
Support multiple documents.
Add conversation memory using modern LangChain APIs.
Implement document citation and source tracking.
Improve retrieval using hybrid search.
Build a web-based RAG chatbot.
🔐 Privacy

This project uses a locally running Llama model through Ollama.

Documents and questions are processed locally by the application, while the Hugging Face embedding model may need an initial internet connection to download its model files.

No Anthropic or OpenAI API key is required for the local Ollama-based setup.

📚 Useful Resources
Python Documentation
LangChain Documentation
Ollama Documentation
Hugging Face
ChromaDB Documentation
Sentence Transformers
👨‍💻 Author

Your Name

GitHub: https://github.com/bibekpandey0521

📜 License

This project is intended for educational and learning purposes.

⭐ If you find this project useful, consider giving it a star on GitHub!