'''
Loss functions in TensorFlow
In this exercise, you will compute the loss using data from the King County housing dataset. You are given a target, price, which is a tensor of house prices, and predictions, which is a tensor of predicted house prices. You will evaluate the loss function and print out the value of the loss.

Instructions 1/2
50 XP
1
Import the keras module from tensorflow. Then, use price and predictions to compute the mean squared error (mse).

2
Modify your code to compute the mean absolute error (mae), rather than the mean squared error (mse).
'''
SOLUTION

1
# Import the keras module from tensorflow
import tensorflow.keras

# Compute the mean squared error (mse)
loss = tensorflow.keras.losses.mse(price, predictions)

# Print the mean squared error (mse)
print(loss.numpy())

2
# Import the keras module from tensorflow
from tensorflow import keras

# Compute the mean absolute error (mae)
loss = keras.losses.mae(price, predictions)

# Print the mean absolute error (mae)
print(loss.numpy())