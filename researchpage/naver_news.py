from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import numpy as np
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
# print(selenium.__version__)

from bs4 import BeautifulSoup
import requests


def naver_news(input: list) -> list:
    """

    keyword extractor에서 반환 받은 [(날개, 0.3), (선풍기, 0.15), (다이슨, 0.05), (에너지,0.03)]에서
    스코어가 0.3 이상인 것만 네이버에서 뉴스을 검색하는 함수
    그런데 keyword extractor에서 반환 받은 keyword가 많기 때문에 동시에 이걸 충족하는 뉴스가 없을 수도 있음 주의(검색 결과 없음)

    """

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    
    percentile_60 = np.percentile([i[1] for i in input],60)
    search_keyword = "+".join([i[0] for i in input if i[1] >= percentile_60])

    url = f'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={search_keyword}+특허'
    driver.get(url)
    driver.maximize_window()  # 브라우저의 크기 전체화면으로 확대
    driver.implicitly_wait(3)
    # 계속 403 오류가 나기 때문에 해더 추가
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

    SCROLL_PAUSE_SEC = 1

    time.sleep(SCROLL_PAUSE_SEC)

    for _ in range(5):

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_SEC)

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    title_info = soup.find_all('a', attrs={'class': 'news_tit'})

    title_link = []

    for i in range(len(title_info)):
        temp = []
        temp.append(title_info[i].get_text())
        temp.append(title_info[i]['href'])
        title_link.append(temp)

    return title_link


print(naver_news([('카메라', 0.5805), ('렌즈', 0.4405), ('무선', 0.4336), ('디지털', 0.4151), 
                        ('기기', 0.3814), ('방사', 0.3422), ('통신', 0.296), ('금속', 0.2955), 
                        ('촬영', 0.2681), ('물질', 0.2553)]))