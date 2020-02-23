'''
Defining variables
Unlike a constant, a variable's value can be modified. This will be quite useful when we want to train a model by updating its parameters. Constants can't be used for this purpose, so variables are the natural choice.

Let's try defining and working with a variable. Note that Variable(), which is used to create a variable tensor, has been imported from tensorflow and is available to use in the exercise.

Instructions
100 XP
Define a variable, A1, as the 1-dimensional tensor: [1, 2, 3, 4].
Print A1. Do not use the .numpy() method. What did this tell you?
Apply .numpy() to A1 and assign it to B1.
Print B1. What did this tell you?
'''
SOLUTION

# Define the 1-dimensional variable A1
A1 = Variable([1, 2, 3, 4])

# Print the variable A1
print(A1)

# Convert A1 to a numpy array and assign it to B1
B1 = A1.numpy()

# Print B1
print(B1)