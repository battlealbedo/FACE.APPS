from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 웹 드라이버 설정
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.cgv.co.kr/user/login/")  # 로그인 페이지로 직접 이동

# 팝업 닫기
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn_close"))).click()
except:
    pass

# 로그인
def login(username, password):
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "txtUserId"))).send_keys(username)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "txtPassword"))).send_keys(password)
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "submit"))).click()

# 메인 함수
def main():
    login("hjhj2932", "jhjh0903!")
    WebDriverWait(driver, 20).until(EC.url_contains("https://www.cgv.co.kr/"))  # 로그인 완료 후 URL 확인
    driver.get("http://www.cgv.co.kr/theaters/default.aspx?areacode=01&theaterCode=0013&date=20241002")  # 지정된 URL로 이동

    # 스크립트가 종료되지 않도록 대기
    input("브라우저를 종료하려면 엔터 키를 누르세요...")

if __name__ == "__main__":
    main()
