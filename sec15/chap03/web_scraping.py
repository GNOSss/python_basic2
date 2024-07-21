import requests
from bs4 import BeautifulSoup


url = "https://news.naver.com/section/101"
response = requests.get(url)
html = response.text


# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# 페이지 제목 및 header 안의 h1 요소 찾기
page_title = soup.title.text
header_h1 = soup.header.h1.text

# id가 info인 section 안의 div 요소들 파싱
info_section_divs = soup.find('section', id='info').find_all('div', recursive=False)

pass