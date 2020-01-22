'''
Correcting column selection errors
A junior detective tried to access the location columns of credit_records, but he made some mistakes. Help correct his code so that we can search for suspicious purchases.

In all exercises going forward, pandas will be imported as pd. The DataFrame credit_records has already been imported.

Instructions
100 XP
Correct the code so that it runs without errors.
'''
SOLUTION
# One or more lines of code contain errors.
# Fix the errors so that the code runs.

# Select the location column in credit_records
location = credit_records['location']

# Select the item column in credit_records
items = credit_records["item"]

# Display results
print(location)