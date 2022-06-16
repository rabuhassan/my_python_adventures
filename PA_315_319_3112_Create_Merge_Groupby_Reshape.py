#!/usr/bin/env python
# coding: utf-8

# ### 3.1.5 Practical Activity: 
# # Create and merge the DataFrames

# In[1]:


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


# In[2]:


movies_merge.head()


# In[3]:


ott_merge.head()


# In[4]:


movies_merge.dtypes


# In[5]:


ott_merge.dtypes


# In[6]:


# Merge the DataFrames on ID. 
movies_list = pd.merge(movies_merge, ott_merge, on='ID', how='left')

movies_list.head()


# In[7]:


# Concat the DataFrames based on rows. 
movies_ott = pd.concat([movies_merge, ott_merge], axis=0)


# In[8]:


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


# In[9]:


movies_list.head()


# -------

# ### 3.1.9 Practical activity: 
# 
# # Use groupby() and aggregate() functions

# ### The Ask
# 
# Therefore, only films released after 2012 (Year>=2012 ) will be taken into consideration as Mandisa explores some business questions.
# 
# 1. How many films from each year (released from 2012 to the present) were watched on Netflix?
# 2. What is the average runtime of movies released each year?
# 3. What are the best and worst reviews movies received on Rotten Tomatoes?

# ### 1. How many films from each year (released from 2012 to the present) were watched on Netflix?

# In[10]:


mo_gpby = movies_list.groupby(['Year'])['Netflix'].agg('sum').reset_index()
mo_gpby[mo_gpby['Year'] >= 2012]


# ### 2. What is the average runtime of movies released each year?

# In[11]:


mo_gpby1 = movies_list.groupby(['Year'])['Runtime'].agg('mean').reset_index()
mo_gpby1[mo_gpby1['Year'] >= 2012]


# ### 3. What are the best and worst reviews movies received on Rotten Tomatoes?

# In[12]:


mo_gpby2 = movies_list.groupby(['Year'])['Rotten Tomatoes'].agg(['min', 'max']).reset_index()
mo_gpby2[mo_gpby2['Year'] >= 2012]


# ----

# ### Practical activity 3.1.12: 
# # Reshaping a DataFrame

# 1. Determine the film release date and content rating.
#     * Identify the DataFrame to use.
#     * Use the pivot() function. 
#     * Specify the parameters: index (Title), columns (Age) and values (Year).

# In[13]:


# Pivot the movies_list DataFrame.
movies_list.pivot(index='Title', columns='Age', values='Year')


# 2. Determine the title of movies, the directors, and genres by content rating.
#     * Identify the DataFrame to use.
#     * Use the pivot() function. 
#     * Specify the parameters: index (Title), columns (Age) and values (Directors, Genres).

# In[20]:


# Pivot the movies_list DataFrame.
movies_list.pivot(index='Title', columns='Age', values=(['Directors', 'Genres']))


# 3. Determine the title of movies, the released year, and language by content rating.
#     * Identify the DataFrame to use.
#     * Use the pivot() function. 
#     * Specify the parameters: index (Title), columns (Age) and values (Year, Language).

# In[21]:


# Pivot the movies_list DataFrame.
movies_list.pivot(index='Title', columns='Age', values=(['Year', 'Language']))


# 4. Determine the Netflix screened movies based on language, runtime, and country. 
#     * Identify the DataFrame to use.
#     * Use the pivot() function. 
#     * Specify the parameters: index (Title), columns (Netflix) and values (Runtime, Language, Country).

# In[22]:


# Pivot the movies_list DataFrame.
movies_list.pivot(index='Title', columns='Netflix', values=(['Runtime', 'Language']))


# 5. Determine the title of movies, specified language, potential runtime, and genres by content rating.
#     * Identify the DataFrame to use.
#     * Use the pivot() function. 
#     * Specify the parameters: index (Title), columns (Age) and values (Runtime, Language, Genres).

# In[24]:


# Pivot the movies_list DataFrame.
movies_list.pivot(index='Title', columns='Age', values=(['Runtime', 'Language', 'Genres']))

