import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('\n************************************************\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    # Asking about the city name and atracing the user attention to the rules of this name
    while city not in CITY_DATA.keys():
        print("\n Please enter the name of city from the following list: ")
        print("\n I--Chicago   II--New York City    III--Washington")
        print("\n ++++ [Just full name of the city is acceptable] ++++ .")
        name_c = input()
        # Unifying the city name form  
        city = name_c.lower()
        if city not in CITY_DATA.keys():
            print("Unacceptable entry; Please try again...")
    print(f"\nYour city is {city.title()}")
  

    # TO DO: get user input for month (all, january, february, ... , june)

    Months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    #Asking the user about the required month and looking for it in the data set
    while month not in Months.keys():
        print("\n Please enter the month from the following list: ")
        print("\n I--January   II--February    III--March    IV--April    V--May    VI--June    VII--All")
        print("\n ++++ [Just all for all data or full name of a specific month is acceptable] ++++ .")
        name_m = input()
        # Unifying the month name form
        month = name_m.lower()
        if month not in Months.keys():
            print("Unacceptable entry; Please try again...")
    print(f"\n You have chosen to explore data for {month.title()}")
 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    Days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    #Asking the user about the required day name and looking for it in the data set
    while day not in Days:
        print("\n Please enter the day of the week from the following list: ")
        print("\n All -- Monday  -- Tuesday  -- Wednesday  --  Thursday  --  Friday  --  Saturday  --  Sunday")
        print("\n ++++ [Just all for all days in the week or full name of a specific day is acceptable] ++++ .")
        name_d = input()
        day = name_d.lower()
        if day not in Days:
            print("Unacceptable entry; Please try again...")
    print(f"\n You have chosen to explore data for {day.title()}")
    print(f"\nYou want to explore data for: {city.upper()}, in {month.upper()} month(s) and {day.upper()} day(s).")
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
    print("\n Data loading please wait...")
    # loading the data from data set for the required city
    df = pd.read_csv(CITY_DATA[city])
    # Converting the Start time to the datetime form  
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # call the data set using the month
    df['month'] = df['Start Time'].dt.month
    # call the data set by using day name
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        months_list = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months_list.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Frequent Start month:', popular_month)
  

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_day = df['day_of_week'].mode()[0]
    print('Most Frequent Start day:', popular_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    # TO DO: display most commonly used start station
    print('\n For The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Uses mode method to find the most common start station
    popu_start_station = df['Start Station'].mode()[0]

    print(f"The most popular start station: {popu_start_station}")

    # TO DO: display most commonly used end station
    popu_end_station = df['End Station'].mode()[0]

    print(f"\nThe most popular end station: {popu_end_station}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combo = df['Start To End'].mode()[0]
    print(f"\n The most frequent combination of trips are from {combo}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print(f"The total trip duration is {hour} hours, {minute} minutes and {second} seconds.")

    # TO DO: display mean travel tim
    average_duration = round(df['Trip Duration'].mean())
    mins, sec = divmod(average_duration, 60)
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print(f"\nThe average trip duration is {hrs} hours, {mins} minutes and {sec} seconds.")
    else:
        print(f"\nThe average trip duration is {mins} minutes and {sec} seconds.")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(f" Types of users distrebution as following: \n\n{user_types}")
    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print(f"\n Users gender distrebution as:\n\n{user_gender}")
    except:
        print("\n No Gender data in this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        comm_year = df['Birth Year'].mode()[0]
        print(f"\n The earliest year of birth: {earliest}\n")
        print(f"\n The most recent year of birth: {most_recent}\n")
        print(f"\n The most common year of birth: {comm_year}")
    except:
        print(" No birth year details for this city.")

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
