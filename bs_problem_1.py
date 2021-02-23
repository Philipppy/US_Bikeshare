import pandas as pd

filename = '\Data\chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)

# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'],dayfirst = True)

# extract hour from the Start Time column to create an hour column
df['hour'] = df['Start Time'].dt.hour

# # find the most common hour (from 0 to 23)
popular_hour = df['hour'].mode().loc[0]

    
print('Most Frequent Start Hour:', popular_hour)