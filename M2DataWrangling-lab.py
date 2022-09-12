#!/usr/bin/env python
# coding: utf-8

# <p style="text-align:center">
#     <a href="https://skills.network/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDA0321ENSkillsNetwork21426264-2022-01-01" target="_blank">
#     <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/assets/logos/SN_web_lightmode.png" width="200" alt="Skills Network Logo"  />
#     </a>
# </p>
# 

# # **Data Wrangling Lab**
# 

# Estimated time needed: **45 to 60** minutes
# 

# In this assignment you will be performing data wrangling.
# 

# ## Objectives
# 

# In this lab you will perform the following:
# 

# *   Identify duplicate values in the dataset.
# 
# *   Remove duplicate values from the dataset.
# 
# *   Identify missing values in the dataset.
# 
# *   Impute the missing values in the dataset.
# 
# *   Normalize data in the dataset.
# 

# <hr>
# 

# ## Hands on Lab
# 

# Import pandas module.
# 

# In[2]:


import pandas as pd


# Load the dataset into a dataframe.
# 

# In[3]:


df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv")


# ## Finding duplicates
# 

# In this section you will identify duplicate values in the dataset.
# 

# Find how many duplicate rows exist in the dataframe.
# 

# In[4]:


# your code goes here
print(df.shape)
full = df
duplicates = full[full.duplicated()]
duplicates.shape


# ## Removing duplicates
# 

# Remove the duplicate rows from the dataframe.
# 

# In[108]:


# your code goes here
derived_unique = full.drop_duplicates()


# Verify if duplicates were actually dropped.
# 

# In[6]:


# your code goes here
derived_unique.shape


# ## Finding Missing values
# 

# Find the missing values for all columns.
# 

# In[7]:


# your code goes here
derived_unique.isnull()


# Find out how many rows are missing in the column 'WorkLoc'
# 

# In[8]:


# your code goes here
derived_unique['WorkLoc'].isnull().sum()


# ## Imputing missing values
# 

# Find the  value counts for the column WorkLoc.
# 

# In[9]:


# your code goes here
# full['WorkLoc'].value_counts()
# print('======')
# derived_unique['WorkLoc'].value_counts()
derived_unique['WorkLoc'].value_counts()


# Identify the value that is most frequent (majority) in the WorkLoc column.
# 

# In[45]:


#make a note of the majority value here, for future reference
#
mode_Work = derived_unique['WorkLoc'].mode()[0]
print(mode_Work)


# Impute (replace) all the empty rows in the column WorkLoc with the value that you have identified as majority.
# 

# In[46]:


# your code goes here
# v = derived_unique['WorkLoc'].fillna('Office')
v = derived_unique
vv = v['WorkLoc'].fillna(mode_Work)
vv.shape


# After imputation there should ideally not be any empty rows in the WorkLoc column.
# 

# Verify if imputing was successful.
# 

# In[27]:


# your code goes here
vv.isnull().sum()


# ## Normalizing data
# 

# There are two columns in the dataset that talk about compensation.
# 
# One is "CompFreq". This column shows how often a developer is paid (Yearly, Monthly, Weekly).
# 
# The other is "CompTotal". This column talks about how much the developer is paid per Year, Month, or Week depending upon his/her "CompFreq".
# 
# This makes it difficult to compare the total compensation of the developers.
# 
# In this section you will create a new column called 'NormalizedAnnualCompensation' which contains the 'Annual Compensation' irrespective of the 'CompFreq'.
# 
# Once this column is ready, it makes comparison of salaries easy.
# 

# <hr>
# 

# List out the various categories in the column 'CompFreq'
# 

# In[13]:


# your code goes here
v['CompFreq'].value_counts()


# Create a new column named 'NormalizedAnnualCompensation'. Use the hint given below if needed.
# 

# Double click to see the **Hint**.
# 
# <!--
# 
# Use the below logic to arrive at the values for the column NormalizedAnnualCompensation.
# 
# If the CompFreq is Yearly then use the exising value in CompTotal
# If the CompFreq is Monthly then multiply the value in CompTotal with 12 (months in an year)
# If the CompFreq is Weekly then multiply the value in CompTotal with 52 (weeks in an year)
# 
# -->
# 

# In[124]:


# your code goes here
vv = v['WorkLoc'].fillna('Office')



mode_freq = derived_unique['CompFreq'].mode()[0] #Most frequent payment
empty_filler_freq = v['CompFreq'].fillna(mode_freq) #

median_total = derived_unique['CompTotal'].median()
empty_filler_total = v['CompTotal'].fillna(median_total)

vq = empty_filler_freq.tolist()
vr = empty_filler_total.tolist()

# print(len(vq), len(vr), len(vv), len(v))


normal_value = []

# for x in range(len(vq)):
#     if vq[x] == 'Yearly':
#         made = vr[x]*1
#         normal_value.append(made)
#     elif x == 'Monthly':
#         normal_value.append(vr[x]*12)
#     elif x == 'Weekly':
#         normal_value.append(vr[x]*52)
#     else:
#         normal_value.append(0)

# print(normal_value)

# print(normal_value)

for x in vq:
    ind = vq.index(x)
    if x == 'Yearly':
        normal_value.append(float(vr[ind]) * 1.0)
    elif x == 'Monthly':
        normal_value.append(float(vr[ind]) * 12.0)
    elif x == 'Weekly':
        normal_value.append(float(vr[ind]) * 52.0)
    else:
        normal_value.append(0)

# print(normal_value)
derived_unique['NormalizedAnnualCompensation'] = normal_value
derived_unique['NormalizedAnnualCompensation']


# In[127]:


# derived_unique['CompFreq'].value_counts()

# empty_filler_total

# median_total

derived_unique['NormalizedAnnualCompensation'].median()


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
