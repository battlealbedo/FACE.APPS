import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import datetime
import random
import telepot

# 텔레봇 설정
token = "7240374983:AAFEAeYlxEFLIaUzeGRVT-OumAk7FjLbIhA"  # 텔레봇 토큰
mc = "7265170310"  # 공개방
bot = telepot.Bot(token)

# 영화 및 날짜 설정
movie = "룩백"
date = "20240910"

# 사용자 에이전트 설정
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1'
option = webdriver.FirefoxOptions()
option.add_argument("--headless")  # 헤드리스 모드 설정
option.set_preference('general.useragent.override', user_agent)
driver = webdriver.Firefox(options=option)

# 코엑스 메가박스 URL
megabox_url = "https://m.megabox.co.kr/booking/theater?brchNo=1351"

# 메가박스 극장 정보 추출
headers = {'User-Agent': user_agent}
retry_count = 5

for _ in range(retry_count):
    try:
        response = requests.get(megabox_url, headers=headers)
        response.raise_for_status()  # HTTP 에러가 발생하면 예외를 발생시킴
        soup = BeautifulSoup(response.text, 'html.parser')
        theater_info = soup.find_all('li', {'class': 'theater-item'})
        break
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}. Retrying...")
        time.sleep(2)
else:
    print("Failed to retrieve Megabox theater information after several attempts.")
    theater_info = []

# 모든 메가박스 극장 정보 출력
for theater in theater_info:
    print(theater.text.strip())

while True:
    # 메가박스 오픈 체크
    driver.get("https://m.megabox.co.kr/booking/theater?brchNo=1351")  # 메가박스 URL로 이동
    time.sleep(5)  # 페이지 로드 대기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select("div.theater-group")  # 선택자 수정
    for title in titles:
        a = title.text.strip().replace("\n", "")
        print(a)
        title_check = (movie in a)
        mx4d_check = ("7관" in a)
        if title_check and mx4d_check:  # MX4D
            open_check = ("준비중" not in a)
            if open_check:
                bot.sendMessage(mc, "빅토리 MX4D 오픈!")
                print("open")
            else:
                if not ready_printed:
                    print("준비중")
                    bot.sendMessage(mc, "오픈준비중!!! 오픈알림 기다리지 말고 미리 들가서 날짜 계속 클릭해서 새로고침 추천")
                    ready_printed = True

    now = datetime.datetime.now()
    print(now)
    time.sleep(random.uniform(30, 32))
    driver.refresh()
    time.sleep(random.uniform(1, 2))