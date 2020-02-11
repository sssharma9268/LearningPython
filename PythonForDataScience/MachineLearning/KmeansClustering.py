
from copy import deepcopy
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()  # for plot styling
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16,9)
plt.style.use('ggplot')
#importing the dataset
data = pd.read_csv('datasets\movie_metadata1.csv')
print (data.shape)
print (data.head)




new_data = [col for col in data.columns if 'facebook' in col]
print(new_data)