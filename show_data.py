# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:57:42 2021

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


response = input("Do you wish to see 5 rows of trip data?" +
                     " Please enter yes or no.\n")
df_loc = 0 
    
while True:
    if response == 'yes':
        print(bikedata.iloc[df_loc:df_loc+5])
        df_loc = df_loc+5
    elif response == 'no':
        print("You decided to quit, Good bye!")
        break
    response = input("Do you wish to continue?"
                     + " Yes will show the next 5 lines, no will quit.\n")
        