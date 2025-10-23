import plotly.graph_objs as go
import plotly.express as px
import pandas as pd


df = pd.read_excel("comparison_all.xlsx")

print(df)
fig = px.line(df, x = "date", y = ["원/달러 환율 (매매기준율)" ])
fig.update_layout(xaxis=dict(autorange="reversed"))
fig.show()