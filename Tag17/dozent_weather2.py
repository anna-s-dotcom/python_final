import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data/weather.xlsx')

# df_usa = df[df['Country'] == 'USA'].copy()
# usa = df_usa.groupby('Day')['Sunshine Duration'].sum()
#
# df_can = df[df['Country'] == 'Canada'].copy()
# can = df_can.groupby('Day')['Sunshine Duration'].sum()
#
#
# plt.scatter(usa.index, usa, label = 'USA', color = 'r')
# plt.plot(can, 'b-.', label = 'Canada')
# plt.xlabel('Tage')
# plt.ylabel('Sunshine Duration')
# plt.legend()
# plt.show()


gr = df.groupby(['Country', 'Day'])['Sunshine Duration'].sum()


plt.plot(gr['USA'], label = 'USA', color = 'r')
plt.plot(gr['Canada'], 'b-.', label = 'Canada')
plt.xlabel('Tage')
plt.ylabel('Sunshine Duration')
plt.legend()
plt.show()

print(gr.index)
print(gr['USA'].values)

print("gr['USA', 5]")
print(gr['USA', 5])
