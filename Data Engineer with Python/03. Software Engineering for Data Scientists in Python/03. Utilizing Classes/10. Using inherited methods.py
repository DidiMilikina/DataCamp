'''
Using inherited methods
You've now defined a Tweets class that's inherited methods from both Document and SocialMedia. In this exercise, you'll use inherited methods to visualize text from both tweets and retweets.

Be aware that this is real data from Twitter and as such there is always a risk that it may contain profanity or other offensive content (in this exercise, and any following exercises that also use real Twitter data).

Instructions 1/3
35 XP
1
import your text_analyzer package.
Define my_tweets as an instance of Tweets using the datacamp_tweets data that has been pre-loaded into your environment.

2
Use the plot_counts() method to plot the top 'hashtag_counts'.
Make sure to check the documentation for my_tweets.plot_counts.

3
Use the plot_counts() method of the retweets attribute to plot the most used hashtags in the retweets subset of the data.
'''
SOLUTION

1
# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

2
# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the tweets
my_tweets.plot_counts('hashtag_counts')

3
# Import needed package
import text_analyzer

# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the retweets
my_tweets.retweets.plot_counts('hashtag_counts')
