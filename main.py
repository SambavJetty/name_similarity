from fastapi import FastAPI, Query
from pydantic import BaseModel
import google.generativeai as genai
import numpy as np
from typing import List, Tuple

# Configure API
genai.configure(api_key="AIzaSyAf7d_R-9AzJJMuHCI6eSeZbby2S26NP20")

# Init FastAPI app
app = FastAPI(title="Name Similarity API with Gemini")

# Names dataset
names = [
    "Geetha", "Gita", "Gitu", "Geeta", "Githa", "Geetika",
    "Anita", "Anitha", "Anita Devi", "Anitha Reddy",
    "Sita", "Seeta", "Sitara", "Sithara", "Seetha",
    "Rita", "Reeta", "Ritha", "Ritika", "Ritika Sharma",
    "Sunita", "Suneeta", "Sunitra", "Sunitha", "Sunitra Devi",
    "Kavita", "Kavitha", "Kavitha Rao", "Kavita Sharma", "Kaviya",
    "Lalita", "Lalitha", "Lalitha Devi", "Lalita Sharma"
]

# ====== Embedding Helper ======
def get_embeddings(texts, task_type="retrieval_document"):
    if isinstance(texts, str):
        texts = [texts]
    try:
        result = genai.embed_content(
            model="models/embedding-001",
            content=texts,
            task_type=task_type
        )
        return np.array(result['embedding'])
    except Exception as e:
        print(f"Embedding error: {e}")
        return np.zeros(768)

# ====== Precompute all name embeddings ======
name_embeddings = np.vstack([get_embeddings(name) for name in names])
name_embeddings = name_embeddings / np.linalg.norm(name_embeddings, axis=1, keepdims=True)


# ====== Core Similarity Function ======
def find_similar_names(query_name: str, top_k: int = 5) -> Tuple[Tuple[str, float], List[Tuple[str, float]]]:
    query_vector = get_embeddings(query_name, task_type="retrieval_query")
    query_vector = query_vector / np.linalg.norm(query_vector)

    similarities = np.dot(name_embeddings, query_vector.T).flatten()
    top_indices = np.argsort(-similarities)[:top_k]

    results = [(names[i], float(similarities[i])) for i in top_indices]
    return results[0], results


# ====== API Schema ======
class SimilarityRequest(BaseModel):
    name: str
    top_k: int = 5


# ====== Routes ======

@app.get("/")
def root():
    return {"message": "Welcome to the Name Similarity API using Gemini!"}


@app.post("/similar-names")
def get_similar_names(req: SimilarityRequest):
    best_match, ranked = find_similar_names(req.name, top_k=req.top_k)
    return {
        "input": req.name,
        "best_match": {"name": best_match[0], "score": round(best_match[1], 4)},
        "ranked_matches": [
            {"name": name, "score": round(score, 4)} for name, score in ranked
        ]
    }
