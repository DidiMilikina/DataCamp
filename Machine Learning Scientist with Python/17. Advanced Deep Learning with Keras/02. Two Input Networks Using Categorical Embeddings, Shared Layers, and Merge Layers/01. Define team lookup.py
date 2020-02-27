'''
Define team lookup
Shared layers allow a model to use the same weight matrix for multiple steps. In this exercise, you will build a "team strength" layer that represents each team by a single number. You will use this number for both teams in the model. The model will learn a number for each team that works well both when the team is team_1 and when the team is team_2 in the input data.

The games_season DataFrame is available in your workspace.

Instructions
100 XP
Count the number of unique teams.
Create an embedding layer that maps each team ID to a single number representing that team's strength.
The output shape should be 1 dimension (as we want to represent the teams by a single number).
The input length should be 1 dimension (as each team is represented by exactly one id).
'''
SOLUTION

# Imports
from keras.layers import Embedding
from numpy import unique

# Count the unique number of teams
n_teams = unique(games_season['team_1']).shape[0]

# Create an embedding layer
team_lookup = Embedding(input_dim=n_teams,
                        output_dim=1,
                        input_length=1,
                        name='Team-Strength')