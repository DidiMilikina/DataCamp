'''
Finding the most common words
Its always advisable once you have created your features to inspect them to ensure that they are as you would expect. This will allow you to catch errors early, and perhaps influence what further feature engineering you will need to do.

The vectorizer (cv) you fit in the last exercise and the sparse array consisting of word counts (cv_trigram) is available in your workspace.

Instructions
100 XP
Create a DataFrame of the features (word counts).
Add the counts of word occurrences and print the top 5 most occurring words.
'''
SOLUTION

# Create a DataFrame of the features
cv_tri_df = pd.DataFrame(cv_trigram.toarray(), 
                 columns=cv_trigram_vec.get_feature_names()).add_prefix('Counts_')

# Print the top 5 words in the sorted output
print(cv_tri_df.sum().sort_values(ascending=False).head())