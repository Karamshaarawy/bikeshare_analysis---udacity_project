import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
days=['mon','tue','wed','thu','fri','sat','sun']
weekday=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
months=["jan","feb",'mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
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
    city_filter=input('would you like to see data for Chicago, New York City or Washington? ')
    c=city_filter.lower()
    while (c not in CITY_DATA):
	    print('there are no information provided about the city name you entered ')
	    print('please choose a city from the list provided ')
	    x=list(CITY_DATA.keys())
	    print('please take care of spilling ')
	    city_filter=input('would you like to see data for Chicago, New York or Washington: ')
	    c=city_filter.lower()
    city=c
    # get user input filters to be used
    day_month_filter=input('would you like to filter the data by day, month both or non at all (day/month/both/none)? ')
    d_m_filter=day_month_filter.lower()
    while d_m_filter !='day' and d_m_filter !='none' and d_m_filter!='month' and d_m_filter!='both':
	    print("please enter a valid value (day/month/both/no)? ")
	    day_month_filter=input('would you like to filter the data by day, month or not at all (day/month/both/none)? ')
	    d_m_filter=day_month_filter.lower()
    # get user input for chosen filters 
    df1=pd.read_csv(CITY_DATA[city])
    df1['Start Time'] =pd.to_datetime(df1["Start Time"])
    df1['month'] =df1["Start Time"].dt.month
    df1['day']=df1['Start Time'].dt.weekday
    months_available=sorted(list((df1['month'].unique())))
    days_available=sorted(list((df1['day'].unique())))
    if d_m_filter=='day':
        day_filter=input("please enter the day you want to show its data "+str(days[days_available[0]:days_available[-1]+1]))
        day_filter=day_filter.lower()
        while day_filter not in days:
            print("please enter a valid value "+str(days[days_available[0]:days_available[-1]+1]))
            day_filter=input("please enter the day you want to show its data "+str(days[days_available[0]:days_available[-1]+1]))
            day_filter=day_filter.lower()
        day=day_filter
        month='none'
    elif d_m_filter=='month':
        month_filter=input("please enter the month you want to show its data "+str(months[months_available[0]-1:months_available[-1]]))
        month_filter=month_filter.lower()
        while month_filter not in months:
            print("please enter a valid value "+str(months[months_available[0]-1:months_available[-1]]))
            month_filter=input("please enter the mont you want to show its data "+str(months[months_available[0]-1:months_available[-1]]))
            month_filter=month_filter.lower()
        month=month_filter
        day='none'
    elif d_m_filter=='both':
        month_filter=input("please enter the month you want to show its data "+str(months[months_available[0]-1:months_available[-1]]))
        month_filter=month_filter.lower()
        while month_filter not in months:
            print("please enter a valid value "+str(months[months_available[0]-1:months_available[-1]]))
            month_filter=input("please enter the mont you want to show its data "+str(months[months_available[0]-1:months_available[-1]]))
            month_filter=month_filter.lower()
        month=month_filter
        day_filter=input("please enter the day you want to show its data "+str(days[days_available[0]:days_available[-1]+1]))
        day_filter=day_filter.lower()
        while day_filter not in days:
            print("please enter a valid value "+str(days[days_available[0]:days_available[-1]+1]))
            day_filter=input("please enter the day you want to show its data "+str(days[days_available[0]:days_available[-1]+1]))
            day_filter=day_filter.lower()
        day=day_filter
    else:
        day="none"
        month="none"
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
    df1=pd.read_csv(CITY_DATA[city])
    df1['Start Time'] =pd.to_datetime(df1["Start Time"])
    df1['month'] =df1["Start Time"].dt.month
    df1['day']=df1['Start Time'].dt.weekday
    if month!='none' and day!='none':
        month = months.index(month)
        day=days.index(day)
        df2=df1[df1['month']==month+1]
        df=df2[df2['day']==day]
    elif month!='none' and day=='none':
        month = months.index(month) 
        df=df1[df1['month']==month+1]
    elif month=='none' and day!='none':
        day=days.index(day)
        df=df1[df1['day']==day]
    else:
        df=df1
    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    if month=='none':
        m_c_m=df['month'].mode()[0]
        m_c_m_c=df[df['month']==m_c_m].values
        count=len(list(m_c_m_c))
        print('the most common month is {} , count {}'.format(m_c_m,count))
    else:
        print('we are showing data from month {}'.format(month) )
    # display the most common day of week
    
    if day=='none':
        m_c_d=df['day'].mode()[0]
        m_c_d_c=df[df['day']==m_c_d].values
        count=len(list(m_c_d_c))
        print('the most common day is {} , count {}'.format(m_c_d,count))
    else:
        print('we are showing data from day {}'.format(day) )
    # display the most common start hour
    df['hour'] =df["Start Time"].dt.hour
    m_c_h=df['hour'].mode()[0]
    m_c_h_c=df[df['hour']==m_c_h].values
    count=len(list(m_c_h_c))
    print('the most common hour is {} , count {}'.format(m_c_h,count))
    m_c_h_c=df[df['hour']==m_c_h].values
    count=len(list(m_c_h_c))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    m_c_s_s=df['Start Station'].mode()[0]
    m_c_s_s_c=df[df['Start Station']==m_c_s_s].values
    count=len(list(m_c_s_s_c))
    print('most common starting station is {} which occured for {} times'.format(m_c_s_s,count))

    # display most commonly used end station
    m_c_e_s=df['End Station'].mode()[0]
    m_c_e_s_c=df[df['End Station']==m_c_e_s].values
    count=len(list(m_c_s_s_c))
    print('most common ending station is {} which occurs for {} times'.format(m_c_e_s,count))

    # display most frequent combination of start station and end station trip
    df['start_stop']='starts from '+df['Start Station']+' and stops at '+df['End Station']
    m_c_t=df['start_stop'].mode()[0]
    m_c_t_c=df[df['start_stop']==m_c_t].values
    count=len(list(m_c_t_c))
    print('most common trip {} which occurs for {} times'.format(m_c_t,count))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    counts_of_trips=df['Trip Duration'].values
    count=len(list(counts_of_trips))
    # display total travel time
    t_t_t=df['Trip Duration'].sum()
    print('total travel time {} seconds for {} trips'.format(t_t_t,count))

    # display mean travel time
    a_t_t=df['Trip Duration'].mean()
    print('average_travel_time {} seconds'.format(a_t_t))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    c_o_e_u_t=df['User Type'].value_counts()
    print(c_o_e_u_t)
    # Display counts of gender
    s='Gender'
    r=df.columns
    if s in r:
        c_o_e_g=df['Gender'].value_counts()
        print(c_o_e_g)

    # Display earliest, most recent, and most common year of birth
    s='Birth Year'
    if s in r:
        e_y_o_b=df['Birth Year'].min()
        e_y_o_b_c=df[df['Birth Year']==e_y_o_b].values
        count=len(list(e_y_o_b_c))
        print('the most earliest year of birth is {} which represent {} person'.format(e_y_o_b,count))
        m_r_y_o_b=df['Birth Year'].max()
        m_r_y_o_b_c=df[df['Birth Year']==m_r_y_o_b].values
        count=len(list(m_r_y_o_b_c))
        print('the most recent year of birth is {} which represent {} person'.format(m_r_y_o_b,count))
        m_c_y_o_b=df['Birth Year'].mode()[0]
        m_c_y_o_b_c=df[df['Birth Year']==m_c_y_o_b].values
        count=len(list(m_c_y_o_b_c))
        print('the most common year of birth is {} which represent {} person'.format(m_c_y_o_b,count))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show=input('would you want to see the raw data? (yes/no)')
        show=show.lower()
        df=df.drop(['day','month','hour','start_stop'],axis=1)
        x=df.shape
        if show=='yes':
            i=5
            print(df[0:i])
            while True:
                show=input('would you want to see more five rows? (yes/no)')
                if show=='yes':
                    print(df[i:i+5])
                    i+=5
                    print(i)
                    if i>=x[0]:
                        print('you have reached the end of the data')
                        break
                elif show=='no':
                    break
                else:
                    print('please enter a valid value (yes/no)')
                    continue			
        restart = input('\nWould you like to restart? Enter yes or no. : ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
