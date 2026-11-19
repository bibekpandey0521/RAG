# pip install beautifulsoup4
# pip install -U lxml


from langchain_community.document_loaders import BSHTMLLoader

loader=BSHTMLLoader(r"C:\Users\bibek.pandey\Downloads\Test.html")

data = loader.load()

print(data)