'''
Evaluate the model
Now that you've fit your model to the tournament training data, evaluate it on the tournament test data. Recall that the tournament test data contains games from after 2010.

Instructions
100 XP
Evaluate the model on the games_tourney_test data.
Recall that the model's inputs are 'home', 'seed_diff', and 'prediction' columns and the target column is 'score_diff'.
'''
SOLUTION

# Evaluate the model on the games_tourney_test dataset
print(model.evaluate(games_tourney_test[['home', 'seed_diff', 'prediction']],
               games_tourney_test['score_diff'], verbose=False))