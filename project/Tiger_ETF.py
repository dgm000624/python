import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta

def fetch_etf_prices(start_date, end_date):
    url = "https://investments.miraeasset.com/tigeretf/ko/product/search/price.ajax"
    payload = {
        "ksdFund": "KR70072R0006",
        "fromDate": start_date.strftime('%Y-%m-%d'),
        "toDate": end_date.strftime('%Y-%m-%d')
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    res = requests.post(url, data=payload, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find("table")
    if table:
        df = pd.read_html(str(table))[0]
        return df
    else:
        print("⚠️ 테이블 없음:", start_date, "~", end_date)
        return pd.DataFrame()

# 전체 수집
today = datetime.today()
total_df = pd.DataFrame()

for i in range(0, 12, 2):
    end = today - timedelta(days=i * 30)
    start = end - timedelta(days=60)
    df = fetch_etf_prices(start, end)
    total_df = pd.concat([total_df, df], ignore_index=True)

# 중복 제거 및 정렬
total_df = total_df.drop_duplicates(subset=[total_df.columns[0]])
total_df = total_df.sort_values(by=total_df.columns[0], ascending=False)

print(total_df.head())