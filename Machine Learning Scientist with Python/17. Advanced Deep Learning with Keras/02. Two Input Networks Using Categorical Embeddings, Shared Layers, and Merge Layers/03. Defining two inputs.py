'''
Defining two inputs
In this exercise, you will define two input layers for the two teams in your model. This allows you to specify later in the model how the data from each team will be used differently.

Instructions
100 XP
Create an input layer to use for team 1. Recall that our input dimension is 1.
Name the input "Team-1-In" so you can later distinguish it from team 2.
Create an input layer to use for team 2, named "Team-2-In".
'''
SOLUTION

# Load the input layer from keras.layers
from keras.layers import Input

# Input layer for team 1
team_in_1 = Input((1,), name='Team-1-In')

# Separate input layer for team 2
team_in_2 = Input((1,), name='Team-2-In')