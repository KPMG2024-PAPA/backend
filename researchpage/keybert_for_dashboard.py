# !pip install keybert
# !pip install kiwipiepy
from keybert import KeyBERT
from kiwipiepy import Kiwi
from transformers import BertModel
import json


def keyword_extractor(input: str) -> list:
    """

    유저가 검색을 위해서 텍스트를 입력하면, 명사 위주로 키워드를 추출하여 키워드+키워드+키워드 형태로 반환합니다.

    예시:
    날개가 없는 선풍기를 만들고 있습니다. 다이슨과 같이 날개가 없어 소음이 적게 발생하고 무게가 가벼워집니다. 또한, 전력 소비가 줄어들어 에너지 효율이 높아집니다. 

    위와 같은 문장은 다음과 같이 결과가 나오게 됩니다.

    [(날개, 0.3), (선풍기, 0.5), (다이슨, 0.2)...]

    """

    text = input

    # text="""
    # 날개가 없는 선풍기를 만들고 있습니다. 다이슨과 같이 날개가 없어 소음이 적게 발생하고 무게가 가벼워집니다. 또한, 전력 소비가 줄어들어 에너지 효율이 높아집니다.
    # """

    # text = """
    # 빠르게 충전되는 2차 전지 제품을 개발하고 있습니다. 이 제품은 자동차용 충전식 배터리로, 72시간 이상 지속될 수 있습니다. 또한 배터리의 크기는 배낭보다도 작습니다.
    # """

    model = BertModel.from_pretrained('skt/kobert-base-v1')
    kw_model = KeyBERT(model)

    kiwi = Kiwi()

    def noun_extractor(text):
        results = []
        result = kiwi.analyze(text)
        for token, pos, _, _ in result[0][0]:
            if len(token) != 1 and pos.startswith('N') or pos.startswith('SL'):
                results.append(token)
        return results

    nouns = noun_extractor(text)
    nouns

    nouns_text = ' '.join(nouns)

    stop_words = [
        "발명", "발명품", "제품", "제품을", "상품", "상품을",
        "것", "이것", "저것",
        "우리", "너", "당신",
        "그리고", "하지만", "그러나",
        "있다", "없다",
        "되다", "하다",
        "사용", "사용하는",
        "가능", "가능한",
        "통해", "을 통해",
        "대한", "에 대한",
        "이러한", "저러한",
        "때문에", "때문",
        "구성", "구성된",
        "기술", "기술적",
        "결과", "결과적",
        "이용", "이용한",
        "제공", "제공하는",
        "시스템", "시스템을",
        "다양한", "여러",
        "관련", "관련된",
        "문제", "문제를",
        "해결", "해결하기",
        "목적", "목적으로",
        "이유", "이유로",
        "사례", "사례를",
        "방법", "방법으로",
        "이후", "이후에"

    ]

    keywords = kw_model.extract_keywords(
        nouns_text, keyphrase_ngram_range=(1, 1), stop_words=stop_words, top_n=10)

    # Convert the list of tuples to a list of dictionaries for JSON serialization
    keywords_list = [{"keyword": kw, "score": score} for kw, score in keywords]

    json_string = json.dumps(keywords_list)

    return json_string


# print(keyword_extractor("날개가 없는 선풍기를 만들고 있습니다. 다이슨과 같이 날개가 없어 소음이 적게 발생하고 무게가 가벼워집니다. 또한, 전력 소비가 줄어들어 에너지 효율이 높아집니다."))
# print(keyword_extractor("본 발명의 일 실시예에 따른 외부 기기와의 무선 통신을 수행할 수 있는 디지털 카메라에 있어서, 카메라 본체 및 카메라 본체에 장착되며, 복수의 촬영 렌즈들을 수용하는 복수의 배럴들을 가진 렌즈 배럴 조립체를 포함하며, 복수의 배럴들 중 어느 하나는 무선 통신을 위한 안테나 기능을 가진 안테나 배럴로 사용되며, 안테나 배럴이 안테나 기능을 수행하기 위한 전파를 방사할 수 있도록, 안테나 배럴은 금속 물질로 이루어지고 안테나 배럴에는 유전체 물질로 채워진 적어도 하나의 슬릿이 형성되며, 안테나 배럴의 외측 표면을 둘러싸는 카메라 본체의 외부 케이싱 부분은, 안테나 배럴의 그라운드로 기능하도록 금속 물질로 이루어지는 것을 특징으로 한다."))
