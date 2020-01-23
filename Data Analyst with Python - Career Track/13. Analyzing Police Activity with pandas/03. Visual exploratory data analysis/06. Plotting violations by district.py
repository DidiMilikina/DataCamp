'''
Plotting violations by district
Now that you've created a frequency table focused on the "K" zones, you'll visualize the data to help you compare what violations are being caught in each zone.

First you'll create a bar plot, which is an appropriate plot type since you're comparing categorical data. Then you'll create a stacked bar plot in order to get a slightly different look at the data. Which plot do you find to be more insightful?

Instructions 1/2
50 XP

Create a bar plot of k_zones.
Display the plot and examine it. What do you notice about each of the zones?

Create a stacked bar plot of k_zones.
Display the plot and examine it. Do you notice anything different about the data than you did previously?
'''
SOLUTION
1.
# Create a bar plot of 'k_zones'
k_zones.plot(kind='bar')

# Display the plot
plt.show()

2. 
# Create a stacked bar plot of 'k_zones'
k_zones.plot(kind='bar', stacked=True)

# Display the plot
plt.show()
