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

df = pd.read_excel('ForCal.xlsx')

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

cols = ['won/dollar', 'gold_price', 'VIX_종가', '금ETF']


correlation_matrix = df.corr(method='pearson', numeric_only=True)

print('-'*20 + "상관계수" + '-'*20)
print(correlation_matrix)

print()
print('-'*20 + "상관계수 정리" + '-'*20)
print(correlation_matrix['gold_price'].sort_values(ascending=False))
