'''
Fit the model and evaluate
Now that you've defined a new model, fit it to the regular season basketball data.

Use the model you fit in the previous exercise (which was trained on the regular season data) and evaluate the model on data for tournament games (games_tourney).

Instructions
100 XP
Fit the model to the games_season dataset, using 'team_1', 'team_2' and 'home' columns as inputs, and the 'score_diff' column as the target.
Fit the model using 1 epoch, 10% validation split and a batch size of 2048.
Evaluate the model on games_tourney, using the same inputs and outputs.
'''
SOLUTION

# Fit the model to the games_season dataset
model.fit([games_season['team_1'], games_season['team_2'], games_season['home']],
          games_season['score_diff'],
          epochs=1,
          verbose=1,
          validation_split=0.1,
          batch_size=2048)

# Evaluate the model on the games_tourney dataset
print(model.evaluate([games_tourney['team_1'], games_tourney['team_2'], games_tourney['home']], games_tourney['score_diff'] , verbose=False))