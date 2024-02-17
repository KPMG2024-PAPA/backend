from fastapi import FastAPI, APIRouter, HTTPException
from typing import List
from similarity.gpt_func import IPC_filtering
from similarity.database import foreign_top_similarity, korea_top_similarity

app = FastAPI()


router = APIRouter(
    prefix="/similarity-check",
)

@router.post("")
async def search_top_similarity(query:str, n_results: int = 10):
    
    try:
        # 한국 특허 1차 필터링
        IPC_codes = IPC_filtering(query)
        # 위에 필터링 된 데이터 기준으로, 유사도 상위 n_results개 반환
        korean_results =  korea_top_similarity(query, n_results, IPC_codes)
        # 위에 필터링 된 데이터 기준으로, 유사도 상위 n_results개 반환
        foreign_results = foreign_top_similarity(query, n_results, IPC_codes)

        return korean_results, foreign_results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
