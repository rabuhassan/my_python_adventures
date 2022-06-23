#!/usr/bin/env python
# coding: utf-8

# ### Practical Activity 4.1.9
# # Create Plots with Seaborn
# ----

# ### 1. Prepara Workstation

# In[24]:


# Import packages
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[25]:


# Load databases and create DataFrames
movies = pd.read_csv('movies.csv')
ott = pd.read_excel('ott.xlsx')

# View the DataFrame. 
print("movies")
print(f"{movies.shape[0]} rows for movies")
print(f"{movies.shape[1]} columns for movies")
print(f"movies has the following columns: {movies.columns}")

print("-------------")

print("ott")
print(f"{ott.shape[0]} rows for ott")
print(f"{ott.shape[1]} columns for ott")
print(f"ott has the following columns: {ott.columns}")
print("-------------")


# In[26]:


movies.head()


# In[27]:


ott.head()


# In[28]:


# Merge the two DataFrames

movies_list = pd.merge(movies, ott, how='left', on='ID')
movies_list


# In[29]:


# View the merged DataFrame. 
print("movies_list")
print(f"{movies_list.shape[0]} rows for movies_list")
print(f"{movies_list.shape[1]} columns for movies_list")
print(f"movies_list has the following columns: {movies_list.columns}")

print("-------------")


# In[30]:


movies_list.head()


# ### 2. Plot Counterplot
# 
# Determine what age group has streamed the most movies. Based on the plot, answer the following questions:
# 1. What age group had the most-streamed movies?
# 2. Can you identify any gaps that Netflix need to address?

# In[35]:


# Create a countplot.
sns.countplot(x='Age', hue='Netflix', data=movies_list)


# * 18+ have streamed the most movies. 
# * It appears that Netflix have far less costomers that are younger than 18. It could be that Netflix have a much smaller selection of movies that are not rated R. 

# ### 3. Histogram Plot
# 
# Based on the plot, answer the following questions:
# 1. What do you understand from the histogram?
# 2. What are the outliers in the data? 

# In[37]:


# Create a histogram.
sns.histplot(data = movies_list, x='IMDb', binwidth=1)


# * Most fall just above average. 
# * There are a couple of outliers.

# ### 4. Scatterplot 
# Determine if there is a correlation between the ratings from Rotten Tomatoes and IMDb. Based on the plot, answer the following questions:
# * What can you infer about the correlation? 
# * If there is a correlation, is the relationship between the ratings strong or weak and positive or negative?

# In[39]:


# Create the scatterplot.
sns.scatterplot(x='IMDb', y='Rotten Tomatoes', data=movies_list)


# * There is a week positive correlation. 

# ### Practical Activity 4.1.12
# # Outliers Analysis
# ----

# In[41]:


# Create a boxplot based on species and body_mass_g.
sns.boxplot(data=movies_list, x='Age', y='IMDb')


# In[ ]:




