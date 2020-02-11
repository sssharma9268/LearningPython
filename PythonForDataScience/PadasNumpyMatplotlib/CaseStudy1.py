# 1. Extract data from the given SalaryGender CSV file and store the data from each column in a separate NumPy array
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

mydataset = pd.read_csv('mydataset\SalaryGender.csv')

salaryArray = np.array(mydataset.loc[:,"Salary"])
genderArray = np.array(mydataset.Gender)
ageArray = np.array(mydataset.Age)
phdArray = np.array(mydataset.PhD)

# print(mydataset)
# print("Age: "+str(ageArray))
# print("Salary: "+str(salaryArray))
# print("Phd: "+str(phdArray))
# print("Gender: "+str(genderArray))


# 2. Find:1. The number of men with a PhD 2. The number of women with a PhD
#Considering female as 1 and male as 0
no_of_men = 0
no_of_women = 0
gender_phd = pd.DataFrame(mydataset.loc[:,["Gender","PhD"]])
# print(gender_phd)
phd =0
for i in range(0,len(gender_phd)):
    if gender_phd.loc[i,"Gender"] == 1 and gender_phd.loc[i]["PhD"] ==1:
        no_of_women+=1
        phd+=1
    elif gender_phd.loc[i,"Gender"] == 0 and gender_phd.loc[i]["PhD"] ==1:
        no_of_men+=1
        phd+=1

# print("No of women with phd: "+str(no_of_women))
# print("No of men with phd: "+str(no_of_men))
# print(phd)

#Solution using group by function
grouped =  mydataset.groupby(["Gender","PhD"])
# print("No of men with phd: "+str(len(grouped.get_group((0,1)))))
# print("No of women with phd: "+str(len(grouped.get_group((1,1)))))


# 3. Use SalaryGender CSV file.
# Store the “Age” and “PhD” columns in one DataFrame
# and delete the data of all people who don’t have a PhD

age_phd = pd.DataFrame(mydataset.loc[:,["Age","PhD"]])

for i in range(0,len(age_phd)):
    if age_phd.loc[i]["PhD"] == 0:
        age_phd = age_phd.drop(i)

    # print(row[2])
# print(age_phd)

# 4. Calculate the total number of people who have a PhD degree
# from SalaryGender CSV file.
grouped = mydataset.groupby(["Gender","PhD"])
total = len(grouped.get_group((0,1)))+len(grouped.get_group((1,1)))
# print("Total no of people who have PhD: "+str(total))


# 5. How  do  you  Count  The  Number  Of  Times  Each  Value  Appears  In  An  Array  Of Integers?
# [0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]
# Answer should be array([4, 2, 1, 1, 3, 2, 0, 0, 0, 1])
# which means 0 comes 4 times, 1 comes 2 times, 2 comes 1 time, 3 comes 1 time and so on.
arr = np.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])

myset = set([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9])
mydict = dict.fromkeys(myset,0)

for i in arr:
    mydict[i] = mydict.get(i) + 1

# print(list(mydict.values()))



# 6. Create a numpy array [[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]]) and filter the elements greater than 5.

arr = np.array([[0, 1, 2],[ 3, 4, 5],[ 6, 7, 8],[ 9,10, 11]])

elements_greater_than_5 = []
for i in arr:
    for j in i:
        if j > 5:
            elements_greater_than_5.append(j)
# print(elements_greater_than_5)

# 7. Create a numpy array having NaN (Not a Number) and print it.
# array([ nan,   1.,   2.,  nan,   3.,   4.,   5.])
# Print the same array omitting all elements which are nan
from numpy import nan
import math
arr = np.array([ nan,   1.,   2.,  nan,   3.,   4.,   5.])

# arr = arr[ np.logical_not(np.isnan(arr)) ]
arr = [value for value in arr if not math.isnan(value)]
# print(arr)


# 8. Create  a  10x10  array  with  random  values  and  find  the  minimum  and  maximum values.
import numpy as np
x = np.random.random((10,10))
# print("Original Array:")
# print(x)
xmin, xmax = x.min(), x.max()
# print("Minimum and Maximum Values:")
# print(xmin, xmax)

# 9. Create a random vector of size 30 and find the mean value.
import numpy as np
vector = np.random.random((30))
# print("Mean value: ")
# print(vector.mean())

# 10. Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9
arr = np.arange(0,11)
values =[]
for x in arr:
    if x < 3 :
        values.append(x)
    if x > 9:
        values.append(x)
# print(values)

# 11. Create a random array of 3 rows and 3 columns and sort it according to 1st  column, 2nd column or 3rd column.

arr = np.random.random((3,3))
# print(arr)

arr.sort(axis = 0)
# print(arr)

