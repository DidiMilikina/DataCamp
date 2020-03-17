'''
Python modularity in the wild
In the slides, we covered 3 ways that you can write modular code with Python: packages, classes, and methods. For reference, you can see the example code we reviewed below.

# Import the pandas PACKAGE
import pandas as pd

# Create some example data
data = {'x': [1, 2, 3, 4], 
        'y': [20.1, 62.5, 34.8, 42.7]}

# Create a dataframe CLASS object
df = pd.DataFrame(data)

# Use the plot METHOD
df.plot('x', 'y')
In this exercise, you'll utilize a class & a method from the popular package numpy.

Instructions
100 XP
Complete the import statement to load the numpy package.
Use numpy's array class to define arr.
Use arr's sort method to sort the numpy array.
'''
SOLUTION

# import the numpy package
import numpy as np

# create an array class object
arr = np.array([8, 6, 7, 5, 3, 0, 9])

# use the sort method
arr.sort()

# print the sorted array
print(arr)
