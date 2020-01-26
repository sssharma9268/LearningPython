import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

mydataset = pd.read_csv('datasets\AllCountries.csv')

print(mydataset.ndim)
print(mydataset.shape)
#print(mydataset.head())
#print(mydataset.tail())
#print(mydataset.info())
# print(mydataset.describe())
# print(mydataset.mean())
# print(mydataset.sum())

# for key, value in mydataset.iteritems():
#     print(key,value)

# for row in mydataset.iterrows():
#     print(row)

for row in range(len(mydataset)):
    if mydataset.loc[row,'LandArea'] < 10:
        mydataset.loc[row,'Category'] = 'Very Small'
    elif mydataset.loc[row,'LandArea'] < 100:
        mydataset.loc[row,'Category'] = 'Small'
    elif mydataset.loc[row,'LandArea'] < 1000:
        mydataset.loc[row,'Category'] = 'Medium'
    else:
        mydataset.loc[row,'Category'] = 'Large'

# print(mydataset.groupby('Category').groups)
#
# for country, group in mydataset.groupby('Category'):
#     print(country)



champion_stats={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka','England'],
           'ICC_rank':[2,3,7,8,4,5],
           'World_champions_Year':[2011,2015,1979,1992,1996,2019],
           'Points':[874,787,753,673,855,700]}

match_stats={'Team':['India','Australia','West Indies','Pakistan','Sri Lanka'],
             'World_cup_played':[11,10,11,9,8],
             'ODIs_played':[733,988,712,679,662]}


df1=pd.DataFrame(champion_stats)
df2=pd.DataFrame(match_stats)

print(df1)
print(df2)

#df3=pd.merge(df1,df2,on='Team') same as inner
df3=pd.merge(df1,df2,on='Team',how='left')
#df3=pd.merge(df1,df2,on='Team',how='right')
#df3=pd.merge(df1,df2,on='Team',how='outer')
print(df3)
