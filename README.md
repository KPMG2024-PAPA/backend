# KPMG backend
KPMG 2024 아이디어톤을 위한 백엔드
---
- 설치
    - `pip install "fastapi[all]"`
    - `pip install openai`
    - `pip install python-dotenv`

- 실행
    - 터미널에서 `uvicorn main:app --reload`를 실행
    - <http://127.0.0.1:8000/docs>에서 API 문서 확인 가능

"""
.
├── README.md
├── gpt
│   └── submit_gpt.py
├── main.py
├── researchpage
│   ├── dashboard
│   │   ├── data
│   │   │   ├── Pretendard-ExtraBold.ttf
│   │   │   ├── Pretendard-Medium.ttf
│   │   │   ├── ipc_application_category.csv
│   │   │   └── ipc_application_subcategory.csv
│   │   ├── gpt_classifier.py
│   │   ├── ipc_category_graph.py
│   │   └── ipc_subcategory_graph.py
│   ├── dashboard_func.py
│   ├── dbpia_api.py
│   ├── keybert_for_dashboard.py
│   └── naver_news.py
└── similarity
    ├── database.py
    ├── gpt_func.py
    ├── routers.py
    └── translation.py

6 directories, 18 files
"""