# 12. Create a four dimensions array get sum over the last two axis at once.
arr = np.arange(0,16)
arr = arr.reshape((4,4))
# print(arr)
# print(arr.sum(axis=0))
# print(arr.sum(axis=1))

# 13. Create a random array and swap two rows of an array.
arr = np.random.random((3,3))
# print(arr)
arr[[0, 2]] = arr[[2, 0]]
# print(arr)
# 14. Create a random matrix and Compute a matrix rank.
from numpy.linalg import matrix_rank
arr = np.random.random((3,3))
# print(matrix_rank(arr))

# 15. Analyse  various  school  outcomes  in  Tennessee  using  pandas.  Suppose  you  are  a public   school administrator.
# Some   schools   in   your   state   of   Tennessee   are performing  below  average  academically.
# Your  superintendent,  under  pressure from frustrated parents and voters, approached you with the task of understanding
# why  these  schools  are  under - performing.
# To  improve  school  performance,  you need to learn more about these schools and their students, just as a business needs
# to understand its own strengths and weaknesses and its customers. Though you is eager  to  build  an  impressive  explanatory
# model,  you  know the  importance  of conducting  preliminary  research  to  prevent  possible  pitfalls  or blind  spots.
# Thus, you engages in a thorough exploratory analysis, which includes: a lit review, data
# collection, descriptive and inferential statistics, and data visualization.
# Phase 1 -Data Collection
# Here  is  a  data  of  every  public  school  in  middle  Tennessee.  The  data  also  includes various  demographic,  school
# faculty,  and  income  variables.  You  need  to  convert  the data into useful information.
# • Read the data in pandas data frame
# • Describe the data to find more details
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

mydataset = pd.read_csv('mydataset\middle_tn_schools.csv')
# print(mydataset.describe())
# Phase 2 - Group data by school ratings
# Chooses  indicators  that  describe  the  student  body  (for  example,
# reduced_lunch)  or school administration (stu_teach_ratio) hoping
# they will explain school_rating. reduced_lunch is  a  variable  measuring  the  average  percentage of students per school
# enrolled in a federal program that provides lunches for students
# from lower - income households. In short, reduced_lunch is a good proxy for household income.
# Isolates ‘reduced_lunch’ and groups the data by ‘school_rating’ using pandas groupby method and then uses describe on the
# re-shaped data
grouped = mydataset.groupby(["school_rating"])
reduced_lunch = pd.DataFrame(mydataset.loc[:,"reduced_lunch"])
# print(reduced_lunch)
# print(grouped.count())

# Phase 3 – Correlation analysis
# Find the correlation between ‘reduced_lunch’ and ‘school_rating’. The values in the correlation matrix table will be between -1
# and 1.
# A value of - 1 indicates the strongest possible negative correlation, meaning as one variable decreases the other increases.
# And a value of 1 indicates the opposite.
rl_sr = pd.DataFrame(mydataset.loc[:,["reduced_lunch","school_rating"]])
corr = rl_sr.corr()
# print(corr)

# Phase 4 – Scatter Plot
# Find the relationship between school_rating and reduced_lunch, Plot a graph with the two variables on a scatter plot.
# Each dot represents a school. The placement of the dot represents that school's rating (Y-axis) and the percentage of its
# students on reduced lunch(x-axis).    The    downward    trend    line    shows    the    negative    correlation
# Between school_rating and reduced_lunch (as one increases, the other decreases). The slope of the trend line indicates how
# much school_rating decreases as re duced_lunch increases.  A  steeper  slope  would  indicate  that  a  small  change in
# reduced_lunch has  a  big  impact  on school_rating while  a  more  horizontal  slope would  indicate  that  the  same  small
# change  in reduced_lunch has  a  smaller  impact on school_rating.
# rl_sr = pd.DataFrame(mydataset.loc[:,["reduced_lunch","school_rating"]])
# reduced_lunch = rl_sr["reduced_lunch"]
# school_rating = rl_sr["school_rating"]
# plt.scatter(reduced_lunch,school_rating)
# plt.xlabel('Reduced Lunch')
# plt.ylabel('School Rating')

# plt.show()
# Phase 5 –Correlation Matrix
# An efficient graph for assessing relationships is the correlation matrix, as seen below; its  color-coded  cells  make  it
# easier  to  interpret  than  the  tabular  correlation  matrix above. Red cells indicate positive correlation; blue cells
# indicate negative correlation; white cells indicate no correlation. The darker the colors, the stronger the correlation
# (positive or negative) between those two variables. Draw a graph of correlation matrix having all important fields of data frame.
import seaborn as sns
corr = mydataset.corr()
plt.figure(figsize=(10,10))
sns.heatmap(corr,cbar=True,square = True, cmap = "YlGnBu")
plt.show()
# print(corr)


