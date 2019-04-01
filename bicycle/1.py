import pandas as pd

filename = 'chicago.csv'

# load data file into a dataframe
df = pd.read_csv(filename)
#print (df.head())
# convert the Start Time column to datetime
df['Start Time'] = pd.to_datetime(df['Start Time'])
#print (df.head())

# extract hour from the Start Time column to create an hour column
def hr_func(ts):
    return ts.hour

df['hour'] = df['Start Time'].apply(hr_func)

#print (df.head())
# find the most common hour (from 0 to 23)
x = df['hour'].value_counts()
popular_hour = x.idxmax()

print('Most Frequent Start Hour:', popular_hour)
