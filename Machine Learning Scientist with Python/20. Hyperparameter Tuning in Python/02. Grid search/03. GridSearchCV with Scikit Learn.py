'''
GridSearchCV with Scikit Learn
The GridSearchCV module from Scikit Learn provides many useful features to assist with efficiently undertaking a grid search. You will now put your learning into practice by creating a GridSearchCV object with certain parameters.

The desired options are:

A Random Forest Estimator, with the split criterion as 'entropy'
5-fold cross validation
The hyperparameters max_depth (2, 4, 8, 15) and max_features ('auto' vs 'sqrt')
Use roc_auc to score the models
Use 4 cores for processing in parallel
Ensure you refit the best model and return training scores
You will have available X_train, X_test, y_train & y_test datasets.

Instructions
100 XP
Create a Random Forest estimator as specified in the context above.
Create a parameter grid as specified in the context above.
Create a GridSearchCV object as outlined in the context above, using the two elements created in the previous two instructions.
'''
SOLUTION

# Create a Random Forest Classifier with specified criterion
rf_class = RandomForestClassifier(criterion='entropy')

# Create the parameter grid
param_grid = {'max_depth': [2, 4, 8, 15], 'max_features': ['auto', 'sqrt']} 

# Create a GridSearchCV object
grid_rf_class = GridSearchCV(
    estimator=rf_class,
    param_grid=param_grid,
    scoring='roc_auc',
    n_jobs=4,
    cv=5,
    refit=True, return_train_score=True)
print(grid_rf_class)