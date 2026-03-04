import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import pickle

# load dataset
df = pd.read_csv("../data/shl_catalog_full.csv")

# combine text fields
texts = (df["name"] + " " + df["description"]).fillna("").tolist()

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Generating embeddings...")

embeddings = model.encode(texts, show_progress_bar=True)

# create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# save index
faiss.write_index(index, "../embeddings/faiss_index.index")

# save metadata
with open("../embeddings/metadata.pkl", "wb") as f:
    pickle.dump(df.to_dict("records"), f)

print("Embeddings and FAISS index saved!")