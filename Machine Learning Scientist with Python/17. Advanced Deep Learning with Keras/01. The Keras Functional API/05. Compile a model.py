'''
Compile a model
The final step in creating a model is compiling it. Now that you've created a model, you have to compile it before you can fit it to data. This finalizes your model, freezes all its settings, and prepares it to meet some data!

During compilation, you specify the optimizer to use for fitting the model to the data, and a loss function. 'adam' is a good default optimizer to use, and will generally work well. Loss function depends on the problem at hand. Mean squared error is a common loss function and will optimize for predicting the mean, as is done in least squares regression.

Mean absolute error optimizes for the median and is used in quantile regression. For this dataset, 'mean_absolute_error' works pretty well, so use it as your loss function.

Instructions
100 XP
Compile the model you created (model).
Use the 'adam' optimizer.
Use mean absolute error (or 'mean_absolute_error') loss.
'''
SOLUTION

# Compile the model
model.compile(optimizer='adam', loss='mean_absolute_error')
