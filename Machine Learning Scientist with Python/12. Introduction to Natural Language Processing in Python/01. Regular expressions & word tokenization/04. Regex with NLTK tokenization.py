'''
Regex with NLTK tokenization
Twitter is a frequently used source for NLP text and tasks. In this exercise, you'll build a more complex tokenizer for tweets with hashtags and mentions using nltk and regex. The nltk.tokenize.TweetTokenizer class gives you some extra methods and attributes for parsing tweets.

Here, you're given some example tweets to parse using both TweetTokenizer and regexp_tokenize from the nltk.tokenize module. These example tweets have been pre-loaded into the variable tweets. Feel free to explore it in the IPython Shell!

Unlike the syntax for the regex library, with nltk_tokenize() you pass the pattern as the second argument.

Instructions 1/4
25 XP
1
From nltk.tokenize, import regexp_tokenize and TweetTokenizer.

2
A regex pattern to define hashtags called pattern1 has been defined for you. Call regexp_tokenize() with this hashtag pattern on the first tweet in tweets and assign the result to hashtags.
Print hashtags (this has already been done for you).

3
Write a new pattern called pattern2 to match mentions and hashtags. A mention is something like @DataCamp.

Then, call regexp_tokenize() with your new hashtag pattern on the last tweet in tweets and assign the result to mentions_hashtags.

You can access the last element of a list using -1 as the index, for example, tweets[-1].
Print mentions_hashtags (this has been done for you).

4
Create an instance of TweetTokenizer called tknzr and use it inside a list comprehension to tokenize each tweet into a new list called all_tokens.
To do this, use the .tokenize() method of tknzr, with t as your iterator variable.
Print all_tokens.

'''
SOLUTION

1
# Import the necessary modules
from nltk.tokenize import regexp_tokenize, TweetTokenizer

2
# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer
# Define a regex pattern to find hashtags: pattern1
pattern1 = r"#\w+"
# Use the pattern on the first tweet in the tweets list
hashtags = regexp_tokenize(tweets[0], pattern1)
print(hashtags)

3
# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer
# Write a pattern that matches both mentions (@) and hashtags
pattern2 = r"([@\#]\w+)"
# Use the pattern on the last tweet in the tweets list
mentions_hashtags = regexp_tokenize(tweets[-1], pattern2)
print(mentions_hashtags)

4
# Import the necessary modules
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import TweetTokenizer
# Use the TweetTokenizer to tokenize all tweets into one list
tknzr = TweetTokenizer()
all_tokens = [tknzr.tokenize(t) for t in tweets]
print(all_tokens)