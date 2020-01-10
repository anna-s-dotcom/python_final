import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from time import time

df = pd.read_csv('data/names.csv', index_col = 0)

# Aufgabe: Bestimme für jedes Jahr, wie häufig ein Name vergeben wurde.


# Groupby:
# DataFrame.groupby('Gruppierungsspalte')['Berechnungsspalte'].formel()
# Gruppierungsspalte: Nach dieser wird Gruppiert
# Berechnungsspalte: Auf diese wird die 'formel()' angewendet
# formel(): Macht aus mehreren werten einen (z.B. sum(), min(), mean())

name1 = 'Bruce'
name2 = 'Anna'

df_n = df[df['Name'] == name1].copy()
s_count1 = df_n.groupby('Year')['Count'].sum()
# print(s_count[2013])
# print(s_count)

df_n = df[df['Name'] == name2].copy()
s_count2 = df_n.groupby('Year')['Count'].sum()

# s_gr_count = df.groupby(['Name', 'Year'])['Count'].sum()
# print(s_gr_count[name, 2013])
# print(s_gr_count[name])

# s_gr_count = df.groupby(['Year', 'Name'])['Count'].sum()
# print(s_gr_count[2013, name])
# print(s_gr_count[:,name])


# Bestimme, in wievielen Staaten der Name vorkam. (Über den gesamten Zeitraum.)

# df_n = df[df['Name']==name].copy()
# states = df_n['State'].unique()
# count = df_n['State'].nunique()

# print(states)
# print(count)

# Wer fertig ist: Plotte den Verlauf der Anzahl eines Names über die Jahre.

plt.plot(s_count1, label = name1)
plt.scatter(s_count1.index, s_count1, color='r', alpha = 0.75, s = 2)
plt.xlabel('Year')
plt.ylabel(f'Amount of {name1}')
plt.legend()
plt.xlim(1910, 2014)
plt.savefig('data/pltfig.png', dpi = 100)
plt.show()


fig = plt.figure()

ax1 = fig.add_subplot(121)
ax1.plot(s_count1, label = name1)
ax1.plot(s_count2, label = name2)
ax1.set_xlabel('Year')
ax1.set_ylabel(f'Amount')
ax1.legend()

ax2 = fig.add_subplot(122)
ax2.scatter(s_count1.index, s_count1, color='r', alpha = 0.75, s = 2, label = name1)
ax2.set_xlabel('Year')
ax2.set_ylabel(f'Amount of {name1}')
# ax2.set_yticks(s_count1)
ax2.set_yticklabels([])
ax2.legend()

plt.show()

fig.savefig('data/fig.png', dpi = 100)
# fig.savefig('data/fig2.png', dpi = 1000)
