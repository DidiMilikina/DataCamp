'''
Features from dates
Another feature engineering task to perform is month and year extraction. Perform this task on the date column of the ufo dataset.

Instructions
100 XP
Print out the head() of the date column.
Using apply(), lambda, and the .month attribute, extract the month from the date column.
Using apply(), lambda, and the .year attribute, extract the year from the date column.
Take a look at the head() of the date, month, and year columns.
'''
SOLUTION
# Look at the first 5 rows of the date column
print(ufo['date'].head(5))

# Extract the month from the date column
ufo["month"] = ufo["date"].apply(lambda x: x.month)

# Extract the year from the date column
ufo["year"] = ufo["date"].apply(lambda x: x.year)

# Take a look at the head of all three columns
print(ufo[['date', 'month', 'year']].head())