#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[25]:


#import dataset
df = pd.read_csv (r'C:\Users\alberto\Desktop\Jan-1-2019-Oct-31-2019.csv')
df


# In[4]:


#interested categories
df_feed = df[df['Placement']=='feed']
df_instagram_stories = df[df['Placement']=='instagram_stories']


# In[5]:


#feed
df_feed['Day'] = pd.to_datetime(df_feed['Day'], errors='coerce')
df_feed['weekday'] = df_feed.Day.dt.weekday_name
df_feed['week'] = df_feed['Day'].dt.week


# In[11]:


#feed group by week number
df_feed.groupby(['week'])


# In[9]:


#feed amount weekly
weekly_df_feed_amount = df_feed.groupby(['week'])[['Amount Spent (SEK)']]
weekly_df_feed_amount = weekly_df_feed_amount.sum()


# In[10]:


#feed impressions weekly (/1000)
weekly_df_feed_impressions = df_feed.groupby(['week'])[['Impressions']]
weekly_df_feed_impressions = weekly_df_feed_impressions.sum()
weekly_df_feed_impressions = weekly_df_feed_impressions / 1000


# In[16]:


#feed grouped by day of the week (amount and impressions /1000)
df_feed.groupby(['weekday'])
day_feed_amount = df_feed.groupby(['weekday'])[['Amount Spent (SEK)']]
day_feed_amount = day_feed_amount.sum()


# In[19]:


#impressions/1000
day_feed_impressions = df_feed.groupby(['weekday'])[['Impressions']]
day_feed_impressions = day_feed_impressions.sum()
day_feed_impressions = day_feed_impressions / 1000


# In[21]:


#instagram stories
df_instagram_stories['Day'] = pd.to_datetime(df_instagram_stories['Day'], errors='coerce')
df_instagram_stories['weekday'] = df_instagram_stories.Day.dt.weekday_name
df_instagram_stories['week'] = df_instagram_stories['Day'].dt.week


# In[200]:


#df_instagram_stories.groupby(['week'])


# In[22]:


#instagram stories weekly amount
weekly_df_instagram_stories_amount = df_instagram_stories.groupby(['week'])[['Amount Spent (SEK)']]
weekly_df_instagram_stories_amount = weekly_df_instagram_stories_amount.sum()


# In[23]:


# instagram stories weekly impressions/1000
weekly_df_instagram_stories_impressions = df_instagram_stories.groupby(['week'])[['Impressions']]
weekly_df_instagram_stories_impressions = weekly_df_instagram_stories_impressions.sum()
weekly_df_instagram_stories_impressions = weekly_df_instagram_stories_impressions /1000


# In[203]:


df_instagram_stories.groupby(['weekday'])


# In[204]:


#day_df_instagram_stories_amount
day_df_instagram_stories_amount = df_instagram_stories.groupby(['weekday'])[['Amount Spent (SEK)']]
day_df_instagram_stories_amount = day_df_instagram_stories_amount.sum()


# In[153]:


#day_df_instagram_stories_impressions /1000
day_df_instagram_stories_impressions = df_instagram_stories.groupby(['weekday'])[['Impressions']]
day_df_instagram_stories_impressions = day_df_instagram_stories_impressions.sum()
day_df_instagram_stories_impressions = day_df_instagram_stories_impressions / 1000 


# In[26]:


#CPM (Cost per 1,000 Impressions)= amount/(impressions/1000)
#weekly CPM= (sum amount)/[(sum impressions)/1000]

CPM_feed_weekly= []

for x in range(len(weekly_df_feed_amount)):
    weekly_df_feed_amount.iloc[x,0] / weekly_df_feed_impressions.iloc[x,0]
    CPM_feed_weekly.append(weekly_df_feed_amount.iloc[x,0] / weekly_df_feed_impressions.iloc[x,0])
CPM_feed_weekly


# In[208]:


#CPM (Cost per 1,000 Impressions)= amount/(impressions/1000)
#weekly CPM= (sum amount)/[(sum impressions)/1000]
weekly_CPM_instagram_stories = []
for x in range(len(weekly_df_instagram_stories_amount)):
    weekly_df_instagram_stories_amount.iloc[x,0] / weekly_df_instagram_stories_impressions.iloc[x,0]
    weekly_CPM_instagram_stories.append(weekly_df_instagram_stories_amount.iloc[x,0] / weekly_df_instagram_stories_impressions.iloc[x,0])
weekly_CPM_instagram_stories


# In[215]:


#CPM (Cost per 1,000 Impressions)= amount/(impressions/1000)
#weekly CPM= (sum amount)/[(sum impressions)/1000]
daily_CPM_feed = []
for x in range(len(day_feed_amount)):
    day_feed_amount.iloc[x,0] / day_feed_impressions.iloc[x,0]
    daily_CPM_feed.append(day_feed_amount.iloc[x,0] / day_feed_impressions.iloc[x,0])

daily_CPM_feed


# In[216]:


#CPM (Cost per 1,000 Impressions)= amount/(impressions/1000)
#weekly CPM= (sum amount)/[(sum impressions)/1000]
daily_CPM_instagram = []
for x in range(len(day_df_instagram_stories_amount)):
    day_df_instagram_stories_amount.iloc[x,0] / day_df_instagram_stories_impressions.iloc[x,0]
    daily_CPM_instagram.append(day_df_instagram_stories_amount.iloc[x,0] / day_df_instagram_stories_impressions.iloc[x,0])

daily_CPM_instagram


# In[ ]:




