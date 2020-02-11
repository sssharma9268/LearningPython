# 1.You are given a dataset, which is present in the LMS, containing the number of hurricanes occurring in the United States along the
# coast of the Atlantic. Load the data from the dataset into your program
# and plot a Bar Graph of the data, taking the Year as the x-axis and the number of hurricanes occurring as the Y-axis.
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

ds = pd.read_csv('mydataset\Hurricanes.csv')

x_year = ds.loc[:,"Year"]

y_Hurricanes = ds.loc[:,"Hurricanes"]

# plt.bar(x_year,y_Hurricanes)
# plt.xlabel("Years")
# plt.ylabel("Hurricanes")
# plt.title("Hurricanes occuring each year")
# plt.show()

# 2.The dataset given, records data of city temperatures over the years
# ’2014 and 2015. Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow.
ds = pd.read_csv('mydataset\CityTemps.csv')
# print(ds)
city_temp1 = np.array(ds["San Francisco"])
city_temp2 = np.array(ds["Moscow"])
year = np.array(ds["Year"])
# plt.hist([city_temp1,city_temp2],label=['San franciso','Moscow'])
# plt.legend()
# plt.show()


# 3.Create csv file from the data file available in LMS which goes by the name ‘M4_assign_dataset’ and read this file into a pandas
# data frame
data = pd.read_csv('mydataset\data_file.txt')
ds = pd.DataFrame(data)
ds.to_csv('mydataset\data_file.csv', index=False)
# print(ds)

# 4. Let the x axis data points and y axis data points are X = [1,2,3,4]
# y = [20, 21, 20.5, 20.8]
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]
# 5.1: Draw a Simple plot


# 5.2: Configure the line and markers in simple plot




# 5.3: configure the axes
# 5.4: Give title of Graph & labels of x axis and y axis
# 5.5: Give error bar if  y_error = [0.12, 0.13, 0.2, 0.1]

# 5.6: define width, height as figsize=(4,5) DPI and adjust plot dpi=100
# 5.7: Give a font size of 14
# y_error = [0.12, 0.13, 0.2, 0.1]
# plt.figure(figsize=(4,5))
# plt.plot(x,y_error,label='error bar')
# plt.plot(x,y, label='simple line')
# plt.grid(True)
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Simple Plot')
# plt.legend()
# plt.rc('font',size=14)
# plt.show()


# 5.8: Draw a scatter graph of any 50 random values of x and y axis
x = np.random.random(50)
y = np.random.random(50)
# plt.scatter(x,y)
# plt.show()

# 5.9: Create a dataframe from following data 'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
# 'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 'female': [0, 1, 1, 0, 1], 'age': [42, 52, 36, 24, 73],
# 'preTestScore': [4, 24, 31, 2, 3], 'postTestScore': [25, 94, 57, 62, 70]
# Draw a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}

df = pd.DataFrame(data)
pre = np.array(df["preTestScore"])
post = np.array(df["postTestScore"])
age = np.array(df["age"])




# 5.10: Draw a Scatterplot from the data in question 9 of preTestScore and postTestScore with the size = 300 and the color determined
# by sex
pre = list(df["preTestScore"])
post = list(df["postTestScore"])
colors=[]
sex = list(df["female"])

for x in sex:
        if x == 0:
                colors.append('b')
        else:
                colors.append('r')

print(colors)
for i in range(len(pre)):
    plt.scatter(pre[i], post[i], s=300, color=colors[i])

plt.show()


