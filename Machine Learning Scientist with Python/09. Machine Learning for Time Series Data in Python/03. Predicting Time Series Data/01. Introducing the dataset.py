'''
Introducing the dataset
As mentioned in the video, you'll deal with stock market prices that fluctuate over time. In this exercise you've got historical prices from two tech companies (Ebay and Yahoo) in the DataFrame prices. You'll visualize the raw data for the two companies, then generate a scatter plot showing how the values for each company compare with one another. Finally, you'll add in a "time" dimension to your scatter plot so you can see how this relationship changes over time.

The data has been loaded into a DataFrame called prices.

Instructions 1/3
35 XP
1
Plot the data in prices. Pay attention to any irregularities you notice

2
Generate a scatter plot with the values of Ebay on the x-axis, and Yahoo on the y-axis. Look up the symbols for both companies from the column names of the DataFrame.

3
Finally, encode time as the color of each datapoint in order to visualize how the relationship between these two variables changes.

'''
SOLUTION

1
# Plot the raw values over time
prices.plot()
plt.show()

2
# Scatterplot with one company per axis
prices.plot.scatter(x='EBAY', y='YHOO')
plt.show()

3
# Scatterplot with color relating to time
prices.plot.scatter('EBAY', 'YHOO', c=prices.index, 
                    cmap=plt.cm.viridis, colorbar=False)
plt.show()