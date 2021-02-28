# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:49:43 2021

@author: Julia und Philipp
"""

import time
import calendar
import pandas as pd
import numpy as np

# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 22:01:09 2021

@author: Julia und Philipp
"""

"""Displays statistics on the most frequent times of travel."""
    
city = 'washington'
month = 'all'
day = 'all'
    
    
#load raw data
bikedata = pd.read_csv(city + ".csv")

#use Start time column to extract months and days of rental events
bikedata['Start Time'] = pd.to_datetime(bikedata['Start Time'])
print(bikedata.head(10))
bikedata['month'] = bikedata['Start Time'].dt.month_name()
print(bikedata.head(10))
bikedata['day'] = bikedata['Start Time'].dt.day_name()
print(bikedata.head(10))

#filter by month
if month != 'all':
        # filter by month to create the new dataframe
        bikedata = bikedata[bikedata['month']==month.capitalize()]
        
#filter by day
if day != 'all':
        # filter by month to create the new dataframe
        bikedata = bikedata[bikedata['day']==day.capitalize()]
        
        
print(bikedata.head(3))


'----------------------------------------------------------------------------'
'----------------------------------------------------------------------------'

print('\nCalculating The Most Popular Stations and Trip...\n')
start_time = time.time()

# display most commonly used start station
print(bikedata['Start Station'].mode().loc[0] + '\n')
print(bikedata['Start Station'].value_counts().head(1))
print('\n')
# display most commonly used end station
print(bikedata['End Station'].mode().loc[0] + '\n')
print(bikedata['End Station'].value_counts().head(1))

# display most frequent combination of start station and end station trip
#group data by Start and End Station
start_end = bikedata.groupby(['Start Station', 'End Station'])
#start_end['count'] = start_end.count()
#start_end.columns=['count']
#print(start_end['count'])
#start_end.sort_values(['count'],ascending=False,inplace=True)
print(start_end)

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)