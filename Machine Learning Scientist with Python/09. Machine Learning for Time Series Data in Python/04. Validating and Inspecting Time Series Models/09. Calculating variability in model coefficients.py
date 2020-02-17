'''
Calculating variability in model coefficients
In this lesson, you'll re-run the cross-validation routine used before, but this time paying attention to the model's stability over time. You'll investigate the coefficients of the model, as well as the uncertainty in its predictions.

Begin by assessing the stability (or uncertainty) of a model's coefficients across multiple CV splits. Remember, the coefficients are a reflection of the pattern that your model has found in the data.

An instance of the Linear regression object (model) is available in your workpsace. Also, the arrays X and y (the data) are available too.

Instructions 1/2
80 XP
1
Initialize a TimeSeriesSplit cross-validation object
Create an array of all zeros to collect the coefficients.
Iterate through splits of the cross-validation object. On each iteration:
Fit the model on training data
Collect the model's coefficients for analysis later

2
Finally, calculate the 95% confidence interval for each coefficient in coefficients using the bootstrap_interval() function you defined in the previous exercise. You can run bootstrap_interval? if you want a refresher on the parameters that this function takes.
'''
SOLUTION

1
# Iterate through CV splits
n_splits = 100
cv = TimeSeriesSplit(n_splits=n_splits)

# Create empty array to collect coefficients
coefficients = np.zeros([n_splits, X.shape[1]])

for ii, (tr, tt) in enumerate(cv.split(X, y)):
    # Fit the model on training data and collect the coefficients
    model.fit(X[tr], y[tr])
    coefficients[ii] = model.coef_

2
# Calculate a confidence interval around each coefficient
bootstrapped_interval = bootstrap_interval(coefficients, percentiles=(2.5, 97.5))

# Plot it
fig, ax = plt.subplots()
ax.scatter(feature_names, bootstrapped_interval[0], marker='_', lw=3)
ax.scatter(feature_names, bootstrapped_interval[1], marker='_', lw=3)
ax.set(title='95% confidence interval for model coefficients')
plt.setp(ax.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()