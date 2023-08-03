import openpyxl
import numpy as np
import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl

data = pd.read_excel('Canada.xlsx',
                   sheet_name='Canada by Citizenship',
                   skiprows=range(20),
                   skipfooter=2)

print(data.head())


# print column headers
print(data.columns)

# remove meaningless columns for smaller manageable dataset
data.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
print(data.head())

# change column names
data.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
print(data.columns)

# add total column --> total immigrants
data['Total']=data.sum(axis=1)
print(data.head())

# check null values
print(data.isnull().sum())

# set the 'country' column as the index
data=data.set_index('Country')
print(data.head)

print(plt.style.available)
mpl.style.use(['ggplot'])


# Switzerland example
years = list(map(int, range(1980, 2014)))
# Switzerland immigration data per years
data.loc['Switzerland',  years]
data.loc['Switzerland', years].plot()
plt.title('Immigration from Switzerland')
plt.ylabel('Number of immigrats')
plt.xlabel('Years')
plt.show()


# immigration trend over the years for India, Pakistan and Bangladesh
ind_pak_ban = data.loc[['India', 'Pakistan', 'Bangladesh'], years]
ind_pak_ban.head()
ind_pak_ban.T
ind_pak_ban.T.plot()
plt.show()

# 4.6.4
# pie plot
# number of immigrants per continent
cont = data.groupby('Continent', axis=0).sum()
cont['Total'].plot(kind='pie', figsize=(7, 7), autopct='%1.1f%%', shadow=True)
plt.title('Immigration per continent')
plt.axis('equal')
plt.show()


# box plot
# number of immigrats of China and Canada over the years
china = data.loc[['China'], years].T
china.plot(kind='box', figsize=(8,6))
plt.title('Box plot of Chinese immigrants')
plt.ylabel('Number of immigrants')
plt.show()


# plot numerous box plots
# box plot of immigrants from India, Pakistan and Bangladesh
ind_pak_ban.T.plot(kind='box', figsize=(8, 7))
plt.title('Box plots of Indian, Pakistanis  and Bangladeshi immigrants')
plt.ylabel('Number of immigrants')
plt.show()


# scatter plot
# new DataFrame containing the years as an index and the total number of immigrants each year
totalPerYear = pd.DataFrame(data[years].sum(axis=0))
totalPerYear.head()
print(totalPerYear.head())
# convert years to integers and make DataFrame presentable
totalPerYear.index = map(int, totalPerYear.index)
totalPerYear.reset_index(inplace=True)
totalPerYear.head()
print(totalPerYear.head())


# area plot
# DataFrame with information for India, China, Pakistan and France
top = data.loc[['India', 'China', 'Pakistan', 'France'], years]
top = top.T
print(top)
colors = ['Black', 'Green', 'Blue', 'Red']
top.plot(kind='area', stacked=False, figsize=(20, 10))
plt.title('Immigration trend from Europe')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()


# histogram
top.plot.hist()
plt.title('Histogram of immigration from Some Populous Countries')
plt.ylabel('Number of years')
plt.xlabel('Number of immigrants')

# 4.6.10
# specify the number of bins and find the bind edges
count, bin_edges = np.histogram(top, 15)
top.plot(kind='hist', figsize=(14, 6), bins=15, alpha=0.6, xticks=bin_edges, color=colors)
plt.show()

# 4.6.11
# stacked histogram
top.plot(kind='hist', figsize=(12, 6), bins=15, xticks=bin_edges, color=colors, stacked=True)
plt.title('Histogram of immigration from Some Populous Countries')
plt.ylabel('Number of years')
plt.xlabel('Number of immigrants')
plt.show()


# bar plot
# number of immigrants from France per year
france = data.loc['France', years]
france.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Year')
plt.ylabel('Number of immigrants')
plt.title('Immigrants from France')
plt.show()


# increase trend since 1997 for over a decade using an annotate function
france.plot(kind='bar', figsize=(10,6))
plt.xlabel('Year')
plt.ylabel('Number of immigrants')
plt.title('Immigrants from France')
plt.annotate('Increasing trend', xy=(19, 4500), rotation=23, va='bottom', ha='left')
plt.annotate('', xy=(29, 5500), xytext=(17, 3800), xycoords='data', arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='black', lw=1.5))
plt.show()


# # put bars horizontally
data_top10 = pd.DataFrame(data.nlargest(10, 'Total')['Total'].sort_values(ascending=True))
data_top10.plot.barh(legend=False, color='crimson', edgecolor='LightCoral')
plt.title('Top 10 immigrant countries to Canada from 1980 to 2013', color='black')
plt.xlabel('Number of immigrants', color='black')
plt.ylabel('Country', color='black')
plt.xticks(color='black')
plt.yticks(color='black')
plt.show()





# pie plot
# number of immigrants per continent
# define colors
colors = ['lightgreen', 'lightblue', 'pink', 'purple', 'grey', 'gold']
# define the ratio of fragments' gaps
explodeTuple = (0.05, 0.05, 0.05, 0.05, 0.05, 0.05)
# plot pie chart
cont = data.groupby('Continent', axis=0).sum()
cont['Total'].plot(kind='pie', figsize=(7, 7), autopct='%1.1f%%', shadow=True, colors=colors, explode=explodeTuple, startangle=60)
plt.title('Immigration per continent')
plt.show()

# scatter plot
# number of immigrants in Canada over the years
canada = data.loc[['Canada'], years].T
plt.scatter(canada, years)
plt.title('Total immigrants in Canada per year')
plt.xlabel('Number of immigrants')
plt.ylabel('Year')
plt.show()

# area plot
# DataFrame with information for India, China, Pakistan and France
top = data.loc[['India', 'China', 'Pakistan', 'France'], years]
top = top.T
print(top)
colors = ['Black', 'Green', 'Blue', 'Red']
top.plot(kind='area', stacked=True, figsize=(20, 10))
plt.title('Immigration trend from Europe')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')
plt.show()

# bar plot
# number of immigrants from Iceland per year
data_iceland = data.loc['Iceland', years]
data_iceland.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Year')
plt.ylabel('Number of immigrants')
plt.title('Immigrants from Iceland')
plt.show()

# horizontal bar plot
# top 15 immigrants to Canada per year
data_top15 = pd.DataFrame(data.nlargest(15, 'Total')['Total'].sort_values(ascending=True))
ax=data_top15.plot.barh(legend=False)
plt.title('Top 15 immigrant countries to Canada from 1980 to 2013')
plt.xlabel('Number of immigrants')
plt.ylabel('Country')
ax.bar_label(ax.containers[0], label_type='edge', padding=15)
plt.show()

