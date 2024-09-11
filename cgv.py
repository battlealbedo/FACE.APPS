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

movie = "바이크"
date = "20240925"
url = f"https://m.cgv.co.kr/WebApp/Reservation/schedule.aspx?tc=0013&rc=01&ymd={date}&fst=&fet=&fsrc="

user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1'
option = webdriver.FirefoxOptions()
option.add_argument("--headless")  # 헤드리스 모드 설정
option.set_preference('general.useragent.override', user_agent)
driver = webdriver.Firefox(options=option)
# cgv 접속
driver.get(url)
time.sleep(1)
driver.refresh()
time.sleep(1)
ready_printed = False
while True:
    # 오픈 체크
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select("li")
    for title in titles:
        a = title.text.strip().replace("\n", "")
        print(a)
        title_check = (movie in a)
        # 특정 관만 체크 (예: movie)
        if title_check:
            open_check = ("준비중" not in a)
            if open_check:
                bot.sendMessage(mc, "바이크 라이더스 오픈!")
                print("open")
            else:
                if not ready_printed:
                    print("준비중")
                    bot.sendMessage(mc, "바이크 라이더스 오픈준비중!!! 오픈알림 기다리지 말고 미리 들어가서 날짜 계속 클릭해서 새로고침 추천")
                    ready_printed = True
    now = datetime.datetime.now()
    print(now)
    time.sleep(random.uniform(30, 32))
    driver.get(url)
    time.sleep(random.uniform(1, 2))