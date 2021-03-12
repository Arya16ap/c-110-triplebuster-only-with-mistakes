import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("data.csv")
data = df["average"].tolist()

fig = ff.create_distplot([data],["average"],show_hist = False)
fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("mean of samples: ", mean)
print("standard deviation of sample",std_deviation)
