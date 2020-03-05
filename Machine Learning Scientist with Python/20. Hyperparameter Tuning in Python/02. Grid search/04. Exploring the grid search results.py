'''
Exploring the grid search results
You will now explore the cv_results_ property of the GridSearchCV object defined in the video. This is a dictionary that we can read into a pandas DataFrame and contains a lot of useful information about the grid search we just undertook.

A reminder of the different column types in this property:

time_ columns
param_ columns (one for each hyperparameter) and the singular params column (with all hyperparameter settings)
a train_score column for each cv fold including the mean_train_score and std_train_score columns
a test_score column for each cv fold including the mean_test_score and std_test_score columns
a rank_test_score column with a number from 1 to n (number of iterations) ranking the rows based on their mean_test_score
Instructions
100 XP
Read the cv_results_ property of the grid_rf_class GridSearchCV object into a data frame & print the whole thing out to inspect.
Extract & print the singular column containing a dictionary of all hyperparameters used in each iteration of the grid search.
Extract & print the row that had the best mean test score by indexing using the rank_test_score column.
'''
SOLUTION

# Read the cv_results property into a dataframe & print it out
cv_results_df = pd.DataFrame(grid_rf_class.cv_results_)
print(cv_results_df)

# Extract and print the column with a dictionary of hyperparameters used
column = cv_results_df.loc[:, ['params']]
print(column)

# Extract and print the row that had the best mean test score
best_row = cv_results_df[cv_results_df['rank_test_score'] == 1 ]
print(best_row)