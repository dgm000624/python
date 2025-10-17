import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://www.goodgold.co.kr/ajax/ajax.chart2.php"
START_DATE = "2022-07-16"
END_DATE = "2025-10-16"
CODE = "gold"
PAGE_ROWS = 5

def fetch_page(page):
    params = {
        "act": "tbl",
        "st_date": START_DATE,
        "end_date": END_DATE,
        "code": CODE,
        "page_rows": PAGE_ROWS,
        "page": page
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

def parse_html_table(html_table):
    soup = BeautifulSoup(html_table, "html.parser")
    rows = soup.select("tbody tr")
    data = []
    for row in rows:
        cols = row.find_all("td")
        record = {
            "date": cols[0].text.strip(),
            "buy_price": cols[1].text.strip().replace(",", ""),
            "sell_price_pure1": cols[2].text.strip().replace(",", ""),
            "sell_price_18k": cols[3].text.strip().replace(",", ""),
            "sell_price_14k": cols[4].text.strip().replace(",", "")
        }
        data.append(record)
    return data

def save_to_csv(data, filename="gold_prices.csv"):
    keys = ["date", "buy_price", "sell_price_pure1", "sell_price_18k", "sell_price_14k"]
    with open(filename, "w", newline='', encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def main():
    first_page_data = fetch_page(1)
    total_page = int(first_page_data["total_page"])
    all_data = []

    print(f"총 {total_page} 페이지 크롤링 시작...")

    for page in range(1, total_page + 1):
        print(f"페이지 {page} 수집 중...")
        page_json = fetch_page(page)
        table_html = page_json["list"]
        page_data = parse_html_table(table_html)
        all_data.extend(page_data)

    print(f"총 {len(all_data)}개 데이터 수집 완료.")
    save_to_csv(all_data)
    print("gold_prices.csv 파일로 저장 완료!")

if __name__ == "__main__":
    main()
