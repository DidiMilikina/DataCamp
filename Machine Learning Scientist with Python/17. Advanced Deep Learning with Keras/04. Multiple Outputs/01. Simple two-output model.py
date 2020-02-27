'''
Simple two-output model
In this exercise, you will use the tournament data to build one model that makes two predictions: the scores of both teams in a given game. Your inputs will be the seed difference of the two teams, as well as the predicted score difference from the model you built in chapter 3.

The output from your model will be the predicted score for team 1 as well as team 2. This is called "multiple target regression": one model making more than one prediction.

Instructions
100 XP
Create a single input layer with 2 columns.
Connect this input to a Dense layer with 2 units.
Create a model with input_tensor as the input and output_tensor as the output.
Compile the model with 'adam' as the optimizer and 'mean_absolute_error' as the loss function.
'''
SOLUTION

# Define the input
input_tensor = Input((2,))

# Define the output
output_tensor = Dense(2)(input_tensor)

# Create a model
model = Model(input_tensor, output_tensor)

# Compile the model
model.compile(optimizer='adam', loss='mean_absolute_error')