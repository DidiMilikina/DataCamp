'''
Checking for correlated features
Let's take a look at the wine dataset again, which is made up of continuous, numerical features. Run Pearson's correlation coefficient on the dataset to determine which columns are good candidates for eliminating. Then, remove those columns from the DataFrame.

Instructions
100 XP
Print out the column correlations of the wine dataset using corr().
Take a minute to look at the correlations. Identify a column where the correlation value is greater than 0.75 at least twice and store it in the to_drop variable.
Drop that column from the DataFrame using drop().
'''
SOLUTION
# Print out the column correlations of the wine dataset
print(wine.corr())

# Take a minute to find the column where the correlation value is greater than 0.75 at least twice
to_drop = "Flavanoids"

# Drop that column from the DataFrame
wine = wine.drop(to_drop, axis=1)