#!/usr/bin/env python
# coding: utf-8

# ### Practical Activity 4.1.9
# # Create Plots with Seaborn
# ----

# ### 1. Prepara Workstation

# In[1]:


# Import packages
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[2]:


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


# In[3]:


movies.head()


# In[4]:


ott.head()


# In[5]:


# Merge the two DataFrames

movies_list = pd.merge(movies, ott, how='left', on='ID')
movies_list


# In[6]:


# View the merged DataFrame. 
print("movies_list")
print(f"{movies_list.shape[0]} rows for movies_list")
print(f"{movies_list.shape[1]} columns for movies_list")
print(f"movies_list has the following columns: {movies_list.columns}")

print("-------------")


# In[7]:


movies_list.head()


# ### 2. Plot Counterplot
# 
# Determine what age group has streamed the most movies. Based on the plot, answer the following questions:
# 1. What age group had the most-streamed movies?
# 2. Can you identify any gaps that Netflix need to address?

# In[8]:


# Create a countplot.
sns.countplot(x='Age', hue='Netflix', data=movies_list)


# * 18+ have streamed the most movies. 
# * It appears that Netflix have far less costomers that are younger than 18. It could be that Netflix have a much smaller selection of movies that are not rated R. 

# ### 3. Histogram Plot
# 
# Based on the plot, answer the following questions:
# 1. What do you understand from the histogram?
# 2. What are the outliers in the data? 

# In[9]:


# Create a histogram.
sns.histplot(data = movies_list, x='IMDb', binwidth=1)


# * Most fall just above average. 
# * There are a couple of outliers.

# ### 4. Scatterplot 
# Determine if there is a correlation between the ratings from Rotten Tomatoes and IMDb. Based on the plot, answer the following questions:
# * What can you infer about the correlation? 
# * If there is a correlation, is the relationship between the ratings strong or weak and positive or negative?

# In[10]:


# Create the scatterplot.
sns.scatterplot(x='IMDb', y='Rotten Tomatoes', data=movies_list)


# * There is a week positive correlation. 

# ### Practical Activity 4.1.12
# # Outliers Analysis
# ----

# In[11]:


# Create a boxplot based on species and body_mass_g.
sns.boxplot(data=movies_list, x='Age', y='IMDb')


# ### Practical Activity 4.1.15
# # Creating a Line and Subplots
# -----

# ### 1. Lineplot
# 
# Cmparing the movies' release year and their IMDb ratings in order to answer the following questions:
# * What can you infer about the users’ ratings for movies released between 1920 and 1940?
# * What can you infer about the users’ ratings for movies released between 1960 and 1980?

# In[12]:


# Create a simple plot.
sns.lineplot(x='Year', y='IMDb', data=movies_list)


# In[13]:


# Create a simple plot. Remove the bands. 
sns.lineplot(x='Year', y='IMDb', data=movies_list, ci=None)


# * Data between 1920 and 1940 is seemingly unreliable. 
# * From 1960 until 2020, there has been an improvement in the data and the errors. 

# ### 2. Enhance Line Plot
# * Compare age, rating, and year of release of the movies in order to answer the following questions:
# * How would you further enhance the lineplot?
# * What can you infer about the movies with a 16+ and 18+ age limit?
# * In which year did the film industry start marking suitable movies for individuals 16+? 
# 

# In[14]:


# Create lineplots with specification.
sns.lineplot(x = 'Year', y = 'IMDb',
             data = movies_list[movies_list['Age'].isin(['16+', '18+'])],
             hue ='Age', ci=None)


# * Movie industry started making movies for 16+ in and around 1970. 

# ### Practical Activity 4.2.5
# # Customising Plots
# -----

# In[15]:


movies_2010 = movies_list[movies_list['Year']>=2010]

ax = sns.countplot(x='Year', data=movies_2010)

ax.set(ylabel='Percent')

total = len(movies_2010['Year'])

for p in ax.patches:
    percentage = '{:.1f}%'.format(100 * p.get_height()/total)
    x = p.get_x()
    y = p.get_y() + p.get_height()
    ax.annotate(percentage, (x, y))

plt.xticks(rotation=90)
plt.show()


# In[16]:


ax = sns.displot(data=movies_list, x='IMDb', bins=10,kind='hist', 
                 palette='GnBu', aspect=1.4, kde=True)

plt.show()


# In[ ]:




