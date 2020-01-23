'''
Selecting from a multi-indexed Series
The output of a single .groupby() operation on multiple columns is a Series with a MultiIndex. Working with this type of object is similar to working with a DataFrame:

The outer index level is like the DataFrame rows.
The inner index level is like the DataFrame columns.
In this exercise, you'll practice accessing data from a multi-indexed Series using the .loc[] accessor.

Instructions
100 XP
Save the output of the .groupby() operation from the last exercise as a new object, arrest_rate. (This has been done for you.)
Print the arrest_rate Series and examine it.
Print the arrest rate for moving violations in bad weather.
Print the arrest rates for speeding violations in all three weather conditions.
'''
SOLUTION
# Save the output of the groupby operation from the last exercise
arrest_rate = ri_weather.groupby(['violation', 'rating']).is_arrested.mean()

# Print the 'arrest_rate' Series
print(arrest_rate)

# Print the arrest rate for moving violations in bad weather
print(arrest_rate['Moving violation']['bad'])

# Print the arrest rates for speeding violations in all three weather conditions
print(arrest_rate['Speeding'])