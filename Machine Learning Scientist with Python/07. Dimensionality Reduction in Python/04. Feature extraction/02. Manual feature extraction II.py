'''
Manual feature extraction II
You're working on a variant of the ANSUR dataset, height_df, where a person's height was measured 3 times. Add a feature with the mean height to the dataset, then drop the 3 original features.

Instructions
100 XP
Add a feature with the mean height to the dataset. Use the .mean() method with axis=1.
Drop the 3 original height features from the dataset.
'''
SOLUTION
# Calculate the mean height
height_df['height'] = height_df[['height_1', 'height_2', 'height_3']].mean(axis=1)

# Drop the 3 original height features
reduced_df = height_df.drop(['height_1', 'height_2', 'height_3'], axis=1)

print(reduced_df.head())