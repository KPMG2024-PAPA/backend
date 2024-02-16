import requests
import xml.etree.ElementTree as ET


def get_dbpia_papers(search_keyword_list: list) -> list:
    """
    keyword extractor에서 반환 받은 keyword를 이용하여 dbpia에서 논문을 검색하는 함수
    [(날개, 0.3), (선풍기, 0.15), (다이슨, 0.05), (에너지,0.03)]
    그런데 keyword extractor에서 반환 받은 keyword가 많기 때문에 동시에 이걸 충족하는 논문이 없을 수 있음 (검색 결과 없음)
    따러서 안전하게 총 5개의 키워드를 반환해줬다면 5개씩 쪼개서 검색바에 넣을 것임.

    """
    # Adjusted to access attributes of Keyword objects
    search_keyword_comb = [
        kw.keyword for kw in search_keyword_list if kw.score > 0.3]

    # 10개 전부, 앞에 5개만, 짝수번째 키워드만, 홀수번째 키워드만

    for search_keyword in search_keyword_comb:

        # API endpoint URL
        url = f"""http://api.dbpia.co.kr/v2/search/search.xml?
        key=6e9ad922eabec9d9f549e8b5dfce765f	
        &target=se
        &searchall={search_keyword}
        &pyear=1 
        &itype=1
        &itype=2
        &itype=4 
        """
        # 최근의 1년만 불러오는 걸로 했음.
        # itype은 자료유형별 검색 중 1=학술저널 | 2=학술대회자료 | 3=전문잡지 | 4=연구보고서

        # Replace 'YOUR_API_KEY' with your actual API key
        # Add other query parameters as needed

        params = {
            "key": "6e9ad922eabec9d9f549e8b5dfce765f",
            "target": "se",  # Example parameter: search in all fields
            "searchall": {search_keyword},  # Your search query
            "pyear": "1",
            "itype": "1"
            # Add other parameters according to API documentation
        }

        # Make the GET request
        response = requests.get(url, params=params)
        # print(response)

        # Check if the request was successful

        if response.status_code == 200 and response.text[:7] != "<error>":

            # Process the XML response
            # print(response.text)  # This will print the raw XML data

            # Parse the XML
            root = ET.fromstring(response.text)

            # Find all item elements and extract titles and link_urls
            result = []

            # 모든 논문에 대한 모든 정보를 담을 리스트
            # [[title, publication_name, publication_date, link_url], [title, publication_name, publication_date, link_url], ...]

            for item in root.findall('.//item'):
                temp = []

                # Path to publication title
                title_element = item.find('title')
                title = title_element.text if title_element is not None else "No title"

                # Path to publication link
                link_url_element = item.find('link_url')
                link_url = link_url_element.text if link_url_element is not None else "No link"

                # Path to publication name
                publication_element = item.find('.//publication/name')
                publication_name = publication_element.text if publication_element.text is not None else "No publication name"

                # Path to publication date
                publication_date_element = item.find('.//issue/yymm')
                publication_date = publication_date_element.text if publication_date_element is not None else "No publication date"

                # DEBUGGER: Print the title and link_url
                # print(
                #     f"Title: {title.replace('<!HS>','').replace('<!HE>','')}")
                # print(
                #     f"Publication: {publication_name.replace('<!HS>','').replace('<!HE>','')}")
                # print(f"Publication Date: {publication_date}")
                # print(f"Link: {link_url}")

                temp.append(title.replace('<!HS>', '').replace('<!HE>', ''))
                temp.append(publication_name.replace(
                    '<!HS>', '').replace('<!HE>', ''))
                temp.append(publication_date)
                temp.append(link_url)

                result.append(temp)

            return result

        else:
            # print("Error:", response.status_code)

            search_keyword_comb.pop()


# print(get_dbpia_papers(['날개', '선풍기', '다이슨', '날개','소음', '발생', '무게', '전력', '소비', '에너지', '효율']))
# print(get_dbpia_papers("날개+선풍기+다이슨+날개+소음+발생+무게+전력+소비+에너지+효율"))
# print(get_dbpia_papers("에너지+날개+효율+전력+소음+선풍기+무게+소비+다이슨+발생"))

# print(get_dbpia_papers([('카메라', 0.5805), ('렌즈', 0.4405), ('무선', 0.4336), ('디지털', 0.4151),
#                         ('기기', 0.3814), ('방사', 0.3422), ('통신', 0.296), ('금속', 0.2955),
#                         ('촬영', 0.2681), ('물질', 0.2553)]))
