'''
Plotting residuals of a regression
Often, you don't just want to see the regression itself but also see the residuals to get a better idea how well the regression captured the data. Seaborn provides sns.residplot() for that purpose, visualizing how far datapoints diverge from the regression line.

In this exercise, you will visualize the residuals of a regression between the 'hp' column (horse power) and the 'mpg' column (miles per gallon) of the auto DataFrame used previously.

Instructions
100 XP
Import matplotlib.pyplot and seaborn using the standard names plt and sns respectively.
Generate a green residual plot of the regression between 'hp' (on the x-axis) and 'mpg' (on the y-axis). You will need to specify the additional data and color parameters.
Display the plot as usual using plt.show(). This has been done for you, so hit 'Submit Answer' to view the plot.
'''
SOLUTION
# Import plotting modules
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a green residual plot of the regression between 'hp' and 'mpg'
sns.residplot('hp', 'mpg', data=auto, color='green')

# Display the plot
plt.show()
