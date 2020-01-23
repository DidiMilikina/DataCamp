'''
Comparing violations by gender
The question we're trying to answer is whether male and female drivers tend to commit different types of traffic violations.

In this exercise, you'll first create a DataFrame for each gender, and then analyze the violations in each DataFrame separately.

Instructions
100 XP
Create a DataFrame, female, that only contains rows in which driver_gender is 'F'.
Create a DataFrame, male, that only contains rows in which driver_gender is 'M'.
Count the violations committed by female drivers and express them as proportions.
Count the violations committed by male drivers and express them as proportions.
'''
SOLUTION
# Create a DataFrame of female drivers
female = ri[ri.driver_gender == 'F']

# Create a DataFrame of male drivers
male = ri[ri.driver_gender == 'M']

# Compute the violations by female drivers (as proportions)
print(female.violation.value_counts(normalize=True))

# Compute the violations by male drivers (as proportions)
print(male.violation.value_counts(normalize=True))