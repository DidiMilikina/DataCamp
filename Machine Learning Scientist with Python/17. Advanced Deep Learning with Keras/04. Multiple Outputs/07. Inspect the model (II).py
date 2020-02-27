'''
Inspect the model (II)
Now you should take a look at the weights for this model. In particular, note the last weight of the model. This weight converts the predicted score difference to a predicted win probability. If you multiply the predicted score difference by the last weight of the model and then apply the sigmoid function, you get the win probability of the game.

Instructions 1/2
50 XP
1
Print the model's weights.
Print the column means of the training data (games_tourney_train).

2
Print the approximate win probability predicted for a close game (1 point difference).
Print the approximate win probability predicted blowout game (10 point difference).
'''
SOLUTION

1
# Print the model weights
print(model.get_weights())

# Print the training data means
print(games_tourney_train.mean())

2
# Import the sigmoid function from scipy
from scipy.special import expit as sigmoid

# Weight from the model
weight = 0.14

# Print the approximate win probability predicted close game
print(sigmoid(1 * weight))

# Print the approximate win probability predicted blowout game
print(sigmoid(10 * weight))