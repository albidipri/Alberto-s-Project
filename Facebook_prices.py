#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


#import dataset
df = pd.read_csv ('....')


# In[8]:


#filtering values
df = df.loc[df['CPC (All)'] >= 10]


# In[19]:


#splitting the PLacement coloumn of the dataset
df_marketplace = df[df['Placement']== 'marketplace']
df_messenger_inbox = df[df['Placement']== 'messenger_inbox']
df_instream_video = df[df['Placement']== 'instream_video'] 
df_facebook_stories = df[df['Placement']=='facebook_stories']
df_messenger_stories = df[df['Placement']=='messenger_stories']
df_feed = df[df['Placement']=='feed']
df_instagram_stories = df[df['Placement']=='instagram_stories']
df_right_hand_column = df[df['Placement']=='right_hand_column']
df_instagram_explore = df[df['Placement']=='instagram_explore']
df_rewarded_video = df[df['Placement']=='rewarded_video']
df_instant_article = df[df['Placement']=='instant_article']
df_an_classic = df[df['Placement']=='an_classic']
df_suggested_video = df[df['Placement']=='suggested_video']


# In[23]:


#df_marketplace
df_marketplace['Day'] = df_marketplace['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View" "Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="Cost per 3-Second Video View",hue='Placement', data=df_marketplace)


# In[45]:


#Messenger Inbox
df_messenger_inbox['Day'] = df_messenger_inbox['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View" "Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="Cost per 1,000 People Reached",hue='Placement', data=df_messenger_inbox)


# In[10]:


#df_instream_video
df_instream_video['Day'] = df_instream_video['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View" "Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="CPM (Cost per 1,000 Impressions)",hue='Placement', data=df_instream_video)


# In[28]:


#df_facebook_stories
df_facebook_stories['Day'] = df_facebook_stories['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View" "Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="CPM (Cost per 1,000 Impressions)",hue='Placement', data=df_facebook_stories)


# In[40]:


#df_feed
df_feed['Day'] = df_feed['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View"
#"Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
#df_feed = df_feed.loc[df["CPC (All)"] >= 10]
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="CPC (All)",hue='Placement', data=df_feed)


# In[11]:


#df_messenger_stories
df_messenger_stories['Day'] = df_messenger_stories['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View"
#"Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="CPM (Cost per 1,000 Impressions)",hue='Placement', data=df_messenger_stories)


# In[27]:


#df_instagram_stories
df_instagram_stories['Day'] = df_instagram_stories['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View"
#"Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="CPM (Cost per 1,000 Impressions)",hue='Placement', data=df_instagram_stories)


# In[26]:


#df_right_hand_column
df_right_hand_column['Day'] = df_right_hand_column['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View"
#"Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="Cost per Post Engagement",hue='Placement', data=df_right_hand_column)


# In[24]:


#df_instagram_explore
df_instagram_explore['Day'] = df_instagram_explore['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View"
#"Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="CPM (Cost per 1,000 Impressions)",hue='Placement', data=df_instagram_explore)


# In[23]:


#df_rewarded_video
df_rewarded_video['Day'] = df_rewarded_video['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View"
#"Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="CPM (Cost per 1,000 Impressions)",hue='Placement', data=df_rewarded_video)


# In[22]:


#df_instant_article
df_instant_article['Day'] = df_instant_article['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View"
#"Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="CPM (Cost per 1,000 Impressions)",hue='Placement', data=df_instant_article)


# In[20]:


#df_an_classic
df_an_classic['Day'] = df_an_classic['Day'].astype('datetime64')
#"CPM (Cost per 1,000 Impressions)" "CPC (All)" "Cost per 1,000 People Reached" "Cost per 3-Second Video View"
#"Cost per 10-Second Video View" "CPC (Cost per Link Click)" "Cost per Post Engagement"
#in order to get the graph desidered, copy and paste the Y value desired in the sns.linplot
plt.figure(dpi=120)
plt.xticks(rotation=90)
sns.lineplot(x='Day',y="CPM (Cost per 1,000 Impressions)",hue='Placement', data=df_an_classic)


# In[24]:


#df_suggested_video
df_suggested_video['Day'] = df_suggested_video['Day'].astype('datetime64')
df_suggested_video.dtype
#plt.figure(dpi=120)
#plt.xticks(rotation=90)
#sns.lineplot(x='Day',y="Cost per 10-Second Video View",hue='Placement', data=df_suggested_video)


# In[12]:


df_instagram_stories['Day'] = pd.to_datetime(df_instagram_stories.Day)


# In[21]:


df


# In[16]:


df_instagram_stories.Day.dt.weekday_name


# In[31]:


df_instagram_stories['Day'] = pd.to_datetime(df_instagram_stories['Day']) - pd.to_timedelta(7, unit='d')
#df_istagram_stories = df_istagram_stories.groupby(['Name', pd.Grouper(key='Day', freq='W-MON')]


# In[32]:


df_instagram_stories


# In[ ]:




