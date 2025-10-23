from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://kr.investing.com/',
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': '__cf_bm=iWY8CR6gUdvhO2F3VWgaEYsL9_pemPOVqPpw9SzV9io-1760919844-1.0.1.1-KDZKgVwXL2RtJMoD2NhpvUmnDTFN1F_8e18IPw_4L3lL9G7mfyk0moQzWt31AkcwjeUXwu2lg2Z0wMct19rOpY2hVRnL6z5EL9svO5JEgS8Oj2DAP55vRMu03zeXEEP3; path=/; expires=Mon, 20-Oct-25 00:54:04 GMT; domain=.investing.com; HttpOnly; Secure; SameSite=None'
}


browser.get("https://kr.investing.com/etfs/411060-historical-data")
browser.get("https://api.investing.com/api/financialdata/historical/1183178?start-date=2024-09-26&end-date=2025-10-20&time-frame=Daily&add-missing-rows=false")
time.sleep(1)
period = browser.find_element(By.CSS_SELECTOR, "div.flex.flex-1.flex-col.justify-center.text-sm.leading-5.text-")
period.click()
cellar = period.find_element(By.CSS_SELECTOR,"input.absolute.left-0.top-0.h-full.w-full.opacity-0")
cellar.click()


a=input()



# <div class="flex flex-1 flex-col justify-center text-sm leading-5 text-[#333]">2025- 09- 16 - 2025- 10- 20</div>
#
# < input
#
#
# class ="absolute left-0 top-0 h-full w-full opacity-0" max="2025-10-20" type="date" value="2024-09-26" >