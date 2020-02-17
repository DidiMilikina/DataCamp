'''
Inspecting Tf-idf values
After creating Tf-idf features you will often want to understand what are the most highest scored words for each corpus. This can be achieved by isolating the row you want to examine and then sorting the the scores from high to low.

The DataFrame from the last exercise (tv_df) is available in your workspace.

Instructions
100 XP
Assign the first row of tv_df to sample_row.
sample_row is now a series of weights assigned to words. Sort these values to print the top 5 highest-rated words.
'''
SOLUTION 

# Isolate the row to be examined
sample_row = tv_df.iloc[0]

# Print the top 5 words of the sorted output
print(sample_row.sort_values(ascending=False).head())