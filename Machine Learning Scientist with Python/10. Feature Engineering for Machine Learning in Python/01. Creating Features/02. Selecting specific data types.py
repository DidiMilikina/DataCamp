'''
Selecting specific data types
Often a data set will contain columns with several different data types (like the one you are working with). The majority of machine learning models require you to have a consistent data type across features. Similarly, most feature engineering techniques are applicable to only one type of data at a time. For these reasons among others, you will often want to be able to access just the columns of certain types when working with a DataFrame.

The DataFrame (so_survey_df) from the previous exercise is available in your workspace.

Instructions
100 XP
Create a subset of so_survey_df consisting of only the numeric (int and float) columns.
Print the column names contained in so_survey_df_num.
'''
SOLUTION
# Create subset of only the numeric columns
so_numeric_df = so_survey_df.select_dtypes(include=['int', 'float'])

# Print the column names contained in so_survey_df_num
print(so_numeric_df.columns)