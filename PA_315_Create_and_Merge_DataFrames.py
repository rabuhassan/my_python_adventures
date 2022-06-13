#!/usr/bin/env python
# coding: utf-8

# ### 3.1.5 Practical Activity: 
# # Create and merge the DataFrames

# In[8]:


# Import packages, load the ott_merge and movies_merge databases, and create the DataFrames
import pandas as pd

movies_merge = pd.read_excel('movies_merge.xlsx')
ott_merge = pd.read_csv('ott_merge.csv')

# View the DataFrame. 
print(movies_merge.shape)
print(ott_merge.shape)
print('-------------')


# How many rows and columns? 
print('movies_merge')
print(f"{movies_merge.shape[0]} rows for movies_merge")
print(f"{movies_merge.shape[1]} columns for movies_merge")
print('-------------')

print('ott')
print(f"{ott_merge.shape[0]} rows for ott_merge")
print(f"{ott_merge.shape[1]} columns for ott_merge")
print('-------------')


# In[3]:


movies_merge.head()


# In[4]:


ott_merge.head()


# In[13]:


movies_merge.dtypes


# In[14]:


ott_merge.dtypes


# In[17]:


# Merge the DataFrames on ID. 
movies_list = pd.merge(movies_merge, ott_merge, on='ID', how='left')

movies_list.head()


# In[19]:


# Concat the DataFrames based on rows. 
movies_ott = pd.concat([movies_merge, ott_merge], axis=0)


# In[20]:


# How many rows and columns? 
print('movies_merge')
print(f"{movies_merge.shape[0]} rows for movies_merge")
print(f"{movies_merge.shape[1]} columns for movies_merge")
print('-------------')

print('ott')
print(f"{ott_merge.shape[0]} rows for ott_merge")
print(f"{ott_merge.shape[1]} columns for ott_merge")
print('-------------')

print('movies_list')
print(f"{movies_list.shape[0]} rows for movies_list")
print(f"{movies_list.shape[1]} columns for movies_list")
print('-------------')

print('movies_ott')
print(f"{movies_ott.shape[0]} rows for movies_ott")
print(f"{movies_ott.shape[1]} columns for movies_ott")
print('-------------')

