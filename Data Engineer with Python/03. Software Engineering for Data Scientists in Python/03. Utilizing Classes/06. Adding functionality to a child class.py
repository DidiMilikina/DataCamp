'''
Adding functionality to a child class
You've just written a SocialMedia class that inherits functionality from Document. As of now, the SocialMedia class doesn't have any functionality different from Document. In this exercise, you will build features into SocialMedia to specialize it for use with Social Media data.

For reference, the definition of Document can be seen below.

class Document:
    # Initialize a new Document instance
    def __init__(self, text):
        self.text = text
        # Pre tokenize the document with non-public tokenize method
        self.tokens = self._tokenize()
        # Pre tokenize the document with non-public count_words
        self.word_counts = self._count_words()

    def _tokenize(self):
        return tokenize(self.text)

    # Non-public method to tally document's word counts
    def _count_words(self):
        # Use collections.Counter to count the document's tokens
        return Counter(self.tokens)
Instructions 1/2
50 XP
1
The function filter_word_counts() has been loaded in your session. Use help() to see its proper usage.
Finish the _count_hashtags method using filter_word_counts() so that only words_counts starting with # remain.

2
Fill in the first line ofSocialMedia's __init__ method using the parent class to properly utilize inheritance.
Properly call the _count_mentions method in __init__ to add a new feature to SocialMedia.
'''
SOLUTION

1
# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, '#')

2
# Define a SocialMedia class that is a child of the `Document class`
class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()
        
    def _count_hashtags(self):
        # Filter attribute so only words starting with '#' remain
        return filter_word_counts(self.word_counts, first_char='#')      
    
    def _count_mentions(self):
        # Filter attribute so only words starting with '@' remain
        return filter_word_counts(self.word_counts, first_char='@')
