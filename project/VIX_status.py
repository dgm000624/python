import requests
import pandas as pd
import time

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
MAX_PAGES = 50
REQUEST_DELAY = 1.5

def crawl_vix_index(max_pages, headers):
    print("-------------------------------------------------------")
    print("VIX 지수 데이터 크롤링 시작...")

    BASE_URL = "https://api.stock.naver.com/index/.VIX/price"

    all_vix_data = []

    for page_num in range(1, max_pages + 1):
        params = {
            "page": str(page_num),
            "pageSize": "10"  # 한 페이지당 데이터 10개
        }

        print(f"  -> VIX 페이지 {page_num}에 데이터 요청 중...")

        try:
            response = requests.get(BASE_URL, headers=headers, params=params, timeout=10)
            response.raise_for_status()

            data_list = response.json()

            if not data_list:
                print(f"VIX 페이지 {page_num}에서 더 이상 데이터가 없습니다. 크롤링 종료.")
                break

            for item in data_list:

                full_date_time = item.get('localTradedAt', '')
                date = full_date_time.split('T')[0] if full_date_time else ''

                close_price = item.get('closePrice', '').replace(',', '')
                fluctuations_ratio = item.get('fluctuationsRatio', '')

                if date and close_price:
                    all_vix_data.append([date, close_price, fluctuations_ratio])

        except requests.exceptions.RequestException as e:
            print(f"VIX 요청 중 HTTP 오류 발생: {e}")
            break
        except Exception as e:
            print(f"VIX JSON 파싱 오류 발생: {e}")
            break

        time.sleep(REQUEST_DELAY)

    return all_vix_data


# ====================================================================
# 메인 실행 및 엑셀 저장
# ====================================================================

if __name__ == "__main__":

    vix_data = crawl_vix_index(MAX_PAGES, header)

    if vix_data:
        # DataFrame 생성
        df_vix = pd.DataFrame(vix_data, columns=['날짜', 'VIX 종가', 'VIX 등락률 (%)'])

        # 숫자형 변환 (분석을 위해)
        df_vix[['VIX 종가', 'VIX 등락률 (%)']] = df_vix[['VIX 종가', 'VIX 등락률 (%)']].apply(pd.to_numeric, errors='coerce')

        # 엑셀 파일로 저장
        try:
            df_vix.to_excel('vix_index.xlsx', index=False, engine='openpyxl')
            print("\n-------------------------------------------------------")
            print(f"[vix_index.xlsx] 파일에 VIX 지수 데이터 {len(df_vix)}개 행 저장 완료.")
        except Exception as e:
            print(f"\nVIX 데이터 엑셀 저장 중 오류 발생: {e}")
    else:
        print("\nVIX 데이터 수집에 실패했거나 데이터가 없습니다.")