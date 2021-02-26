import time
import calendar
import pandas as pd
import numpy as np

#create possible user entries for the data
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['all','january','february', 'march', 'april', 'may', 'june']

weekdays = list(calendar.day_name)
weekdays_lower = [weekdays_lower.lower() for weekdays_lower in weekdays]
weekdays_lower.append('all')

#Check for valid input
def valid_input (message, inputs):
    """
    

    Parameters
    ----------
    message : (str) - dialog displayed to the user
    inputs : (list) - list of valid inputs

    Returns
    -------
    response : (str) - valid user intput 

    """
    
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

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington)
    city = valid_input("Please enter a city out of the options 'Chicago', 'New York City' "
                      "and 'Washington': ",list(CITY_DATA.keys()))

    # get user input for month (all, january, february, ... , june)
    month = valid_input("Please enter a month out of the options 'all', 'january' "
                        ", 'february', 'march', 'april', 'may', 'june': ",months)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = valid_input("Please enter a weekday out of the options"
                      " 'all','monday',...,'sunday': ",weekdays_lower)

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city + ".csv")
    
    #use Start time column to extract months and days of rental events
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month_name()
    
    df['day'] = df['Start Time'].dt.day_name()
    
    
    #filter by month
    if month != 'all':
            # filter by month to create the new dataframe
            df = df[df['month']==month.capitalize()]
            
    #filter by day
    if day != 'all':
            # filter by month to create the new dataframe
            df = df[df['day']==day.capitalize()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(bikedata.month.mode().loc[0] + '\n')
    
    # display the most common day of week
    print(bikedata.day.mode().loc[0] + '\n')
    
    # display the most common start hour
    print(bikedata['Start Time'].dt.hour.mode().loc[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
