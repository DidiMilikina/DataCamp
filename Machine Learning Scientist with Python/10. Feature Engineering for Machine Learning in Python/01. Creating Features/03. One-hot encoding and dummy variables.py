'''
One-hot encoding and dummy variables
To use categorical variables in a machine learning model, you first need to represent them in a quantitative way. The two most common approaches are to one-hot encode the variables using or to use dummy variables. In this exercise, you will create both types of encoding, and compare the created column sets. We will continue using the same DataFrame from previous lesson loaded as so_survey_df and focusing on its Country column.

Instructions 1/2
50 XP
1
One-hot encode the Country column, adding "OH" as a prefix for each column.
2
Create dummy variables for the Country column, adding "DM" as a prefix for each column.
'''
SOLUTION

1
# Convert the Country column to a one hot encoded Data Frame
one_hot_encoded = pd.get_dummies(so_survey_df, columns=['Country'], prefix='OH')

# Print the columns names
print(one_hot_encoded.columns)

2
# Create dummy variables for the Country column
dummy = pd.get_dummies(so_survey_df, columns=['Country'], drop_first=True, prefix='DM')

# Print the columns names
print(dummy.columns)