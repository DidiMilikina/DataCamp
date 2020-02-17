'''
Method chaining
When applying multiple operations on the same column (like in the previous exercises), you made the changes in several steps, assigning the results back in each step. However, when applying multiple successive operations on the same column, you can "chain" these operations together for clarity and ease of management. This can be achieved by calling multiple methods sequentially:

# Method chaining
df['column'] = df['column'].method1().method2().method3()

# Same as 
df['column'] = df['column'].method1()
df['column'] = df['column'].method2()
df['column'] = df['column'].method3()
In this exercise you will repeat the steps you performed in the last two exercises, but do so using method chaining.

Instructions
100 XP
Remove the commas (,) from the RawSalary column of so_survey_df.
Remove the dollar ($) signs from the RawSalary column.
Remove the pound (£) signs from the RawSalary column.
Convert the RawSalary column to float.
'''
SOLUTION

# Use method chaining
so_survey_df['RawSalary'] = so_survey_df['RawSalary']\
                              .str.replace(',', '')\
                              .str.replace('$', '')\
                              .str.replace('£', '')\
                              .astype('float')
 
# Print the RawSalary column
print(so_survey_df['RawSalary'])