#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Data Visualization Lab**
# 

# Estimated time needed: **45 to 60** minutes
# 

# In this assignment you will be focusing on the visualization of data.
# 
# The data set will be presented to you in the form of a RDBMS.
# 
# You will have to use SQL queries to extract the data.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# *   Visualize the distribution of data.
# 
# *   Visualize the relationship between two features.
# 
# *   Visualize composition of data.
# 
# *   Visualize comparison of data.
# 

# <hr>
# 

# ## Demo: How to work with database
# 

# Download database file.
# 

# In[2]:


get_ipython().system('wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m4_survey_data.sqlite')


# Connect to the database.
# 

# In[3]:


import sqlite3
conn = sqlite3.connect("m4_survey_data.sqlite") # open a database connection


# Import pandas module.
# 

# In[4]:


import pandas as pd


# ## Demo: How to run an sql query
# 

# In[5]:


# print how many rows are there in the table named 'master'
QUERY = """
SELECT COUNT(*)
FROM master
"""

# the read_sql_query runs the sql query and returns the data as a dataframe
df = pd.read_sql_query(QUERY,conn)
df.head()


# ## Demo: How to list all tables
# 

# In[6]:


# print all the tables names in the database
QUERY = """
SELECT name as Table_Name FROM
sqlite_master WHERE
type = 'table'
"""
# the read_sql_query runs the sql query and returns the data as a dataframe
pd.read_sql_query(QUERY,conn)


# ## Demo: How to run a group by query
# 

# In[7]:


QUERY = """
SELECT Age,COUNT(*) as count
FROM master
group by age
order by age
"""
pd.read_sql_query(QUERY,conn)


# ## Demo: How to describe a table
# 

# In[8]:


table_name = 'master'  # the table you wish to describe

QUERY = """
SELECT sql FROM sqlite_master
WHERE name= '{}'
""".format(table_name)

df = pd.read_sql_query(QUERY,conn)
print(df.iat[0,0])


# # Hands-on Lab
# 

# ## Visualizing distribution of data
# 

# ### Histograms
# 

# Plot a histogram of `ConvertedComp.`
# 

# In[9]:


# your code goes here
QUERY = """
SELECT ConvertedComp 
FROM master
"""
data_ConvertedComp = (pd.read_sql_query(QUERY,conn)).dropna()
data_ConvertedComp.plot(kind='hist', figsize=(15,5), title='Converted Comp Distribution')


# ### Box Plots
# 

# Plot a box plot of `Age.`
# 

# In[10]:


# your code goes here
QUERY = """
SELECT Age
FROM master
"""

data_Age = (pd.read_sql_query(QUERY, conn)).dropna()
data_Age.plot(kind='box', figsize=(5, 5), title='Age_Scatter_Plot')


# ## Visualizing relationships in data
# 

# ### Scatter Plots
# 

# Create a scatter plot of `Age` and `WorkWeekHrs.`
# 

# In[11]:


# your code goes here
QUERY = """
SELECT Age as Age, WorkWeekHrs as WorkWeekHrs
FROM master
"""

# pd.read_sql_query(QUERY,conn)
data = (pd.read_sql_query(QUERY,conn)).dropna()

# len(data['Age'].dropna())
# len(data['WorkWeekHrs'].dropna())

# data['Age'].value_counts().sum()
# data['WorkWeekHrs'].value_counts().sum()
data.plot(kind='scatter', x='Age', y='WorkWeekHrs')


# ### Bubble Plots
# 

# Create a bubble plot of `WorkWeekHrs` and `CodeRevHrs`, use `Age` column as bubble size.
# 

# In[96]:


# your code goes here
QUERY = """
SELECT WorkWeekHrs as WorkWeekHrs, CodeRevHrs as CodeRevHrs
FROM master
"""

data_bubble = (pd.read_sql_query(QUERY, conn)).dropna()

