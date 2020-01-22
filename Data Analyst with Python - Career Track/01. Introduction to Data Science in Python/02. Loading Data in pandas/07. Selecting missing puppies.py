'''
Selecting missing puppies
Let's return to our DataFrame of missing puppies, which is loaded as mpr. Let's select a few different rows to learn more about the other missing dogs.

Instructions
100 XP
Select the dogs where Age is greater than 2.
Select the dogs whose Status is equal to Still Missing.
Select all dogs whose Dog Breed is not equal to Poodle.
'''
SOLUTION
# Select the dogs where Age is greater than 2
greater_than_2 = mpr[mpr.Age > 2]
print(greater_than_2)

# Select the dogs whose Status is equal to Still Missing
still_missing = mpr[mpr.Status == 'Still Missing']
print(still_missing)

# Select all dogs whose Dog Breed is not equal to Poodle
not_poodle = mpr[mpr['Dog Breed'] != 'Poodle']
print(not_poodle)