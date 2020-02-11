# Business challenge/requirement
# BigMart is one of the biggest retailer of Europe and has operations across multiple countries.
# You are a data analyst in IT team of BigMart. Invoice and SKU wise Sales
# Data for Year 2011 is shared with you. You need to prepare meaningful charts to show case the various sales trends for 2011 to
# top management.
# Key issues
# Data should be displayed pictorially to capture the attention of top management
# Considerations  NONE
# Data volume-Approx 500K records –
# file BigMartSalesData.csv
# Business benefits
# This exercise is an annual exercise and BigMart makes important investment decision based on trends Approach to Solve
# You have to use fundamentals of Matplotlib covered in module 5 and plot following 4 chart/graph

# 1. Plot Total Sales Per Month for Year 2011.  How the total sales
# Have increased over months in Year 2011. Which month has lowest Sales?
# 2. Plot Total Sales Per Month for Year 2011 as Bar Chart.  Is Bar Chart Better to visualize than Simple Plot?
# 3. Plot Pie Chart for Year 2011 Country Wise. Which Country contributes highest towards sales?
# 4. Plot Scatter Plot for the invoice amounts and see the concentration of amount. In which range most of the invoice amounts are
# concentrated
# Enhancements for code You can try these enhancements in code
# 1. Change the bar chart to show the value of bar
# 2. In Pie Chart Play With Parameters shadow =True, startangle=90 and see how different the chart looks
# 3. In scatter plot change the color of Scatter Points
#
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np

ds = pd.read_csv('mydataset\BigMartSalesData.csv')
data = pd.DataFrame(ds.loc[:,['Amount','Month','Year']])


total_sales = np.zeros(13)


# for i in range(len(data)):
#     if data.loc[i,'Year'] == 2011:
#         month = data.loc[i,'Month']
#         sales = data.loc[i,'Amount']
#         total_sales[month] = total_sales[month] +sales

#Simple plot and bar chart
# x= np.arange(13)
# plt.plot(x,total_sales)
# plt.bar(x,total_sales)
# plt.grid(True)
# plt.xlabel('Months')
# plt.ylabel('Total Sales')
# plt.title('Total Sales Each Month for Year 2011')
# plt.show()


#Pie Plot

# df_new_bigdata = ds[ds['Year'] == 2011]
# country_wise_sales = df_new_bigdata.groupby('Country').sum()['Amount']
# plt.pie(country_wise_sales.values, labels=country_wise_sales.index,autopct='%1.1f%%')
# plt.title('Country wise sales for 2011')
# plt.show()

# Scatter Plot
# plt.figure(figsize=(30,30))
selected_data=ds.loc[:,['InvoiceNo','Amount']]
x=np.arange(500000)
y=np.array(selected_data['Amount'])
print(x,y)
plt.scatter(y,y)
# plt.xlim(0,20000)
plt.show()


# import pandas
# import numpy
# import matplotlib.pyplot as plt
# plt.figure(figsize=(30,30))
# dataset=pandas.read_csv('..\datasets\AllCountries.csv')
# selected_data=dataset.loc[:,['Country','GDP','BirthRate']]
# x=numpy.array(selected_data["GDP"])
# y=numpy.array(selected_data['BirthRate'])
# print(x,y)
# plt.scatter(x,y)
# plt.xlim(0,20000)
# plt.show()

#

# import pandas
# import matplotlib.pyplot as plt
# plt.figure(figsize=(50,50))
# dataset=pandas.read_csv('..\datasets\AllCountries.csv')
# selected_data=dataset.loc[:,['Country','GDP','BirthRate']]
# sorted_data=selected_data.sort_values(by='GDP',ascending=False)
# selected_sorted_data=sorted_data.iloc[:10]
# print(selected_sorted_data)
# plt.pie(selected_sorted_data['GDP'],labels=selected_sorted_data['Country'])
# plt.show()


#  plt.pie(df.sum(numeric_only=True).values, labels = df.sum(numeric_only=True).index)
# plt.axis('equal')
# plt.show()

# from sklearn.preprocessing import Imputer
# imputed_values = Imputer(missing_values='NaN', strategy='mean',axis=0)
# df_salary_imputed = imputed_values.fit_transform(df_salary)


# import matplotlib.pyplot as plt
# df_new_bigdata = df_bigdata[df_bigdata['Year'] == 2011]
# country_wise_sales = df_new_bigdata.groupby('Country').sum()['Amount']
# plt.pie(country_wise_sales.values, labels=country_wise_sales.index,autopct='%1.1f%%')
# plt.title('Country wise sales for 2011')
# plt.show()



