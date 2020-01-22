'''
Load a DataFrame
A ransom note was left at the scene of Bayes' kidnapping. Eventually, we'll want to analyze the frequency with which each letter occurs in the note, to help us identify the kidnapper. For now, we just need to load the data from ransom.csv into Python.

We'll load the data into a DataFrame, a special data type from the pandas module. It represents spreadsheet-like data (something with rows and columns).

We can create a DataFrame from a CSV (comma-separated value) file by using the function pd.read_csv.

Instructions
100 XP
Use pd.read_csv to load data from a CSV file called ransom.csv. This file represents the frequency of each letter in the ransom note for Bayes.
'''
SOLUTION
# Import pandas
import pandas as pd

# Load the 'ransom.csv' into a DataFrame
r = pd.read_csv('ransom.csv')

# Display DataFrame
print(r)