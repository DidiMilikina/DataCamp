'''
Finding the missing values
While having a summary of how much of your data is missing can be useful, often you will need to find the exact locations of these missing values. Using the same subset of the StackOverflow data from the last exercise (sub_df), you will show how a value can be flagged as missing.

Instructions 1/3
35 XP
1
Print the first 10 entries of the DataFrame.

2
Print the locations of the missing values in the first 10 rows.

3
Print the locations of the non-missing values in the first 10 rows.
'''
SOLUTION

1
# Print the top 10 entries of the DataFrame
print(sub_df.head(10))

2
# Print the locations of the missing values
print(sub_df.head(10).isnull())

3
# Print the locations of the non-missing values
print(sub_df.head(10).notnull())