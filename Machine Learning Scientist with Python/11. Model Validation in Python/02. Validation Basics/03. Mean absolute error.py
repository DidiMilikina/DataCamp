'''
Mean absolute error
Communicating modeling results can be difficult. However, most clients understand that on average, a predictive model was off by some number. This makes explaining the mean absolute error easy. For example, when predicting the number of wins for a basketball team, if you predict 42, and they end up with 40, you can easily explain that the error was two wins.

In this exercise, you are interviewing for a new position and are provided with two arrays. y_test, the true number of wins for all 30 NBA teams in 2017 and predictions, which contains a prediction for each team. To test your understanding, you are asked to both manually calculate the MAE and use sklearn.

Instructions
100 XP
Manually calculate the MAE using n as the number of observations predicted.
Calculate the MAE using sklearn.
Print off both accuracy values using the print statements.
'''
SOLUTION

from sklearn.metrics import mean_absolute_error

# Manually calculate the MAE
n = len(predictions)
mae_one = sum(abs(y_test - predictions)) / n
print('With a manual calculation, the error is {}'.format(mae_one))

# Use scikit-learn to calculate the MAE
mae_two = mean_absolute_error(y_test, predictions)
print('Using scikit-lean, the error is {}'.format(mae_two))