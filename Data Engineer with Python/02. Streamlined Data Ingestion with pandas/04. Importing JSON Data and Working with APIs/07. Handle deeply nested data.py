'''
Handle deeply nested data
Last exercise, you flattened data nested down one level. Here, you'll unpack more deeply nested data.

The categories attribute in the Yelp API response contains lists of objects. To flatten this data, you'll employ json_normalize() arguments to specify the path to categories and pick other attributes to include in the data frame. You should also change the separator to facilitate column selection and prefix the other attributes to prevent column name collisions. We'll work through this in steps.

pandas (as pd) and json_normalize() have been imported. JSON-formatted Yelp data on cafes in NYC is stored as data.

Instructions 1/3
35 XP
1
Use json_normalize() to flatten records under the businesses key in data, setting underscores (_) as separators.

2
Specify the record_path to the categories data.

3
Set the meta keyword argument to get business name, alias, rating, and the attributes nested under coordinates: latitude and longitude.
Add "biz_" as a meta_prefix to prevent duplicate column names.
'''
SOLUTION

1
# Flatten businesses records and set underscore separators
flat_cafes = json_normalize(data["businesses"],
                  sep='_')

# View the data
print(flat_cafes.head())

2
# Specify record path to get categories data
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path='categories')

# View the data
print(flat_cafes.head())

3
# Load other business attributes and set meta prefix
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories",
                    		meta=['name', 
                                  'alias',  
                                  'rating',
                          		  ['coordinates', 'latitude'], 
                          		  ['coordinates', 'longitude']],
                    		meta_prefix='biz_')





# View the data
print(flat_cafes.head())