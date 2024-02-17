import urllib.request
import os
import json
from dotenv import load_dotenv

load_dotenv()

papago_client_id = os.getenv("PAPAGO_CLIENT_ID") # 개발자센터에서 발급받은 Client ID 값
papago_client_secret = os.getenv("PAPAGO_CLIENT_SECRET") # 개발자센터에서 발급받은 Client Secret 값
papago_url=os.getenv("PAPAGO_URL")


def korean_to_english(korean_query):
    encText = urllib.parse.quote(korean_query)
    data="source=ko&target=en&text=" + encText
    request = urllib.request.Request(papago_url)
    request.add_header("X-Naver-Client-Id",papago_client_id)
    request.add_header("X-Naver-Client-Secret",papago_client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_body = response_body.decode('utf-8')
        # print(response_body)
        
        parsed = json.loads(response_body)
        translated_text = parsed['message']['result']['translatedText']
        return translated_text
    else:
        print("Error Code:" + rescode)
