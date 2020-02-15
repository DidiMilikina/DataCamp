'''
Text classification using tf/idf vectors
Now that we've encoded the volunteer dataset's title column into tf/idf vectors, let's use those vectors to try to predict the category_desc column.

Instructions
100 XP
Using train_test_split, split the text_tfidf vector, along with your y variable, into training and test sets. Set the stratify parameter equal to y, since the class distribution is uneven. Notice that we have to run the toarray() method on the tf/idf vector, in order to get in it the proper format for scikit-learn.
Use Naive Bayes' fit() method on the X_train and y_train variables.
Print out the score() of the X_test and y_test variables.
'''
SOLUTION
# Split the dataset according to the class distribution of category_desc
y = volunteer["category_desc"]
X_train, X_test, y_train, y_test = train_test_split(text_tfidf.toarray(), y, stratify=y)

# Fit the model to the training data
nb.fit(X_train, y_train)

# Print out the model's accuracy
print(nb.score(X_test, y_test))