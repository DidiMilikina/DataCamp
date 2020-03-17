'''
Using your class's functionality
You've now added additional functionality to your Document class's __init__ method that automatically processes text for your users. In this exercise, you'll act as one of those users to see the benefits of your hard work.

The Document class (copied below) has been loaded into your environment (complete with your new updates).

class Document:
  def __init__(self, text):
    self.text = text
    # pre tokenize the document with non-public tokenize method
    self.tokens = self._tokenize()
    # pre tokenize the document with non-public count_words
    self.word_counts = self._count_words()

  def _tokenize(self):
    return tokenize(self.text)

  # non-public method to tally document's word counts with Counter
  def _count_words(self):
    return Counter(self.tokens)
Instructions
100 XP
Instructions
100 XP
Create a new Document instance from the datacamp_tweets data set loaded into your environment. The datacamp_tweets object is a single string containing hundreds of tweets written by DataCamp & DataCamp users.
Print the first 5 tokens from datacamp_doc.
Print the top 5 most common words that were calculated by the non-public _count_words() method automatically in the Document.__init__ method.
'''
SOLUTION

# create a new document instance from datacamp_tweets
datacamp_doc = Document(datacamp_tweets)

# print the first 5 tokens from datacamp_doc
print(datacamp_doc.tokens[:5])

# print the top 5 most used words in datacamp_doc
print(datacamp_doc._count_words().most_common(5))
