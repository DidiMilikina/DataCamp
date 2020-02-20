'''
Mapping feature indices with feature names
In the lesson video, we had seen that CountVectorizer doesn't necessarily index the vocabulary in alphabetical order. In this exercise, we will learn to map each feature index to its corresponding feature name from the vocabulary.

We will use the same three sentences on lions from the video. The sentences are available in a list named corpus and has already been printed to the console.

Instructions
100 XP
Instantiate a CountVectorizer object. Name it vectorizer.
Using fit_transform(), generate bow_matrix for corpus.
Using the get_feature_names() method, map the column names to the corresponding word in the vocabulary.
'''
SOLUTION

# Create CountVectorizer object
vectorizer = CountVectorizer()

# Generate matrix of word vectors
bow_matrix = vectorizer.fit_transform(corpus)

# Convert bow_matrix into a DataFrame
bow_df = pd.DataFrame(bow_matrix.toarray())

# Map the column names to vocabulary 
bow_df.columns = vectorizer.get_feature_names()

# Print bow_df
print(bow_df)