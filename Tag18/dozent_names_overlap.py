import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from time import time

df = pd.read_csv('data/names.csv', index_col = 0)

minYear = df['Year'].min()
maxYear = df['Year'].max()
anz = df['Year'].nunique() # == len(df['Year'].unique())

print(minYear)
print(maxYear)
print((maxYear-minYear+1)==anz)

# Aufgabe erstelle eine zusammenstellung (Series, Numpy Array) aller Männer und aller Frauennamen.
# Bonus: Stelle fest ob sich die Namen überlappen.
# Bonus 2: Wenn ja, welche Namen überlappen sich.

dff = df[df['Gender'] == 'F'].copy()
dfm = df[df['Gender'] == 'M'].copy()

t = time()
f = dff['Name'].unique()
m = dfm['Name'].unique()
names = np.intersect1d(f, m, assume_unique = True)
print('First unique:', time()-t)

# print(len(names))
# print(len(f))
# print(len(m))
# names = []
# for i in f:
#     if i in m:
#         names.append(i)
# print(len(names))

t = time()
print(np.intersect1d(dff['Name'].values, dfm['Name'].values))
print('Ohne unique:', time()-t)
# np.setdiff1d(f, m) -> gibt die differenz (exlusiven elemente)
