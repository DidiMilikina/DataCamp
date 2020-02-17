'''
Visualizing messy data
Let's take a look at a new dataset - this one is a bit less-clean than what you've seen before.

As always, you'll first start by visualizing the raw data. Take a close look and try to find datapoints that could be problematic for fitting models.

The data has been loaded into a DataFrame called prices.

Instructions
100 XP
Visualize the time series data using Pandas.
Calculate the number of missing values in each time series. Note any irregularities that you can see. What do you think they are?
'''
SOLUTION
# Visualize the dataset
prices.plot(legend=False)
plt.tight_layout()
plt.show()

# Count the missing values of each time series
missing_values = prices.isnull().sum()
print(missing_values)