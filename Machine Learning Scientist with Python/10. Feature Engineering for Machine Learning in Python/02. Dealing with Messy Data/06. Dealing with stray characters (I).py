'''
Dealing with stray characters (I)
In this exercise, you will work with the RawSalary column of so_survey_df which contains the wages of the respondents along with the currency symbols and commas, such as $42,000. When importing data from Microsoft Excel, more often that not you will come across data in this form.

Instructions 1/2
50 XP
1
Remove the commas (,) from the RawSalary column.

2
Remove the dollar ($) signs from the RawSalary column.
'''
SOLUTION 

1
# Remove the commas in the column
so_survey_df['RawSalary'] = so_survey_df['RawSalary'].str.replace(',', '')

2
# Remove the dollar signs in the column
so_survey_df['RawSalary'] = so_survey_df['RawSalary'].str.replace('$', '')