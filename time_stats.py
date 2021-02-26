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

print('\nCalculating The Most Frequent Times of Travel...\n')
start_time = time.time()

# display the most common month
print(bikedata.month.mode().loc[0] + '\n')

# display the most common day of week
print(bikedata.day.mode().loc[0] + '\n')

# display the most common start hour
#bikedata['hour'] = bikedata['Start Time'].dt.hour
print(bikedata['Start Time'].dt.hour.mode().loc[0])

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)