import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import cross_val_score
import seaborn as sns # used for plot interactive graph. I like it most for plot
from sklearn.linear_model import LogisticRegression # to apply the Logistic regression
from sklearn.model_selection import train_test_split # to split the data into two parts
from sklearn import metrics # for the check the error and accuracy of the model
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('datasets\data.csv',header=0)

# print(data.head(6))
# print(data.info())

data.drop("Unnamed: 32",axis=1,inplace=True)
data.drop("id",axis=1,inplace=True)
# print(data.columns)
data['diagnosis']=data['diagnosis'].map({'M':1,'B':0})
# print(data.describe())

sns.countplot(data['diagnosis'],label="Count")
#to check the distribution of classes in our dataset. How many malignant data is there and how many beningnant data are there

# plt.show()

corr = data.corr() # .corr is used for find corelation
plt.figure(figsize=(14,14))
sns.heatmap(corr, cbar = True,  square = True,
            cmap= 'coolwarm')
# plt.show()

prediction_var = ['texture_mean','perimeter_mean','smoothness_mean','compactness_mean','symmetry_mean']

train, test = train_test_split(data, test_size = 0.3)# in this our main data is splitted into train and test
# we can check their dimension
# print(train.shape)
# print(test.shape)

train_X = train[prediction_var]# taking the training data input
train_y=train.diagnosis# This is output of our training data
# same we have to do for test
test_X= test[prediction_var] # taking test data inputs
test_y =test.diagnosis   #output value of test dat

logistic = LogisticRegression()
logistic.fit(train_X,train_y)
temp=logistic.predict(test_X)
# print(metrics.accuracy_score(temp,test_y)) # to check the accuracy

clf = DecisionTreeClassifier(random_state=0)
cross_val_score(clf, train_X, train_y, cv=10)
clf.fit(train_X,train_y, sample_weight=None, check_input=True, X_idx_sorted=None)
clf.get_params(deep=True)
clf.predict(test_X, check_input=True)
clf.predict_log_proba(test_X)
clf.predict(test_X,check_input=True)
print(clf.score(test_X,test_y, sample_weight=None))

from sklearn.externals.six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())