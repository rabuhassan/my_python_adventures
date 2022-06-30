#!/usr/bin/env python
# coding: utf-8

# ### Week 5 Practical Activities

# # 5.2.8 Practical activity: Search the Twitter API

# ### 1. Prepare Workstation

# In[2]:


# Import Libraries
import yaml
from yaml.loader import SafeLoader
from twitter import *

# Import the YAML file - remember to specify the whole path.
twitter_creds = yaml.safe_load(open('twitter.yaml', 'r').read())

# Pass your Twitter credentials.
twitter_api = Twitter(auth=OAuth(twitter_creds['access_token'],
                                 twitter_creds['access_token_secret'], 
                                 twitter_creds['api_key'],
                                 twitter_creds['api_secret_key'] ))
# Check connection.
print(twitter_api)

# Run connection test with search.
python_tweets = twitter_api.search.tweets(q='#python')

# View the output.
print(python_tweets)


# ### 2. Identify Worldwide Trends

# In[4]:


# Identify worldwide trends.
trends_worldwide = twitter_api.trends.available()

# How many trends are available.
print(len(trends_worldwide))

# Example of trends_worldwide.
trends_worldwide[0]


# ### 3. Identify Specified Cities (London and New York)

# In[7]:


# Find London & New York.
first_city = 'London'
second_city = 'New York'

# Create a variable.
list_of_names_first_city = [_ for _ in trends_worldwide if _['name'] == first_city]
list_of_names_second_city = [_ for _ in trends_worldwide if _['name'] == second_city]


# In[12]:


# View the output.
print(len(list_of_names_first_city))

# Use index to find London.
list_of_names_first_city[0]


# In[13]:


# View the output.
print(len(list_of_names_second_city))

# Use index to find New York.
list_of_names_second_city[0]


# In[16]:


# List of 'where on earth identifiers' (woeid).
# London
list_of_names_first_city[0]['woeid']


# In[17]:


# List of 'where on earth identifiers' (woeid).
# New York
list_of_names_second_city[0]['woeid']


# ### 4. Trends in London

# In[18]:


# Look at common trends in London.
london_trends = twitter_api.trends.place(_id = list_of_names_first_city[0]['woeid'])

# View the output.
london_trends


# In[19]:


# View output as a DataFrame.
# Import Pandas.
import pandas as pd

# Create a DataFrame.
london_trends_pd = pd.DataFrame(london_trends[0]['trends'])

# View the DataFrame.
london_trends_pd


# In[20]:


# Limit the output to more than 50k tweets.
london_trends_50k_pd = london_trends_pd[london_trends_pd['tweet_volume'] > 50000].sort_values('tweet_volume', ascending=False)

# View the output.
print(london_trends_50k_pd.shape)
london_trends_50k_pd


# In[21]:


# Save output as CSV file.
london_trends_50k_pd.to_csv('london_50k.csv', index=False)


# ### 5. Trends in New York

# In[22]:


# Look at common trends in New York.
newyork_trends = twitter_api.trends.place(_id = list_of_names_second_city[0]['woeid'])

# View the output.
newyork_trends


# In[23]:


# View output as a DataFrame.

# Create a DataFrame.
newyork_trends_pd = pd.DataFrame(newyork_trends[0]['trends'])

# View the DataFrame.
newyork_trends_pd


# In[24]:


# Limit the output to more than 50k tweets.
newyork_trends_50k_pd = newyork_trends_pd[newyork_trends_pd['tweet_volume'] > 50000].sort_values('tweet_volume', ascending=False)

# View the output.
print(newyork_trends_50k_pd.shape)
newyork_trends_50k_pd


# In[25]:


# Save output as CSV file.
newyork_trends_50k_pd.to_csv('newyork_50k.csv', index=False)


# ### 6. Common Trends between London and New York

# In[26]:


# Trends in London.

# Import JSON.
import json

# Search for London.
london_trends = twitter_api.trends.place(_id=44418)

# View JSON output.
print (json.dumps(london_trends, indent=4))


# In[27]:


# Trends in New York. 

# Search for London.
newyork_trends = twitter_api.trends.place(_id=2459115)

# View JSON output.
print (json.dumps(newyork_trends, indent=4))


# In[28]:


# Find common topics.
london_trends_list = [trend['name'] for trend in london_trends[0]['trends']]

# View the output.
print(london_trends_list)


# In[29]:


# Find common topics.
newyork_trends_list = [trend['name'] for trend in newyork_trends[0]['trends']]

# View the output.
print(newyork_trends_list)


# In[30]:


# Find common trends between cities.
london_trends_set = set(london_trends_list)
newyork_set = set(newyork_trends_list)

# Set the variable.
common_trends = london_trends_set.intersection(london_trends_set)

# View the output.
print(common_trends)


# ---

# In[ ]:




