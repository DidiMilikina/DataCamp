'''
Evaluating a CNN with test data
To evaluate a trained neural network, you should provide a separate testing data set of labeled images. The model you fit in the previous exercise is available in your workspace.

Instructions
100 XP
Evaluate the data on a separate test set: test_data and test_labels.
Use the same batch size that was used for fitting (10 images per batch).
'''
SOLUTION

# Evaluate the model on separate test data
model.evaluate(test_data, test_labels, batch_size=10)
