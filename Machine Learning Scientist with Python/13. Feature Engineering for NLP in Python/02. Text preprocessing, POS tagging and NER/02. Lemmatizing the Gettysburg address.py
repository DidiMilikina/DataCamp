'''
Lemmatizing the Gettysburg address
In this exercise, we will perform lemmatization on the same gettysburg address from before.

However, this time, we will also take a look at the speech, before and after lemmatization, and try to adjudge the kind of changes that take place to make the piece more machine friendly.

Instructions 1/3
35 XP
1
Print the gettysburg address to the console.

2
Loop over doc and extract the lemma for each token of gettysburg.

3
Convert lemmas into a string using join.
'''
SOLUTION

1
# Print the gettysburg address
print(gettysburg)

2
import spacy

# Load the en_core_web_sm model
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
doc = nlp(gettysburg)

# Generate lemmas
lemmas = [token.lemma_ for token in doc]

3
import spacy

# Load the en_core_web_sm model
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
doc = nlp(gettysburg)

# Generate lemmas
lemmas = [token.lemma_ for token in doc]

# Convert lemmas into a string
print(' '.join(lemmas))