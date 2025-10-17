import pandas as pd

df = pd.read_excel('recent_goldndollar.xlsx')

df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

cols = ['won/dollar', 'gold_price']


correlation_matrix = df.corr(method='pearson', numeric_only=True)

print('-'*20 + "상관계수" + '-'*20)
print(correlation_matrix)

print()
print('-'*20 + "상관계수 정리" + '-'*20)
print(correlation_matrix['gold_price'].sort_values(ascending=False))
