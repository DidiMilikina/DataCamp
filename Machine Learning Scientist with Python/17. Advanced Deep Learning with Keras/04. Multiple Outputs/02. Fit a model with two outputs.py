'''
Fit a model with two outputs
Now that you've defined your 2-output model, fit it to the tournament data. I've split the data into games_tourney_train and games_tourney_test, so use the training set to fit for now.

This model will use the pre-tournament seeds, as well as your pre-tournament predictions from the regular season model you built previously in this course.

As a reminder, this model will predict the scores of both teams.

Instructions
100 XP
Fit the model to the games_tourney_train dataset using 100 epochs and a batch size of 16384.
The input columns are 'seed_diff', and 'pred'.
The target columns are 'score_1' and 'score_2'.
'''
SOLUTION

# Fit the model
model.fit(games_tourney_train[['seed_diff', 'pred']],
  		  games_tourney_train[['score_1', 'score_2']],
  		  verbose=True,
  		  epochs=100,
  		  batch_size=16384)