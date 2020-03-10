'''
Replicate validation score
You've seen both validation and Public Leaderboard scores in the video. However, the code examples are available only for the test data. To get the validation scores you have to repeat the same process on the holdout set.

Throughout this chapter, you will work with New York City Taxi competition data. The problem is to predict the fare amount for a taxi ride in New York City. The competition metric is the root mean squared error.

The first goal is to evaluate the Baseline model on the validation data. You will replicate the simplest Baseline based on the mean of "fare_amount". Recall that as a validation strategy we used a 30% holdout split with validation_train as train and validation_test as holdout DataFrames. Both of them are available in your workspace.

Instructions
100 XP
Calculate the mean of "fare_amount" over the whole validation_train DataFrame.
Assign this naive prediction value to all the holdout predictions. Store them in the "pred" column.
'''
SOLUTION

import numpy as np
from sklearn.metrics import mean_squared_error
from math import sqrt

# Calculate the mean fare_amount on the validation_train data
naive_prediction = np.mean(validation_train['fare_amount'])

# Assign naive prediction to all the holdout observations
validation_test['pred'] = naive_prediction

# Measure the local RMSE
rmse = sqrt(mean_squared_error(validation_test['fare_amount'], validation_test['pred']))
print('Validation RMSE for Baseline I model: {:.3f}'.format(rmse))