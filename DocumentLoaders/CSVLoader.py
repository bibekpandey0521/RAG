from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(r"C:\Users\bibek.pandey\Downloads\Survey.csv")
data = loader.load()
# print(data)
print(type(data))
# print(data[0])
print(data[1])