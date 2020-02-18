'''
Create two holdout sets
You recently created a simple random forest model to predict Tic-Tac-Toe game wins for your boss, and at her request, you did not do any parameter tuning. Unfortunately, the overall model accuracy was too low for her standards. This time around, she has asked you to focus on model performance.

Before you start testing different models and parameter sets, you will need to split the data into training, validation, and testing datasets. Remember that after splitting the data into training and testing datasets, the validation dataset is created by splitting the training dataset.

The datasets X and y have been loaded for your use.

Instructions
100 XP
Create temporary datasets and testing datasets (X_test, y_test). Use 20% of the overall data for the testing datasets.
Using the temporary datasets (X_temp, y_temp), create training (X_train, y_train) and validation (X_val, y_val) datasets.
Use 25% of the temporary data for the validation datasets.
'''
SOLUTION

# Create temporary training and final testing datasets
X_temp, X_test, y_temp, y_test  =\
    train_test_split(X, y, test_size=0.2, random_state=1111)

# Create the final training and validation datasets
X_train, X_val, y_train, y_val =\
    train_test_split(X_temp, y_temp, test_size=0.25, random_state=1111)