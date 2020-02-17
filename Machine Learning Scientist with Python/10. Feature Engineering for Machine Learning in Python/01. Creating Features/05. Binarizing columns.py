'''
Binarizing columns
While numeric values can often be used without any feature engineering, there will be cases when some form of manipulation can be useful. For example on some occasions, you might not care about the magnitude of a value but only care about its direction, or if it exists at all. In these situations, you will want to binarize a column. In the so_survey_df data, you have a large number of survey respondents that are working voluntarily (without pay). You will create a new column titled Paid_Job indicating whether each person is paid (their salary is greater than zero).

Instructions
100 XP
Create a new column called Paid_Job filled with zeros.
Replace all the Paid_Job values with a 1 where the corresponding ConvertedSalary is greater than 0.
'''
SOLUTION
# Create the Paid_Job column filled with zeros
so_survey_df['Paid_Job'] = 0

# Replace all the Paid_Job values where ConvertedSalary is > 0
so_survey_df.loc[so_survey_df['ConvertedSalary'] > 0, 'Paid_Job'] = 1

# Print the first five rows of the columns
print(so_survey_df[['Paid_Job', 'ConvertedSalary']].head())