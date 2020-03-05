'''
Genetic Hyperparameter Tuning with TPOT
You're going to undertake a simple example of genetic hyperparameter tuning. TPOT is a very powerful library that has a lot of features. You're just scratching the surface in this lesson, but you are highly encouraged to explore in your own time.

This is a very small example. In real life, TPOT is designed to be run for many hours to find the best model. You would have a much larger population and offspring size as well as hundreds more generations to find a good model.

You will create the estimator, fit the estimator to the training data and then score this on the test data.

For this example we wish to use:

3 generations
4 in the population size
3 offspring in each generation
accuracy for scoring
A random_state of 2 has been set for consistency of results.

Instructions
100 XP
Assign the values outlined in the context to the inputs for tpot_clf.
Create the tpot_clf classifier with the correct inputs.
Fit the classifier to the training data (X_train & y_train are available in your workspace).
Use the fitted classifier to score on the test set (X_test & y_test are available in your workspace).
'''
SOLUTION

# Assign the values outlined to the inputs
number_generations = 3
population_size = 4
offspring_size = 3
scoring_function = 'accuracy'

# Create the tpot classifier
tpot_clf = TPOTClassifier(generations=number_generations, population_size=population_size,
                          offspring_size=offspring_size, scoring=scoring_function,
                          verbosity=2, random_state=2, cv=2)

# Fit the classifier to the training data
tpot_clf.fit(X_train, y_train)

# Score on the test set
print(tpot_clf.score(X_test, y_test))