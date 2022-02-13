import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']




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
    city=input('Would you like to see data for Chicago, new york city, or Washington?').lower()
    while city not in CITY_DATA.keys():
        print('invalid input, please try again')
        city=input('Would you like to see data for Chicago, new york city, or Washington?').lower()
    
    #filter month and day 

    filt=['month','day','none','both']
    filterr=input('Would you like to filter the data by month, day,both, or none?').lower()
    while  filterr not in filt:
        print('invalid input, please try again')
        filterr=input('Would you like to filter the data by month, day,both, or none?').lower()
        
        
        
    # get user input for month (all, january, february, ... , june)    
    if filterr=='month'or filterr=='both' :
        months=['january','february', 'march','april', 'may','june']
        month=input('Which month - January, February, March, April, May, or June?').lower()
        while month not in months:
            print('invalid input, please try again')
            month=input('Which month - January, February, March, April, May, or June?').lower()
        if filterr=='month':
            day='all'
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if filterr=='day' or filterr=='both':
        days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
        while day not in days:
            print('invalid input, please try again')
            day=input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?').lower()
        if filterr=='day':
            month='all'
    #if user didn't choose filter 
    if filterr=='none' :
        month=day='all'


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
    # read data of the city that user choose
    df=pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    #filter by month 
    if month!='all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month=months.index(month)+1
        df = df[df['month']==month]
        
    # filter by day of week   
    if day!='all':
        df = df[df['day_of_week']==day.title()]
    
    


    return df





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].mode()[0]
    print('the most common month is {}'.format(common_month))


    # display the most common day of week
    common_day0fweek=df['day_of_week'].mode()[0]
    print('the most common day of week is {}'.format(common_day0fweek))


    # display the most common start hour
    df['hour'] =df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('the most common start hour is {}'.format(common_hour.round())) #Suggestions
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def trip_stations(df):
    """Displays statistics on the most frequent trip stations."""

    print('\nCalculating Trip stations...\n')
    start_time = time.time()

    # display the most common start station
    common_start_station=df['Start Station'].mode()[0]
    print('the most common start station: {}'.format(common_start_station))


    # display the most common end station
    common_end_station=df['End Station'].mode()[0]
    print('the most common end station: {}'.format(common_end_station))
    
    
    #display the most common trip from start to end 
    df['trip']=df['Start Station']+'to'+df['End Station']
    common_trip=df['trip'].mode()[0]
    print('the most frequent combination of start station and end station is {}'.format(common_trip))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time=df['Trip Duration'].sum()
        
    print('total travel time: {} seconds.'.format(total_time.round())) #Suggestions 


    # display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('mean travel time: {} seconds.'.format(mean_time.round()))  #Suggestions 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user=df['User Type'].value_counts()


    # Display counts of gender
    if 'Gender' in df.columns:
        counts_of_gender=df['Gender'].value_counts()
        print('the counts of each gender : {}'.format(counts_of_gender))
    else:
        print('gender only available for NYC and Chicago')


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_birth=df['Birth Year'].min()
        print('the oldest birth is {}'.format(int(earliest_birth))) #Suggestions 
        recent_birth=df['Birth Year'].max()
        print('the youngest  birth is {}'.format(int(recent_birth)))  #Suggestions 
        most_common_year=df['Birth Year'].mode()[0]
        print('the most common year of birth is  {}'.format(int(most_common_year)))  #Suggestions 


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def raw_data(df):
    """Displays raw Data."""

    print('\nDisplaying the raw Data...\n')
    start_time = time.time()

    # display the most common start station
    display=input('would like want to see the raw data, Answer with yes or no please ').lower()
    pd.set_option('display.max_columns',200) #Suggestions
    r=5
    i=0 #Requires Changes
    if display=='yes':
        
        print(df.head(5))
    else:
        print('no data to show')
    while True:
        more_display=input('would like to see 5 more rows of the data, Answer with yes or no please ').lower()
        if more_display=='yes':
            raws=r+5
            i+=5 #Requires Changes
            print(df.iloc[i:raws,:]) #Requires Changes
        elif more_display=='no':
            break
        else:
            print('invalid input, please try again')



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        trip_stations(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        # Requires Changes , remove line 273,274
        #city, month, day = get_filters()
        #df = load_data(city, month, day)
        #---------------------------------------------
        #Suggestions 
        answer=['yes','no']

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            break
        elif restart.lower() not in answer:
            print(' invalid input, please try again.\n')
            restart = input('\nWould you like to restart? Enter yes or no.\n')


if __name__ == "__main__":
	main()