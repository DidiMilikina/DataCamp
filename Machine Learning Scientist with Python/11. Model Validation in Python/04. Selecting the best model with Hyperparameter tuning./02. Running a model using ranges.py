'''
Running a model using ranges
You have just finished creating a list of hyperparameters and ranges to use when tuning a predictive model for an assignment. You have used max_depth, min_samples_split, and max_features as your range variable names.

Instructions
100 XP
Randomly select a max_depth, min_samples_split, and max_features using your range variables.
Print out all of the parameters for rfr to see which values were randomly selected.
'''
SOLUTION

from sklearn.ensemble import RandomForestRegressor

# Fill in rfr using your variables
rfr = RandomForestRegressor(
    n_estimators=100,
    max_depth=random.choice(max_depth),
    min_samples_split=random.choice(min_samples_split),
    max_features=random.choice(max_features))

# Print out the parameters
print(rfr.get_params())