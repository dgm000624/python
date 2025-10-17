import pandas as pd
from selenium import webdriver
# wd = webdriver.Chrome()
wd = webdriver.Chrome()

wd.get(url="https://www.coffeebeankorea.com/store/store.asp")

# if __name__ == "__main__":
#     main()

def main():
    result = []
    print('CoffeeBean store crawling >>>>>>>>>>>>>>>>')
    CoffeeBean_store(result)

    CB_tbl = pd.DataFrame(result, columns = ('store', 'address', 'phone'))
    CB_tbl.to_csv('./CoffeeBean_EXCEL.csv', encoding='cp949', mode='w', index=True)