'''
Leveraging documentation
When writing code for Data Science, it's inevitable that you'll need to install and use someone else's code. You'll quickly learn that using someone else's code is much more pleasant when they use good software engineering practices. In particular, good documentation makes the right way to call a function obvious. In this exercise you'll use python's help() method to view a function's documentation so you can determine how to correctly call a new method.

The list words has been loaded in your session.

Instructions 1/2
50 XP
1
View the documentation of the Counter.most_common method using the help() function. Note, you need to run the import statement before completing this step.

2
Correctly call Counter.most_common() by reading its documentation.
Print the results stored in top_5_words.
'''
SOLUTION

1

# load the Counter function into our environment
from collections import Counter

# View the documentation for Counter.most_common
help(Counter.most_common)

2
# load the Counter function into our environment
from collections import Counter

# View the documentation for Counter.most_common
help(Counter.most_common)

# use Counter to find the top 5 most common words
top_5_words = Counter(words).most_common(5)

# display the top 5 most common words
print(top_5_words)
