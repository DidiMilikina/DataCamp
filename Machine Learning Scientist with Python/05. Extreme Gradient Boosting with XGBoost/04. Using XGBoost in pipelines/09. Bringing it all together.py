'''
Bringing it all together
Alright, it's time to bring together everything you've learned so far! In this final exercise of the course, you will combine your work from the previous exercises into one end-to-end XGBoost pipeline to really cement your understanding of preprocessing and pipelines in XGBoost.

Your work from the previous 3 exercises, where you preprocessed the data and set up your pipeline, has been pre-loaded. Your job is to perform a randomized search and identify the best hyperparameters.

Instructions
100 XP
Set up the parameter grid to tune 'clf__learning_rate' (from 0.05 to 1 in increments of 0.05), 'clf__max_depth' (from 3 to 10 in increments of 1), and 'clf__n_estimators' (from 50 to 200 in increments of 50).
Using your pipeline as the estimator, perform 2-fold RandomizedSearchCV with an n_iter of 2. Use "roc_auc" as the metric, and set verbose to 1 so the output is more detailed. Store the result in randomized_roc_auc.
Fit randomized_roc_auc to X and y.
Compute the best score and best estimator of randomized_roc_auc.
'''
SOLUTION
# Create the parameter grid
gbm_param_grid = {
    'clf__learning_rate': np.arange(0.05, 1, 0.05),
    'clf__max_depth': np.arange(3, 10, 1),
    'clf__n_estimators': np.arange(50, 200, 50)
}

# Perform RandomizedSearchCV
randomized_roc_auc = RandomizedSearchCV(estimator=pipeline, param_distributions=gbm_param_grid, cv=2 ,n_iter=2, scoring='roc_auc', verbose=1)

# Fit the estimator
randomized_roc_auc.fit(X, y)

# Compute metrics
print(randomized_roc_auc.best_score_)
print(randomized_roc_auc.best_estimator_)