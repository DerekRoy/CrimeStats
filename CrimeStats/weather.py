import pandas as pd 
import matplotlib.pyplot as plt

w13 = pd.read_csv("2013Weather.csv", header = 22)
w14 = pd.read_csv("2014Weather.csv", header = 22)
w15 = pd.read_csv("2015Weather.csv", header = 22)
w16 = pd.read_csv("2016Weather.csv", header = 22)
w17 = pd.read_csv("2017Weather.csv", header = 22)

w = w13.append(w14)
w = w.append(w15)
w = w.append(w16)
w = w.append(w17)
w = w[['Year', 'Month', 'Day', 'Mean Temp (°C)']]

weather = w.groupby(['Year','Month']).mean()
weather = weather.reset_index()
weather = weather.groupby('Month').mean()
