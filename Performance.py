import csv

import pandas as pd
import plotly.express as px

reader = pd.read_csv('data.csv')
student_id = reader.loc[reader['student_id'] == 'TRL_987']
print(student_id.groupby('level')['attempt'].mean())

chart = px.scatter(student_id,
  x=student_id.groupby('level')['attempt'].mean(),
  y=['level1','level2','level3','level4'],
   color='red'
  )
  
