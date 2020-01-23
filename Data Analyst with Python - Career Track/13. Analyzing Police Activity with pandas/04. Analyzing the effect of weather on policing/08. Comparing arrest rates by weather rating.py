'''
Comparing arrest rates by weather rating
Do police officers arrest drivers more often when the weather is bad? Find out below!

First, you'll calculate the overall arrest rate.
Then, you'll calculate the arrest rate for each of the weather ratings you previously assigned.
Finally, you'll add violation type as a second factor in the analysis, to see if that accounts for any differences in the arrest rate.
Since you previously defined a logical order for the weather categories, good < bad < worse, they will be sorted that way in the results.

Instructions 1/3
35 XP
1
Calculate the overall arrest rate by taking the mean of the is_arrested Series.
2
Calculate the arrest rate for each weather rating using a .groupby().
3
Calculate the arrest rate for each combination of violation and rating. How do the arrest rates differ by group?
'''
SOLUTION
1. 
# Calculate the overall arrest rate
print(ri_weather.is_arrested.mean())
2. 
# Calculate the arrest rate for each 'rating'
print(ri_weather.groupby('rating').is_arrested.mean())
3. 
# Calculate the arrest rate for each 'violation' and 'rating'
print(ri_weather.groupby(['violation', 'rating']).is_arrested.mean())