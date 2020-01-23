'''
Counting protective frisks
During a vehicle search, the police officer may pat down the driver to check if they have a weapon. This is known as a "protective frisk."

In this exercise, you'll first check to see how many times "Protective Frisk" was the only search type. Then, you'll use a string method to locate all instances in which the driver was frisked.

Instructions
100 XP
Count the search_type values to see how many times "Protective Frisk" was the only search type.
Create a new column, frisk, that is True if search_type contains the string "Protective Frisk" and False otherwise.
Check the data type of frisk to confirm that it's a Boolean Series.
Take the sum of frisk to count the total number of frisks.
'''
SOLUTION
# Count the 'search_type' values
print(ri.search_type.value_counts())

# Check if 'search_type' contains the string 'Protective Frisk'
ri['frisk'] = ri.search_type.str.contains('Protective Frisk', na=False)

# Check the data type of 'frisk'
print(ri['frisk'].dtype)

# Take the sum of 'frisk'
print(ri['frisk'].sum())