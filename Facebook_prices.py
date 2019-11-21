import numpy as np
import pandas as pd
from pandas import DataFrame
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[7]:


#import dataset
df = pd.read_csv (r'C:....')


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







