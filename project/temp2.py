import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


url = f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&ssc=tab.nx.all&query=%EB%AF%B8%EA%B5%AD+%EA%B8%88%EB%A6%AC&oquery=%EC%A4%91%EC%95%99%EC%9D%80%ED%96%89+%EA%B8%88+%EB%A7%A4%EC%9E%85%EB%9F%89&tqi=jncV0wqosesssSNAdMossssst%2Bw-376087&ackey=i8nk8vhr'

profit = requests.get(url)
print(profit.status_code)
soup = BeautifulSoup(markup=profit.text,features='html.parser')
# print(soup.prettify())
rows = soup.find_all('tr')

data = []
for row in rows:
    cells = row.find_all('td')
    if len(cells) == 3:
        date = cells[0].get_text(strip=True)  # 날짜
        rate_before = cells[1].get_text(strip=True).replace('\n',' ').strip()  # 변동 전 금리
        rate_after = cells[2].get_text(strip=True).replace('\n',' ').strip()   # 변동 후 금리
        data.append([date, rate_before, rate_after])

for d in data:
    print(d)

    with open('interest_rates.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        # 헤더 작성
        writer.writerow(['Date', 'Rate Before', 'Rate After'])
        # 데이터 작성
        writer.writerows(data)

    print("CSV 파일이 'interest_rates.csv' 이름으로 저장되었습니다.")