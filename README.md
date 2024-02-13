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

```
.
├── README.md
├── __init__.py
├── __pycache__
│   ├── config.cpython-311.pyc
│   └── main.cpython-311.pyc
├── config.py
├── main.py
├── patent_specifications
│   ├── __pycache__
│   │   └── router.cpython-311.pyc
│   └── router.py
└── sql_database
    ├── __pycache__
    │   └── database.cpython-311.pyc
    ├── crud.py
    ├── database.py
    ├── models.py
    └── shcemas.py
```

6 directories, 13 files
