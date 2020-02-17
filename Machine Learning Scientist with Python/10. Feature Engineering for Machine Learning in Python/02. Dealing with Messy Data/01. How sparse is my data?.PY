'''
How sparse is my data?
Most data sets contain missing values, often represented as NaN (Not a Number). If you are working with Pandas you can easily check how many missing values exist in each column.

Let's find out how many of the developers taking the survey chose to enter their age (found in the Age column of so_survey_df) and their gender (Gender column of so_survey_df).

Instructions 1/2
50 XP
1
Subset the DataFrame to only include the 'Age' and 'Gender' columns.
Print the number of non-missing values in both columns.
'''
SOLUTION

1
# Subset the DataFrame
sub_df = so_survey_df[['Age', 'Gender']]

# Print the number of non-missing values
print(sub_df.notnull().sum())