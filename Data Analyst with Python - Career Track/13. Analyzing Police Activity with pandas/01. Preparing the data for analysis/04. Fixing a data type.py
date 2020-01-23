'''
Fixing a data type
We saw in the previous exercise that the is_arrested column currently has the object data type. In this exercise, we'll change the data type to bool, which is the most suitable type for a column containing True and False values.

Fixing the data type will enable us to use mathematical operations on the is_arrested column that would not be possible otherwise.

Instructions
100 XP
Examine the head of the is_arrested column to verify that it contains True and False values and to check the column's data type.
Use the .astype() method to convert is_arrested to a bool column.
Check the new data type of is_arrested to confirm that it is now a bool column.
'''
SOLUTION
# Examine the head of the 'is_arrested' column
print(ri.is_arrested.head())

# Change the data type of 'is_arrested' to 'bool'
ri['is_arrested'] = ri.is_arrested.astype(bool)

# Check the data type of 'is_arrested' 
print(ri['is_arrested'])