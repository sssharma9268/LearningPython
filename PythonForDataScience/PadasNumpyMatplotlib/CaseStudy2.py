# Business challenge/requirement
# You are a data analyst with University of Cal USA (Not a machine learning expert yet as you still have not completed ML with
# Python Course :-)).The University has data of Math, Physics and Data Structure  score of sophomore students. This data is stored in
# different files. The University has hired a data science company to do analysis of scores and find if there is any correlation of score
# with age, ethnicity etc. Before the data is given to the company you have to do data wrangling. Key issues Ensure students identify is
# not revealed   to the agency and only relevant data is shared Considerations NONE
# Data volume-In thousands, but only around 1800 records are shared in files MathScoreTerm1.csv
# DSScoreTerm1.csv, PhysicsScoreTerm1.csv
# Additional information-NA
# Business benefits-
# University can get more students enrollment by improving its international ranking through personalized course/curriculum for students
# Approach to Solve
# You have to use fundamentals of Numpy and Pandas covered in module 4.
# 1. Read the three csv files which contains the score of same students in term1 for each Subject
# 2. Remove the name and ethnicity column (to ensure confidentiality)
# 3. Fill missing score data with zero
# 4. Merge the three files
# 5. Change Sex(M/F) Columnto 1/2 for further analysis
# 6. Store the data in new file –ScoreFinal.csv
# Enhancements for code
# You can try these enhancements in code
# 1. Convert ethnicity to numerical value
# 2. Fill the missing score for a student to the average of the class
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

mathsDataset = pd.read_csv('mydataset\MathScoreTerm1.csv')
physicsDataset = pd.read_csv('mydataset\PhysicsScoreTerm1.csv')
dataStructureDataset = pd.read_csv('mydataset\DSScoreTerm1.csv')

dataStructureDataset.drop("Name",axis=1,inplace=True)
dataStructureDataset.drop("Ethinicity",axis=1,inplace=True)
mathsDataset.drop("Name",axis=1,inplace=True)
mathsDataset.drop("Ethinicity",axis=1,inplace=True)
physicsDataset.drop("Name",axis=1,inplace=True)
physicsDataset.drop("Ethinicity",axis=1,inplace=True)


for i in range(0,len(dataStructureDataset)):
    if np.isnan(dataStructureDataset.loc[i,"Score"]):
        dataStructureDataset.at[i,"Score"] = 0
for i in range(0,len(mathsDataset)):
    if np.isnan(mathsDataset.loc[i,"Score"]):
        mathsDataset.at[i,"Score"] = 0

for i in range(0,len(physicsDataset)):
    if np.isnan(physicsDataset.loc[i,"Score"]):
        physicsDataset.at[i,"Score"] = 0


df3=pd.merge(mathsDataset,physicsDataset,on=['Age','Sex','ID'],how='inner')
df3 = pd.merge(df3,dataStructureDataset,on=['Age','Sex','ID'])
df3['Sex']=df3['Sex'].map({'M':1,'F':2})


print(df3)