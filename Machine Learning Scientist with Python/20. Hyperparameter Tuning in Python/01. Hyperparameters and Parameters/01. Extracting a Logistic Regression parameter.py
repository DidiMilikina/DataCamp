'''
Extracting a Logistic Regression parameter
You are now going to practice extracting an important parameter of the logistic regression model. The logistic regression has a few other parameters you will not explore here but you can review them in the scikit-learn.org documentation for the LogisticRegression() module under 'Attributes'.

This parameter is important for understanding the direction and magnitude of the effect the variables have on the target.

In this exercise we will extract the coefficient parameter (found in the coef_ attribute), zip it up with the original column names, and see which variables had the largest positive effect on the target variable.

You will have available:

A logistic regression model object named log_reg_clf
The X_train DataFrame
sklearn and pandas have been imported for you.

Instructions
100 XP
Create a list of the original column names used in the training DataFrame.
Extract the coefficients of the logistic regression estimator.
Create a DataFrame of coefficients and variable names & view it.
Print out the top 3 'positive' variables based on the coefficient size.
'''
SOLUTION

# Create a list of original variable names from the training DataFrame
original_variables = list(X_train.columns)

# Extract the coefficients of the logistic regression estimator
model_coefficients = log_reg_clf.coef_[0]

# Create a dataframe of the variables and coefficients & print it out
coefficient_df = pd.DataFrame({"Variable" : original_variables, "Coefficient": model_coefficients})
print(coefficient_df)

# Print out the top 3 positive variables
top_three_df = coefficient_df.sort_values(by=['Coefficient'], axis=0, ascending=False)[0:3]
print(top_three_df)