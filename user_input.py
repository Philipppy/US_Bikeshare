import calendar

# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:38:24 2021

@author: Julia und Philipp

"""

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['jan','feb', 'mar', 'apr', 'may', 'jun','all']

weekdays = list(calendar.day_name)
#print(weekdays)

weekdays_lower = [weekdays_lower.lower() for weekdays_lower in weekdays]
weekdays_lower.append('all')
#print(weekdays_lower)

def valid_input (message, inputs):
    
    while True:
        response = input(message).lower()
        if response in inputs:
            return response
            break
        elif response == "new york":
            response = "new york city"
            return response
            break
        else:
            print("This is not a valid input, please try again")
        
        

city = valid_input("Please enter a city out of the options 'Chicago', 'New York City' "
"and 'Washington': ",list(CITY_DATA.keys()))

print(city)

month = valid_input("Please enter a month out of the options 'all', 'january' "
", 'february', 'march', 'april', 'may', 'june'.\n" 
" Three characters are sufficient, e.g. january = jan: ",months)

print(month)

day = valid_input("Please enter a weekday out of the options 'all','monday',...,'sunday': ",weekdays_lower)

print(day)