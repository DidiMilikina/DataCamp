'''
Percentage based outlier removal
One way to ensure a small portion of data is not having an overly adverse effect is by removing a certain percentage of the largest and/or smallest values in the column. This can be achieved by finding the relevant quantile and trimming the data using it with a mask. This approach is particularly useful if you are concerned that the highest values in your dataset should be avoided. When using this approach, you must remember that even if there are no outliers, this will still remove the same top N percentage from the dataset.

Instructions
100 XP
Find the 95th quantile of the ConvertedSalary column.
Trim the so_numeric_df DataFrame to retain all rows where ConvertedSalary is less than it's 95th quantile.
Plot the histogram of so_numeric_df[['ConvertedSalary']].
Plot the histogram of trimmed_df[['ConvertedSalary']].
'''
SOLUTION
# Find the 95th quantile
quantile = so_numeric_df['ConvertedSalary'].quantile(0.95)

# Trim the outliers
trimmed_df = so_numeric_df[so_numeric_df['ConvertedSalary'] < quantile]

# The original histogram
so_numeric_df[['ConvertedSalary']].hist()
plt.show()
plt.clf()

# The trimmed histogram
trimmed_df[['ConvertedSalary']].hist()
plt.show()