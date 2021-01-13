import time
import pandas as pd
import numpy as np

CITY_DATA = {1: 'chicago.csv',
             2: 'new_york_city.csv',
             3: 'washington.csv'}

MONTHS = {1: 'January', 2: 'February', 3: 'March',
          4: 'April', 5: 'May', 6: 'June'}

DAYS = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday',
        4: 'Thursday', 5: 'Friday', 6: 'Saturday',
        7: 'Sunday'}

FILTER = {1: 'month', 2: 'day', 3: 'both', 4: 'none'}


def input_check(message, dic):
    """ Asks user to specify a city, month, and day. Also, handle unexpected input.

        This function takes a message and dictionary
         message - the user will know which data should type it.
         dic - to check if the user types an invalid value.

         Try & Except will handle it
         return - user input
    """
    while True:
        try:
            user_input = int(input(message))
            # Note : when the user inputs value does not in dic, the check_value go to except
            check_value = dic[user_input]
            return user_input
        except ValueError as e:
            print('Sorry, you must type an integer.\n Try again')
        except KeyError as e:
            print('Sorry, you type a number is not in the list.\n Try again ')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # The reason that let me choose an integer as input
    # it will make the check operation easier and allow using Try and except
    print('Please for the following questions type your response as an integer')

    city = input_check('''Would you like to see data for Chicago, New York city, Washington?
                                    1=Chicago
                                    2=New York city
                                    3=Washington\n''', CITY_DATA)

    filter_by = input_check('''Would you like to filter the data by month, day, both ,
                               or not at all ( "none" for no time filter).? 
                                     1=month
                                     2=day 
                                     3=both
                                     4=none\n''', FILTER)

    if filter_by == 1:
        month = input_check('''Which month?
                                     1=January, 2=February, 3=March,
                                     4=April, 5=May, 6=June \n''', MONTHS)
        day = 'all'

    elif filter_by == 2:
        day = input_check('''Which day?
                                      1=Monday, 2=Tuesday,  3=Wednesday
                                      4=Thursday, 5=Friday, 6=Saturday
                                      7=Sunday\n ''', DAYS)
        month = 'all'
    elif filter_by == 3:
        month = input_check('''Which month?
                                      1=January, 2=February, 3=March,
                                      4=April, 5=May, 6=June \n''', MONTHS)
        day = input_check('''Which day?
                                      1=Monday, 2=Tuesday,  3=Wednesday
                                      4=Thursday, 5=Friday, 6=Saturday
                                      7=Sunday\n ''', DAYS)
    else:
        day, month = 'all', 'all'

    print('-' * 40)
    return city, month, day, filter_by


def load_data(city, month, day, filter_by):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime for calculating (Popular times of travel)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Create Three columns to store the extracted month, day of week and hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day
    df['hour'] = df['Start Time'].dt.hour

    # filter by month to create the new DataFrame
    if FILTER[filter_by] == 'month':
        df = df[df['month'] == month]

    # filter by day of week if applicable
    elif FILTER[filter_by] == 'day':
        df = df[df['day_of_week'] == day]

    # filter by day of week and month if applicable
    elif FILTER[filter_by] == 'both':
        df = df[df['month'] == month]
        df = df[df['day_of_week'] == day]
    # no filter
    else:
        pass

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    # Display the most common month
    print('The most common month is:', df['month'].mode()[0], '\n')

    # Display the most common day of week
    print('The most common day of week is:', df['day_of_week'].mode()[0], '\n')

    # Display the most common start hour
    print('The most common start hour is:', df['hour'].mode()[0], '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    print('The most commonly used start station is:', df['Start Station'].mode()[0], '\n')

    # Display most commonly used end station
    print('The most commonly used end station is:', df['End Station'].mode()[0], '\n')

    # Display most frequent combination of start station and end station trip
    # Create a new column to store start station and end station
    df['combination'] = df['Start Station'] + ' ' + df['End Station']
    print('The most frequent combination of start station and end station trip is: ', df['combination'].mode()[0], '\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time by using NUMPY
    print('The total travel time is: {} {} '.format(np.sum(df['Trip Duration']), 'Seconds \n'))
    # display mean travel time by using NUMPY
    print('The mean travel time is: {} {}'.format(np.mean(df['Trip Duration']), 'Seconds \n'))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df.groupby(['User Type'])['User Type'].count())

    # Gender and Birth only available in Chicago and New York City
    if city != 3:
        # Display counts of gender
        print(df.groupby(['Gender'])['Gender'].count())

        # Display earliest year of birth
        print('The earliest year of birth is:', df['Birth Year'].min())
        # Display the most recent year of birth
        print('The most recent year of birth is:', df['Birth Year'].max())
        # Display the most common year of birth
        print('The most common year of birth is:', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


# Prompt the user if he/she would like to see the raw data
def print_rawdata(df):
    """ The script should print 5 rows of the data at a time, then ask the user
        if they would like to see 5 more rows of the data

        takes df that is already filtered

        return - 5 rows of the data at a time
    """
    raw_counter = 1
    while True:
        raw_data = input('Would you like to see some raw data? Type Yes or No.\n').lower()
        if raw_data == 'yes':
            print(df[raw_counter:raw_counter+5])
            raw_counter += 5
        elif raw_data == 'no':
            break
        else:
            print('Sorry, you must type yes or no')


def main():
    while True:
        city, month, day, filter_by = get_filters()

        df = load_data(city, month, day, filter_by)
        print('The following results depend on your choices.\n city: {} , filter by: {}'
              .format((CITY_DATA[city][:-4]).title(), FILTER[filter_by].title()))
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        print_rawdata(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you for using our program.')
            break



if __name__ == "__main__":
    main()
