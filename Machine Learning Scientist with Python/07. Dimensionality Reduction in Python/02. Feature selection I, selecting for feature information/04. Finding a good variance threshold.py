'''
Finding a good variance threshold
You'll be working on a slightly modified subsample of the ANSUR dataset with just head measurements pre-loaded as head_df.

Instructions 1/4
35 XP
1
Create a boxplot on head_df.

2
Normalize the data by dividing the dataframe with its mean values.

3
Print the variances of the normalized data.

4
Inspect the printed variances. If you want to remove the 2 very low variance features. What would be a good variance threshold?
'''
SOLUTION

1
# Create the boxplot
head_df.boxplot()

plt.show()

2
# Normalize the data
normalized_df = head_df / np.mean(head_df)

normalized_df.boxplot()
plt.show()

3
# Normalize the data
normalized_df = head_df / head_df.mean()

# Print the variances of the normalized data
print(normalized_df.var())

4
A threshold of 1.0e-03 (0.001) will remove the two low variance features.