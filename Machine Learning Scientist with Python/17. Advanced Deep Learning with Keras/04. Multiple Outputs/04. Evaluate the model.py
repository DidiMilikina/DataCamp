'''
Evaluate the model
Now that you've fit your model and inspected it's weights to make sure it makes sense, evaluate it on the tournament test set to see how well it performs on new data.

Instructions
100 XP
Evaluate the model on games_tourney_test.
Use the same inputs and outputs as the training set.
'''
SOLUTION

# Evaluate the model on the tournament test data
print(model.evaluate(games_tourney_test[['seed_diff', 'pred']], games_tourney_test[['score_1', 'score_2']], verbose=False))