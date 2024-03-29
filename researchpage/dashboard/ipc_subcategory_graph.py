import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import io
import base64

plt.matplotlib.rcParams['font.family'] = 'AppleGothic'

font_path_title = "./researchpage/dashboard/data/Pretendard-ExtraBold.ttf"
font_path_text = "./researchpage/dashboard/data/Pretendard-Medium.ttf"

ipc_application_subcategory = pd.read_csv('./researchpage/dashboard/data/ipc_application_subcategory.csv', index_col=0)

def ipc_subcategory_graph(ipc_subcategory: str) -> base64:  
   
   """
   gpt_classifier에서 A01과 같이 반환 받아
   ipc_application_category.csv의 ipc_subcategory에 그대로 입력하고
   base64로 인코딩된 이미지를 반환합니다.

   """
   custom_font_title = FontProperties(fname=font_path_title, size=20)
   custom_font_text = FontProperties(fname=font_path_text, size=10)
   
   patent_class = {'A01': ['농업', '임업', '축산', '수렵', '포획', '어업'],
 'A21': ['제빵；반죽 제조 또는 가공의 기계 혹은 설비；제빵용 반죽'],
 'A22': ['도살', '육처리', '가금 또는 어류의 처리'],
 'A23': ['식품 또는 식료품', '타류에 속하지 않는 그것들의 처리'],
 'A24': ['담배', '엽권담배', '지권담배', '흡연용구'],
 'A41': ['의류'],
 'A42': ['두의'],
 'A43': ['신발류'],
 'A44': ['장신구류', '귀금속보석류'],
 'A45': ['수지품 또는 여행용품'],
 'A46': ['브러시(Brush)제품'],
 'A47': ['가구', '가정용품', '가정용 설비', '커피 빻는 기구', '향신료 빻는 기구', '진공청소기 일반'],
 'A61': ['위생학', '의학 및 수의학'],
 'A62': ['인명구조', '소방'],
 'A63': ['운동', '놀이'],
 'B01': ['물리적 혹은 화학적 방법 또는 장치일반'],
 'B02': ['파쇄', '분쇄 또는 미분쇄', '제분을 위한 곡립의 전처리'],
 'B03': ['액체에 의하여 또는 풍력 테이블 또는 지그에 의하는 고체물질의 분리', '자기 또는 정전기에 의하는 분리'],
 'B04': ['물리적 또는 화학적 공정을 행하기 위한 원심장치 또는 기계'],
 'B05': ['무화 또는 분무일반', '액체 또는 타유동성 재료의 표면에의 적용일반'],
 'B06': ['기계적 진동의 발생 또는 전달일반'],
 'B07': ['고체상호의 분리', '선별'],
 'B08': ['청소'],
 'B09': ['고체폐기물 처리', '오염된 토양의 재생'],
 'B21': ['본질적으로 재료의 제거가 없는 기계적 금속가공', '금속의 펀칭'],
 'B22': ['주조', '분말야금'],
 'B23': ['공작기계', '딜리 분류되지 않는 금속가공'],
 'B24': ['연삭 연마'],
 'B25': ['수송구', '휴대용 동력 구동 공구', '휴대용 기구의 손잡이', '작업장 설비', '매니플레이터'],
 'B26': ['절단수공구', '절단', '절단기'],
 'B27': ['목재 또는 유사재료의 가공 또는 보존', '못박기 기계 또는 스테이플 기계 일반'],
 'B28': ['시멘트', '점토', '석재의 가공'],
 'B29': ['플래스틱의 가공', '가소상태 물질의 가공 일반'],
 'B30': ['프레스'],
 'B31': ['종이류 제품의 제조', '종이류의 가공'],
 'B32': ['적층체'],
 'B41': ['인쇄', '라이닝 장치', '타이프라이터', '스탬프'],
 'B42': ['제본', '앨범', '파일', '특수인쇄물'],
 'B43': ['필기용 또는 제도용기구', '책상 부속구'],
 'B44': ['장식기술'],
 'B60': ['차량 일반'],
 'B61': ['철도'],
 'B62': ['철도 이외의 노면차량'],
 'B63': ['선박 또는 그 밖의 물 위에 뜨는 구조물', '관련 의장품'],
 'B64': ['항공기', '비행', '우주공학'],
 'B65': ['운반', '포장', '저장', '얇거나 단섬유 부재의 취급'],
 'B66': ['견인장치', '양중장치', '권상장치'],
 'B67': ['병', '단지 또는 유사한 용기의 개봉 또는 밀봉', '액체의 취급'],
 'B68': ['마구', '충전물'],
 'B81': ['마이크로 구조기술'],
 'B82': ['나노기술'],
 'C01': ['무기화학'],
 'C02': ['물', '폐수', '하수 또는 오니(슬러지)의 처리'],
 'C03': ['유리', '광물 및 슬래그울(Slag wool)'],
 'C04': ['시멘트', '콘크리트', '인조석', '세라믹스', '내화물'],
 'C05': ['비료', '그 제조'],
 'C06': ['화학', '성냥'],
 'C07': ['유기화학'],
 'C08': ['유기고분자 화합물', '그 제조 또는 화학적 가공', '그에 따르는 조성물'],
 'C09': ['염료', '페인트', '광택제', '천연수지', '접착제', '여러 가지의 조성물', '재료의 응용'],
 'C10': ['석유', '가스 및 코크스공업', '일산화탄소를 함유하는 공업가스', '연료', '윤활제', '이탄'],
 'C11': ['동물성 및 식물성 유지방', '지방성물질 또는 왁스', '그것들로부터 유래된 지방산', '세정제', '양초'],
 'C12': ['생화학', '맥주', '주정', '포도주', '미생물학', '효소학', '돌연변이 또는 유전자 공학'],
 'C13': ['당 공업'],
 'C14': ['원피(skins)', '나피(hides)', '생피(pelts)', '유피(leather)'],
 'C21': ['철야금'],
 'C22': ['야금', '철 또는 비합철금', '합금의 처리 또는 비철금속의 처리'],
 'C23': ['금속재료의 피복',
  '금속피복재료',
  '화학적 표면처리',
  '금속질재료의 확산처리',
  '진공증착',
  '스퍼터링',
  '이온주입법 또는 화학 증착에 의한 피복 일반',
  '금속질재료의 방식 또는 이물질형성방지일반'],
 'C25': ['전기분해 또는 전기 영동방법', '그것을 위한 장치'],
 'C30': ['결정 성장'],
 'C40': ['조합된 기술'],
 'C99': ['섹션C중에서 그밖에 분류되지 않은 주제'],
 'D01': ['천연 또는 인조사 또는 섬유', '방적'],
 'D02': ['사', '사 또는 로프의 기계적 끝마무리', '정경 또는 빔권취'],
 'D03': ['제직'],
 'D04': ['부직포', '편물', '트리밍', '부직포', '레이스뜨기', '꼰끈'],
 'D05': ['봉제', '자수', '터프팅(tufting)'],
 'D06': ['섬유 또는 유사물의 처리', '세탁', '타류에 속하지 아니한 가소성 재료'],
 'D07': ['로프', '전기적인 것 이외의 케이블'],
 'D21': ['제지', '셀룰로스의 제조'],
 'E01': ['도로', '철도 또는 교량의 건설'],
 'E02': ['기초', '수공', '토사의 이송'],
 'E03': ['상수', '하수'],
 'E04': ['건축물'],
 'E05': ['자물쇠', '열쇠', '창 및 문의 부속품', '금고'],
 'E06': ['도어', '창', '셔터 또는 롤러', '블라인드 일반', '사다리'],
 'E21': ['지표 또는 암석의 굴착', '채광'],
 'F01': ['기계 또는 기관일반', '기계설비일반', '증기기관'],
 'F02': ['연소기관(열가스 또는 연소생성물을 이용하는 기관 설비)'],
 'F03': ['액체용 기계 또는 기관',
  '풍력원동기',
  '스프링원동기',
  '중력 원동기',
  '다른 종류에 속하지 않는 기계동력 또는 반동추진력을 발생하는 것'],
 'F04': ['액체용 용적형기계', '액체 또는 압축성 액체용 펌프'],
 'F15': ['유체압 액튜에이터', '수력학 또는 공기역학 일반'],
 'F16': ['기계요소 및 단위', '기계 또는 장치의 효과적 기능을 발휘하고 유지하기 위한 일반적 수단', '단열 일반'],
 'F17': ['가스 또는 액체의 저장 또는 분배'],
 'F21': ['조명'],
 'F22': ['증기발생'],
 'F23': ['연소장치', '연소방법'],
 'F24': ['가열', '레인지', '환기'],
 'F25': ['냉동 또는 냉각',
  '가열과 냉동을 조합한 시스템',
  '히트펌프 시스템',
  '얼음의 제조와 저장',
  '기체의 액화 또는 고체화'],
 'F26': ['건조'],
 'F27': ['노(furnace) 킬른(kiln)', '오븐(Oven) 또는 레토르트(Retort)'],
 'F28': ['열교환 일반'],
 'F41': ['무기'],
 'F42': ['탄약', '폭파'],
 'F99': ['섹션F중에서 그밖에 분류되지 않은 주제'],
 'G01': ['측정', '시험'],
 'G02': ['광학'],
 'G03': ['전자사진', '영화', '광파 이외의 파를 사용하는 유사기술', '영화', '사진', '홀로그래피'],
 'G04': ['시계 제작'],
 'G05': ['제어', '조정'],
 'G06': ['산술논리연산', '계산', '계수'],
 'G07': ['검사장치'],
 'G08': ['신호'],
 'G09': ['교육', '암호방법', '전시', '광고', '봉인'],
 'G10': ['악기', '음향'],
 'G11': ['정보저장'],
 'G12': ['기계의 세부'],
 'G16': ['특정의 용도 분야에 특히 적합한 정보통신기술'],
 'G21': ['핵공학'],
 'G99': ['섹션G중에서 그밖에 분류되지 않은 주제'],
 'H01': ['기본적 전기소자'],
 'H02': ['전력의 발전', '변환', '배전'],
 'H03': ['기본전자회로'],
 'H04': ['전기통신기술'],
 'H05': ['달리 분류되지 않는 전기기술'],
 'H10': ['반도체 장치', '달리 제공되지 않는 전기 고체 상태 장치']}
    
   plt.rcParams['axes.spines.top'] = False
   plt.rcParams['axes.spines.right'] = False
      
   # Plotting the time series data
   plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
   plt.plot(ipc_application_subcategory.index, ipc_application_subcategory[ipc_subcategory], marker='o', linestyle='-', color="#b57dfa")  # Replace 'column_name' with the name of the column you want to plot
   plt.title(f'소분류 {ipc_subcategory} 특허 출원 추이', fontproperties = custom_font_title)  # Add a title to the plot ;  fontweight='bold'; fontsize=30
   plt.text(0.5, 0.95, ", ".join(patent_class[ipc_subcategory]),ha='center', fontproperties = custom_font_text, transform=plt.gca().transAxes)
   plt.text(1, -0.1, "참고: IPSS 지식 재산 통계 서비스", ha='right', fontproperties = custom_font_text, transform=plt.gca().transAxes)
   plt.xlabel('연도', fontproperties = custom_font_text)  # Add a label to the x-axis
   plt.ylabel('소분류 출원 추이', fontproperties = custom_font_text)  # Add a label to the y-axis
   plt.xticks(fontproperties=custom_font_text)
   plt.yticks(fontproperties=custom_font_text) 
   # plt.grid(True)  # Add grid lines
   #  plt.show()
    
   img_bytes_io = io.BytesIO()
   plt.savefig(img_bytes_io, format='png')
   img_bytes_io.seek(0)
   plt.close()  # Close the plot to free up memory


   # Encode the image to base64
   img_base64 = base64.b64encode(img_bytes_io.getvalue()).decode()

   return img_base64
