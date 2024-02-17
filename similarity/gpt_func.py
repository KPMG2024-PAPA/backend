import re
import os
import ast 
import time
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

api_base = os.getenv("API_BASE_URL")
api_key = os.getenv("API_KEY")
deployment_name = os.getenv("DEPLOYMENT_NAME")
api_version = os.getenv("API_VERSION")

client = AzureOpenAI(
    api_key=api_key,  
    api_version=api_version,
    base_url=f"{api_base}/openai/deployments/{deployment_name}"
)


def call_gpt_code(input_text):
    prompt = """
        Accurately identify specific IPC Codes of given patent abstract up to three. If you cannot find specific IPC Codes, provide the most relevant codes as the answer. 
        Answer as a format of 'IPC Code: {IPC code 1, 2, 3}'
        """
    response = client.chat.completions.create(
        model=deployment_name,
        messages=[
            { "role": "system", 
              "content": prompt },
            { "role": "user", "content": [{"type": "text", "text": input_text}] } 
        ],
        max_tokens=1000 
    )
    # 응답에서 정보 추출
    answer = response.choices[0].message.content
    return answer


### functions required ###
def extract_codes(response_text):
    code_pattern = r"([A-Z]\d{2}[A-Z])"
    codes = re.findall(code_pattern, response_text)
    return codes


def IPC_filtering(query: str):
    # IPC 코드 추출
    answer = call_gpt_code(query)
    input_codes = extract_codes(answer)

    return input_codes
    
    

