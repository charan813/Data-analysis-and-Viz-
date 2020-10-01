import pandas as pd
movies= pd.read_csv("E:/Study/Data Science/P4-Movie-Ratings.csv")

movies.head()
movies.columns=['Film','Genre','Rotten_ratings','Audience_ratings','Budget_millions','Year']

movies.Film=movies.Film.astype('category')
movies.Genre=movies.Genre.astype('category')
movies.Year=movies.Year.astype('category')

from matplotlib import pyplot as plt
import seaborn as sns


#Joint plots
sns.set(style="white", color_codes=True)
j1= sns.jointplot(data=movies,x='Rotten_ratings', y='Audience_ratings') # hex allows you to observe clusters

#HISTOGRAMS

#distribution plots
m1=sns.distplot(movies.Audience_ratings,bins=15)
m2=sns.distplot(movies.Rotten_ratings,bins=15)

#Histograms
n1=plt.hist(movies.Audience_ratings,bins=15)
n2=plt.hist(movies.Rotten_ratings,bins=15)

#Stacked histograms/ Distribution plot

plt.hist(movies.Budget_millions)
movies[movies.Genre == "Drama"].Budget_millions

#combined chart overlayed
plt.hist(movies[movies.Genre=="Action"].Budget_millions,label='Action')
plt.hist(movies[movies.Genre=="Drama"].Budget_millions,label='Drama')
plt.hist(movies[movies.Genre=="Thriller"].Budget_millions,label='Thriller')
plt.legend()
plt.show()

x=[movies[movies.Genre=="Action"].Budget_millions, movies[movies.Genre=="Drama"].Budget_millions, movies[movies.Genre=="Thriller"].Budget_millions]
plt.hist(x,stacked= True)

#Doing it for multiples Genres using loops
list1=list() # creating an empty list
mylabels=list()
for gen in movies.Genre.cat.categories:
    list1.append(movies[movies.Genre==gen].Budget_millions)
    mylabels.append(gen)
    
plt.hist(list1,bins=15,stacked=False,label=mylabels)
plt.legend()
plt.show()
#Scatter plot
viz1 = sns.lmplot(data=movies,x='Rotten_ratings',y='Audience_ratings',hue='Genre',fit_reg=False)

#Kernel Density Estimate plot ... Bivariate Distribution
k1=sns.kdeplot(movies.Rotten_ratings,movies.Audience_ratings,shade=True)
sns.set_style('dark')
k2=sns.kdeplot(movies.Budget_millions,movies.Audience_ratings)
k3=sns.kdeplot(movies.Budget_millions,movies.Rotten_ratings)

# SUBPLOTS

f, axes= plt.subplots(1,2, figsize=(12,6),sharex=True,sharey=True)
k2=sns.kdeplot(movies.Budget_millions,movies.Audience_ratings,ax=axes[0])
k3=sns.kdeplot(movies.Budget_millions,movies.Rotten_ratings,ax=axes[1])
k2.set(xlim=(-20,160))

#boxplots vs violinplot
v=sns.violinplot(data=movies,x='Genre',y='Rotten_ratings')
w=sns.boxplot(data=movies,x='Genre',y='Rotten_ratings')
#Genre specific violinplot broken down by year
v2=sns.violinplot(data=movies[movies.Genre=='Drama'],x='Year',y='Rotten_ratings')

#FacetGrid both lines of code must run together
g=sns.FacetGrid(movies,row='Genre',col="Year",hue='Genre')
kws=dict(s=50,linewidth=0.5, edgecolor='black')
g=g.map(plt.scatter,'Rotten_ratings','Audience_ratings',**kws)
#                    facet grids can be populated with any type of chart
g=sns.FacetGrid(movies,row='Genre',col="Year",hue='Genre')
g=g.map(plt.hist,'Budget_millions')



#controlling axes and adding diagonals

