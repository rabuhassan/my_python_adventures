#!/usr/bin/env python
# coding: utf-8

# # 2.1.10 Practical Activites: 
# ## 2.1.10 & 2.2.8
# ## Importing Data and Handling Missing Values

# In[1]:


import pandas as pd


# In[2]:


movies = pd.read_excel('movies.xlsx')
ott = pd.read_csv('ott.csv')


# In[3]:


movies


# In[4]:


ott


# In[5]:


print(ott.shape)
print(ott.dtypes)


# In[6]:


print(movies.shape)
print(movies.dtypes)


# In[8]:


# Check for any missing values in Age

movies['Age'].isnull().sum()


# In[9]:


# Replace the missing values in Age column with set value "Others".
movies['Age'][movies['Age'].isna()] = "Others"


# In[10]:


movies['Age'].isnull().sum()


# ### Checking for any missing values in Directors, Genres, Country, and Language.
# 
# 

# In[22]:


movies['Directors'].isnull().sum()


# In[23]:


movies['Genres'].isnull().sum()


# In[24]:


movies['Country'].isnull().sum()


# In[25]:


movies['Language'].isnull().sum()


# ### Replace the missing values in Directors, Generes, Country, and Language. 

# In[26]:


movies['Directors'][movies['Directors'].isna()] = "Others"


# In[27]:


movies['Genres'][movies['Genres'].isna()] = "Others"


# In[28]:


movies['Country'][movies['Country'].isna()] = "Others"


# In[29]:


movies['Language'][movies['Language'].isna()] = "Others"


# In[30]:


movies['Directors'].isnull().sum()


# In[31]:


movies['Genres'].isnull().sum()


# In[32]:


movies['Country'].isnull().sum()


# In[33]:


movies['Language'].isnull().sum()


# In[38]:


# Determine the data type first.
print(movies.dtypes)


# In[39]:


movies['Rotten Tomatoes'].isnull().sum()


# In[40]:


movies['IMDb'].isnull().sum()


# In[43]:


movies['Rotten Tomatoes'].fillna(movies['Rotten Tomatoes'].mean(),inplace=True)
movies['IMDb'].fillna(movies['IMDb'].mean(),inplace=True)


# In[42]:


movies['Rotten Tomatoes'].isnull().sum()


# In[44]:


movies['IMDb'].isnull().sum()


# In[ ]:




