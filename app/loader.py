from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from app.chunker import split_documents
from app.vectordb import create_vector_store

loader = PyPDFLoader("data/docs/Gen AI_assignment.pdf")

documents = loader.load()

chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

print("Vector Database Created Successfully!")