'''
Feature importances
Although some candy attributes, such as chocolate, may be extremely popular, it doesn't mean they will be important to model prediction. After a random forest model has been fit, you can review the model's attribute, .feature_importances_, to see which variables had the biggest impact. You can check how important each variable was in the model by looping over the feature importance array using enumerate().

If you are unfamiliar with Python's enumerate() function, it can loop over a list while also creating an automatic counter.

Instructions
100 XP
Loop through the feature importance output of rfr.
Print the column names of X_train and the importance score for that column.
'''
SOLUTION

# Fit the model using X and y
rfr.fit(X_train, y_train)

# Print how important each column is to the model
for i, item in enumerate(rfr.feature_importances_):
      # Use i and item to print out the feature importance of each column
    print("{0:s}: {1:.2f}".format(X_train.columns[i], item))