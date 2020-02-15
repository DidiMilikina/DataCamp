'''
Removing features without variance
A sample of the Pokemon dataset has been loaded as pokemon_df. To get an idea of which features have little variance you should use the IPython Shell to calculate summary statistics on this sample. Then adjust the code to create a smaller, easier to understand, dataset.

Instructions 1/3
50 XP
1
Use the .describe() method to find the numeric feature without variance and remove its name from the list assigned to number_cols.

2
Combine the two lists of feature names to sub-select the chosen features from pokemon_df.

3
Find the non-numeric feature without variance and remove its name from the list assigned to non_number_cols.
'''
SOLUTION
1
# Remove the feature without variance from this list
number_cols = ['HP', 'Attack', 'Defense']

2
# Remove the feature without variance from this list
number_cols = ['HP', 'Attack', 'Defense']

# Leave this list as is for now
non_number_cols = ['Name', 'Type', 'Legendary']

# Sub-select by combining the lists with chosen features
df_selected = pokemon_df[number_cols + non_number_cols]

# Prints the first 5 lines of the new dataframe
print(df_selected.head())

3
# Leave this list as is
number_cols = ['HP', 'Attack', 'Defense']

# Remove the feature without variance from this list
non_number_cols = ['Name', 'Type']

# Create a new dataframe by subselecting the chosen features
df_selected = pokemon_df[number_cols + non_number_cols]

# Prints the first 5 lines of the new dataframe
print(df_selected.head())
