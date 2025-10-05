import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime
import random
import telepot
import re  # 숫자 추출을 위한 정규식

# 텔레봇 설정
token = "7240374983:AAFEAeYlxEFLIaUzeGRVT-OumAk7FjLbIhA"
mc = "7265170310"
bot = telepot.Bot(token)

# 감지하고 싶은 날짜 (숫자만 기준으로 감지)
target_day = "15"

# 사용자 에이전트 설정
user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1'
option = webdriver.FirefoxOptions()
option.add_argument("--headless")
option.set_preference('general.useragent.override', user_agent)
driver = webdriver.Firefox(options=option)

# 코엑스 메가박스 URL
megabox_url = "https://m.megabox.co.kr/booking/"
headers = {'User-Agent': user_agent}
retry_count = 5

for _ in range(retry_count):
    try:
        response = requests.get(megabox_url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        theater_info = soup.find_all('li', {'class': 'theater-item'})
        break
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}. Retrying...")
else:
    print("Failed to retrieve Megabox theater information.")
    theater_info = []

# 극장 정보 출력
for theater in theater_info:
    print(theater.text.strip())

# 루프 시작
while True:
    driver.get("https://m.megabox.co.kr/booking/theater?brchNo1=0068&brchDirectAt=Y")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#playDateList .item"))
    )

    date_elements = driver.find_elements(By.CSS_SELECTOR, "#playDateList .item")
    for element in date_elements:
        date_text = element.text.strip().replace("\n", "")
        numbers_only = re.sub(r"[^0-9]", "", date_text)

        print(f"[디버그] 원래 텍스트: '{element.text.strip()}'")
        print(f"[디버그] 줄바꿈 제거 후: '{date_text}'")
        print(f"[디버그] 숫자만 추출: '{numbers_only}'")

        # 숫자 기준 날짜 오픈 체크
        if numbers_only == target_day:
            bot.sendMessage(mc, f"{target_day}일 날짜 오픈됨!")
            print("날짜 오픈 확인")

    now = datetime.datetime.now()
    print(now)
    time.sleep(random.uniform(9, 11))
    driver.refresh()
    time.sleep(random.uniform(1, 2))