from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    r"C:\Users\bibek.pandey\Downloads\Docker.pdf",
    extraction_mode="layout"
)

pages = loader.load()

print(type(pages))

print(pages[0].page_content)