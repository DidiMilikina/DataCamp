'''
Am I underfitting?
You are creating a random forest model to predict if you will win a future game of Tic-Tac-Toe. Using the tic_tac_toe dataset, you have created training and testing datasets, X_train, X_test, y_train, and y_test.

You have decided to create a bunch of random forest models with varying amounts of trees (1, 2, 3, 4, 5, 10, 20, and 50). The more trees you use, the longer your random forest model will take to run. However, if you don't use enough trees, you risk underfitting. You have created a for loop to test your model at the different number of trees.

Instructions
100 XP
For each loop, predict values for both the X_train and X_test datasets.
For each loop, append the accuracy_score() of the y_train dataset and the corresponding predictions to train_scores.
For each loop, append the accuracy_score() of the y_test dataset and the corresponding predictions to test_scores.
Print the training and testing scores using the print statements.
'''
SOLUTION

from sklearn.metrics import accuracy_score

test_scores, train_scores = [], []
for i in [1, 2, 3, 4, 5, 10, 20, 50]:
    rfc = RandomForestClassifier(n_estimators=i, random_state=1111)
    rfc.fit(X_train, y_train)
    # Create predictions for the X_train and X_test datasets.
    train_predictions = rfc.predict(X_train)
    test_predictions = rfc.predict(X_test)
    # Append the accuracy score for the test and train predictions.
    train_scores.append(round(accuracy_score(y_train, train_predictions), 2))
    test_scores.append(round(accuracy_score(y_test, test_predictions), 2))
# Print the train and test scores.
print("The training scores were: {}".format(train_scores))
print("The testing scores were: {}".format(test_scores))