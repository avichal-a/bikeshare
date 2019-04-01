import time
import pandas as pd
import numpy as np
import datetime
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february', 'march', 'april', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'saturday', 'sunday']

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
    cities = ["chicago", "new york city", "washington"] 
    while True:
    
        print("PLease enter the city name from the given [chicago, new york city, washington]" )
        city = input()
        city = city.lower()
        if city  in cities:
            break;
      
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:

        print("PLease enter the month  [all, january, february, ... , june]" )
        month = input().lower()
	#monthq = monthq.lower()
        if month in months:
            break;


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:

        print("PLease enter the day  [all, monday, tuesday, ... sunday]" )
        day = input().lower()
	#day = day.lower()
        if day in days:
            break;


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
	# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    #print(df.head)
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
           
        mm = months.index(month)
        
        # filter by month to create the new dataframe
        df = df [ df['month'] == mm]
       
    # filter by day of week if applicable
    if day != 'all':
        daays = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        # filter by day of week to create the new dataframe
        dd = daays.index(day)
        
        df = df [ df['day_of_week'] == dd] 
    
    return df
    
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    fd = df['Start Time'].dt.month
    m = fd.value_counts()
    mo = m.idxmax()
    print("\nThe most common month is:", months[mo])

    # TO DO: display the most common day of week
    dw = df['Start Time'].dt.weekday
    w = dw.value_counts()
    wd = w.idxmax()
    daays = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    print("\nThe most common Day of week is:", daays[wd])


    # TO DO: display the most common start hour
    dh = df['Start Time'].dt.hour
    h = dh.value_counts()
    hh = h.idxmax()
    print("\nThe most common hour is:", hh)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    s = df['Start Station'].value_counts()
    st = s.idxmax()
    print("\nmost commonly used start station is:", st);
    		
    # TO DO: display most commonly used end station
    se = df['End Station'].value_counts()
    ste = se.idxmax()
    print("\nmost commonly used end station is:", ste);
    # TO DO: display most frequent combination of start station and end station trip
    qq = df.groupby('End Station')
    sq = qq['Start Station'].value_counts()
    sse = sq.idxmax()
    print("\nmost frequent combination of start station and end station trip",sse)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    TTT =   df['End Time'].dt.hour -df['Start Time'].dt.hour
    MTT =   df['End Time'].dt.minute -df['Start Time'].dt.minute
    STT =   df['End Time'].dt.second -df['Start Time'].dt.second
    TM = STT.sum()//60
    TM = MTT.sum() + TM
    H = (TM //60) + TTT.sum()
    TM = TM % 60;
    S =  STT.sum() % 60
    #print(H, TM, S)
    #MTT = TTT.mean()
 	
    # TO DO: display total travel time
    print("total travel time" , H,"hour", TM,"minute", S,"second")
   # a = df['Start Time'].dt.hour.mean()
    def cor(v):
    	if(v<0):
           return v/60
         #else :
           return 0 

    MTT = MTT + STT[ (STT < 0)] /60
    TTT = MTT[MTT < 0]/60 +TTT       
        
    S = (STT > 0).mean()
    TM = (MTT > 0).mean() 
    H =   TTT.mean()
    #TM = TM % 60;
    #S =  STT.mean() % 60
    print("Mean travel time","hour$ minute$ second$",H,TM,S )	

    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

		
    #df['Birth Year'] = pd.to_datetime(df['Birth Year']) 
    #print(df['Birth Year'].head)
  
    # TO DO: Display counts of user types
    a = df['User Type'].value_counts();
    print("\nUser type counts",a)
    try :
    	# TO DO: Display counts of gender
    	M = (df[df['Gender'] == 'Male'])
    	F = df[df['Gender'] == 'Female']
    	print("\nMale count" ,  len(M.index)," Fenale Count",len(F.index))   	     
    except KeyError:
        print("Gender column not present in file")
    try : 
    	# TO DO: Display earliest, most recent, and most common year of birth
    	now = datetime.datetime.now()
    	DIFF =  now.year - df['Birth Year']
    	#print(DIFF.head )
    	x = df['Birth Year'].max()
    	print ("Eraliest Birh year is", now.year - DIFF.max() ) 
    	print ("Most recent Birh year is", now.year - DIFF.min() )
    	print ("Most common Birh year is", df['Birth Year'][x] ) 
    	print("\nThis took %s seconds." % (time.time() - start_time))
    except KeyError:
        print("Birth Year column not present in file")
    print('-'*40)


def main(): 
	while True:
		city, month, day = get_filters()
		df = load_data(city, month, day)
        
		time_stats(df)
		station_stats(df)
		trip_duration_stats(df)
		user_stats(df)
		fl=0
		c = 0
		while True:
			x ="\n would you like to see raw data ? yes or no \n"
			y ="\n would you like to see more ? yes or no \n"
			if fl == 0 :
				print (x)
				fl = 1
			else :
				print (y)
			raw = input()
			if raw.lower()!= 'yes' :
				break
			
			print(df[c:c+5])
			c = c + 5	

		restart = input('\nWould you like to restart? Enter yes or no.\n')
		if restart.lower() != 'yes':
			break


if __name__ == "__main__":
	main()
