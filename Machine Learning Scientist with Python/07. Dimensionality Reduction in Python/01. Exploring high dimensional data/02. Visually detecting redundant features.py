'''
Visually detecting redundant features
Data visualization is a crucial step in any data exploration. Let's use Seaborn to explore some samples of the US Army ANSUR body measurement dataset.

Two data samples have been pre-loaded as ansur_df_1 and ansur_df_2.

Seaborn has been imported as sns.

Instructions 1/4
25 XP
1
Create a pairplot of the ansur_df_1 data sample and color the points using the 'Gender' feature.

2
Two features are basically duplicates, remove one of them from the dataset.

3
Now create a pairplot of the ansur_df_2 data sample and color the points using the 'Gender' feature.

4
One feature has no variance, remove it from the dataset.
'''
SOLUTION

1
# Create a pairplot and color the points using the 'Gender' feature
sns.pairplot(ansur_df_1, hue='Gender', diag_kind='hist')

# Show the plot
plt.show()

2
# Remove one of the redundant features
reduced_df = ansur_df_1.drop('body_height', axis=1)

# Create a pairplot and color the points using the 'Gender' feature
sns.pairplot(reduced_df, hue='Gender')

# Show the plot
plt.show()

3
# Create a pairplot and color the points using the 'Gender' feature
sns.pairplot(ansur_df_2, hue='Gender', diag_kind='hist')


# Show the plot
plt.show()

4
# Remove the redundant feature
reduced_df = ansur_df_2.drop('n_legs', axis=1)

# Create a pairplot and color the points using the 'Gender' feature
sns.pairplot(reduced_df, hue='Gender', diag_kind='hist')

# Show the plot
plt.show()