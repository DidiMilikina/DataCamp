'''
Tf-idf with Wikipedia
Now it's your turn to determine new significant terms for your corpus by applying gensim's tf-idf. You will again have access to the same corpus and dictionary objects you created in the previous exercises - dictionary, corpus, and doc. Will tf-idf make for more interesting results on the document level?

TfidfModel has been imported for you from gensim.models.tfidfmodel.

Instructions 1/2
50 XP
1
Initialize a new TfidfModel called tfidf using corpus.
Use doc to calculate the weights. You can do this by passing [doc] to tfidf.
Print the first five term ids with weights.
2
Sort the term ids and weights in a new list from highest to lowest weight. This has been done for you.
Using your pre-existing dictionary, print the top five weighted words (term_id) from sorted_tfidf_weights, along with their weighted score (weight).
'''
SOLUTION

1
# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[doc]

# Print the first five weights
print(tfidf_weights[:5])

2
# Create a new TfidfModel using the corpus: tfidf
tfidf = TfidfModel(corpus)

# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = tfidf[doc]

# Print the first five weights
print(tfidf_weights[:5])

# Sort the weights from highest to lowest: sorted_tfidf_weights
sorted_tfidf_weights = sorted(tfidf_weights, key=lambda w: w[1], reverse=True)

# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(dictionary.get(term_id), weight)

