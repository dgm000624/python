import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

news_url = 'https://s.search.naver.com/p/newssearch/3/api/tab/more?abt=%5B%7B%22eid%22%3A%22NEWS-CROP-IMG%22%2C%22value%22%3A%7B%22bucket%22%3A%22%22%2C%22bt%22%3A%222%22%2C%22is_control%22%3Atrue%7D%7D%5D&cluster_rank=244&de=&ds=&eid=&field=0&force_original=&is_dts=0&is_sug_officeid=0&mynews=0&news_office_checked=&nlu_query=&nqx_theme=&nso=so%3Ar%2Cp%3Aall%2Ca%3Aall&nx_and_query=&nx_search_hlquery=&nx_search_query=&nx_sub_query=&office_category=&office_section_code=0&office_type=0&pd=0&photo=0&query=%EC%9D%B8%EB%8F%84+%2B+%EA%B8%88&query_original=&rev=0&service_area=&sm=tab_smr&sort=0&spq=0&ssc=tab.news.all&start=1'
response = requests.get(news_url, headers=headers)

print(response.status_code)  # 200아니면 망한거
print(len(response.text))

soup = BeautifulSoup(response.text, 'html.parser')
print(soup)


tag_span = soup.find('a')
tag_title = tag_span.find('\"title\":\"\u003cmark\u003e금\u003c/mark\u003e')
print(tag_title)

# print(tag_span.count)