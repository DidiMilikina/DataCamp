'''
Exploring with dir and help
A new method has been added to the Document class. The method is a convenience wrapper around the plot_counter() function you wrote in an earlier exercise. In this exercise, you'll use dir() and help() to identify how to utilize the new method.

Instructions 1/3
35 XP
1
import the text_analyzer package.
Define my_doc as an instance of Document with the text stored in datacamp_tweets. datacamp_tweets has been pre-loaded in your environment.

3
Run help() on the plot method you discovered with dir() to see how to properly use the functionality.
Plot my_doc's word counts using the new plot method.

'''
SOLUTION

1
# Import needed package
import text_analyzer

# Create instance of document
my_doc = text_analyzer.Document(datacamp_tweets)

3
# Import needed package
import text_analyzer

# Create instance of document
my_doc = text_analyzer.Document(datacamp_tweets)

# Run help on my_doc's plot method
help(my_doc.plot_counts)

# Plot the word_counts of my_doc
my_doc.plot_counts()
