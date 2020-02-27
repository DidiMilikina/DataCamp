'''
Plotting models
In addition to summarizing your model, you can also plot your model to get a more intuitive sense of it. Your model is available in the workspace.

Instructions 1/4
35 XP
1
Save the model plot to the file 'model.png'.
Import and display 'model.png' into Python using matplotlib.

2
How many inputs does this model have?

3
How many outputs does this model have?

4
Which layer is shared between 2 inputs?
'''
SOLUTION

1
# Imports
import matplotlib.pyplot as plt
from keras.utils import plot_model

# Plot the model
plot_model(model, to_file='model.png')

# Display the image
data = plt.imread('model.png')
plt.imshow(data)
plt.show()

2
>3

3
>1

4
Team-Strength