#!/usr/bin/env python
# coding: utf-8

# ## Week 6 Practical Activities

# # 6.1.6 Practical activity: Preparing quantitative data 

# The Objective of this activity is to: 
# 
# 1. set up the workspace
# 2. get to know the data
# 3. define sub-data sets
# 4. detect outliers
# 5. remove outliers.
# 

# ## 1. Prepare Workstation

# In[1]:


# Import libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error
from sklearn.metrics import median_absolute_error, mean_squared_error, mean_squared_log_error

import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')

# Get multiple outputs in the same cell.
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'


# In[6]:


# Import the csv file and create the DataFrame.
data = pd.read_csv('raw_sales.csv', index_col=['datesold'],                    parse_dates =['datesold'])

#View the DataFrame
print(data.shape)
data.head()


# ## 2. Get to know the data 

# In[7]:


# Plot the house prices as a time series.
# Plot the size.
data.plot(figsize=(12, 4))

# Specify the legend and title of the plot.
plt.legend(loc='best')
plt.title('Housing Prices')
plt.show(block=False);

# Check for missing values.
data.isna().sum()


# In[8]:


# Count the number of values in a specified column of the DataFrame.
print(data['bedrooms'].value_counts())

# Create a plot.
plt.title('Count of number of bedrooms')

sns.despine(left=True);
sns.countplot(x='bedrooms', data=data)


# ## 3. Create a subset

# In[9]:


# Create a copy of the original data for convinience.
data_sub = data.copy()


# Data set cosnsisting of houses with 1 bedroom: 
df_1 = data_sub[data_sub['bedrooms']==1]
print(df_1.shape)


# Data set cosnsisting of houses with 2 bedrooms: 
df_2 = data_sub[data_sub['bedrooms']==2]
print(df_2.shape)


# Data set cosnsisting of houses with 3 bedrooms: 
df_3 = data_sub[data_sub['bedrooms']==3]
print(df_3.shape)


# Data set cosnsisting of houses with 4 bedrooms: 
df_4 = data_sub[data_sub['bedrooms']==4]
print(df_4.shape)


# Data set cosnsisting of houses with 5 bedrooms: 
df_5 = data_sub[data_sub['bedrooms']==5]
print(df_5.shape)


# ## 4. Detect outliers

# In[12]:


# Set the plot size.
fig, axes = plt.subplots(nrows=3, ncols=2,figsize=(20,20))

# 1 bedroom:
axes[0][0].hist(df_1['price'])
axes[0][0].title.set_text('1 bedroom price histogram')

# 2 bedroom:
axes[0][1].hist(df_2['price'])
axes[0][1].title.set_text('2 bedroom price histogram')

# 3 bedroom:
axes[1][0].hist(df_3['price'])
axes[1][0].title.set_text('3 bedroom price histogram')

# 4 bedroom
axes[1][1].hist(df_4['price'])
axes[1][1].title.set_text('4 bedroom price histogram')

# 5 bedroom:
axes[2][0].hist(df_5['price'])
axes[2][0].title.set_text('5 bedroom price histogram')


fig.delaxes(axes[2][1])

plt.show()


# ### 1-bedroom

# In[17]:


# Create a boxplot for 1 bedroom.
# Set figure size.
fig = plt.figure(figsize=(18, 4))

# Create a boxplot.
ax = sns.boxplot(x=df_1['price'], whis=1.5)


# In[14]:


