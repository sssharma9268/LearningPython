# From the data provided on Hollywood movies:
# 1.Find the highest rated movie in the “Quest” story type.
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('datasets\HollywoodMovies.csv')
# movies = df.loc[:,['Movie','Story','RottenTomatoes','AudienceScore']]
# movies = movies[movies['Story']=='Quest']
#
# print(movies.sort_values(by=['RottenTomatoes','AudienceScore'],ascending=False).iloc[0])

# 2. Find the genre in which there has been the greatest number of movie releases
# movies = df.loc[:,['Movie','Genre']]

# grouped = movies.groupby('Genre')
# result=grouped.count().sort_values(by='Movie',ascending=False)
# print(result.iloc[0])

# 3. Print the names of the top five movies with the costliest budgets.

# movies = df.loc[:, ['Movie', 'Budget']]
#
# print(movies.sort_values(by='Budget',ascending=False).head())
# 4. Is there any correspondence between the critics’ evaluation of a movie and its acceptance by the public?
# Find out, by plotting the net profitability of a movie against the ratings it receives on Rotten Tomatoes.
# print(df.loc[:,['RottenTomatoes','Profitability']].sort_values(by='Profitability',ascending=False))
#Simple plot and bar chart
# y= np.array(pd.Series(df['Profitability']))
# x= np.array(pd.Series(df['RottenTomatoes']))
#
# plt.bar(x,y)
# plt.grid(True)
# plt.xlabel('Rotten Tomatoes')
# plt.ylabel('Net Profitability')
# plt.title('critics’ evaluation of a movie and its acceptance by the public')
# plt.show()

# 5. Perform Operations on Files
# 5.1: From the raw data below create a data frame
# 'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
# 'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
# 'age': [42, 52, 36, 24, 73],
# 'preTestScore': [4, 24, 31, ".", "."],
# 'postTestScore': ["25,000", "94,000", 57, 62, 70]

data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
'age': [42, 52, 36, 24, 73],
'preTestScore': [4, 24, 31, ".", "."],
'postTestScore': ["25,000", "94,000", 57, 62, 70]}

#df = pd.DataFrame(data)

# 5.2: Save the dataframe into a csv file as example.csv
#df.to_csv('datasets\example.csv')

# 5.3: Read the example.csv and print the data frame
df = pd.read_csv('datasets\example.csv')
# print(df)

# 5.4: Read the example.csv without column heading
# Question 5: Read the example.csv and make the index columns as 'First Name’ and 'Last Name'
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
#print(df)
df.rename(columns={'first_name': 'First Name', 'last_name': 'Last Name'},inplace= True)
# print(df)
# 5.6:  Print  the  data  frame  in  a  Boolean  form  as  True  or  False.  True  for  Null/  NaN values and false for non-null values
# print(df.isnull())
# for key,value in df.iteritems():
#     print(key)
#     print(value)

# for index,row in df.iterrows():
#     if row['First Name'] or row['Last Name'] or row['age'] or row['preTestScore'] or row['postTestScore']:
#         print('False')
#     else:
#         print('True')

# 5.7: Read the dataframe by skipping first 3 rows and print the data frame
new_df = df.loc[3:,:]
# print(new_df)
# 5.8: Load a csv file while interpreting "," in strings around numbers as thousands seperators.
# Check the raw data 'postTestScore' column has, as thousands separator. Comma should be ignored while reading the data.
# It is default behaviour, but you need to give argument to read_csv function which makes sure commas are ignored.
#
# 6.Perform Operations on Files
# 6.1: From the raw data below create a Pandas Series 'Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'
# a) Print all elements in lower case
# series = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
# for data in series:
#     if data is not np.nan:
#         print(str(data).lower())

# print(series)
# b) Print all the elements in upper case
# for data in series:
#     if data is not np.nan:
#         print(str(data).upper())
# c) Print the length of all the elements
# for data in series:
#     if data is not np.nan:
#         print(len(str(data)))

# 6.2: From the raw data below create a Pandas Series
# ' Atul', 'John ', ' jack ', 'Sam'
# a) Print all elements after stripping spaces from the left and right
series = pd.Series([' Atul', 'John ', ' jack ', 'Sam'])
# for data in series:
#     if data is not np.nan:
#         print(str(data).strip())

# b) Print all the elements after removing spaces from the left only
# for data in series:
#     if data is not np.nan:
#         print(str(data).lstrip())
# c) Print all the elements after removing spaces from the right only
# for data in series:
#     if data is not np.nan:
#         print(str(data).rstrip())

# 6.3: -Create a series from the raw data below
# 'India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'
# a)split the individual strings wherever ‘_’ comes and create a list out of it.
# b)Access the individual element of a list
# c)Expand the elements so that all individual elements get splitted by ‘_’ and insted of list returns individual elements

# series = pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
# myList = []
# for data in series:
#     if data is not np.nan:
#         l = str(data).split('_')
#         print(l)

# 6.4: Create a series and replace either X or dog with XX-XX 'A', 'B', 'C', 'AabX', 'BacX','', np.nan, CABA', 'dog', 'cat'
series = pd.Series(['A', 'B', 'C', 'AabX', 'BacX','', np.nan,'CABA', 'dog', 'cat'])
#print(series.str.replace('X|dog', 'XX-XX ', case=False))

# 6.5: Create a series and remove dollar from the numeric values
# '12', '-$10', '$10,000'
series=pd.Series(['12', '-$10', '$10,000'])
# print(series.str.replace(r'$', ''))

# 6.6:-
# Create a series and reverse all lower case words
# 'india 1998', 'big country', np.nan
series = pd.Series(['india 1998', 'big country', np.nan])
pat=r'[a-z]+'
repl=lambda m: m.group(0)[::-1]
# print(series.str.replace(pat,repl))
# 6.7: Create pandas series and print true if value is alphanumeric in series or false if value is not alpha numeric in series.
# '1', '2', '1a', '2b', '2003c'
s=pd.Series([1, 2, '1a', '2b', '2003c'])
# print(s.str.isalnum())

# 6.8: Create pandas series and print true if value is containing ‘A’
# '1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'
s=pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
# print(s.str.contains('A'))
# 6.9: Create pandas series and print in three columns value 0 or 1 is a or b or c exists in values
# 'a', 'a|b', np.nan, 'a|c'
s=pd.Series(['a', 'a|b', np.nan, 'a|c'])
# print(s.str.get_dummies(sep='|'))
# 6.10: Create pandas dataframe having keys and ltable and rtable as below
# -'key': ['One', 'Two'], 'ltable': [1, 2]
# 'key': ['One', 'Two'], 'rtable': [4, 5]
# Merge both the tables based of key
ltable={'key': ['One', 'Two'], 'ltable': [1, 2]}
rtable={'key': ['One', 'Two'], 'rtable': [4, 5]}
df1=pd.DataFrame(ltable)
df2=pd.DataFrame(rtable)
df3=pd.merge(df1,df2,on='key')
print(df3)