import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data/weather.xlsx')

# print(df.columns)

# ['Year', 'Month', 'Day', 'Hour', 'Temperature', 'Sunshine Duration', 'Wind Speed', 'Wind Direction', 'City', 'Country']

# sun = df['Sunshine Duration']
#
# print(type(sun[379]))


# Aufgabe: Gib alle Tage mit der höchsten Sonnenscheindauer aus. (Einmal für USA, einmal für Canada)

####### alle summen für canada

# erstelle dataframe für spalte 'Country' == Canada
df_can = df[df['Country'] == 'Canada'].copy()
# erstelle array, welches alle möglichen tage enthält
days = df_can['Day'].unique()

# erstelle leere liste für die summen der Sonnenscheindauer
sums = []
dsums = {}
# iteriere über alle möglichen tage
for day in days:
    # erstelle boolsche series, welche immer an den stellen
    # für einen tag = True sonst False
    bool_series_day = df_can['Day'] == day
    # print(df_can['Day'])
    # print(bool_series_day)

    # erstelle mit hilfe der bool series ein gefiltertes dataframe
    df_day = df_can[bool_series_day]
    # print(df_day)

    # bilde summe der Sonnenscheindauer für einen tag
    sum = df_day['Sunshine Duration'].sum()
    # print(day, sum)

    # hänge die summe an die liste der summen an
    sums.append(sum)
    dsums[day] = sum

# print(sums)
# print(max(sums))
# print(dsums)

import numpy as np

# i = index wo in sums der maximale wert steht
i = np.argmax(sums)
print(days[i], sums[i])


######### alle summen usa
boo_series_usa = df['Country'] == 'USA'
df_usa = df[boo_series_usa].copy()

days = df_usa['Day'].unique()

day_max = 0
day_of_max = None
for day in days:
    df_day = df_usa[df_usa['Day'] == day]
    day_sum = df_day['Sunshine Duration'].sum()

    if day_sum >= day_max:
        day_max = day_sum
        day_of_max = day

print(day_of_max, day_max)


##################### kurzschreibweise

countries = df['Country'].unique()

sums_all = []
for country in countries:
    df_country = df[df['Country'] == country].copy()
    sums_country = []
    for day in df_country['Day'].unique():
        df_day = df_country[df_country['Day'] == day]
        sum = df_day['Sunshine Duration'].sum()
        sums_country.append(sum)
    sums_all.append(max(sums_country))

print(sums_all)
