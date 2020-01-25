'''
The standard deviation and the variance
As mentioned in the video, the standard deviation is the square root of the variance. You will see this for yourself by computing the standard deviation using np.std() and comparing it to what you get by computing the variance with np.var() and then computing the square root.

Instructions
100 XP
Compute the variance of the data in the versicolor_petal_length array using np.var() and store it in a variable called variance.

Print the square root of this value.

Print the standard deviation of the data in the versicolor_petal_length array using np.std().
'''
SOLUTION
# Compute the variance: variance
variance = np.var(versicolor_petal_length)

# Print the square root of the variance
print(np.sqrt(variance))

# Print the standard deviation
print(np.std(versicolor_petal_length))