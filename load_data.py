import time
import calendar
import pandas as pd
import numpy as np


# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:15:47 2021

@author: Julia und Philipp
"""

"""
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
"""

city = 'washington'
month = 'february'
day = 'wednesday'
    
    
#load raw data
bikedata = pd.read_csv(city + ".csv")

#use Start time column to extract months and days of rental events
bikedata['Start Time'] = pd.to_datetime(bikedata['Start Time'])
print(bikedata.head(10))
bikedata['month'] = bikedata['Start Time'].dt.month_name()
print(bikedata.head(10))
bikedata['day'] = bikedata['Start Time'].dt.day_name()
print(bikedata.head(10))



    
    
        
    
    
        