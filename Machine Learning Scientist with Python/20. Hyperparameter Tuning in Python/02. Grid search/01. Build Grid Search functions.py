'''
Build Grid Search functions
In data science it is a great idea to try building algorithms, models and processes 'from scratch' so you can really understand what is happening at a deeper level. Of course there are great packages and libraries for this work (and we will get to that very soon!) but building from scratch will give you a great edge in your data science work.

In this exercise, you will create a function to take in 2 hyperparameters, build models and return results. You will use this function in a future exercise.

You will have available the X_train, X_test, y_train and y_test datasets available.

Instructions
100 XP
Build a function that takes two parameters called learn_rate and max_depth for the learning rate and maximum depth.
Add capability in the function to build a GBM model and fit it to the data with the input hyperparameters.
Have the function return the results of that model and the chosen hyperparameters (learn_rate and max_depth).
'''
SOLUTION

# Create the function
def gbm_grid_search(learn_rate, max_depth):

	# Create the model
    model = GradientBoostingClassifier(learning_rate=learn_rate, max_depth=max_depth)
    
    # Use the model to make predictions
    predictions = model.fit(X_train, y_train).predict(X_test)
    
    # Return the hyperparameters and score
    return([learn_rate, max_depth, accuracy_score(y_test, predictions)])