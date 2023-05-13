from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, requests
from bs4 import BeautifulSoup

service = Service('Users/woonmong/python/ChatGPT/chatGPT_test/과제/chromedriver.exe') # Chrome 드라이버 경로 지정
driver = webdriver.Chrome(service=service) # Service 객체 사용하여 드라이버 실행

url = "https://www.google.com/"
driver.get(url)
time.sleep(1)

# search keyword "python"
element = driver.find_element(By.ID,"APjFqb")
element.send_keys("python")
time.sleep(1)
# Press Enter Key
element.send_keys(Keys.RETURN)
time.sleep(1)

# 검색 결과 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
results = []

# 검색 결과에서 제목 및 링크 추출
search_results = soup.find_all('div', {'class': 'g'})
for result in search_results:
    title = result.find('h3').text
    link = result.find('a')['href']
    results.append((title, link))

for data in results:
    print(data)

