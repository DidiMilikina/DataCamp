'''
Train a deep CNN with pooling to classify images
Training a CNN with pooling layers is very similar to training of the deep networks that y have seen before. Once the network is constructed (as you did in the previous exercise), the model needs to be appropriately compiled, and then training data needs to be provided, together with the other arguments that control the fitting procedure.

The following model from the previous exercise is available in your workspace:

Convolution => Max pooling => Convolution => Flatten => Dense

Instructions
100 XP
Compile this model to use the categorical cross-entropy loss function and the Adam optimizer.
Train the model for 3 epochs with batches of size 10.
Use 20% of the data as validation data.
Evaluate the model on test_data with test_labels (also batches of size 10).
'''
SOLUTION

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Fit to training data
model.fit(train_data, train_labels, epochs=3, batch_size=10, validation_split=0.2)

# Evaluate on test data 
model.evaluate(test_data, test_labels, batch_size=10)