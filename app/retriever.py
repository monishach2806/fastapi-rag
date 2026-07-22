from dotenv import load_dotenv

load_dotenv()

from langchain_chroma import Chroma
from app.embedding import get_embedding_model
def get_retriever():
    embedding_model=get_embedding_model()
    vector_store=Chroma(persist_directory="db",embedding_function=embedding_model)
    retriever=vector_store.as_retriever(search_kwargs={"k":3})
    return retriever
if __name__ == "__main__":
    retriever = get_retriever()

    docs = retriever.invoke("What is the objective of this assignment?")

    print(docs[0].page_content)