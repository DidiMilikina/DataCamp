'''
Grid search with XGBoost
Now that you've learned how to tune parameters individually with XGBoost, let's take your parameter tuning to the next level by using scikit-learn's GridSearch and RandomizedSearch capabilities with internal cross-validation using the GridSearchCV and RandomizedSearchCV functions. You will use these to find the best model exhaustively from a collection of possible parameter values across multiple parameters simultaneously. Let's get to work, starting with GridSearchCV!

Instructions
100 XP
Create a parameter grid called gbm_param_grid that contains a list of "colsample_bytree" values (0.3, 0.7), a list with a single value for "n_estimators" (50), and a list of 2 "max_depth" (2, 5) values.
Instantiate an XGBRegressor object called gbm.
Create a GridSearchCV object called grid_mse, passing in: the parameter grid to param_grid, the XGBRegressor to estimator, "neg_mean_squared_error" to scoring, and 4 to cv. Also specify verbose=1 so you can better understand the output.
Fit the GridSearchCV object to X and y.
Print the best parameter values and lowest RMSE, using the .best_params_ and .best_score_ attributes, respectively, of grid_mse.
'''
SOLUTION
# Create the parameter grid: gbm_param_grid
gbm_param_grid = {
    'colsample_bytree': [0.3, 0.7],
    'n_estimators': [50],
    'max_depth': [2, 5]
}

# Instantiate the regressor: gbm
gbm = xgb.XGBRegressor()

# Perform grid search: grid_mse
grid_mse = GridSearchCV(param_grid=gbm_param_grid, estimator=gbm, scoring='neg_mean_squared_error', cv=4, verbose=1)


# Fit grid_mse to the data
grid_mse.fit(X, y)

# Print the best parameters and lowest RMSE
print("Best parameters found: ", grid_mse.best_params_)
print("Lowest RMSE found: ", np.sqrt(np.abs(grid_mse.best_score_)))