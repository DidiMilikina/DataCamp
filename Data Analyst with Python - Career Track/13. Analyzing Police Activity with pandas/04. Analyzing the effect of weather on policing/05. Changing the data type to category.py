'''
Changing the data type to category
Since the rating column only has a few possible values, you'll change its data type to category in order to store the data more efficiently. You'll also specify a logical order for the categories, which will be useful for future exercises.

Instructions
100 XP
Create a list object called cats that lists the weather ratings in a logical order: 'good', 'bad', 'worse'.
Change the data type of the rating column from object to category. Make sure to use the cats list to define the category ordering.
Examine the head of the rating column to confirm that the categories are logically ordered.
'''
SOLUTION
# Create a list of weather ratings in logical order
cats = ['good', 'bad', 'worse']

# Change the data type of 'rating' to category
weather['rating'] = weather.rating.astype('category', ordered=True, categories=cats)

# Examine the head of 'rating'
print(weather['rating'].head())