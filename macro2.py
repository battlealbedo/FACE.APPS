from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 웹 드라이버 설정
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # 전체화면으로 창 열기
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.megabox.co.kr/")  # 메가박스 기본 페이지로 이동

# 로그인 함수
def login(username, password):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@title='로그인']"))).click()  # 로그인 버튼 클릭
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ibxLoginId"))).send_keys(username)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "ibxLoginPwd"))).send_keys(password)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "btnLogin"))).click()  # 로그인 버튼 클릭

    # 비밀번호 변경 창이 뜨면 "다음에 하기" 버튼 클릭
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='button lyclose']"))).click()
    except:
        pass  # 비밀번호 변경 창이 뜨지 않으면 무시

# 날짜 변경 함수
def change_date(target_date):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "date-list")))
    date_buttons = driver.find_elements(By.CLASS_NAME, "date-area button")
    for button in date_buttons:
        if button.get_attribute("date-data") == target_date:
            button.click()
            break

# 메인 함수
def main():
    login("hjhj2932", "hjhj0903!!")
    WebDriverWait(driver, 20).until(EC.url_contains("https://www.megabox.co.kr/"))  # 로그인 완료 후 URL 확인
    driver.get("https://www.megabox.co.kr/theater/time?brchNo=0019")  # 지정된 URL로 이동
    change_date("2024.10.04")  # 원하는 날짜로 변경

    # 스크립트가 종료되지 않도록 대기
    input("브라우저를 종료하려면 엔터 키를 누르세요...")

if __name__ == "__main__":
    main()
