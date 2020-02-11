'''
Automated boosting round selection using early_stopping
Now, instead of attempting to cherry pick the best possible number of boosting rounds, you can very easily have XGBoost automatically select the number of boosting rounds for you within xgb.cv(). This is done using a technique called early stopping.

Early stopping works by testing the XGBoost model after every boosting round against a hold-out dataset and stopping the creation of additional boosting rounds (thereby finishing training of the model early) if the hold-out metric ("rmse" in our case) does not improve for a given number of rounds. Here you will use the early_stopping_rounds parameter in xgb.cv() with a large possible number of boosting rounds (50). Bear in mind that if the holdout metric continuously improves up through when num_boost_rounds is reached, then early stopping does not occur.

Here, the DMatrix and parameter dictionary have been created for you. Your task is to use cross-validation with early stopping. Go for it!

Instructions
100 XP
Perform 3-fold cross-validation with early stopping and "rmse" as your metric. Use 10 early stopping rounds and 50 boosting rounds. Specify a seed of 123 and make sure the output is a pandas DataFrame. Remember to specify the other parameters such as dtrain, params, and metrics.
Print cv_results.
'''
SOLUTION
# Create your housing DMatrix: housing_dmatrix
housing_dmatrix = xgb.DMatrix(data=X, label=y)

# Create the parameter dictionary for each tree: params
params = {"objective":"reg:linear", "max_depth":4}

# Perform cross-validation with early stopping: cv_results
cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, metrics='rmse', early_stopping_rounds=10, num_boost_round=50, seed=123, as_pandas=True, nfold=3)

# Print cv_results
print(cv_results)