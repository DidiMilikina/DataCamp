'''
Hello nets!
You're going to build a simple neural network to get a feeling for how quickly it is to accomplish in Keras.

You will build a network that takes two numbers as input, passes them through a hidden layer of 10 neurons, and finally outputs a single non-constrained number.

A non-constrained output can be obtained by avoiding setting an activation function in the output layer. This is useful for problems like regression, when we want our output to be able to take any value.


Instructions
100 XP
Instructions
100 XP
Import the Sequential model from keras.models and the Denselayer from keras.layers.
Create an instance of the Sequential model.
Add a 10-neuron hidden Dense layer with an input_shape of two neurons.
Add a final 1-neuron output layer and summarize your model with summary().
'''
SOLUTION

# Import the Sequential model and Dense layer
from keras.models import Sequential
from keras.layers import Dense

# Create a Sequential model
model = Sequential()

# Add an input layer and a hidden layer with 10 neurons
model.add(Dense(10, input_shape=(2,), activation="relu"))

# Add a 1-neuron output layer
model.add(Dense(1))

# Summarise your model
model.summary()