'''
Engineering numerical features - datetime
There are several columns in the volunteer dataset comprised of datetimes. Let's take a look at the start_date_date column and extract just the month to use as a feature for modeling.

Instructions
100 XP
Use Pandas to_datetime() function on the volunteer["start_date_date"] column and store it in a new column called start_date_converted.
To retrieve just the month, apply a lambda function to volunteer["start_date_converted"] that grabs the .month attribute from the row. Store this in a new column called start_date_month.
Print the head() of just the start_date_converted and start_date_month columns.
'''
SOLUTION
# First, convert string column to date column
volunteer["start_date_converted"] = pd.to_datetime(volunteer["start_date_date"])

# Extract just the month from the converted column
volunteer["start_date_month"] = volunteer['start_date_converted'].apply(lambda row: row.month)

# Take a look at the converted and new month columns
print(volunteer[['start_date_converted', 'start_date_month']].head())