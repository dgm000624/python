import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
MAX_PAGES = 50
REQUEST_DELAY = 1.5


def crawl_exchange_rate(max_pages, headers):
    print("\n-------------------------------------------------------")
    print("달러 환율 데이터 크롤링 시작")

    BASE_URL = "https://finance.naver.com"
    HISTORY_PATH = "/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_USDKRW"
    all_exchange_data = []

    for page_num in range(1, max_pages + 1):
        target_url = f"{BASE_URL}{HISTORY_PATH}&page={page_num}"
        print(f"  -> 페이지 {page_num}에 데이터 요청 중...")

        try:
            response = requests.get(target_url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # 이전에 분석된 정확한 테이블 클래스 사용
            table = soup.find('table', {'class': 'tbl_exchange today'})

            if table:
                rows = table.find('tbody').find_all('tr')

                if not rows:
                    print(f"데이터 행을 찾을 수 없습니다. 종료.")
                    break

                for row in rows:
                    cols = row.find_all('td')
                    if len(cols) >= 2:
                        date = cols[0].text.strip()  # 0번째 <td>: 날짜
                        price = cols[1].text.strip()  # 1번째 <td>: 매매기준율

                        # 쉼표(,)와 공백 제거
                        price = price.replace(',', '').strip()

                        all_exchange_data.append([date, price])
            else:
                print(f"환율 테이블을 찾을 수 없습니다.")
                break

        except requests.exceptions.RequestException as e:
            print(f"환율 요청 중 오류 발생: {e}")
            break

        time.sleep(REQUEST_DELAY)

    return all_exchange_data


#============================================================

if __name__ == "__main__":

    # 원/달러 환율 데이터 수집
    exchange_data = crawl_exchange_rate(MAX_PAGES, HEADERS)

    if exchange_data:
        df_exchange = pd.DataFrame(exchange_data, columns=['날짜', '원/달러 환율 (매매기준율)'])
        df_exchange['원/달러 환율 (매매기준율)'] = pd.to_numeric(df_exchange['원/달러 환율 (매매기준율)'], errors='coerce')

        try:
            df_exchange.to_excel('usd_krw_exchange.xlsx', index=False, engine='openpyxl')
            print("\n-------------------------------------------------------")
            print("성공적으로 저장되었습니다.")
        except Exception as e:
            print(f"\n오류 발생: {e}")