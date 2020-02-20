'''
Identifying people mentioned in a news article
In this exercise, you have been given an excerpt from a news article published in TechCrunch. Your task is to write a function find_people that identifies the names of people that have been mentioned in a particular piece of text. You will then use find_people to identify the people of interest in the article.

The article is available as the string tc and has been printed to the console. The required spacy model has also been already loaded as nlp.

Instructions
100 XP
Create a Doc object for text.
Using list comprehension, loop through doc.ents and create a list of named entities whose label is PERSON.
Using find_persons(), print the people mentioned in tc.
'''
SOLUTION

def find_persons(text):
  # Create Doc object
  doc = nlp(text)
  
  # Identify the persons
  persons = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
  
  # Return persons
  return persons

print(find_persons(tc))