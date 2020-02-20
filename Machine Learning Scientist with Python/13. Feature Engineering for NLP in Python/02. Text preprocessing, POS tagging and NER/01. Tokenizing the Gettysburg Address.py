'''
Tokenizing the Gettysburg Address
In this exercise, you will be tokenizing one of the most famous speeches of all time: the Gettysburg Address delivered by American President Abraham Lincoln during the American Civil War.

The entire speech is available as a string named gettysburg.

Instructions
100 XP
Load the en_core_web_sm model using spacy.load().
Create a Doc object doc for the gettysburg string.
Using list comprehension, loop over doc to generate the token texts.
'''
SOLUTION

import spacy

# Load the en_core_web_sm model
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
doc = nlp(gettysburg)

# Generate the tokens
tokens = [token.text for token in doc]
print(tokens)