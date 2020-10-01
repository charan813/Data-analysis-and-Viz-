import pandas as pd
import os

#Method 1 : Specify full path to file

stats= pd.read_csv("E:/Study/Data Science/Section 5/P4-Demographic-Data.csv")

# Number of rows
len(stats) #195 rows imported

#number of columns
len(stats.columns)

# Top rows
stats.head(7) # printing out Bottom 7 rows . Default n rows set to 5

# Bottom Rows
stats.tail(7) # printing out Bottom 7 rows . Default n rows set to 5

#information columns
stats.info()

#stats on columns
stats.describe().transpose()

#renaming Columns of a dataframe
stats.columns=['CountryName','CountryCode','BirthRate',\
               'InternetUsers','IncomeGroup']

    
# Subsetting Dataframes
# 1.Rows
# 2.columns
# 3.Combine the two

# Part 1. Rows
stats[:26]

# Exercise to reverse the dataframe
stats[::-1] #Used the slicing principles

#get only every 20th row
stats[::20]

# Part 2 . Columns
stats[['CountryName','BirthRate','IncomeGroup']].head()

#quickaccess- requires name/ column name to be oneword mainly for a single column
stats.CountryName
stats.BirthRate

#Part3. Combining the two
stats[:40][['CountryName','BirthRate']]#getting 40 rows and all columns.. then subsetting for column names
stats[['CountryName','BirthRate']][:40]#Getting subset of columns and then slicing for rows

stats.head()



#### Filtering Data Frames.
# Filter by Rows is the norm
 
Filter = stats.InternetUsers<2
Filter2= stats.BirthRate>40

#Filtering Data Frame without using new variables

stats[Filter & Filter2]
stats[(stats.BirthRate >40) & (stats.InternetUsers<2)]

#Filtering Data Frame for a single Row
stats[stats.CountryName == "Malta"]

### Accessing Individual elements 
#.at for labels(P.S Even integers are treated as labels)
# iat() for direct integer location

stats.iat[3,4]
stats.iat[0,1]

stats.at[2,'BirthRate']
# why we need .at

sub10=stats[::10]
sub10.iat[10,0]
sub10.at[10,"CountryName"]
# gives different results. iat[] checks based on the index of the filtered data frame on sub10
# .at[] is looking for label or id 10. hence gives azerbaijan instead of libya

### Introduction to SEABORN

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=8,6
import seaborn as sns

#distribution plot
viz1= sns.distplot(stats["InternetUsers"],bins=30)

#Boxplots
viz2= sns.boxplot(data= stats,x='IncomeGroup',y='BirthRate')

#seaborn gallery

viz3= sns.lmplot(data=stats,x='InternetUsers',y='BirthRate',fit_reg=False,hue='IncomeGroup',size=10,markers='x')

#######KEYWORD ARGUEMENTS IN PYTHON
## Marker SIZE

viz3= sns.lmplot(data=stats,x='InternetUsers',y='BirthRate',fit_reg=False,hue='IncomeGroup',size=10, markers='o',scatter_kws={'s':100})









