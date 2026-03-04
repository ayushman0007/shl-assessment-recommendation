import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

index_path = os.path.join(BASE_DIR, "embeddings", "faiss_index.index")
metadata_path = os.path.join(BASE_DIR, "embeddings", "metadata.pkl")

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(index_path)

with open(metadata_path, "rb") as f:
    metadata = pickle.load(f)


def search_assessments(query, top_k=10):

    query_vector = model.encode([query])

    distances, indices = index.search(np.array(query_vector), top_k)

    results = [metadata[i] for i in indices[0]]

    return results


if __name__ == "__main__":

    query = input("Enter query: ")

    results = search_assessments(query)

    for r in results:
        print(r["name"], r["url"])