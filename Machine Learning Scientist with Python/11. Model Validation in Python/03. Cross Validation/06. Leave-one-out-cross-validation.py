'''
Leave-one-out-cross-validation
Let's assume your favorite candy is not in the candy dataset, and that you are interested in the popularity of this candy. Using 5-fold cross-validation will train on only 80% of the data at a time. The candy dataset only has 85 rows though, and leaving out 20% of the data could hinder our model. However, using leave-one-out-cross-validation allows us to make the most out of our limited dataset and will give you the best estimate for your favorite candy's popularity!

In this exercise, you will use cross_val_score() to perform LOOCV.

Instructions
100 XP
Create a scorer using mean_absolute_error for cross_val_score() to use.
Fill out cross_val_score() so that the model rfr, the newly defined mae_scorer, and LOOCV are used.
Print the mean and the standard deviation of scores using numpy (loaded as np).
'''
SOLUTION

from sklearn.metrics import mean_absolute_error, make_scorer

# Create scorer
mae_scorer = make_scorer(mean_absolute_error)

rfr = RandomForestRegressor(n_estimators=15, random_state=1111)

# Implement LOOCV
scores = cross_val_score(rfr, X=X, y=y, cv=85, scoring=mae_scorer)

# Print the mean and standard deviation
print("The mean of the errors is: %s." % np.mean(scores))
print("The standard deviation of the errors is: %s." % np.std(scores))