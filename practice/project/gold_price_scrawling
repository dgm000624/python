import json
from bs4 import BeautifulSoup
import requests
import pandas as pd

st_date = "2023-01-20"
end_date = "2025-10-20"
page = "1"


url = f"https://www.goodgold.co.kr/ajax/ajax.chart2.php?act=tbl&st_date={st_date}&end_date={end_date}&code=gold&page_rows=5&page={page}"

res = requests.get(url)
print(res.status_code)
res = json.loads(res.text)
soup = BeautifulSoup(res['list'], 'html.parser')
total_page = int(res['total_page'])

data = []

for i in range(1, total_page+1):
    url = f"https://www.goodgold.co.kr/ajax/ajax.chart2.php?act=tbl&st_date={st_date}&end_date={end_date}&code=gold&page_rows=5&page={i}"
    res = requests.get(url)
    res = json.loads(res.text)
    soup = BeautifulSoup(res['list'], 'html.parser')
    row = soup.find("tbody")
    trs = row.find_all("tr")
    for k in trs:
        tds = k.find_all("td")
        data.append({"date":tds[0].text, "value":tds[1].text})
    print(f"{i}번째 페이지 완료")

df = pd.DataFrame(data)
df.to_excel("gold_price_prac.xlsx", index=False, engine='openpyxl')
print("저장완료")

