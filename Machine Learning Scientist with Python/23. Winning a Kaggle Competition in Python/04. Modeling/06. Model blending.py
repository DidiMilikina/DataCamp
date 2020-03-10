'''
Model blending
You will start creating model ensembles with a blending technique.

Your goal is to train 2 different models on the New York City Taxi competition data. Make predictions on the test data and then blend them using a simple arithmetic mean.

The train and test DataFrames are already available in your workspace. features is a list of columns to be used for training and it is also available in your workspace. The target variable name is "fare_amount".

Instructions
100 XP
Train a Gradient Boosting model on the train data using features list, and the "fare_amount" column as a target variable.
Train a Random Forest model in the same manner.
Make predictions on the test data using both Gradient Boosting and Random Forest models.
Find the average of both models predictions.
'''
SOLUTION

from sklearn.ensemble import GradientBoostingRegressor, RandomForestRegressor

# Train a Gradient Boosting model
gb = GradientBoostingRegressor().fit(train[features], train.fare_amount)

# Train a Random Forest model
rf = RandomForestRegressor().fit(train[features], train.fare_amount)

# Make predictions on the test data
test['gb_pred'] = gb.predict(test[features])
test['rf_pred'] = rf.predict(test[features])

# Find mean of model predictions
test['blend'] = (test['gb_pred'] + test['rf_pred']) / 2
print(test[['gb_pred', 'rf_pred', 'blend']].head(3))