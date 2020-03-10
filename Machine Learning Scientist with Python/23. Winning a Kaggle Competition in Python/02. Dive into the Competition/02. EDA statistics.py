'''
EDA statistics
As mentioned in the slides, you'll work with New York City taxi fare prediction data. You'll start with finding some basic statistics about the data. Then you'll move forward to plot some dependencies and generate hypotheses on them.

The train and test DataFrames are already available in your workspace.

Instructions 1/2
50 XP
1
Find the shapes of the train and test data.
Look at the head of the train data.

2
Describe the "fare_amount" column to get some statistics about the target variable.
Find the distribution of the "passenger_count" in the train data (using the value_counts() method).
'''
SOLUTION

1
# Shapes of train and test data
print('Train shape:', train.shape)
print('Test shape:', test.shape)

# Train head()
print(train.head())

2
# Shapes of train and test data
print('Train shape:', train.shape)
print('Test shape:', test.shape)

# Train head()
print(train.head())

# Describe the target variable
print(train.fare_amount.describe())

# Train distribution of passengers within rides
print(train.passenger_count.value_counts())