data_bubble.plot(kind='scatter', x='WorkWeekHrs', y='CodeRevHrs', alpha=0.5, s=data_bubble['WorkWeekHrs']/data_bubble['CodeRevHrs'])


# ## Visualizing composition of data
# 

# ### Pie Charts
# 

# Create a pie chart of the top 5 databases that respondents wish to learn next year. Label the pie chart with database names. Display percentages of each database on the pie chart.
# 

# In[112]:


# your code goes here

QUERY = """
SELECT * 
FROM DatabaseDesireNextYear 
WHERE DatabaseDesireNextYear IS NOT NULL

"""
data_dd_next_year = (pd.read_sql_query(QUERY, conn)).dropna()

data_pie = (data_dd_next_year['DatabaseDesireNextYear'].value_counts()).head(5)

data_pie.plot(kind='pie', y='0', title='Pie Chart Top 5 DataBase', shadow=True, autopct='%1.2f%%', labeldistance=0.9)

# data_numerical = pd.DataFrame([], index=data_dd_next_year['DatabaseDesireNextYear'].unique())

# QUERY = """
# SELECT *
# FROM master
# WHERE Respondent is not NULL
# """
# # DatabaseDesireNextYear

# data_respondent = (pd.read_sql_query(QUERY, conn)).dropna()


# ### Stacked Charts
# 

# Create a stacked chart of median `WorkWeekHrs` and `CodeRevHrs` for the age group 30 to 35.
# 

# In[98]:


# your code goes here
QUERY = """
SELECT Age, WorkWeekHrs, CodeRevHrs from master
WHERE Age BETWEEN 30 AND 35
"""

data_stacked = (pd.read_sql_query(QUERY, conn)).dropna()

extra_data = data_stacked.groupby(['Age'])['WorkWeekHrs','CodeRevHrs'].median()

# data_stacked_median = data_stacked[data_stacked['Age'] == data_stacked['Age'].median() ]

# extra_data = pd.DataFrame([data_stacked['WorkWeekHrs'], data_stacked['CodeRevHrs']]).transpose()

extra_data.plot(kind="bar", stacked=True)


# ## Visualizing comparison of data
# 

# ### Line Chart
# 

# Plot the median `ConvertedComp` for all ages from 45 to 60.
# 

# In[105]:


# your code goes here
QUERY = '''
SELECT Age, ConvertedComp FROM master
'''

data_converted = (pd.read_sql_query(QUERY, conn)).groupby(['Age'])['ConvertedComp'].median()

data_converted.plot(kind='line', x='ConvertedComp', title='ConvertedComp for all ages from 45 to 60.')


# ### Bar Chart
# 

# Create a horizontal bar chart using column `MainBranch.`
# 

# In[121]:


# your code goes here
QUERY = '''
SELECT Age, MainBranch FROM master
'''

data_mainbranch = (pd.read_sql_query(QUERY, conn)).groupby(['MainBranch'])['MainBranch'].count()

data_mainbranch.plot(kind='barh', figsize=(5, 5))


# Close the database connection.
# 

# In[ ]:


conn.close()


# ## Authors
# 

# Ramesh Sannareddy
# 

# ### Other Contributors
# 

# Rav Ahuja
# 

# ## Change Log
# 

# | Date (YYYY-MM-DD) | Version | Changed By        | Change Description                 |
# | ----------------- | ------- | ----------------- | ---------------------------------- |
# | 2020-10-17        | 0.1     | Ramesh Sannareddy | Created initial version of the lab |
# 

# Copyright © 2020 IBM Corporation. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01&cm_mmc=Email_Newsletter-\_-Developer_Ed%2BTech-\_-WW_WW-\_-SkillsNetwork-Courses-IBM-DA0321EN-SkillsNetwork-21426264&cm_mmca1=000026UJ&cm_mmca2=10006555&cm_mmca3=M12345678&cvosrc=email.Newsletter.M12345678&cvo_campaign=000026UJ).
# 
