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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("Enter the city name: \n").lower()
    while city not in ['chicago','new york city','washington']:
        print("INVALID CITY")
        city=input("Enter a valid city name: \n").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Enter the month name: \n").lower()
    while month not in ['all','january','february','march','april','may','june']:
        print("INVALID MONTH")
        month=input("Enter a valid month name: \n").lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Enter the day name: \n").lower()
    while day not in ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']:
        print("INVALID DAY")
        month=input("Enter a valid day name: \n").lower()

    print('-'*40)
    return city,month,day


def load_data(city,month,day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
      # load data file into a dataframe
    df =pd.read_csv(CITY_DATA[city]) 

    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df =df[df['Start Time'].dt.month==month] 

    # filter by day of week if applicable
    
    if day != 'all':
        day=day.title()
        # filter by day of week to create the new dataframe
        days=["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
        day = days.index(day)+1
        df =df[df['Start Time'].dt.day==day] 
#     print(df["Start Time"])
    return df





def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    if month=='all':
        df['month'] =df['Start Time'].dt.month
        common_month=df['month'].mode()[0] 
        print("The most common month: ",common_month)

    # TO DO: display the most common day of week
    if day=='all':
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        common_day=df['day_of_week'].mode()[0]
        print("the most common day of week: ",common_day)
    # TO DO: display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    # Find the most common hour (from 0 to 23)
    common_hour=df['hour'].mode()[0]
    print("The most common hour is:",common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Popular_start_station=df['Start Station'].mode()[0]
    print("The most commonly used start station: ",Popular_start_station)
    # TO DO: display most commonly used end station
    Popular_end_station=df['End Station'].mode()[0]
    print("The most commonly used end station: ",Popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df["The whole trip"]=df['Start Station'] +" to "+df['End Station']
    popular_trip=df["The whole trip"].mode()[0]
    print("The most commonly used trip: ",popular_trip)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("Total travel time: ",total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print("Mean travel time: ",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    

    # TO DO: Display counts of gender
    try:
        gender=df["Gender"].value_counts()
        print("counts of gender\n",gender)
    except:
        print("No column called gender")
        
            

#     TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_of_birth=df['Birth Year'].min()
        most_recent_year_of_birth=df['Birth Year'].max()
        most_common_year_of_birth=df['Birth Year'].mode()[0]
        print("The earliest  year of birth is:  \n",earliest_year_of_birth)
        print("The most recent  year of birth is:  \n",most_recent_year_of_birth)
        print("The most common  year of birth is:  \n",most_common_year_of_birth)
        print("\nThis took %s seconds." % (time.time() - start_time))
    except:
        print("There isn't a column called Birth Year in this dataset ")
    print('-'*40)

def display_data_row_by_row(city):
    answer=input("Would you display the row data of this city \n ENTER yes or no, please\n").lower()
    while answer=='yes':
        try:
            for bulk in pd.read_csv(CITY_DATA[city],chunksize=5):
                print(bulk)
                answer=input("Would you display another bulk of row data of this city \n ENTER yes or no, please\n").lower()
                
                if answer != 'yes':
                    print("THANK YOU FOR YOUR TIME :)")
                    break
            break
        except KeyboardInterrupt:
            print("THANK YOU FOR YOUR TIME :)")
            break
    
def main():
    while True:
        city,month,day = get_filters()
        
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data_row_by_row(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
