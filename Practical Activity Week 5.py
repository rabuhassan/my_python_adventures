#!/usr/bin/env python
# coding: utf-8

# ## Week 5 Practical Activities

# # 5.1.5 Practical activity: Scraping COVID Data

# The objective of this activity is to supply each department with requires different information for each continent on the list:
# 
# * The executives need to know the total cases and the number of deaths.
# * Claims need to know the number of new cases, new deaths, active cases, and serious/critical cases.
# * Clients need to know the number of total cases and total recoveries.

# In[1]:


# Import the following libraries: Pandas, Requests, BeautifulSoup

from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[18]:


# Create a URL and requests variables.

url = 'https://www.worldometers.info/coronavirus/'
page = requests.get(url)

# check reponse is 200 to confirm connection. 
if page.status_code == 200:
    html_doc = page.text
    
# Create Beautiful Soup object. 
soup = BeautifulSoup(html_doc)

# Print the output.
print(soup.prettify())


# In[19]:


# Extract the tabular data. Determine the table ID from the website, and extract the contents.
table = soup.find('table', attrs={'id': 'main_table_countries_today'})

# View the information in a readable format.
print(table.prettify())


# In[20]:


# Extract all of the rows of the table.
rows = table.find_all("tr", attrs= {'style': ""})

# View the rows.
rows


# In[16]:


# Store the extracted data.
output = []

column_names = ['ID', 'Country,Others', 'Total Cases', 
                'New Cases', 'Total Deaths', 'New Deaths',
                'Total Recovered', 'New Recovered', 'Active Cases',
                'Serious/Critical', 'Tot Cases/1M pop', 'Deaths/1M pop',
                'Total Tests', 'Tests/1M pop', 'Population']


# Create a for loop statement.
for country in rows:
    country_data = country.find_all("td")
    if country_data:
        # Extract the text within each element.
        country_text = [td.text for td in country_data]
        output.append(dict(zip(column_names, country_text)))
        
# Create an output.
output


# In[22]:


# Create Covid DataFrame directly from the output.
covid_df = pd.DataFrame(output)

# View the DataFrame.
covid_df


# In[ ]:





# In[ ]:




