'''
scikit-learn's methods
You have decided to build a regression model to predict the number of new employees your company will successfully hire next month. You open up a new Python script to get started, but you quickly realize that sklearn has a lot of different modules. Let's make sure you understand the names of the modules, the methods, and which module contains which method.

Follow the instructions below to load in all of the necessary methods for completing cross-validation using sklearn. You will use modules:

metrics
model_selection
ensemble
Instructions
100 XP
Load the method for calculating the scores of cross-validation.
Load the random forest regression method.
Load the mean square error metric.
Load the method for creating a scorer to use with cross-validation.
'''
SOLUTION

# Instruction 1: Load the cross-validation method
from sklearn.model_selection import cross_val_score

# Instruction 2: Load the random forest regression model
from sklearn.ensemble import RandomForestRegressor

# Instruction 3: Load the mean squared error method
# Instruction 4: Load the function for creating a scorer
from sklearn.metrics import mean_squared_error, make_scorer