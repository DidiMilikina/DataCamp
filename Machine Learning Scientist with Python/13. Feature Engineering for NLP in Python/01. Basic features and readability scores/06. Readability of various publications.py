'''
Readability of various publications
In this exercise, you have been given excerpts of articles from four publications. Your task is to compute the readability of these excerpts using the Gunning fog index and consequently, determine the relative difficulty of reading these publications.

The excerpts are available as the following strings:

forbes- An excerpt from an article from Forbes magazine on the Chinese social credit score system.
harvard_law- An excerpt from a book review published in Harvard Law Review.
r_digest- An excerpt from a Reader's Digest article on flight turbulence.
time_kids - An excerpt from an article on the ill effects of salt consumption published in TIME for Kids.
Instructions
100 XP
Import the Textatistic class from textatistic.
Compute the readability_scores dictionary for each excerpt using Textatistic.
Select the Gunning fog index from the readability_scores dictionary for each excerpt and append it to gunning_fog_scores.
Print the list of Gunning fog indices.
'''
SOLUTION

# Import Textatistic
from textatistic import Textatistic

# List of excerpts
excerpts = [forbes, harvard_law, r_digest, time_kids]

# Loop through excerpts and compute gunning fog index
gunning_fog_scores = []
for excerpt in excerpts:
  readability_scores = Textatistic(excerpt).scores
  gunning_fog = readability_scores['gunningfog_score']
  gunning_fog_scores.append(gunning_fog)

# Print the gunning fog indices
print(gunning_fog_scores)