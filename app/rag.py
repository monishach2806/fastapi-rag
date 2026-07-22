from dotenv import load_dotenv

load_dotenv()
import os
from google import genai
from app.retriever import get_retriever

# Gemini Client
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def ask_question(question):
    # Get retriever
    retriever = get_retriever()

    # Retrieve relevant documents
    docs = retriever.invoke(question)

    # Combine retrieved chunks
    context = "\n\n".join(doc.page_content for doc in docs)

    # Prompt
    prompt = f"""
You are a helpful AI assistant.

Answer the user's question ONLY using the context provided below.
If the answer is not present in the context, reply:
"I don't know based on the provided context."

Context:
{context}

Question:
{question}
"""

    # Generate answer using Gemini
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    question = "What is the objective of this assignment?"
    answer = ask_question(question)
    print(answer)