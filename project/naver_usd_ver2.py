from bs4 import BeautifulSoup
import requests
import pandas as pd

end_page = 10
page = 0

data = []
for k in range(1, end_page+1) :
    page +=1
    url = f"https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_USDKRW&page={page}"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    tbody = soup.find("tbody")
    trs = tbody.find_all("tr")
    for i in trs:
        date = i.find("td", attrs={"class": "date"})
        price = i.find("td", attrs={"class": "num"})
        data.append({"date": date.text, "usd_price": price.text})
    print(f"{page}번째 페이지 크롤링 완료")



df = pd.DataFrame(data)
df.to_excel("naver_usd_crawling.xlsx", index="False", engine="openpyxl")
print("저장완료")

