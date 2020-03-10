'''
Baseline based on the date
We've already built 3 different baseline models. To get more practice, let's build a couple more. The first model is based on the grouping variables. It's clear that the ride fare could depend on the part of the day. For example, prices could be higher during the rush hours.

Your goal is to build a baseline model that will assign the average "fare_amount" for the corresponding hour. For now, you will create the model for the whole train data and make predictions for the test dataset.

The train and test DataFrames are available in your workspace. Moreover, the "pickup_datetime" column in both DataFrames is already converted to a datetime object for you.

Instructions
100 XP
Get the hour from the "pickup_datetime" column for the train and test DataFrames.
Calculate the mean "fare_amount" for each hour on the train data.
Make test predictions using pandas' map() method and the grouping obtained.
Write predictions to the file.
'''
SOLUTION

# Get pickup hour from the pickup_datetime column
train['hour'] = train['pickup_datetime'].dt.hour
test['hour'] = test['pickup_datetime'].dt.hour

# Calculate average fare_amount grouped by pickup hour 
hour_groups = train.groupby('hour')['fare_amount'].mean()

# Make predictions on the test set
test['fare_amount'] = test.hour.map(hour_groups)

# Write predictions
test[['id','fare_amount']].to_csv('hour_mean_sub.csv', index=False)