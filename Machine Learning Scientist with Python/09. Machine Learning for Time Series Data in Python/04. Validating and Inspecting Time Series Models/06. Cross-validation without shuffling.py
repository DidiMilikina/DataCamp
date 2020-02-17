'''
Cross-validation without shuffling
Now, re-run your model fit using block cross-validation (without shuffling all datapoints). In this case, neighboring time-points will be kept close to one another. How do you think the model predictions will look in each cross-validation loop?

An instance of the Linear regression model object is available in your workspace. Also, the arrays X and y (training data) are available too.

Instructions
100 XP
Instantiate another cross-validation object, this time using KFold cross-validation with 10 splits and no shuffling.
Iterate through this object to fit a model using the training indices and generate predictions using the test indices.
Visualize the predictions across CV splits using the helper function (visualize_predictions()) we've provided.
'''
SOLUTION

# Create KFold cross-validation object
from sklearn.model_selection import KFold
cv = KFold(n_splits=10, shuffle=False, random_state=1)

# Iterate through CV splits
results = []
for tr, tt in cv.split(X, y):
    # Fit the model on training data
    model.fit(X[tr], y[tr])
    
    # Generate predictions on the test data and collect
    prediction = model.predict(X[tt])
    results.append((prediction, tt))
    
# Custom function to quickly visualize predictions
visualize_predictions(results)