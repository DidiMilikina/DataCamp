'''
Preparing the DataFrames
In this exercise, you'll prepare the traffic stop and weather rating DataFrames so that they're ready to be merged:

With the ri DataFrame, you'll move the stop_datetime index to a column since the index will be lost during the merge.
With the weather DataFrame, you'll select the DATE and rating columns and put them in a new DataFrame.
Instructions
100 XP
Reset the index of the ri DataFrame.
Examine the head of ri to verify that stop_datetime is now a DataFrame column, and the index is now the default integer index.
Create a new DataFrame named weather_rating that contains only the DATE and rating columns from the weather DataFrame.
Examine the head of weather_rating to verify that it contains the proper columns.
'''
SOLUTION
# Reset the index of 'ri'
ri.reset_index(inplace=True)

# Examine the head of 'ri'
print(ri.head())

# Create a DataFrame from the 'DATE' and 'rating' columns
weather_rating = weather[['DATE', 'rating']]

# Examine the head of 'weather_rating'
print(weather_rating.head())