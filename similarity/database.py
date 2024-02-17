from fastapi import FastAPI
from fastapi import APIRouter
from typing import List
import chromadb
import ast
from sentence_transformers import SentenceTransformer

# ChromaDB 클라이언트 설정
client = chromadb.HttpClient(host="localhost", port=8888)
korean_patents = client.get_collection(name="korean_patents")
foreign_patents = client.get_collection(name="foriegn_patents")
korean_model = SentenceTransformer('snunlp/KR-SBERT-V40K-klueNLI-augSTS')
foreign_model = SentenceTransformer('AI-Growth-Lab/PatentSBERTa')


def korea_top_similarity(query: str, n_results: int,  IPCs: List[str] = []):

    query_embedding = korean_model.encode(query).tolist()
    unique_IPCs = list(set(IPCs))

    result = korean_patents.query(
        query_embeddings=[query_embedding],
        n_results=n_results+100,
    )


    # 검색 결과 반환
    ids = result.get('ids', [[]])[0]
    distances = result.get('distances', [[]])[0]
    metadatas = result.get('metadatas', [[]])[0]
    IPC_codes = [ast.literal_eval(metadata.get('IPC_code_only')) for metadata in metadatas]


    # 필터링된 결과를 저장할 리스트 초기화
    filtered_results = []

    # metadatas를 순회하며 필터링 조건에 맞는 문서 선택
    for id, distance, IPC_code, metadata in zip(ids, distances, IPC_codes, metadatas):
        # IPC_code 리스트와 unique_IPCs 리스트의 교집합이 있는지 확인
        if any(ipc in unique_IPCs for ipc in IPC_code):
            # 아래 지수누나가 원하는 칼럼 넘겨주면 됨
            filtered_results.append({
                "id": id,
                "distance": distance,
                "IPC_code_only": metadata.get('IPC_code_only'),
                "요약": metadata.get('요약')
            })
    
    # 필터링된 결과 중 상위 5개만 선택
    top_filtered_results = filtered_results[:n_results]

    return {"results": top_filtered_results}



def foreign_top_similarity(query: str, n_results: int,  IPCs: List[str] = []):
    # 사용자 입력을 임베딩
    query_embedding = foreign_model.encode(query).tolist()
    unique_IPCs = list(set(IPCs))

    result = foreign_patents.query(
        query_embeddings=[query_embedding],
        n_results=n_results+100,
    )

    # 검색 결과 반환
    ids = result.get('ids', [[]])[0]
    distances = result.get('distances', [[]])[0]
    metadatas = result.get('metadatas', [[]])[0]
    IPC_codes = [metadata.get('ipc_category') for metadata in metadatas]


    # 필터링된 결과를 저장할 리스트 초기화
    filtered_results = []

    # metadatas를 순회하며 필터링 조건에 맞는 문서 선택
    for id, distance, IPC_code, metadata in zip(ids, distances, IPC_codes, metadatas):
        # IPC_code 리스트와 unique_IPCs 리스트의 교집합이 있는지 확인
        if any(ipc in unique_IPCs for ipc in IPC_code):
            # 아래 지수누나가 원하는 칼럼 넘겨주면 됨
            filtered_results.append({
                "id": id,
                "distance": distance,
                "IPC_category": metadata.get('ipc_category'),
                "요약": metadata.get('요약')
            })
    
    # 필터링된 결과 중 상위 5개만 선택
    top_filtered_results = filtered_results[:n_results]

    return {"results": top_filtered_results}
