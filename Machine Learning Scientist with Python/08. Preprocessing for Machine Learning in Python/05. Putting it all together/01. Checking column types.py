'''
Checking column types
Take a look at the UFO dataset's column types using the dtypes attribute. Two columns jump out for transformation: the seconds column, which is a numeric column but is being read in as object, and the date column, which can be transformed into the datetime type. That will make our feature engineering efforts easier later on.

Instructions
100 XP
Print out the dtypes of the ufo dataset.
Change the type of the seconds column by passing the float type into the astype() method.
Change the type of the date column by passing ufo["date"] into the pd.to_datetime() function.
Print out the dtypes of the seconds and date columns, to make sure it worked.
'''
SOLUTION
# Check the column types
print(ufo.dtypes)

# Change the type of seconds to float
ufo["seconds"] = ufo['seconds'].astype('float')

# Change the date column to type datetime
ufo["date"] = pd.to_datetime(ufo['date'])

# Check the column types
print(ufo[['seconds', 'date']].dtypes)