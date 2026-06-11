from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def chunk_text(text, chunk_size=1000):

    chunks = []

    for i in range(0, len(text), chunk_size):
        chunks.append(text[i:i + chunk_size])

    return chunks


def create_embeddings(chunks):

    return embedding_model.encode(chunks)


def retrieve_relevant_chunks(
    question,
    chunks,
    embeddings,
    top_k=5
):

    query_embedding = embedding_model.encode(
        [question]
    )[0]

    similarities = cosine_similarity(
        [query_embedding],
        embeddings
    )[0]

    top_indices = np.argsort(
        similarities
    )[-top_k:][::-1]

    return [
        chunks[i]
        for i in top_indices
    ]

import ollama


def answer_question(question, paper_text):

    chunks = chunk_text(paper_text)

    embeddings = create_embeddings(chunks)

    relevant_chunks = retrieve_relevant_chunks(
        question,
        chunks,
        embeddings
    )

    context = "\n\n".join(relevant_chunks)

    prompt = f"""
Answer the user's question using ONLY the information
provided in the context below.

If the answer is not found in the context,
say:
"I could not find that information in the paper."

Context:
{context}

Question:
{question}
"""
    print("\nRETRIEVED CONTEXT:\n")
    print(context[:2000])
    print("\n" + "=" * 50 + "\n")
    response = ollama.chat(
        model="gemma4:latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    print("\nFINAL ANSWER:")
    print(answer[:500])

    return answer