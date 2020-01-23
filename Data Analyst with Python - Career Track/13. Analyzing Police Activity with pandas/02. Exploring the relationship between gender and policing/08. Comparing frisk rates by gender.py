'''
Comparing frisk rates by gender
In this exercise, you'll compare the rates at which female and male drivers are frisked during a search. Are males frisked more often than females, perhaps because police officers consider them to be higher risk?

Before doing any calculations, it's important to filter the DataFrame to only include the relevant subset of data, namely stops in which a search was conducted.

Instructions
100 XP
Create a DataFrame, searched, that only contains rows in which search_conducted is True.
Take the mean of the frisk column to find out what percentage of searches included a frisk.
Calculate the frisk rate for each gender using a .groupby().
'''
SOLUTION
# Create a DataFrame of stops in which a search was conducted
searched = ri[ri.search_conducted == True]

# Calculate the overall frisk rate by taking the mean of 'frisk'
print(searched.frisk.mean())

# Calculate the frisk rate for each gender
print(searched.groupby('driver_gender').frisk.mean())