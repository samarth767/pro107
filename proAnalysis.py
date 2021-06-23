import csv
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('./mathData/data2.csv')

fig2 = px.scatter(df.groupby('level')['attempt'].mean(), x='student_id', y='level', color='attempt',
                  size='attempt', size_max=75
                  )
fig2.show()
