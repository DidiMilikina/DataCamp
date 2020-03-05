'''
Using the best results
While it is interesting to analyze the results of our grid search, our final goal is practical in nature; we want to make predictions on our test set using our estimator object.

We can access this object through the best_estimator_ property of our grid search object.

In this exercise we will take a look inside the best_estimator_ property and then use this to make predictions on our test set for credit card defaults and generate a variety of scores. Remember to use predict_proba rather than predict since we need probability values rather than class labels for our roc_auc score. We use a slice [:,1] to get probabilities of the positive class.

You have available the X_test and y_test datasets to use and the grid_rf_class object from previous exercises.

Instructions
100 XP
Check the type of the best_estimator_ property.
Use the best_estimator_ property to make predictions on our test set.
Generate a confusion matrix and ROC_AUC score from our predictions.
'''
SOLUTION

# See what type of object the best_estimator_ property is
print(type(grid_rf_class.best_estimator_))

# Create an array of predictions directly using the best_estimator_ property
predictions = grid_rf_class.best_estimator_.predict(X_test)

# Take a look to confirm it worked, this should be an array of 1's and 0's
print(predictions[0:5])

# Now create a confusion matrix 
print("Confusion Matrix \n", confusion_matrix(y_test, predictions))

# Get the ROC-AUC score
predictions_proba = grid_rf_class.best_estimator_.predict_proba(X_test)[:,1]
print("ROC-AUC Score \n", roc_auc_score(y_test, predictions_proba))