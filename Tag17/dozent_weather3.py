import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data/weather.xlsx')


# print(df['Year'])
df['Year'] = df['Year'].astype(str)
# print()
# print(df['Year'])
df['Month'] = df['Month'].astype(str)
df['Day'] = df['Day'].astype(str)

df['New Date'] = df[['Year', 'Month', 'Day']].apply(lambda x: ' '.join(x), axis = 1)
# print(df['New Date'])

df['New Date'] = pd.to_datetime(df['New Date'])
# print(df['New Date'])
