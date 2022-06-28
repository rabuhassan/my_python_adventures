#!/usr/bin/env python
# coding: utf-8

# ### Week 5 Practical Activities

# # 5.2.4 Practical activity: Making a GET request to an API

# ### Prepare Workstation

# In[10]:


# Import Libraries
import requests
import json
import pandas as pd

# Identify the URL's.
BPI_URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
USA_URL = 'https://datausa.io/api/data?drilldowns=Nation&measures=Population'


# ## Bitcoin Price Index

# ### 1. Request Access to Bitcoin Price Index

# In[11]:


# Create a variable. 
response_BPI = requests.get(BPI_URL)

# Print the status_code. 
print(response_BPI.status_code)


# ### 2. Retrieve the headers of the API.

# In[12]:


# HTTP headers.
info_BPI = requests.head(BPI_URL)
print(info_BPI.headers)


# ### 3. Parce the JSON data and format it.  

# In[28]:


# Parse JSON data with loads().
content_BPI = json.loads(response_BPI.text)
print(type(content_BPI))

# Formatting JSON.
print(json.dumps(content_BPI, indent=4))


# ### 4. Create a Pandas Dataframe & Save CSV / JSON

# In[21]:


# Create and view the DataFrame. 
BPI = pd.DataFrame(content_BPI)
BPI.head()


# In[25]:


# Save the JSON file to .json.

# Create a JSON file.
bitcoin_json = json.dumps(content_BPI)

with open('bitcoin_json.json', 'w') as f:
    json.dump(content_BPI, f)
    
# Save as a CSV file without index.
pd.read_json(bitcoin_json).to_csv('bitcoin_csv.csv', index=False)


# ## USA Population Data

# ### 1. Request Access to USA Population Data

# In[26]:


# Create a variable. 
response_USA = requests.get(USA_URL)

# Print the status_code. 
print(response_USA.status_code)


# ### 2. Retrieve the headers of the API.

# In[27]:


# HTTP headers.
info_USA = requests.head(USA_URL)
print(info_USA.headers)


# ### 3. Parce the JSON data and format it.  

# In[30]:


# Parse JSON data with loads().
content_USA = json.loads(response_USA.text)
print(type(content_USA))

# Formatting JSON.
print(json.dumps(content_USA, indent=4))


# In[ ]:




