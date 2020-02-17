'''
Fitting a simple model: classification
In this exercise, you'll use the iris dataset (representing petal characteristics of a number of flowers) to practice using the scikit-learn API to fit a classification model. You can see a sample plot of the data to the right.

Note: This course assumes some familiarity with Machine Learning and scikit-learn. For an introduction to scikit-learn, we recommend the Supervised Learning with Scikit-Learn and Preprocessing for Machine Learning in Python courses.

Instructions 1/2
10 XP
1
Print the first five rows of data.

2
Extract the "petal length (cm)" and "petal width (cm)" columns of data and assign it to X.
Fit a model on X and y.
'''
SOLUTION

1
# Print the first 5 rows for inspection
print(data.head(5))

2
from sklearn.svm import LinearSVC

# Construct data for the model
X = data[['petal length (cm)', 'petal width (cm)']]
y = data[['target']]

# Fit the model
model = LinearSVC()
model.fit(X, y)