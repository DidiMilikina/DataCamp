'''
dding functionality to your package
Thanks to your work before, you already have a skeleton for your python package. In this exercise, you will work to define the functions needed for a text analysis of word usage.

In the file counter_utils.py, you will write 2 functions to be a part of your package: plot_counter and sum_counters. The structure of your package can be seen in the tree below. For the coding portions of this exercise, you will be working in the file counter_utils.py.

text_analyzer
├── __init__.py
└── counter_utils.py
Instructions 1/3
35 XP
1
Define top_items using plot_counter's inputs.

2
Return the correct output from sum_counters.

3

'''
SOLUTION 

1
# Import needed functionality
from collections import Counter

def plot_counter(counter, n_most_common=5):
  # Subset the n_most_common items from the input counter
  top_items = counter.most_common(n_most_common)
  # Plot `top_items`
  plot_counter_most_common(top_items)


2
# Import needed functionality
from collections import Counter

def sum_counters(counters):
  # Sum the inputted counters
  return sum(counters, Counter())
