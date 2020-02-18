'''
Create one holdout set
Your boss has asked you to create a simple random forest model on the tic_tac_toe dataset. She doesn't want you to spend much time selecting parameters; rather she wants to know how well the model will perform on future data. For future Tic-Tac-Toe games, it would be nice to know if your model can predict which player will win.

The dataset tic_tac_toe has been loaded for your use.

Note that in Python, =\ indicates the code was too long for one line and has been split across two lines.

Instructions
100 XP
Create the X dataset by creating dummy variables for all of the categorical columns.
Split X and y into train (X_train, y_train) and test (X_test, y_test) datasets.
Split the datasets using 10% for testing
'''
SOLUTION


# Create dummy variables using pandas
X = pd.get_dummies(tic_tac_toe.iloc[:,0:9])
y = tic_tac_toe.iloc[:, 9]

# Create training and testing datasets. Use 10% for the test set
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.1, random_state=1111)