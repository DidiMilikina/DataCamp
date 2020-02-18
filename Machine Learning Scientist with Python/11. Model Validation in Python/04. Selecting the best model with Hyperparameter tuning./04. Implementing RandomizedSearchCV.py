'''
Implementing RandomizedSearchCV
You are hoping that using a random search algorithm will help you improve predictions for a class assignment. You professor has challenged your class to predict the overall final exam average score.

In preparation for completing a random search, you have created:

param_dist: the hyperparameter distributions
rfr: a random forest regression model
scorer: a scoring method to use
Instructions
100 XP
Load the method for conducting a random search in sklearn.
Complete a random search by filling in the parameters: estimator, param_distributions, and scoring.
Use 5-fold cross validation for this random search.
'''
SOLUTION

# Import the method for random search
from sklearn.model_selection import RandomizedSearchCV

# Build a random search using param_dist, rfr, and scorer
random_search =\
    RandomizedSearchCV(
        estimator=rfr,
        param_distributions=param_dist,
        n_iter=10,
        cv=5,
        scoring=scorer)