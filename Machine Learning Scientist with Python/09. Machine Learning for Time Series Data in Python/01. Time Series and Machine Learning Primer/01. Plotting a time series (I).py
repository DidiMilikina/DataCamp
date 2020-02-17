'''
Plotting a time series (I)
In this exercise, you'll practice plotting the values of two time series without the time component.

Two DataFrames, data and data2 are available in your workspace.

Unless otherwise noted, assume that all required packages are loaded with their common aliases throughout this course.

Note: This course assumes some familiarity with time series data, as well as how to use them in data analytics pipelines. For an introduction to time series, we recommend the Introduction to Time Series Analysis in Python and Visualizing Time Series Data with Python courses.

Instructions 1/3
15 XP
1
Print the first five rows of data.

2
Print the first five rows of data2.

3
Plot the values column of both the data sets on top of one another, one per axis object.
'''
SOLUTION

1
# Print the first 5 rows of data
print(data.head(5))

2
# Print the first 5 rows of data2
print(data2.head(5))

3
# Plot the time series in each dataset
fig, axs = plt.subplots(2, 1, figsize=(5, 10))
data.iloc[:1000].plot(y='data_values', ax=axs[0])
data2.iloc[:1000].plot(y='data_values', ax=axs[1])
plt.show()