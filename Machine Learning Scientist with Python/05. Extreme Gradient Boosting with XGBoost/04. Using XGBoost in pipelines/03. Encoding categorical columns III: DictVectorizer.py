'''
Encoding categorical columns III: DictVectorizer
Alright, one final trick before you dive into pipelines. The two step process you just went through - LabelEncoder followed by OneHotEncoder - can be simplified by using a DictVectorizer.

Using a DictVectorizer on a DataFrame that has been converted to a dictionary allows you to get label encoding as well as one-hot encoding in one go.

Your task is to work through this strategy in this exercise!

Instructions
100 XP
Import DictVectorizer from sklearn.feature_extraction.
Convert df into a dictionary called df_dict using its .to_dict() method with "records" as the argument.
Instantiate a DictVectorizer object called dv with the keyword argument sparse=False.
Apply the DictVectorizer on df_dict by using its .fit_transform() method.
Hit 'Submit Answer' to print the resulting first five rows and the vocabulary.
'''
SOLUTION
# Import DictVectorizer
from sklearn.feature_extraction import DictVectorizer

# Convert df into a dictionary: df_dict
df_dict = df.to_dict('records')

# Create the DictVectorizer object: dv
dv = DictVectorizer(sparse=False)

# Apply dv on df: df_encoded
df_encoded = dv.fit_transform(df_dict)

# Print the resulting first five rows
print(df_encoded[:5,:])

# Print the vocabulary
print(dv.vocabulary_)