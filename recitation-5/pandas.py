import pandas as pd

df1 = pd.read_csv('stations.csv')

print(df1.to_string()) 

df1 = pd.read_csv('readings.csv')

print(df1.to_string()) 