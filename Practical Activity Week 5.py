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


# # 5.1.7 Practical activity: Convert, Clean, and Analyse Data

# In[23]:


# Save the DataFrame as a CSV file without index.
covid_df.to_csv('cases.csv', index=False)


# In[24]:


# Create a JSON file.
import json

# Create a JSON file.
output_json = json.dumps(output)

# View the output.
output_json


# In[25]:


# Save the JSON file to .json.
with open('cases_json.json', 'w') as f:
    json.dump(output, f)


# In[26]:


# Read the JSON using Pandas, output to .csv.
pd.read_json(output_json).to_csv('cases_csv.csv', index=False)


# In[37]:


# Import and read the CSV file.
data_csv = pd.read_csv('cases_csv.csv')

# View the data.
print(data_csv.head())

# Import and read the JSON file.
data_json = pd.read_json('cases_json.json')

# View the DataFrame. 
data_json.head()


# In[28]:


# View the CSV and JSON DataFrames.
print(data_csv.dtypes)
print(data_csv.columns)

print(data_json.dtypes)
print(data_json.columns)


# In[32]:


# Create a subset.
data_report = data_csv[['Country/Others', 'Total Cases', 'Total Deaths',
                        'Total Recovered', 'Active Cases', 'Serious/Critical']]

# View the column names.
print(data_report.columns)
data_report


# In[33]:


# Determine missing values.
data_report.isnull().sum()


# In[34]:


# Save the DataFrame as a CSV file without index.
data_report.to_csv('cases_report.csv', index=False)


# In[35]:


# View the saved CSV.
cases_report = pd.read_csv('cases_report.csv')

# View the DataFrame.
cases_report.head()

