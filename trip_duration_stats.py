# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 21:40:36 2021

@author: Julia und Philipp
"""


import time
import calendar
import datetime
import pandas as pd
import numpy as np


#https://stackoverflow.com/questions/22923775/calculate-pandas-dataframe-time-difference-between-two-columns-in-hours-and-minu
#https://www.datasciencemadesimple.com/difference-two-timestamps-seconds-minutes-hours-pandas-python-2/

city = 'washington'
month = 'all'
day = 'all'
    
    
#load raw data
bikedata = pd.read_csv(city + ".csv")

#use Start time column to extract months and days of rental events
bikedata['Start Time'] = pd.to_datetime(bikedata['Start Time'])
bikedata['End Time'] = pd.to_datetime(bikedata['End Time'])
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
#trip duration per trip in minutes
timediff = (bikedata['End Time'] - bikedata['Start Time']).astype('timedelta64[s]')/60
#total traveltime in hours
total_travel_t =timediff.sum()/60
#round to two decimals:
total_travel_t= round(total_travel_t,2)
print(total_travel_t)

#mean travel time in minutes
mean_travel_t = timediff.mean()
#round to two decimals
mean_travel_t = round(mean_travel_t,2)
print(mean_travel_t)

