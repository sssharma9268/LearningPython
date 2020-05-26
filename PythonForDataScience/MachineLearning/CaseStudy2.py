# Objectives:
# 1.Provide the learner some more practice
# For exploratory data analysis.
# 2.Equip the learner to fit and evaluate a linear regression model.
# Questions:
# 1.Load the data from “cereal.csv” and plot histograms of sugar and vitamin content across different cereals.
# [Hint: Extract values of a specific column using their labels and use hist method of pyplot]
# 2. The names of the manufactures are coded using alphabets, create a new column with their fullname using the below mapping.
# 'N': 'Nabisco',
# 'Q': 'Quaker Oats',
# 'K': 'Kelloggs',
# 'R': 'Raslston Purina',
# 'G': 'General Mills' ,
# 'P' :'Post' ,
# 'A':'American Home Foods Products'
# Create a bar plot where each manufacturer is on the y axis and the h
# eight of the bars depict the number of cereals manufactured by them.
# [Hint: Try using countplot this time or bar method of pyplot]
# 3. Extract the rating as your target variable ‘y’ and all numerical parameters as your predictors ‘x’. Separate 25% of your data as test set.
# 4. Fit a linear regression module and measure the mean squared error on test dataset.
# [Hint: Explore linear models and metrics section of sklearn documentation]
#
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

cereal = pd.read_csv('datasets\cereal.csv')

sugars= cereal['sugars']
vitamins = cereal['vitamins']
# print(sugars)
# plt.hist(np.array(sugars),np.array(vitamins))
# cereal.plot(x='sugars',y='vitamins',kind='hist')
# plt.show()
# print(cereal.head())

mydict = {'N': 'Nabisco','Q': 'Quaker Oats','K': 'Kelloggs','R': 'Raslston Purina',
'G': 'General Mills' ,
'P' :'Post' ,
'A':'American Home Foods Products'}

mfr = cereal['mfr']

for row in range(len(cereal)):
    # print(cereal.loc[row,'mfr'])
    # print(mydict.get(cereal.loc[row,'mfr']))
    cereal.loc[row,'fullname'] = mydict.get(cereal.loc[row,'mfr'])

print(cereal.columns)

df = cereal[{'fullname','cups'}]
df.plot.bar()
plt.show
fullname = df['fullname']
fullnamess = fullname.drop_duplicates()
print(fullnamess)
y_pos = np.arange(len(fullnamess))
plt.bar(y_pos, list(df['cups']), align='center', alpha=0.5)
plt.xticks(y_pos, fullnamess)
plt.ylabel('Manufacturers')
plt.title('No of Cereals manufactured by manufacturers')
plt.show()

import seaborn as sns

#creating a correlation matrix

cereal.rating = pd.Categorical(cereal.rating)
cereal['rating'] = cereal.rating.cat.codes
print(cereal.head())
y = cereal.rating

print(y)
cereal.drop('rating',axis=1,inplace=True)
cereal.drop('name',axis=1,inplace=True)
cereal.drop('fullname',axis=1,inplace=True)
cereal.drop('mfr',axis=1,inplace=True)
cereal.drop('type',axis=1,inplace=True)
x=cereal

correlations = cereal.corr()
sns.heatmap(correlations,square = True, cmap = "YlGnBu")
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()

from sklearn.model_selection import train_test_split
from sklearn import metrics
#testing data size is of 33% of entire data
x_train, x_test, y_train, y_test =train_test_split(x,y, test_size = 0.25, random_state =5)

print(x_train.head())
from sklearn.linear_model import LinearRegression
#fitting our model to train and test
lm = LinearRegression()
model = lm.fit(x_train,y_train)

pred_y = lm.predict(x_test)
print(metrics.accuracy_score(pred_y,y_test,normalize=True,sample_weight=None))
plt.scatter(y_test,pred_y,'c','b')
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
# plt.show()
