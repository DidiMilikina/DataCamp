'''
Analyzing the best results
At the end of the day, we primarily care about the best performing 'square' in a grid search. Luckily Scikit Learn's gridSearchCv objects have a number of parameters that provide key information on just the best square (or row in cv_results_).

Three properties you will explore are:

best_score_ – The score (here ROC_AUC) from the best-performing square.
best_index_ – The index of the row in cv_results_ containing information on the best-performing square.
best_params_ – A dictionary of the parameters that gave the best score, for example 'max_depth': 10
The grid search object grid_rf_class is available.

A dataframe (cv_results_df) has been created from the cv_results_ for you on line 6. This will help you index into the results.

Instructions
100 XP
Extract and print out the ROC_AUC score from the best performing square in grid_rf_class.
Create a variable from the best-performing row by indexing into cv_results_df.
Create a variable, best_n_estimators by extracting the n_estimators parameter from the best-performing square in grid_rf_class and print it out.
'''
SOLUTION

# Print out the ROC_AUC score from the best-performing square
best_score = grid_rf_class.best_score_
print(best_score)

# Create a variable from the row related to the best-performing square
cv_results_df = pd.DataFrame(grid_rf_class.cv_results_)
best_row = cv_results_df.loc[[grid_rf_class.best_index_]]
print(best_row)

# Get the n_estimators parameter from the best-performing square and print
best_n_estimators = grid_rf_class.best_params_["n_estimators"]
print(best_n_estimators)