# The columns you want to search for outliers in.
cols = ['price'] 

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0,1) and not (0,100).
Q1 = df_1[cols].quantile(0.25) 
Q3 = df_1[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a Boolean array of the rows with (any) non-outlier column values.
condition = ~((df_1[cols] < (Q1 - 1.5 * IQR)) | (df_1[cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Filter our DataFrame based on condition.
df_1_non_outlier = df_1[condition]
df_1_non_outlier.shape


# In[26]:


# Plot to see if outliers have been removed: 
# whis=multiplicative factor.
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_1_non_outlier['price'],whis=1.5)


# ### 2-bedrooms

# In[34]:


# Create a boxplot for 2 bedroom.
# Set figure size.
fig = plt.figure(figsize=(18, 4))

# Create a boxplot.
ax = sns.boxplot(x=df_2['price'], whis=1.5)


# In[22]:


# The columns you want to search for outliers in.
cols = ['price'] 

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0,1) and not (0,100).
Q1 = df_2[cols].quantile(0.25) 
Q3 = df_2[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a Boolean array of the rows with (any) non-outlier column values.
condition = ~((df_2[cols] < (Q1 - 1.5 * IQR)) | (df_2[cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Filter our DataFrame based on condition.
df_2_non_outlier = df_2[condition]
df_2_non_outlier.shape


# In[27]:


# Plot to see if outliers have been removed: 
# whis=multiplicative factor.
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_2_non_outlier['price'],whis=1.5)


# ### 3-bedrooms

# In[19]:


# Create a boxplot for 3 bedroom.
# Set figure size.
fig = plt.figure(figsize=(18, 4))

# Create a boxplot.
ax = sns.boxplot(x=df_3['price'], whis=1.5)


# In[23]:


# The columns you want to search for outliers in.
cols = ['price'] 

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0,1) and not (0,100).
Q1 = df_3[cols].quantile(0.25) 
Q3 = df_3[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a Boolean array of the rows with (any) non-outlier column values.
condition = ~((df_3[cols] < (Q1 - 1.5 * IQR)) | (df_3[cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Filter our DataFrame based on condition.
df_3_non_outlier = df_3[condition]
df_3_non_outlier.shape


# In[28]:


# Plot to see if outliers have been removed: 
# whis=multiplicative factor.
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_3_non_outlier['price'],whis=1.5)


# ### 4-bedrooms

# In[20]:


# Create a boxplot for 4 bedroom.
# Set figure size.
fig = plt.figure(figsize=(18, 4))

# Create a boxplot.
ax = sns.boxplot(x=df_4['price'], whis=1.5)


# In[24]:


# The columns you want to search for outliers in.
cols = ['price'] 

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0,1) and not (0,100).
Q1 = df_4[cols].quantile(0.25) 
Q3 = df_4[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a Boolean array of the rows with (any) non-outlier column values.
condition = ~((df_4[cols] < (Q1 - 1.5 * IQR)) | (df_4[cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Filter our DataFrame based on condition.
df_4_non_outlier = df_4[condition]
df_4_non_outlier.shape


# In[29]:


# Plot to see if outliers have been removed: 
# whis=multiplicative factor.
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_4_non_outlier['price'],whis=1.5)


# ### 5-bedrooms

# In[21]:


# Create a boxplot for 5 bedroom.
# Set figure size.
fig = plt.figure(figsize=(18, 4))

# Create a boxplot.
ax = sns.boxplot(x=df_5['price'], whis=1.5)


# In[ ]:


# The columns you want to search for outliers in.
cols = ['price'] 

# Calculate quantiles and IQR.
# Same as np.percentile but maps (0,1) and not (0,100).
Q1 = df_5[cols].quantile(0.25) 
Q3 = df_5[cols].quantile(0.75)
IQR = Q3 - Q1
IQR

# Return a Boolean array of the rows with (any) non-outlier column values.
condition = ~((df_5[cols] < (Q1 - 1.5 * IQR)) | (df_5[cols] > (Q3 + 1.5 * IQR))).any(axis=1)

# Filter our DataFrame based on condition.
df_5_non_outlier = df_5[condition]
df_5_non_outlier.shape


# In[30]:


# Plot to see if outliers have been removed: 
# whis=multiplicative factor.
fig = plt.subplots(figsize=(12, 2))

ax = sns.boxplot(x=df_5_non_outlier['price'],whis=1.5)


# ----

# # 6.1.8 Practical activity: Time-series forecasting

# The objective of this activity is to forecast the prices of houses by:
# 
# 1. plotting the sub-data sets
# 2. resampling to remove noise
# 3. using a time-series moving average.

# ### 1-bedroom

# In[37]:


# Create a plot for 1 bedroom.
# Calculate max and min.
df_1_non_outlier['price'].min()
df_1_non_outlier['price'].max()


# Plot the time-series data.
df_1_non_outlier.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title('Time series plot for house with 1 bedroom')
plt.show(block=False)


# In[38]:


# Resample the data set with 1 bedroom.
df_1_res = df_1_non_outlier.resample('M').mean()
df_1_res.head()


# Drop the missing values: 
df_1_res.dropna(inplace= True)
df_1_res.isna().sum()


# Plot the time-series data:
df_1_res.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title("Time series plot after resampling")
plt.show(block=False)


# In[39]:


# Discussed in tutorial video.
# Function to calculate and plot the simple moving average: 
def plot_moving_average(series, window, plot_intervals=False, scale=1.96):

    rolling_mean = series.rolling(window=window).mean()
    
    plt.figure(figsize=(12,4))
    plt.title("Moving average\n window size = {}".format(window))
    plt.plot(rolling_mean, 'g', label='Simple moving average trend')
    
    # Plot confidence intervals for smoothed values.
    if plot_intervals:
        mae = mean_absolute_error(series[window:], rolling_mean[window:])
        deviation = np.std(series[window:] - rolling_mean[window:])
        lower_bound = rolling_mean - (mae + scale * deviation)
        upper_bound = rolling_mean + (mae + scale * deviation)
        plt.plot(upper_bound, 'r--', label='Upper bound / Lower bound')
        plt.plot(lower_bound, 'r--')
            
    plt.plot(series[window:], label='Actual values')
    plt.legend(loc='best')
    plt.grid(True)


# In[40]:


# 1 bedroom:
# 5 days:
plot_moving_average(df_1_res.price, 5, plot_intervals=True)

# 30-days smoothing:
plot_moving_average(df_1_res.price, 30, plot_intervals=True)

# 90-days smoothing:
plot_moving_average(df_1_res.price, 90, plot_intervals=True)


# ### 2-bedrooms

# In[45]:


# Create a plot for 2 bedroom.
# Calculate max and min.
df_2_non_outlier['price'].min()
df_2_non_outlier['price'].max()


# Plot the time-series data.
df_2_non_outlier.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title('Time series plot for house with 2 bedroom')
plt.show(block=False)


# In[42]:


# Resample the data set with 1 bedroom.
df_2_res = df_2_non_outlier.resample('M').mean()
df_2_res.head()


# Drop the missing values: 
df_2_res.dropna(inplace= True)
df_2_res.isna().sum()


# Plot the time-series data:
df_2_res.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title("Time series plot after resampling")
plt.show(block=False)


# In[43]:


# 2 bedroom:
# 5 days:
plot_moving_average(df_2_res.price, 5, plot_intervals=True)

# 30-days smoothing:
plot_moving_average(df_2_res.price, 30, plot_intervals=True)

# 90-days smoothing:
plot_moving_average(df_2_res.price, 90, plot_intervals=True)


# ### 3-bedrooms

# In[46]:


# Create a plot for 3 bedroom.
# Calculate max and min.
df_3_non_outlier['price'].min()
df_3_non_outlier['price'].max()


# Plot the time-series data.
df_3_non_outlier.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title('Time series plot for house with 3 bedroom')
plt.show(block=False)


# In[49]:


# Resample the data set with 3 bedroom.
df_3_res = df_3_non_outlier.resample('M').mean()
df_3_res.head()


# Drop the missing values: 
df_3_res.dropna(inplace= True)
df_3_res.isna().sum()


# Plot the time-series data:
df_3_res.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title("Time series plot after resampling")
plt.show(block=False)


# In[52]:


# 3 bedroom:
# 5 days:
plot_moving_average(df_3_res.price, 5, plot_intervals=True)

# 30-days smoothing:
plot_moving_average(df_3_res.price, 30, plot_intervals=True)

# 90-days smoothing:
plot_moving_average(df_3_res.price, 90, plot_intervals=True)


# ### 4-bedrooms

# In[47]:


# Create a plot for 4 bedroom.
# Calculate max and min.
df_4_non_outlier['price'].min()
df_4_non_outlier['price'].max()


# Plot the time-series data.
df_2_non_outlier.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title('Time series plot for house with 4 bedroom')
plt.show(block=False)


# In[50]:


# Resample the data set with 4 bedroom.
df_4_res = df_4_non_outlier.resample('M').mean()
df_4_res.head()


# Drop the missing values: 
df_4_res.dropna(inplace= True)
df_4_res.isna().sum()


# Plot the time-series data:
df_4_res.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title("Time series plot after resampling")
plt.show(block=False)


# In[53]:


# 4 bedroom:
# 4 days:
plot_moving_average(df_4_res.price, 5, plot_intervals=True)

# 30-days smoothing:
plot_moving_average(df_4_res.price, 30, plot_intervals=True)

# 90-days smoothing:
plot_moving_average(df_4_res.price, 90, plot_intervals=True)


# ### 5-bedrooms

# In[48]:


# Create a plot for 5 bedroom.
# Calculate max and min.
df_5_non_outlier['price'].min()
df_5_non_outlier['price'].max()


# Plot the time-series data.
df_5_non_outlier.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title('Time series plot for house with 5 bedroom')
plt.show(block=False)


# In[51]:


# Resample the data set with 5 bedroom.
df_5_res = df_5_non_outlier.resample('M').mean()
df_5_res.head()


# Drop the missing values: 
df_5_res.dropna(inplace= True)
df_5_res.isna().sum()


# Plot the time-series data:
df_5_res.plot(figsize=(12, 4))
plt.legend(loc='best')
plt.title("Time series plot after resampling")
plt.show(block=False)


# In[54]:


# 5 bedroom:
# 5 days:
plot_moving_average(df_5_res.price, 5, plot_intervals=True)

# 30-days smoothing:
plot_moving_average(df_5_res.price, 30, plot_intervals=True)

# 90-days smoothing:
plot_moving_average(df_5_res.price, 90, plot_intervals=True)


# ---

# In[ ]:




