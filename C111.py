import pandas as pd 
import random
import statistics
import csv
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
df=pd.read_csv('studentMarks.csv')
data=df['Math_score'].tolist()
fig=ff.create_distplot([data],['Math_scores'],show_hist=False)
fig.show()