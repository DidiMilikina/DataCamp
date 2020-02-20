'''
Named entities in a sentence
In this exercise, we will identify and classify the labels of various named entities in a body of text using one of spaCy's statistical models. We will also verify the veracity of these labels.

Instructions
100 XP
Use spacy.load() to load the en_core_web_sm model.
Create a Doc instance doc using text and nlp.
Loop over doc.ents to print all the named entities and their corresponding labels.
'''
SOLUTION

# Load the required model
nlp = spacy.load('en_core_web_sm')

# Create a Doc instance 
text = 'Sundar Pichai is the CEO of Google. Its headquarters is in Mountain View.'
doc = nlp(text)

# Print all named entities and their labels
for ent in doc.ents:
    print(ent.text, ent.label_)