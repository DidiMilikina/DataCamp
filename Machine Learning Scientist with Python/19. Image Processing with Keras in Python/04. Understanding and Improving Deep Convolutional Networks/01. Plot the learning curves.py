'''
Plot the learning curves
During learning, the model will store the loss function evaluated in each epoch. Looking at the learning curves can tell us quite a bit about the learning process. In this exercise, you will plot the learning and validation loss curves for a model that you will train.

Instructions
100 XP
Fit the model to the training data (train_data).
Use a validation split of 20%, 3 epochs and batch size of 10.
Plot the training loss.
Plot the validation loss.
'''
SOLUTION

import matplotlib.pyplot as plt

# Train the model and store the training object
training = model.fit(train_data, train_labels, epochs=3, batch_size=10, validation_split=0.2)

# Extract the history from the training object
history = training.history

# Plot the training loss 
plt.plot(history['loss'])
# Plot the validation loss
plt.plot(history['val_loss'])

# Show the figure
plt.show()