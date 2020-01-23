'''
Setting the index
The last step that you'll take in this chapter is to set the stop_datetime column as the DataFrame's index. By replacing the default index with a DatetimeIndex, you'll make it easier to analyze the dataset by date and time, which will come in handy later in the course!

Instructions
100 XP
Set stop_datetime as the DataFrame index.
Examine the index to verify that it is a DatetimeIndex.
Examine the DataFrame columns to confirm that stop_datetime is no longer one of the columns.
'''
SOLUTION
# Set 'stop_datetime' as the index
ri.set_index('stop_datetime', inplace=True)

# Examine the index
print(ri.index)

# Examine the columns
print(ri.columns)