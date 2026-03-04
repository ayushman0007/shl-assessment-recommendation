from fastapi import FastAPI
from pydantic import BaseModel
from retrieval.retrieve import search_assessments

app = FastAPI()

class QueryRequest(BaseModel):
    query: str


@app.get("/health")
def health():
    return {"status": "API is running"}


@app.post("/recommend")
def recommend(request: QueryRequest):

    results = search_assessments(request.query)

    output = []

    for r in results:
        output.append({
            "assessment_name": r["name"],
            "url": r["url"]
        })

    return {"recommended_assessments": output}

import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("api.main:app", host="0.0.0.0", port=port)