#!/usr/bin/env python
# coding: utf-8

# # Data Analysis Project: Bike-Share Analysis

# ## Case Study: How does a Bike-Share navigate speedy success?

# ## Scenario
# ### In this project we study from a bike-share company to properly assess the current usage and to improve on the membership of the business. 

# ## Preparation

# In[2]:


# Libraries
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import glob
import datetime as dt
import time 


# In[3]:


# Folder path where the data for the last 12 months is kept in this case the data is stored locally
path = r'C:\Users\andyw\Desktop\Computer Science\Bike_data\All_data'
all_files = glob.glob(os.path.join(path , "*.csv"))

df_all_files = (pd.read_csv(f) for f in all_files)
bike_data = pd.concat(df_all_files, ignore_index=True)


# In[59]:


#Usefull variables for the analysis
minute = 60
hour = 60 * minute
day = 24 * hour
months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]


# In[10]:


#Calculate the 'ride_length' as a datetime object
bike_data['started_at'] = pd.to_datetime(bike_data['started_at'], format='%Y-%m-%d %H:%M:%S')
bike_data['ended_at'] = pd.to_datetime(bike_data['ended_at'], format='%Y-%m-%d %H:%M:%S')


# In[11]:


#Convert the data into seconds for operations and then back to hours
bike_data['ride_length'] = (bike_data['ended_at'] - bike_data['started_at'])
bike_data['ride_length'] = (((bike_data.ride_length.dt.days * 24)*hour) + ((bike_data.ride_length.dt.seconds)))
bike_data['ride_length'] = bike_data['ride_length'] / hour

bike_data


# In[19]:


#formats a column with the day of the week where 0 is Monday and 6 is Sunday
bike_data['day_of_week'] = bike_data['started_at'].dt.day_name()
bike_data['month'] = bike_data['started_at'].dt.month_name()


# ## Analysis

# ### Guiding Questions:
# #### - How should you organize your data to perform analysis on it?
# #### - Has your data been properly formatted?
# #### - What surpices did you discover in the data?
# #### - How will these insigths help anwser your business questions?
# 
# ### Key tasks:
# #### 1. Aggregate your data so it's useful and accessible.
# #### 2. Organize and format your data.
# #### 3. Perform calculations.
# #### 4. Indetify trends and relationships.
# 
# ### Deliverables
# #### Summary of Analysis

# In[21]:


#This calculates the mean ride length
mean_rl = bike_data['ride_length'].mean()
print(mean_rl)
#This calculates the max ride length
max_rl = bike_data['ride_length'].max()
print(max_rl)
#This calculates the mode ride length
mode_rl = bike_data['ride_length'].mode()
print(mode_rl)

bike_data


# ## Visualization of Data

# In[87]:


#Pivot table that focuses around the average ride length of members and casuals. 
table_1 = pd.pivot_table(bike_data, values='ride_length', index=['member_casual'], aggfunc=np.mean)
table_1

#Bar-plot between member type and ride length
ax1 = table_1.plot(kind='bar', color=['#273c75'], title='Ride Length Per Member Types')
plt.xticks(rotation=30, horizontalalignment="center")
plt.xlabel("Member Types")
plt.ylabel("Average Ride Length")


#Pivot table that focuses around the average ride length per day of the week where 0=Monday and its split between members and casual. 
table_2 = pd.pivot_table(bike_data, values='ride_length', index=['member_casual'], columns=['day_of_week'], aggfunc=np.mean)
table_2

#Bar-plot between member type
ax2 = table_2.plot(kind='bar', title='Ride Length for Member Types Per Weekday')
plt.xticks(rotation=30, horizontalalignment="center")
plt.xlabel("Member Types")
plt.ylabel("Average Ride Length")

#Pivot table that focuses around the number of rides per member type per day of the week where 0=Monday
table_3 = pd.pivot_table(bike_data, values='ride_id', index=['member_casual'], columns=['day_of_week'], aggfunc='count')
table_3

#Bar-plot between member type and the number of rides
ax3 = table_3.plot(kind='bar', title='Ride Count for Member Types Per Weekday')
plt.xticks(rotation=30, horizontalalignment="center")
plt.xlabel("Member Types")
plt.ylabel("Ride Count")

#Pivot table that focuses around the average ride length for member types per months
table_4 = pd.pivot_table(bike_data, values='ride_length', index=['month'], columns=['member_casual'], aggfunc=np.mean)
table_4

#Bar-plot between member type and the number of rides
ax4 = table_4.plot(kind='bar', title='Ride Length For Member Types')
plt.xticks(rotation=30, horizontalalignment="center")
plt.xlabel("Months")
plt.ylabel("Average Ride Length")

#Pivot table that focuses around the average ride count of ride type per month for casual and member riders
table_5 = pd.pivot_table(bike_data, values='ride_id', index=['month'], columns=['member_casual'], aggfunc='count')
table_5

#Bar-plot table that focuses around monthly count of ride types per member types
ax5 = table_5.plot(kind='bar', title='Ride Count Per Month')
plt.xticks(rotation=30, horizontalalignment="center")
plt.xlabel("Months")
plt.ylabel("Ride Count")


# ## Summary

# ### How do annual and casual riders use Cyclistic bikes differently?
# Based on the data and the analysis we see a few key point differeces between the types of riders.
# First, we see that average ride is longer for casual riders than member riders by a little over double the time.
# Second, we see that Sundays have the longest average ride length for both casual and member types. While the shortest is on tuesdays. Its important to note that for both groups we see that average ride length to be higher from Friday to Monday and shortest from Tuesday to thursday. That being said the difference is much more pronounce for the casual rider type.
# Third, in general the number of rides was higher for members throughout the week unlike casuals types which only had high number of rides during the weekends from friday to sunday.
# Another thing to note is the fact that when looking at the data through the year it is apparent that the summer and fall are the strongest months for business for bohth casuals and members. Out of the nine months in a year members do end up having more rides than casuals riders. However, the ride length is highest throughout the year for casual riders than member riders.
# 
# ### Based on the data charts the suggestions for this case study are:
# Increase the marketing strategy to suggest how more beneficial the yearly membership is to the casual riders since they spend the most time riding the bikes. That being said, while casual riders do longer rides, members and casual riders seem to do almost the same amount of rides per year. Interestingly enough the marketing team should focus their efforts around the summer and fall since those are the months where the highest number of casual riders are available. 
# 

# In[ ]:




