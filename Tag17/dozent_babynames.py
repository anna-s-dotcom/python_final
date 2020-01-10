# Aufgabe:
# Gib die Top 3 der Frauen und die Top 3 der Männer für jede Ethnizität aus. (Daten: Popular_Baby_Names.csv)

import pandas as pd

df = pd.read_csv('data/Popular_Baby_Names.csv').drop_duplicates()

# year = df['Year of Birth'].max()
#
# df = df[df['Year of Birth'] == year]
#
# dff = df[df['Gender'] == 'FEMALE'].copy()
# dfm = df[df['Gender'] == 'MALE'].copy()
#
# # print(dfm)
# for etn in dff['Ethnicity'].unique():
#     dffe = dff[dff['Ethnicity'] == etn].copy()
#     # dffe = dffe.sort_values('Rank')
#     print(dffe.head(3))
#
# etnicity = dfm['Ethnicity'].unique()
# for etn in etnicity:
#     dfme = dfm[dfm['Ethnicity'] == etn].copy()
#     print(dfme.head(3))

################################################

dff = df[df['Gender'] == 'FEMALE'].copy()
dfm = df[df['Gender'] == 'MALE'].copy()

years = df['Year of Birth'].unique()

for year in years:
    dffy = dff[(dff['Year of Birth'] == year) & (dff['Rank'] < 4)].copy()
    print(dffy)
    # for etn in dffy['Ethnicity'].unique():
    #     dffe = dffy[dffy['Ethnicity'] == etn].copy()
    #     # dffe = dffe.sort_values('Rank')
    #     print(dffe)

# etnicity = dfm['Ethnicity'].unique()
# for etn in etnicity:
#     dfme = dfm[dfm['Ethnicity'] == etn].copy()
#     print(dfme.head(3))
