from bs4 import BeautifulSoup

html='<h1 id="title">럭스</h1><div class="top"><ul class="menu"><li><a href="http://www.luxwave.co.kr/index.html" class="login">로그인</a></li></ul><ul class="brand"><li><a href="http://www.luxwave.co.kr/media/">한빛미디어</a></li><li><a href=http://www.luxwave.co.kr/song/">럭스웨이브</a></li></ul></div>'

soup = BeautifulSoup(markup=html, features='html.parser')
#print(soup.prettify())

print(soup.h1)
# tag_h1 = soup.h1
# print(tag_h1)

tag_div = soup.div
print(tag_div.text)

tag_ul = soup.ul

print(tag_ul)
print(tag_ul.text)

tag_ul_all = soup.find_all('ul')
#print(tag_ul_all)
print(tag_ul_all[0].text)