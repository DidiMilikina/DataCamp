'''
Creating a grandchild class
In this exercise you will be using inheritance to create a Tweet class from your SocialMedia class. This new grandchild class of Document will be able to tackle Twitter specific details such as retweets.

Instructions
100 XP
Complete the class statement so that Tweets inherits from SocialMedia. SocialMedia has already been loaded in your environment.
Use super() to call the __init__ method of the parent class.
Define retweet_text. Use help() to complete the call to filter_lines with the correct parameter name. filter_lines has already been loaded in your environment.
return retweet_text from _process_retweets as an instance of SocialMedia.
'''
SOLUTION

# Define a Tweet class that inherits from SocialMedia
class Tweets(SocialMedia):
    def __init__(self, text):
        # Call parent's __init__ with super()
        super().__init__(SocialMedia)
        # Define retweets attribute with non-public method
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        # Filter tweet text to only include retweets
        retweet_text = filter_lines(self.text, first_chars='RT')
        # Return retweet_text as a SocialMedia object
        return retweet_text(SocialMedia(retweet_text))
