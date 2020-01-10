import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/names.csv', index_col = 0)

df2 = df.copy()


# Erstelle ein Balkendiagram, der die häufigkeit eines Names in einem Jahrzehnt.
name = 'Bruce'

df2 = df2[df2['Name'] == name]

df2['Year'] = (df2['Year']//10)*10
# print(df2['Year'])

s_gr_jz = df2.groupby('Year')['Count'].sum()
print(s_gr_jz)
print(type(s_gr_jz))

# fig = plt.figure()
#
# ax = fig.add_subplot(111)
# ax.bar(s_gr_jz.index, s_gr_jz, width = 7)
# ax.set_xticks(s_gr_jz.index)
# ax.set_xticklabels(s_gr_jz.index, rotation = 45)
# ax.set_xlabel('Jahrzehnte')
# ax.set_ylabel('Anzahl')
# plt.show()
