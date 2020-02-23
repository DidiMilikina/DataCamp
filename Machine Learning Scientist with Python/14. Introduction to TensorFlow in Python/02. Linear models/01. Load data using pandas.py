'''
Load data using pandas
Before you can train a machine learning model, you must first import data. There are several valid ways to do this, but for now, we will use a simple one-liner from pandas: pd.read_csv(). Recall from the video that the first argument specifies the path or URL. All other arguments are optional.

In this exercise, you will import the King County housing dataset, which we will use to train a linear model later in the chapter.

Instructions
100 XP
Import pandas under the alias pd.
Assign the path to a string variable with the name data_path.
Load the dataset as a pandas dataframe named housing.
Print the price column of housing.
'''
SOLUTION

# Import pandas under the alias pd
import pandas as pd 

# Assign the path to a string variable named data_path
data_path = 'kc_house_data.csv'

# Load the dataset as a dataframe named housing
housing = pd.read_csv(data_path)

# Print the price column of housing
print(housing['price'])