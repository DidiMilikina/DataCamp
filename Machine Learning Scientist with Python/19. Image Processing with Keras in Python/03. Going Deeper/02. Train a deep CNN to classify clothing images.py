'''
Train a deep CNN to classify clothing images
Training a deep learning model is very similar to training a single layer network. Once the model is constructed (as you have done in the previous exercise), the model needs to be compiled with the right set of parameters. Then, the model is fit by providing it with training data, as well as training labels. After training is done, the model can be evaluated on test data.

The model you built in the previous exercise is available in your workspace.

Instructions
100 XP
Compile the model to use the categorical cross-entropy loss function and the Adam optimizer.
Train the network with train_data for 3 epochs with batches of 10 images each.
Use randomly selected 20% of the training data as validation data during training.
Evaluate the model with test_data, use a batch size of 10.
'''
SOLUTION

# Compile model
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# Fit the model to training data 
model.fit(train_data, train_labels, 
          validation_split=0.2, 
          epochs=3, batch_size=10)

# Evaluate the model on test data
model.evaluate(test_data, test_labels, batch_size=10)