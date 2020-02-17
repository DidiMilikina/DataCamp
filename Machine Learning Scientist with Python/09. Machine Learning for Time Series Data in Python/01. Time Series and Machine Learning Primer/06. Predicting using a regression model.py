'''
Predicting using a regression model
Now that you've fit a model with the Boston housing data, lets see what predictions it generates on some new data. You can investigate the underlying relationship that the model has found between inputs and outputs by feeding in a range of numbers as inputs and seeing what the model predicts for each input.

A 1-D array new_inputs consisting of 100 "new" values for "AGE" (proportion of owner-occupied units built prior to 1940) is available in your workspace along with the model you fit in the previous exercise.

Instructions
100 XP
Review new_inputs in the shell.
Reshape new_inputs appropriately to generate predictions.
Run the given code to visualize the predictions.
'''
SOLUTION
# Generate predictions with the model using those inputs
predictions = model.predict(new_inputs.reshape([-1, 1]))

# Visualize the inputs and predicted values
plt.scatter(new_inputs, predictions, color='r', s=3)
plt.xlabel('inputs')
plt.ylabel('predictions')
plt.show()