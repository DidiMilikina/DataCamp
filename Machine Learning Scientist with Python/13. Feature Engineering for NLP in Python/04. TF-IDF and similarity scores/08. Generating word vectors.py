'''
Generating word vectors
In this exercise, we will generate the pairwise similarity scores of all the words in a sentence. The sentence is available as sent and has been printed to the console for your convenience.

Instructions
100 XP
Create a Doc object doc for sent.
In the nested loop, compute the similarity between token1 and token2.
'''
SOLUTION

# Create the doc object
doc = nlp(sent)

# Compute pairwise similarity scores
for token1 in doc:
  for token2 in doc:
    print(token1.text, token2.text, token1.similarity(token2))