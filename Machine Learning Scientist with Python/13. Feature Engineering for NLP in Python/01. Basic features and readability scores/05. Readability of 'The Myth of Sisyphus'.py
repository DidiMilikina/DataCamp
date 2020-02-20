'''
Readability of 'The Myth of Sisyphus'
In this exercise, you will compute the Flesch reading ease score for Albert Camus' famous essay The Myth of Sisyphus. We will then interpret the value of this score as explained in the video and try to determine the reading level of the essay.

The entire essay is in the form of a string and is available as sisyphus_essay.

Instructions
100 XP
Import the Textatistic class from textatistic.
Compute the readability_scores dictionary for sisyphus_essay using Textatistic.
Print the Flesch reading ease score from the readability_scores dictionary.
'''
SOLUTION

# Import Textatistic
from textatistic import Textatistic

# Compute the readability scores 
readability_scores = Textatistic(sisyphus_essay).scores

# Print the flesch reading ease score
flesch = readability_scores['flesch_score']
print("The Flesch Reading Ease is %.2f" % (flesch))