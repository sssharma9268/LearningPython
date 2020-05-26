# Case Study
# Objective:
# 1.Make the learner load the data using pandas.
# 2.Create new columns in dataset from existing columns.
# 3.Use pandas to answer questions of interest.
# 4.Plot variables of interest.
# Dataset used:
# Prisoners dataset sourced from data.gov.in
# Questions:
# 1.Data Loading:
# a.Load the dataset “prisoners.csv” using pandas and display the first and last five rows in the dataset.
# [Hint: Refer to read_csv,head and tail methods in pandas]
# b.Use describe method in pandas and find out the number of columns. Can you say something about those rows who have zero inmates?
# [Hint: Use the loc attribute of dataframe combined with conditional
# checks]
#
# 2.Data Manipulation:
# a.Create a new column -’total_benefitted’ that is a sum of inmates benefitted through all modes.[Hint: Use sum method with
# appropriate xis]
# b.Create a new row -“totals” that is the sum of all inmates benefitted through each mode across all states.
#
# 3.Plotting:
# a.Make a bar plot with each state name on the x -axis and their total benefitted inmates as their bar heights. Which state has the maximum
# number of beneficiaries?
# [Hint: Use bar method of pyplot]
# b.Make a pie chart that depicts the ratio among different modes of
# benefits.
# [Hint: Use pie method of pyplot]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('datasets\prisoners.csv')
# print(df)

#1 a. Display the first and last five rows in the dataset.
# print(df.head(5))
# print(df.tail(5))

# 1b.Use describe method in pandas and find out the number of columns. Can you say something about those rows who have zero inmates
# print('No. of columns in df DataFrame are ', len(df.columns))
# print('No. of zero inmates')
# print(df.loc[df['No. of Inmates benefitted by Elementary Education']==0])
# print(df.loc[df['No. of Inmates benefitted by Adult Education']==0])
# print(df.loc[df['No. of Inmates benefitted by Higher Education']==0])
# print(df.loc[df['No. of Inmates benefitted by Computer Course']==0])

# 2a.Create a new column total_benefitted that is a sum of inmates benefitted through all modes
df['total_benefitted']=df.iloc[:,2:6].sum(axis=1)
# print(df.info())


# 2b.Create a new row -totals that is the sum of all inmates benefitted through each mode across all states

totals = pd.DataFrame([[df['No. of Inmates benefitted by Elementary Education'].sum(axis=0,skipna=True),
                       df['No. of Inmates benefitted by Adult Education'].sum(axis=0,skipna=True),
                       df['No. of Inmates benefitted by Higher Education'].sum(axis=0,skipna=True),
                       df['No. of Inmates benefitted by Computer Course'].sum(axis=0,skipna=True)]],
                      columns= ['No. of Inmates benefitted by Elementary Education','No. of Inmates benefitted by Adult Education','No. of Inmates benefitted by Higher Education','No. of Inmates benefitted by Computer Course'])

# df3= pd.merge(df,totals,on=list(totals.columns.values),how="outer")
# for col in df3.columns:
#     print(df3.loc[35:,col])


x=df.loc[:,['STATE/UT']]
y=df.iloc[:,2:6].sum(axis=1)
print(x)
print(y)
x2=list(x)
y2=list(y)
# x3=list(x2)
# y3=list(y2)
plt.plot(x2,y2)
plt.grid()
plt.show()

# 3.Plotting:
# a.Make a bar plot with each state name on the x -axis and their total benefitted inmates as their bar heights. Which state has the maximum
# number of beneficiaries?
# [Hint: Use bar method of pyplot]
# b.Make a pie chart that depicts the ratio among different modes of
# benefits.
# [Hint: Use pie method of pyplot]