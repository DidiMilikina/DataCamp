'''
Lasso model results
Now that you've trained the Lasso model, you'll score its predictive capacity (R2) on the test set and count how many features are ignored because their coefficient is reduced to zero.

The X_test and y_test datasets have been pre-loaded for you.

The Lasso() model and StandardScaler() have been instantiated as la and scaler respectively and both were fitted to the training data.

Instructions
100 XP
Transform the test set with the pre-fitted scaler.
Calculate the R2 value on the scaled test data.
Create a list that has True values when coefficients equal 0.
Calculate the total number of features with a coefficient of 0.
'''
SOLUTION
# Transform the test set with the pre-fitted scaler
X_test_std = scaler.transform(X_test, y_test)

# Calculate the coefficient of determination (R squared) on X_test_std
r_squared = la.score(X_test_std, y_test)
print("The model can predict {0:.1%} of the variance in the test set.".format(r_squared))

# Create a list that has True values when coefficients equal 0
zero_coef = la.coef_ == 0

# Calculate how many features have a zero coefficient
n_ignored = sum(zero_coef)
print("The model has ignored {} out of {} features.".format(n_ignored, len(la.coef_)))