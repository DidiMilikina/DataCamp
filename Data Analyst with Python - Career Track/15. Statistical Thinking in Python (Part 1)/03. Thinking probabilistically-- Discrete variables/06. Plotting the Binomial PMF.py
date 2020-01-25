'''
Plotting the Binomial PMF
As mentioned in the video, plotting a nice looking PMF requires a bit of matplotlib trickery that we will not go into here. Instead, we will plot the PMF of the Binomial distribution as a histogram with skills you have already learned. The trick is setting up the edges of the bins to pass to plt.hist() via the bins keyword argument. We want the bins centered on the integers. So, the edges of the bins should be -0.5, 0.5, 1.5, 2.5, ... up to max(n_defaults) + 1.5. You can generate an array like this using np.arange() and then subtracting 0.5 from the array.

You have already sampled out of the Binomial distribution during your exercises on loan defaults, and the resulting samples are in the NumPy array n_defaults.

Instructions
100 XP
Using np.arange(), compute the bin edges such that the bins are centered on the integers. Store the resulting array in the variable bins.
Use plt.hist() to plot the histogram of n_defaults with the normed=True and bins=bins keyword arguments.
Show the plot.
'''
SOLUTION
# Compute bin edges: bins
bins = np.arange(max(n_defaults) + 1.5) - 0.5

# Generate histogram
_ = plt.hist(n_defaults, normed=True, bins=bins)

# Label axes
_ = plt.xlabel('X')
_ = plt.ylabel('Y')

# Show the plot
plt.show()