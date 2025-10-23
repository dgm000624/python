# import pandas as pd
#
# df = pd.read_excel('ForCal.xlsx')
# # print(df['won/dollar']-df['gold_price'])
# # df['date'] = pd.to_datetime(df['date'])
# # df = df.set_index('date')
# dfDOLLAR = df['won/dollar']
# dfGOLD = df['gold_price']
# dfDATE = df['date']
# dfVIX = df['VIX_종가']
# dfETF = df['금ETF']
#
# dfDOLLAR_GOLD = df.merge(dfDOLLAR, dfGOLD)
#

import pandas as pd
#엑셀 읽어오기
df = pd.read_excel('gold_interests.xlsx')
#엑셀의 'date'를 시간데이터로 바꾸기
df['date'] = pd.to_datetime(df['date'])
# 기준 인덱스를 'date'로 하겠다
df = df.set_index('date')
# 해당 날짜 이후의 데이터만 수집
df = df[df.index > '2024-10-01']
# 사용할 y축(상관계수를 구하고 싶은 요소)
cols = ['buy_price', 'interest_rate']
# df의 기본 내장 기능중 pearson기법 사용
correlation_matrix = df.corr(method='pearson', numeric_only=True)
print('-'*20 + "상관계수" + '-'*20)
# 결과 출력
print(correlation_matrix)
print()
print('-'*20 + "상관계수 정리" + '-'*20)
# 'buy_price'(금값)기준으로 상관계수를 정렬
print(correlation_matrix['buy_price'].sort_values(ascending=False))