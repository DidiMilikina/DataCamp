'''
Text vectorization
Let's transform the desc column in the UFO dataset into tf/idf vectors, since there's likely something we can learn from this field.

Instructions
100 XP
Print out the head() of the ufo["desc"] column.
Set vec equal to the TfidfVectorizer() object.
Use vec's fit_transform() method on the ufo["desc"] column.
Print out the shape of the desc_tfidf vector, to take a look at the number of columns this created. The output is in the shape (rows, columns).
'''
SOLUTION
# Take a look at the head of the desc field
print(ufo['desc'].head())

# Create the tfidf vectorizer object
vec = TfidfVectorizer()

# Use vec's fit_transform method on the desc field
desc_tfidf = vec.fit_transform(ufo['desc'])

# Look at the number of columns this creates
print(desc_tfidf.shape)