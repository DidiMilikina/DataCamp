'''
Encoding categorical variables
There are couple of columns in the UFO dataset that need to be encoded before they can be modeled through scikit-learn. You'll do that transformation here, using both binary and one-hot encoding methods.

Instructions
100 XP
Using apply(), write a lambda that returns a 1 if the value is us, else return 0. This is something we learned in Chapter 3 if you need a refresher.
Next, print out the number of unique() values of the type column.
Using pd.get_dummies(), create a one-hot encoded set of the type column.
Finally, use pd.concat() to concatenate the ufo dataset to the type_set encoded variables.
'''
SOLUTION
# Use Pandas to encode us values as 1 and others as 0
ufo["country_enc"] = ufo["country"].apply(lambda x: 1 if x == 'us' else 0)

# Print the number of unique type values
print(len(ufo['type'].unique()))

# Create a one-hot encoded set of the type values
type_set = pd.get_dummies(ufo['type'])

# Concatenate this set back to the ufo DataFrame
ufo = pd.concat([ufo, type_set], axis=1)