from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from openpyxl import Workbook

service = Service('Users/woonmong/python/ChatGPT/chatGPT_test/과제/chromedriver.exe')
driver = webdriver.Chrome(service=service)

url = "https://book.interpark.com/bookPark/html/book.html"
driver.get(url)
time.sleep(1)

# 베스트셀러 탭으로 이동
element = driver.find_element(By.CLASS_NAME, 'gnbleft.n1')
element.click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 제목 저자 list
book_list = []

# 제목, 저자 정보 가져오기
search_results = soup.find_all('div', {'class': ['itemName', 'itemMeta']})

for result in search_results:
    title = result.find('strong')
    author = result.find('span', {'class': 'author'})
    company = result.find('span',{'class':'company'})
    
    if title:
        title_element = title.text.strip()
    elif author and company:
        author_element = author.text.strip()
        company_element = company.text.strip()
        # 중간 None 값을 걸러내기 위함
        book_list.append([title_element,author_element,company_element])
    else:
        print("error")

driver.quit()

# 추출한 도서 정보를 엑셀 파일로 저장
workbook = Workbook()
sheet = workbook.active
sheet.append(["제목", "저자","출판사"])

for book in book_list:
    sheet.append(book)

workbook.save("도서목록.xlsx")
workbook.close()