'''
Training a CNN to classify clothing types
Before training a neural network it needs to be compiled with the right cost function, using the right optimizer. During compilation, you can also define metrics that the network calculates and reports in every epoch. Model fitting requires a training data set, together with the training labels to the network.

The Conv2D model you built in the previous exercise is available in your workspace.

Instructions
100 XP
Compile the network using the 'adam' optimizer and the 'categorical_crossentropy' cost function. In the metrics list define that the network to report 'accuracy'.
Fit the network on train_data and train_labels. Train for 3 epochs with a batch size of 10 images. In training, set aside 20% of the data as a validation set, using the validation_split keyword argument.
'''
SOLUTION

# Compile the model 
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Fit the model on a training set
model.fit(train_data, train_labels, 
          validation_split=0.2, 
          epochs=3, batch_size=10)