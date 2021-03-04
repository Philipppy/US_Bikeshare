# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 20:28:46 2021

@author: Julia und Philipp
"""

import time
import calendar
import datetime
import pandas as pd
import numpy as np

city = 'chicago'
month = 'all'
day = 'all'
    
    
#load raw data
bikedata = pd.read_csv(city + ".csv")

#use Start time column to extract months and days of rental events
bikedata['Start Time'] = pd.to_datetime(bikedata['Start Time'])
bikedata['End Time'] = pd.to_datetime(bikedata['End Time'])
#print(bikedata.head(10))
bikedata['month'] = bikedata['Start Time'].dt.month_name()
#print(bikedata.head(10))
bikedata['day'] = bikedata['Start Time'].dt.day_name()
#print(bikedata.head(10))

#filter by month
if month != 'all':
        # filter by month to create the new dataframe
        bikedata = bikedata[bikedata['month']==month.capitalize()]
        
#filter by day
if day != 'all':
        # filter by month to create the new dataframe
        bikedata = bikedata[bikedata['day']==day.capitalize()]
        
        
#print(bikedata.head(3))

'----------------------------------------------------------------------------'
'----------------------------------------------------------------------------'

print('\nCalculating User Stats...\n')
start_time = time.time()

# Display counts of user types
print('Usertypes:\n')
print(bikedata['User Type'].value_counts())

# Display counts of gender
print('Gender:\n')
print(bikedata['Gender'].value_counts())

# Display earliest, most recent, and most common year of birth
print('\nEarliest year of birth:\n')
print(int(bikedata['Birth Year'].min()))

print('\nMost recent year of birth:\n')
print(int(bikedata['Birth Year'].max()))

print('\nMost common year of birth:\n')
print(int(bikedata['Birth Year'].mode().iloc[0]))


print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)
