'''
Classification predictions
In model validation, it is often important to know more about the predictions than just the final classification. When predicting who will win a game, most people are also interested in how likely it is a team will win.

Probability	Prediction	Meaning
0 < .50	0	Team Loses
.50 +	1	Team Wins
In this exercise, you look at the methods, .predict() and .predict_proba() using the tic_tac_toe dataset. The first method will give a prediction of whether Player One will win the game, and the second method will provide the probability of Player One winning. Use rfc as the random forest classification model.

Instructions
100 XP
Create two arrays of predictions. One for the classification values and one for the predicted probabilities.
Use the .value_counts() method for a pandas Series to print the number of observations that were assigned to each class.
Print the first observation of probability_predictions to see how the probabilities are structured.
'''
SOLUTION

# Fit the rfc model. 
rfc.fit(X_train, y_train)

# Create arrays of predictions
classification_predictions = rfc.predict(X_test)
probability_predictions = rfc.predict_proba(X_test)

# Print out count of binary predictions
print(pd.Series(classification_predictions, probability_predictions).value_counts())

# Print the first value from probability_predictions
print('The first predicted probabilities are: {}'.format(probability_predictions[0]))