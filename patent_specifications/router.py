from fastapi import APIRouter, HTTPException, File, UploadFile, Form
from typing import Optional
from dotenv import load_dotenv
import openai
from config import get_openai_setting

load_dotenv()
router = APIRouter()

settings = get_openai_setting()
openai.api_key = settings.OPENAI_KEY

router = APIRouter(
    prefix="/patent-specification",
)

# 이미지와 텍스트 입력 받기 -> openai 
@router.post("", tags=['patent-specification'])
async def process_text_and_image(
    text: str = Form(...),
    image: Optional[UploadFile] = File(None)
):
    return text, image
    
"""
    # 텍스트 처리
    try:
        response = openai.Completion.create(
            engine="text-davinci-003", 
            prompt=text,
            max_tokens=50  
        )
        text_response = response.choices[0].text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    # 이미지 처리 (예시로 파일 이름 반환)
    image_filename = image.filename if image else "No image uploaded"
    
    return {"text_response": text_response, "image_info": image_filename}
"""
