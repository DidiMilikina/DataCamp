'''
tf-idf vectors for TED talks
In this exercise, you have been given a corpus ted which contains the transcripts of 500 TED Talks. Your task is to generate the tf-idf vectors for these talks.

In a later lesson, we will use these vectors to generate recommendations of similar talks based on the transcript.

Instructions
100 XP
Import TfidfVectorizer from sklearn.
Create a TfidfVectorizer object. Name it vectorizer.
Generate tfidf_matrix for ted using the fit_transform() method.
'''
SOLUTION

# Import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

# Create TfidfVectorizer object
vectorizer = TfidfVectorizer()

# Generate matrix of word vectors
tfidf_matrix = vectorizer.fit_transform(ted)

# Print the shape of tfidf_matrix
print(tfidf_matrix.shape)