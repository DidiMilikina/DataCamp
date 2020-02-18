'''
Precision vs. recall
The accuracy metrics you use to evaluate your model should always be based on the specific application. For this example, let's assume you are a really sore loser when it comes to playing Tic-Tac-Toe, but only when you are certain that you are going to win.

Choose the most appropriate accuracy metric, either precision or recall, to complete this example. But remember, if you think you are going to win, you better win!

Use rfc, which is a random forest classification model built on the tic_tac_toe dataset.

Instructions
100 XP
Import the precision or the recall metric for sklearn. Only one method is correct for the given context.
Calculate the precision or recall using y_test for the true values and test_predictions for the predictions.
Print the final score based on your selected metric.
'''
SOLUTION
from sklearn.metrics import precision_score

test_predictions = rfc.predict(X_test)

# Create precision or recall score based on the metric you imported
score = precision_score(y_test, test_predictions)

# Print the final result
print("The precision value is {0:.2f}".format(score))