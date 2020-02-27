'''
Inspect the model (I)
Now that you've fit your model, let's take a look at it. You can use the .get_weights() method to inspect your model's weights.

The input layer will have 4 weights: 2 for each input times 2 for each output.

The output layer will have 2 weights, one for each output.

Instructions
100 XP
Print the model's weights.
Print the column means of the training data (games_tourney_train).
'''
SOLUTION

# Print the model's weights
print(model.get_weights())

# Print the column means of the training data
print(games_tourney_train.mean())