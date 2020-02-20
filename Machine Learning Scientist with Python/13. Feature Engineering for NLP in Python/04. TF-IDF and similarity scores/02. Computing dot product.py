'''
Computing dot product
In this exercise, we will learn to compute the dot product between two vectors, A = (1, 3) and B = (-2, 2), using the numpy library. More specifically, we will use the np.dot() function to compute the dot product of two numpy arrays.

Instructions
100 XP
Initialize A (1,3) and B (-2,2) as numpy arrays using np.array().
Compute the dot product using np.dot() and passing A and B as arguments.
'''
SOLUTION

# Initialize numpy vectors
A = np.array([1, 3])
B = np.array([-2, 2])

# Compute dot product
dot_prod = np.dot(A, B)

# Print dot product
print(dot_prod)