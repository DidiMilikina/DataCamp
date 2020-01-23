'''
Comparing search rates by gender
In this exercise, you'll compare the rates at which female and male drivers are searched during a traffic stop. Remember that the vehicle search rate across all stops is about 3.8%.

First, you'll filter the DataFrame by gender and calculate the search rate for each group separately. Then, you'll perform the same calculation for both genders at once using a .groupby().

Instructions 1/3
35 XP

Filter the DataFrame to only include female drivers, and then calculate the search rate by taking the mean of search_conducted.
Filter the DataFrame to only include male drivers, and then repeat the search rate calculation.
Group by driver gender to calculate the search rate for both groups simultaneously. (It should match the previous results.)
'''
SOLUTION
1. 
# Calculate the search rate for female drivers
print(ri[ri.driver_gender == 'F'].search_conducted.mean())
2. 
# Calculate the search rate for male drivers
print(ri[ri.driver_gender == 'M'].search_conducted.mean())
3. 
# Calculate the search rate for both groups simultaneously
print(ri.groupby('driver_gender').search_conducted.mean())