'''
Combining object columns
Currently, the date and time of each traffic stop are stored in separate object columns: stop_date and stop_time.

In this exercise, you'll combine these two columns into a single column, and then convert it to datetime format. This will enable convenient date-based attributes that we'll use later in the course.

Instructions
100 XP
Use a string method to concatenate stop_date and stop_time (separated by a space), and store the result in combined.
Convert combined to datetime format, and store the result in a new column named stop_datetime.
Examine the DataFrame .dtypes to confirm that stop_datetime is a datetime column.
'''
SOLUTION
# Concatenate 'stop_date' and 'stop_time' (separated by a space)
combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')

# Convert 'combined' to datetime format
ri['stop_datetime'] = pd.to_datetime(combined)

# Examine the data types of the DataFrame
print(ri.dtypes)