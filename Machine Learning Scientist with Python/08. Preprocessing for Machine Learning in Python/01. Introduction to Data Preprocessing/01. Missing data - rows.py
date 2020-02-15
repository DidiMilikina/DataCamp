'''
Missing data - rows
Taking a look at the volunteer dataset again, we want to drop rows where the category_desc column values are missing. We're going to do this using boolean indexing, by checking to see if we have any null values, and then filtering the dataset so that we only have rows with those values.

Instructions
100 XP
Check how many values are missing in the category_desc column using isnull() and sum().
Subset the volunteer dataset by indexing by where category_desc is notnull(), and store in a new variable called volunteer_subset.
Take a look at the .shape attribute of the new dataset, to verify it worked correctly.
'''
SOLUTION
# Check how many values are missing in the category_desc column
print(volunteer['category_desc'].isnull().sum())

# Subset the volunteer dataset
volunteer_subset = volunteer[volunteer['category_desc'].notnull()]

# Print out the shape of the subset
print(volunteer_subset.shape)