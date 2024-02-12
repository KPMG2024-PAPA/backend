from fastapi import FastAPI
from pydantic import BaseModel
from sql_database.database import engineconn
import uvicorn
from patent_specifications.router import router as patent_router

app = FastAPI()

engine = engineconn()
session = engine.create_session()

app.include_router(patent_router)

@app.get("/test")
def test():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

