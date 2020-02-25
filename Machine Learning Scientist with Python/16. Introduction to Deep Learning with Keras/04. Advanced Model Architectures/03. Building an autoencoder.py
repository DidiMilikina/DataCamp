'''
Building an autoencoder
Autoencoders have several interesting applications like anomaly detection or image denoising. They aim at producing an output identical to its inputs. The input will be compressed into a lower dimensional space, encoded. The model then learns to decode it back to its original form.

You will encode and decode the MNIST dataset of handwritten digits, the hidden layer will encode a 32-dimensional representation of the image, which originally consists of 784 pixels.

The Sequential model and Dense layers are ready for you to use.

Let's build an autoencoder!

Instructions
100 XP
Create a Sequential model.
Add a dense layer with as many neurons as the encoded image dimensions and input_shape the original size of the image.
Add a final layer with as many neurons as pixels in the input images.
Compile your autoencoder using adadelta as an optimizer and binary_crossentropy loss, then summarise it.
'''
SOLUTION

# Start with a sequential model
autoencoder = Sequential()

# Add a dense layer with the original image as input
autoencoder.add(Dense(32, input_shape=(784, ), activation="relu"))

# Add an output layer with as many nodes as the image
autoencoder.add(Dense(784, activation="sigmoid"))

# Compile your model
autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')

# Take a look at your model structure
autoencoder.summary()