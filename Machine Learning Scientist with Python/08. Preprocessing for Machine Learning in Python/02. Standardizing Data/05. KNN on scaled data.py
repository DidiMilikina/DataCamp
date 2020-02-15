'''
KNN on scaled data
The accuracy score on the unscaled wine dataset was decent, but we can likely do better if we scale the dataset. The process is mostly the same as the previous exercise, with the added step of scaling the data. Once again, the knn model as well as the X and y data and labels set have already been created for you.

Instructions
100 XP
Create the StandardScaler() method, stored in a variable named ss.
Apply the ss.fit_transform method to the X dataset.
Use the knn model's fit() method on the X_train data and y_train labels, to fit the model to the data.
Print out the knn model's score() on the X_test data and y_test labels to evaluate the model.
'''
SOLUTION
# Create the scaling method.
ss = StandardScaler()

# Apply the scaling method to the dataset used for modeling.
X_scaled = ss.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)

# Fit the k-nearest neighbors model to the training data.
knn.fit(X_train, y_train)

# Score the model on the test data.
print(knn.score(X_test, y_test))