'''
POS tagging in Lord of the Flies
In this exercise, you will perform part-of-speech tagging on a famous passage from one of the most well-known novels of all time, Lord of the Flies, authored by William Golding.

The passage is available as lotf and has already been printed to the console.

Instructions
100 XP
Load the en_core_web_sm model.
Create a doc object for lotf using nlp().
Using the text and pos_ attributes, generate tokens and their corresponding POS tags.
'''
SOLUTION

# Load the en_core_web_sm model
nlp = spacy.load('en_core_web_sm')

# Create a Doc object
doc = nlp(lotf)

# Generate tokens and pos tags
pos = [(token.text, token.pos_) for token in doc]
print(pos)