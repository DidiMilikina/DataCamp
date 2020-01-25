'''
Distribution of no-hitters and cycles
Now, you'll use your sampling function to compute the waiting time to observe a no-hitter and hitting of the cycle. The mean waiting time for a no-hitter is 764 games, and the mean waiting time for hitting the cycle is 715 games.

Instructions
100 XP
Use your successive_poisson() function to draw 100,000 out of the distribution of waiting times for observing a no-hitter and a hitting of the cycle.
Plot the PDF of the waiting times using the step histogram technique of a previous exercise. Don't forget the necessary keyword arguments. You should use bins=100, normed=True, and histtype='step'.
Label the axes.
Show your plot.
'''
SOLUTION
# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(tau1=764, tau2=715, size=100000)

# Make the histogram
_ = plt.hist(waiting_times, bins=100, normed=True, histtype='step')


# Label axes
_ = plt.xlabel('Waiting time to observe a no-hitter')
_ = plt.ylabel('Hitting of the cycle')

# Show the plot
plt.show()
