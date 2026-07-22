from langchain_chroma import Chroma
from app.embedding import get_embedding_model
def create_vector_store(chunks):
    embedding_model=get_embedding_model()
    vector_store=Chroma.from_documents(documents=chunks, embedding=embedding_model,persist_directory="db")
    return vector_store    