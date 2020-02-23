'''
Defining Estimators
In the previous exercise, you defined a list of feature columns, feature_list, and a data input function, input_fn(). In this exercise, you will build on that work by defining an estimator that makes use of input data.

Instructions 1/2
100 XP
1
Use a deep neural network regressor with 2 nodes in both the first and second hidden layers and 1 training step.

2
Modify the code to use a LinearRegressor(), remove the hidden_units, and set the number of steps to 2.
'''
SOLUTION

1
# Define the model and set the number of steps
model = estimator.DNNRegressor(feature_columns=feature_list, hidden_units=[2, 2])
model.train(input_fn, steps=1)

2
# Define the model and set the number of steps
model = estimator.LinearRegressor(feature_columns=feature_list)
model.train(input_fn, steps=2)