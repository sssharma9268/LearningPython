import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

bos1 = pd.read_csv('datasets\BostonHousing.csv')

x = bos1.iloc[:,0:13]
y = bos1["medv"]

# print(x,y)

# import seaborn as sns
# names = []
# #creating a correlation matrix
# correlations = bos1.corr()
# sns.heatmap(correlations,square = True, cmap = "YlGnBu")
# plt.yticks(rotation=0)
# plt.xticks(rotation=90)
# plt.show()

from sklearn.model_selection import train_test_split
#testing data size is of 33% of entire data
x_train, x_test, y_train, y_test =train_test_split(x,y, test_size = 0.33, random_state =5)

print(x_train.head())
from sklearn.linear_model import LinearRegression
#fitting our model to train and test
lm = LinearRegression()
model = lm.fit(x_train,y_train)

pred_y = lm.predict(x_test)

plt.scatter(y_test,pred_y,'c','b')
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.show()