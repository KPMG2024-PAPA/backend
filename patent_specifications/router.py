from fastapi import APIRouter, HTTPException, File, UploadFile, Form
from typing import Optional
from dotenv import load_dotenv
import openai
from config import get_openai_setting

load_dotenv()
router = APIRouter()

settings = get_openai_setting()
openai.api_key = settings.OPENAI_KEY


# openAI 모델 호출, 텍스트 처리
@router.post("patent/process-text/")
async def process_text(text: str = Form(...)):
    return {text}
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=text,
            max_tokens=50  
        )
        return {"response": response.choices[0].text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    """
