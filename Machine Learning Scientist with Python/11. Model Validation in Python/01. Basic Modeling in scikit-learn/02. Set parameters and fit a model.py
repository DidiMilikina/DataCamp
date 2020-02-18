'''
Set parameters and fit a model
Predictive tasks fall into one of two categories: regression or classification. In the candy dataset, the outcome is a continuous variable describing how often the candy was chosen over another candy in a series of 1-on-1 match-ups. To predict this value (the win-percentage), you will use a regression model.

In this exercise, you will specify a few parameters using a random forest regression model rfr.

Instructions
100 XP
Add a parameter to rfr so that the number of trees built is 100 and the maximum depth of these trees is 6.
Make sure the model is reproducible by adding a random state of 1111.
Use the .fit() method to train the random forest regression model with X_train as the input data and y_train as the response.
'''
SOLUTION

# Set the number of trees
rfr.n_estimators = 100

# Add a maximum depth
rfr.max_depth = 6

# Set the random state
rfr.random_state = 1111

# Fit the model
rfr.fit(X_train, y_train)