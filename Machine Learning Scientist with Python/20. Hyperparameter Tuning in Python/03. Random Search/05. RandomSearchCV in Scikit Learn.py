'''
RandomSearchCV in Scikit Learn
Let's practice building a RandomizedSearchCV object using Scikit Learn.

The hyperparameter grid should be for max_depth (all values between and including 5 and 25) and max_features ('auto' and 'sqrt').

The desired options for the RandomizedSearchCV object are:

A RandomForestClassifier Estimator with n_estimators of 80.
3-fold cross validation (cv)
Use roc_auc to score the models
Use 4 cores for processing in parallel (n_jobs)
Ensure you refit the best model and return training scores
Only sample 5 models for efficiency (n_iter)
X_train & y_train datasets are loaded for you.

Remember, to extract the chosen hyperparameters these are found in cv_results_ with a column per hyperparameter. For example, the column for the hyperparameter criterion would be param_criterion.

Instructions
100 XP
Create a hyperparameter grid as specified in the context above.
Create a RandomizedSearchCV object as outlined in the context above.
Fit the RandomizedSearchCV object to the training data.
Index into the cv_results_ object to print the values chosen by the modeling process for both hyperparameters (max_depth and max_features).
'''
SOLUTION

# Create the parameter grid
param_grid = {'max_depth': list(range(5,26)), 'max_features': ['auto' , 'sqrt']} 

# Create a random search object
random_rf_class = RandomizedSearchCV(
    estimator = RandomForestClassifier(n_estimators=80),
    param_distributions = param_grid, n_iter = 5,
    scoring='roc_auc', n_jobs=4, cv = 3, refit=True, return_train_score = True )

# Fit to the training data
random_rf_class.fit(X_train, y_train)

# Print the values used for both hyperparameters
print(random_rf_class.cv_results_['param_max_depth'])
print(random_rf_class.cv_results_['param_max_features']) 