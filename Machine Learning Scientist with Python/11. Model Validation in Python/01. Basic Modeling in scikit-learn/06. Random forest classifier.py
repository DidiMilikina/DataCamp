'''
Random forest classifier
This exercise reviews the four modeling steps discussed throughout this chapter using a random forest classification model. You will:

Create a random forest classification model.
Fit the model using the tic_tac_toe dataset.
Make predictions on whether Player One will win (1) or lose (0) the current game.
Finally, you will evaluate the overall accuracy of the model.
Let's get started!

Instructions 1/4
100 XP
1
Create rfc using the scikit-learn implementation of random forest classifiers and set a random state of 1111.

2
Fit rfc using X_train for the training data and y_train for the responses.

3
Predict the class values for X_test.

4
Use the method .score() to print an accuracy metric for X_test given the actual values y_test.
'''
SOLUTION

1
from sklearn.ensemble import RandomForestClassifier

# Create a random forest classifier
rfc = RandomForestClassifier(n_estimators=50, max_depth=6, random_state=1111)

2
from sklearn.ensemble import RandomForestClassifier

# Create a random forest classifier
rfc = RandomForestClassifier(n_estimators=50, max_depth=6, random_state=1111)

# Fit rfc using X_train and y_train
rfc.fit(X_train, y_train)

3
from sklearn.ensemble import RandomForestClassifier

# Create a random forest classifier
rfc = RandomForestClassifier(n_estimators=50, max_depth=6, random_state=1111)

# Fit rfc using X_train and y_train
rfc.fit(X_train, y_train)

# Create predictions on X_test
predictions = rfc.predict(X_test)
print(predictions[0:5])

4
from sklearn.ensemble import RandomForestClassifier

# Create a random forest classifier
rfc = RandomForestClassifier(n_estimators=50, max_depth=6, random_state=1111)

# Fit rfc using X_train and y_train
rfc.fit(X_train, y_train)

# Create predictions on X_test
predictions = rfc.predict(X_test)
print(predictions[0:5])

# Print model accuracy using score() and the testing data
print(rfc.score(X_test, y_test))