'''
Examining traffic violations
Before comparing the violations being committed by each gender, you should examine the violations committed by all drivers to get a baseline understanding of the data.

In this exercise, you'll count the unique values in the violation column, and then separately express those counts as proportions.

Instructions
100 XP
Count the unique values in the violation column of the ri DataFrame, to see what violations are being committed by all drivers.
Express the violation counts as proportions of the total.
'''
SOLUTION
# Count the unique values in 'violation'
print(ri.violation.value_counts())

# Express the counts as proportions
print(ri.violation.value_counts(normalize=True))