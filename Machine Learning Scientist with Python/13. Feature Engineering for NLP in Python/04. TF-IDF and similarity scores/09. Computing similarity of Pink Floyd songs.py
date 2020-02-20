'''
Computing similarity of Pink Floyd songs
In this final exercise, you have been given lyrics of three songs by the British band Pink Floyd, namely 'High Hopes', 'Hey You' and 'Mother'. The lyrics to these songs are available as hopes, hey and mother respectively.

Your task is to compute the pairwise similarity between mother and hopes, and mother and hey.

Instructions
100 XP
Create Doc objects for mother, hopes and hey.
Compute the similarity between mother and hopes.
Compute the similarity between mother and hey.
'''
SOLUTION

# Create Doc objects
mother_doc = nlp(mother)
hopes_doc = nlp(hopes)
hey_doc = nlp(hey)

# Print similarity between mother and hopes
print(mother_doc.similarity(hopes_doc))

# Print similarity between mother and hey
print(mother_doc.similarity(hey_doc))