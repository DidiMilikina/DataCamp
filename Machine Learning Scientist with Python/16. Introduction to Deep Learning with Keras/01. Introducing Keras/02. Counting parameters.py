'''
Counting parameters
You've just created a neural network. Create a new one now and take some time to think about the weights of each layer. The Keras Dense layer and the Sequential model are already loaded for you to use.

This is the network you will be creating:


Instructions 1/2
50 XP
1
Instantiate a new Sequential() model.
Add a Dense() layer with five neurons and three neurons as input.
Add a final dense layer with one neuron and no activation.

2
Given the model you just built, which answer is correct regarding the number of weights (parameters) in the hidden layer?
'''
SOLUTION

1
# Instantiate a new Sequential model
model = Sequential()

# Add a Dense layer with five neurons and three inputs
model.add(Dense(5, input_shape=(3,), activation="relu"))

# Add a final Dense layer with one neuron and no activation
model.add(Dense(1))

# Summarize your model
model.summary()

2
