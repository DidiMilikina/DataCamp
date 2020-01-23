'''
Calculating the search rate
During a traffic stop, the police officer sometimes conducts a search of the vehicle. In this exercise, you'll calculate the percentage of all stops in the ri DataFrame that result in a vehicle search, also known as the search rate.

Instructions
100 XP
Check the data type of search_conducted to confirm that it's a Boolean Series.
Calculate the search rate by counting the Series values and expressing them as proportions.
Calculate the search rate by taking the mean of the Series. (It should match the proportion of True values calculated above.)
'''
SOLUTION
# Check the data type of 'search_conducted'
print(ri.search_conducted.dtype)

# Calculate the search rate by counting the values
print(ri.search_conducted.value_counts(normalize=True))

# Calculate the search rate by taking the mean
print(ri.search_conducted.mean())