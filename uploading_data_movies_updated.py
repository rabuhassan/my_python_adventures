#!/usr/bin/env python
# coding: utf-8

# # Practical Activites: 
# 
# ## 2.1.10 & 2.2.6 & 2.3.6
# 
# ### Importing Data, Handling Missing Values, and Filtering

# ## 2.1.10

# In[28]:


import pandas as pd


# In[29]:


movies = pd.read_excel('movies.xlsx')
ott = pd.read_csv('ott.csv')


# In[30]:


movies


# In[31]:


ott


# In[32]:


print(ott.shape)
print(ott.dtypes)


# In[33]:


print(movies.shape)
print(movies.dtypes)


# ## 2.2.6

# In[7]:


# Check for any missing values in Age

movies['Age'].isnull().sum()


# In[8]:


# Replace the missing values in Age column with set value "Others".
movies['Age'][movies['Age'].isna()] = "Others"


# In[9]:


movies['Age'].isnull().sum()


# ### Checking for any missing values in Directors, Genres, Country, and Language.
# 
# 

# In[10]:


movies['Directors'].isnull().sum()


# In[11]:


movies['Genres'].isnull().sum()


# In[12]:


movies['Country'].isnull().sum()


# In[13]:


movies['Language'].isnull().sum()


# ### Replace the missing values in Directors, Generes, Country, and Language. 

# In[14]:


movies['Directors'][movies['Directors'].isna()] = "Others"


# In[15]:


movies['Genres'][movies['Genres'].isna()] = "Others"


# In[16]:


movies['Country'][movies['Country'].isna()] = "Others"


# In[17]:


movies['Language'][movies['Language'].isna()] = "Others"


# In[18]:


movies['Directors'].isnull().sum()


# In[19]:


movies['Genres'].isnull().sum()


# In[20]:


movies['Country'].isnull().sum()


# In[21]:


movies['Language'].isnull().sum()


# In[22]:


# Determine the data type first.
print(movies.dtypes)


# In[23]:


movies['Rotten Tomatoes'].isnull().sum()


# In[24]:


movies['IMDb'].isnull().sum()


# In[25]:


movies['Rotten Tomatoes'].fillna(movies['Rotten Tomatoes'].mean(),inplace=True)
movies['IMDb'].fillna(movies['IMDb'].mean(),inplace=True)


# In[26]:


movies['Rotten Tomatoes'].isnull().sum()


# In[27]:


movies['IMDb'].isnull().sum()


# ## 2.3.6
# ### Filter the data
# **Activity Objective:**
# * filter the values in the data to gain useful insights
# * modify the DataFrame to write fewer lines of code and ensure accuracy
# * describe the patterns, trends, and spread of the data set. 

# In[39]:


# Column Names and Data Types
print(movies.dtypes)
print(ott.dtypes)


# In[41]:


print(list(movies.columns))
print(list(ott.columns))


# In[42]:


# Filter the DataFrame according to numeric variables
# Calculate the IQR

movies_num = movies.select_dtypes('number')
movies_num = movies_num.drop('Year', axis =1)


# In[43]:


movies_num


# In[47]:


# Calculate Q1 and Q3
Q1 = movies_num.quantile(0.25)
Q3 = movies_num.quantile(0.75)

print(Q1)
print(Q3)


# In[49]:


IQR = Q3 - Q1
print(IQR)


# In[50]:


# Evaluate the data
movies_num.describe()


# In[ ]:




