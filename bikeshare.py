import time
import pandas as pd
import numpy as np
import json

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

user_name = input('Hello! My name is Philip Promise, What is your name?\n')
name = user_name
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    chicago = 'chicago'
    washington = 'washington'
    new_york = 'new york'

    print('\nHello {}, Let\'s explore some US bikeshare data!\n'.format(user_name))
    print('*****************************************************************************************************************************************************\n')

    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago','washington','new york']
    while True:
        city = input('How Would you like to view data? chicago, new york or washington\n').lower()
        if city not in cities:
            print("Incorrect input! Try again..\n")
            continue
        else:
            print('Lets Procees!')
            break
    print('You\'ve chosen to view data for {}! If this is not true, restart the program now!'.format(city))

      # Get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("\nWhich month would you like to filter by? january, february, march, april, may, june or type 'all' if you do not have any preference?\n").lower()
        if month not in months:
            print("Sorry, I didn't catch that. Try again.")
            continue
        else:
            break

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
    while True:
        day = input('\nWhich day? (sunday, monday, tuesday  e.t.c.)\n',).lower()
        if day not in days:
            print('Kindly try again.r')
            continue
        else:
            break
    print('Just a moment.. loading the data.')
    return city, month, day

    print('-'*40)


def load_data(city, month, day):
    import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

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

    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month

    # Filter by month if applicable
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if month != 'all':

        # Using the index of the months list
        month = months.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    df['day'] = df['Start Time'].dt.day_name()
    # Filter by day of week if applicable

    if day != 'all':
        days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']

        # Filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is: ', most_common_month)

    # Display the most common day of week
    most_common_day = df['day'].mode()[0]
    print('The most common day is :', most_common_day)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    start_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    most_commonly_used_start_station = df['Start Station'].mode()[0]
    print('The most common start station :', most_commonly_used_start_station)

    # Display most commonly used end station
    most_commonly_used_end_station = df['End Station'].mode()[0]
    print('The most common used end station :', most_commonly_used_end_station)

    # Display most frequent combination of start station and end station trip
    most_frequent_start_end_station = df.groupby(['Start Station', 'End Station']).count()
    print('The most frequent start and end station :', most_commonly_used_start_station, "&" ,most_commonly_used_end_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_time_travel = df['Trip Duration'].sum()
    print('total time travel :', total_time_travel)

    # Display mean travel time
    mean_time_travel = df['Trip Duration'].mean()
    print("The mean time travel :", mean_time_travel)

    # Display the total trip duration for each user type
    group_by_user_trip = df.groupby(['User Type']).sum()['Trip Duration']
    for index, user_trip in enumerate(group_by_user_trip):
        print("  {}: {}".format(group_by_user_trip.index[index], user_trip))

    print("\nThis took %s seconds." %(time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df.groupby(['User Type']).sum()
    print("The count of user types :\n", user_counts)

    # Display counts of gender
    gender_count = df.groupby(['Gender']).sum()
    print('The count of gender : \n', gender_count)

    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = df['Birth Year'].min()
    print('The earliest year of birtsh is: ', earliest_birth_year)

    most_recent_birth_year = df['Birth Year'].min()
    print('The most recent year of birth is: ', most_recent_birth_year)

    most_common_birth_year = df['Birth Year'].mode()
    print('The most common year of birth: ', most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """Displays raw bikeshare data."""
    length_of_row = df.shape[0]

    # Iteration starting from 0 to the number of rows in steps of 5
    for i in range(0, length_of_row, 5):
        trip_data = input('\nWould you like to examine each user trip data? Type \'yes\' or \'no\'\n> ')
        if trip_data.lower() != 'yes':
            break

        # Retrieve data and convert to json format and then split each json row data
        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in row_data:
            # Pretty print each user data
            parsed_row = json.loads(row)
            json_row = json.dumps(parsed_row, indent=2)
            print(json_row)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        display_data(df)

        if city == ('new york city' or 'washington'):
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('\nThank you for your time, {}.'.format(name))
            return


if __name__ == "__main__":
	main()
