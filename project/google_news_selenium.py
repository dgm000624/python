from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import timedelta, datetime

browser = webdriver.Chrome()

Start_date = "09/15/2025"
End_date = "10/30/2025"
repeat = 5
Search_Word = "금%2B시세"
page = 0
#Start_date로부터 End_date까지 Search_Word에 해당하는 웹피이지로 이동

def plusdate(days):
    start_date = datetime.strptime(Start_date, "%m/%d/%Y")
    new_date = start_date + timedelta(days=days)
    return new_date.strftime("%m/%d/%Y")

url = f"https://www.google.com/search?q={Search_Word}&sca_esv=b321de86df217229&tbs=cdr:1,cd_min:{Start_date},cd_max:{Start_date}&tbm=nws&sxsrf=AE3TifNoYV5Bw0RbdAZ7t2GBerwTXlsAEw:1760927493881&ei=BZ_1aN3ONf7Fp84Px7PakQI&start={page}&sa=N&ved=2ahUKEwid5f2N3rGQAxX-4skDHceZNiI4ChDy0wN6BAgGEAc&biw=1920&bih=911&dpr=1"

browser.get(url)
buttonInterface = browser.find_element(By.CSS_SELECTOR, "tr[jsname='TeSSVd']")
buttons = len(buttonInterface.find_elements(By.CSS_SELECTOR, "td.NKTSme"))
# nextButton = buttonInterface.find_elements(By.CSS_SELECTOR, "td.NKTSme")

titles = []


time.sleep(1)
for i in range(0,buttons+1) :
    articles = browser.find_elements(By.CSS_SELECTOR, "div.n0jPhd.ynAwRc.MBeuO.nDgy9d")
    for k in articles:
        titles.append({"date" : Start_date, "article" : k.text})
    print(f"{i+1}번째 페이지 수집 완료")
    # nextButton[i].click()
    if i != buttons :
        buttonInterface = browser.find_element(By.CSS_SELECTOR, "tr[jsname='TeSSVd']")
        nextButton = buttonInterface.find_elements(By.CSS_SELECTOR, "td.NKTSme")
        try :
            nextButton[i].click()
        except IndexError:
            break
        time.sleep(1)



for i in titles :
    print(i)


a = input()
