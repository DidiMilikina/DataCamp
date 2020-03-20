'''
Settle a debate with .apply()
Word has gotten to the Arizona Diamondbacks about your awesome analytics skills. They'd like for you to help settle a debate amongst the managers. One manager claims that the team has made the playoffs every year they have had a win percentage of 0.50 or greater. Another manager says this is not true.

Let's use the below function and the .apply() method to see which manager is correct.

def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc,2)
A DataFrame named dbacks_df has been loaded into your session.

Instructions 1/4
25 XP
1
Print the first five rows of the dbacks_df DataFrame to see what the data looks like.

2
Create a pandas Series called win_percs by applying the calc_win_perc() function to each row of the DataFrame with a lambda function.

3
Create a new column in dbacks_df called WP that contains the win percentages you calculated in the above step.

4
'''
SOLUTION

1
# Display the first five rows of the DataFrame
print(dbacks_df.head(5))

2
# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

3
# Display the first five rows of the DataFrame
print(dbacks_df.head())

# Create a win percentage Series 
win_percs = dbacks_df.apply(lambda row: calc_win_perc(row['W'], row['G']), axis=1)
print(win_percs, '\n')

# Append a new column to dbacks_df
dbacks_df['WP'] = win_percs
print(dbacks_df, '\n')

# Display dbacks_df where WP is greater than 0.50
print(dbacks_df[dbacks_df['WP'] >= 0.50])