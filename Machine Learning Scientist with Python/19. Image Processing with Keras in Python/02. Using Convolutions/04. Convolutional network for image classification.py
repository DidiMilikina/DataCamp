'''
Convolutional network for image classification
Convolutional networks for classification are constructed from a sequence of convolutional layers (for image processing) and fully connected (Dense) layers (for readout). In this exercise, you will construct a small convolutional network for classification of the data from the fashion dataset.

Instructions
100 XP
Add a Conv2D layer to construct the input layer of the network. Use a kernel size of 3 by 3. You can use the img_rows and img_cols objects available in your workspace to define the input_shape of this layer.
Add a Flatten layer to translate between the image processing and classification part of your network.
Add a Dense layer to classify the 3 different categories of clothing in the dataset.
'''
SOLUTION

# Import the necessary components from Keras
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten

# Initialize the model object
model = Sequential()

# Add a convolutional layer
model.add(Conv2D(10, kernel_size=3, activation='relu', 
               input_shape=(img_rows, img_cols, 1)))

# Flatten the output of the convolutional layer
model.add(Flatten())
# Add an output layer for the 3 categories
model.add(Dense(3, activation='softmax'))