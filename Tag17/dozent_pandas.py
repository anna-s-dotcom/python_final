import pandas as pd

df = pd.read_csv('data/astronauts.csv', delimiter = ',')

# print(df.head())
# # Series (Spalte)
# print(df['Space Walks'])
# # Series (Zeile)
# print(df.iloc[0])


df2 = df[df['Space Walks'] == 7].copy()

# print(df2[['Name', 'Space Walks']])

# # iloc greift auf zeilennummer zu
# print(df2.iloc[0])
# print()
# # loc greift auf den tatsächlichen index zu
# print(df2.loc[34])

# df2.to_csv('data/spacewalks.csv')

new_df = pd.read_csv('data/spacewalks.csv', index_col = 0)

print(df2)
print()
print(new_df)
