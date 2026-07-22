from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import ask_question

app = FastAPI()


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "RAG API is Running!"}


@app.post("/ask")
def ask(query: Query):
    answer = ask_question(query.question)
    return {
        "question": query.question,
        "answer": answer
    }