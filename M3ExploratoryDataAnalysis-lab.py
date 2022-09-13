#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Exploratory Data Analysis Lab**
# 

# Estimated time needed: **30** minutes
# 

# In this module you get to work with the cleaned dataset from the previous module.
# 
# In this assignment you will perform the task of exploratory data analysis.
# You will find out the distribution of data, presence of outliers and also determine the correlation between different columns in the dataset.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# *   Identify the distribution of data in the dataset.
# 
# *   Identify outliers in the dataset.
# 
# *   Remove outliers from the dataset.
# 
# *   Identify correlation between features in the dataset.
# 

# ***
# 

# ## Hands on Lab
# 

# Import the pandas module.
# 

# In[1]:


import pandas as pd


# Load the dataset into a dataframe.
# 

# In[2]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")


# ## Distribution
# 

# ### Determine how the data is distributed
# 

# The column `ConvertedComp` contains Salary converted to annual USD salaries using the exchange rate on 2019-02-01.
# 
# This assumes 12 working months and 50 working weeks.
# 

# Plot the distribution curve for the column `ConvertedComp`.
# 

# In[44]:


# your code goes here
dist_plot_data = df['ConvertedComp']
dist_plot_data.plot(kind='kde', figsize=(10,10), title='Measure', xlabel = 'ConvertedComp')


# Plot the histogram for the column `ConvertedComp`.
# 

# In[37]:


# your code goes here
hist_plot_data = df['ConvertedComp']
# plt = hist_plot_data.plot.hist(bins=12, alpha=0.5)
hist_plot_data.plot(kind='hist', figsize=(10,10), title="Converted Comp!", xlabel="Treat")


# What is the median of the column `ConvertedComp`?
# 

# In[8]:


# your code goes here
df['ConvertedComp'].median()


# How many responders identified themselves only as a **Man**?
# 

# In[14]:


# your code goes here
df['Gender'].value_counts()['Man']


# Find out the  median ConvertedComp of responders identified themselves only as a **Woman**?
# 

# In[24]:


# your code goes here
df[df['Gender'] =='Woman'].value_counts().sum()


# Give the five number summary for the column `Age`?
# 

# **Double click here for hint**.
# 
# <!--
# min,q1,median,q3,max of a column are its five number summary.
# -->
# 

# In[29]:


# your code goes here
# df["Age"].unique()

df.describe()['Age']


# Plot a histogram of the column `Age`.
# 

# In[26]:


# your code goes here
plt = age_plot_data.plot.hist(bins=15, alpha=0.5)


# ## Outliers
# 

# ### Finding outliers
# 

# Find out if outliers exist in the column `ConvertedComp` using a box plot?
# 

# In[123]:


# your code goes here
df['ConvertedComp'].plot(kind='box',figsize=(10,10))


# Find out the Inter Quartile Range for the column `ConvertedComp`.
# 

# In[61]:


# your code goes here
import numpy
values = df['ConvertedComp']
ranges = values.quantile([0, 0.25, 0.5, 0.75, 1])
inter_quartile = ranges[0.75] - ranges[0.25]
print(f'The inter quartile range is {inter_quartile}')


# Find out the upper and lower bounds.
# 

# In[58]:


# your code goes here
upper_bound = values.max()
lower_bound = values.min()

print(f'Upper Bound is: {upper_bound} and the lower bound is {lower_bound}')


# Identify how many outliers are there in the `ConvertedComp` column.
# 

# In[77]:


# your code goes here
lower_out = ranges[0.25] - (1.5 * inter_quartile)
higher_out = ranges[0.75] + (1.5 * inter_quartile)
((values < lower_out) | (values > higher_out)).sum()


# Create a new dataframe by removing the outliers from the `ConvertedComp` column.
# 

# In[96]:


# your code goes here

new_dataframe = df[(df['ConvertedComp'] > lower_out) & (df['ConvertedComp'] < higher_out)]
new_dataframe


# ## Correlation
# 

# ### Finding correlation
# 

# Find the correlation between `Age` and all other numerical columns.
# 

# In[127]:


# your code goes here
new_dataframe.corr()


# In[126]:


# check = (df[df['Gender']== 'Woman'])['ConvertedComp'].median()
# check['ConvertedComp'].median()
# check = (df[df['Gender']== 'Woman'])['ConvertedComp'].median()
# new_dataframe['ConvertedComp'].median()

# df['Age'].plot(kind='box',figsize=(10,10))

# new_dataframe['ConvertedComp'].mean()

# from scipy.stats import pearsonr
# newest = new_dataframe.dropna()

# num = newest.select_dtypes(include='number')

# pearson_coef, p_value = pearsonr(num['Age'], num['Respondent'])

# print(f'pearson_coef is {pearson_coef} and p_value is {p_value}')


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
