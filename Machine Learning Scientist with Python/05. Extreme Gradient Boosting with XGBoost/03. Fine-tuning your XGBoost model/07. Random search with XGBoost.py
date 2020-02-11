'''
Random search with XGBoost
Often, GridSearchCV can be really time consuming, so in practice, you may want to use RandomizedSearchCV instead, as you will do in this exercise. The good news is you only have to make a few modifications to your GridSearchCV code to do RandomizedSearchCV. The key difference is you have to specify a param_distributions parameter instead of a param_grid parameter.

Instructions
100 XP
Create a parameter grid called gbm_param_grid that contains a list with a single value for 'n_estimators' (25), and a list of 'max_depth' values between 2 and 11 for 'max_depth' - use range(2, 12) for this.
Create a RandomizedSearchCV object called randomized_mse, passing in: the parameter grid to param_distributions, the XGBRegressor to estimator, "neg_mean_squared_error" to scoring, 5 to n_iter, and 4 to cv. Also specify verbose=1 so you can better understand the output.
Fit the RandomizedSearchCV object to X and y.
'''
SOLUTION
# Create the parameter grid: gbm_param_grid 
gbm_param_grid = {
    'n_estimators': [25],
    'max_depth': range(2, 12)
}

# Instantiate the regressor: gbm
gbm = xgb.XGBRegressor(n_estimators=10)

# Perform random search: grid_mse
randomized_mse = RandomizedSearchCV(param_distributions=gbm_param_grid, estimator=gbm, scoring='neg_mean_squared_error', n_iter=5, cv=4, verbose=1)


# Fit randomized_mse to the data
randomized_mse.fit(X, y)

# Print the best parameters and lowest RMSE
print("Best parameters found: ", randomized_mse.best_params_)
print("Lowest RMSE found: ", np.sqrt(np.abs(randomized_mse.best_score_)))