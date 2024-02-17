from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import urllib.request
from similarity.translation import korean_to_english
from similarity.gpt_func import IPC_filtering
from similarity.database import foreign_top_similarity, korea_top_similarity

app = FastAPI()

class SimilarityQuery(BaseModel):
    query: str
    n_results: int = 10

router = APIRouter(prefix="/similarity-check")

@router.post("")
def search_top_similarity(query_data: SimilarityQuery):
    try:
        korean_query = query_data.query
        n_results = query_data.n_results
        IPC_codes = IPC_filtering(korean_query)
        english_query = korean_to_english(korean_query)
        korean_results = korea_top_similarity(korean_query, n_results, IPC_codes)
        foreign_results = foreign_top_similarity(english_query, n_results, IPC_codes)

        return {"korean_results": korean_results, "foreign_results": foreign_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.include_router(router)
