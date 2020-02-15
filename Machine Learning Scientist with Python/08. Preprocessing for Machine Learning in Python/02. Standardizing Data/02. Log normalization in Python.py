'''
Log normalization in Python
Now that we know that the Proline column in our wine dataset has a large amount of variance, let's log normalize it.

Numpy has been imported as np in your workspace.

Instructions
100 XP
Print out the variance of the Proline column for reference.
Use the np.log() function on the Proline column to create a new, log-normalized column named Proline_log.
Print out the variance of the Proline_log column to see the difference.
'''
SOLUTION
# Print out the variance of the Proline column
print(wine['Proline'].var())

# Apply the log normalization function to the Proline column
wine['Proline_log'] = np.log(wine['Proline'])

# Check the variance of the normalized Proline column
print(wine['Proline_log'])