import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

mydataset = pd.read_csv('mydataset\Hurricanes.csv')

# print(mydataset)

#plt.plot([1,2,3,4])
#plt.show()

y = np.arange(10)*10
x = np.arange(10)
plt.plot([x/10 for x in y],y)
plt.plot(x,[a**2 for a in x])
plt.plot(x,[a**3 for a in x])
# plt.show()

#Series
#here the indexing will be done automatically starting from zero till the length of an array
arr = np.array([11,12,[13,14],15,16])
#In case of dictionary the keys will be taken as index
data_dict = {'a':1,'b':2,'c':3}
series = pd.Series(data_dict)
#to access data u can access it using slicing
# print(series)

#DataFrame

list = [[20,30],[40,50],[60,70]]
list2 = [{'a':1,'b':2,'c':3},{'a':7,'b':8},{'a':11,'b':12,'c':13,'d':14}]
#if some keys not present in some dictionary and present in some, then takes NaN value for those columns. Here key will be taken as column names
#by defualt row indexing starts from zero till length of data structures. You can specify your own indexing like below
dataframe = pd.DataFrame(list2,index=['row-1','row-2','row-3'])
# print(dataframe)

#Other way to create Data frames
indexList = ['a','b','c']
data = {'one':pd.Series(np.arange(1,5),index=['a', 'b', 'c', 'd']),
        'two':pd.Series([11,12,13],index=indexList)}

dataframe2 = pd.DataFrame(data)
#Adding a new column to Dataframe with more rows..it will drop the extra row if index not matched
dataframe2['three'] = pd.Series([21,22,23,24,25],index=['a', 'b', 'c', 'd','e'])
#accessing perticular row using loc and iloc
# print(dataframe2.loc['a'])
# print(dataframe2.iloc[0])

#appending a row for all columns by default or u can specify perticular columns
row = pd.DataFrame([[99, 88], [101, 102]], columns=['two', 'three'])
dataframe2=dataframe2.append(row, sort=False)
print(dataframe2)