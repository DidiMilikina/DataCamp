'''
Cosine similarity matrix of a corpus
In this exercise, you have been given a corpus, which is a list containing five sentences. The corpus is printed in the console. You have to compute the cosine similarity matrix which contains the pairwise cosine similarity score for every pair of sentences (vectorized using tf-idf).

Remember, the value corresponding to the ith row and jth column of a similarity matrix denotes the similarity score for the ith and jth vector.

Instructions
100 XP
Initialize an instance of TfidfVectorizer. Name it tfidf_vectorizer.
Using fit_transform(), generate the tf-idf vectors for corpus. Name it tfidf_matrix.
Use cosine_similarity() and pass tfidf_matrix to compute the cosine similarity matrix cosine_sim.
'''
SOLUTION

# Initialize an instance of tf-idf Vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Generate the tf-idf vectors for the corpus
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)

# Compute and print the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
print(cosine_sim)