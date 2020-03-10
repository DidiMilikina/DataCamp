'''
Testing Kaggle forum ideas
Unfortunately, not all the Forum posts and Kernels are necessarily useful for your model. So instead of blindly incorporating ideas into your pipeline, you should test them first.

You're given a function get_cv_score(), which takes a train dataset as an argument and returns the overall validation root mean squared error over 3-fold cross-validation. The train DataFrame is already available in your workspace.

You should try different suggestions from the Kaggle Forum and check whether they improve your validation score.

Instructions 1/2
50 XP
1
Suggestion 1: the passenger_count feature is useless. Let's see! Drop this feature and compare the scores.
Take Hint (-15 XP)
2
This first suggestion worked. Suggestion 2: Sum of "pickup_latitude" and "distance_km" is a good feature. Let's try it!
'''
SOLUTION

1
# Delete passenger_count column
new_train_1 = train.drop('passenger_count', axis=1)

# Compare validation scores
initial_score = get_cv_score(train)
new_score = get_cv_score(new_train_1)

print('Initial score is {} and the new score is {}'.format(initial_score, new_score))

2
# Create copy of the initial train DataFrame
new_train_2 = train.copy()

# Find sum of pickup latitude and ride distance
new_train_2['weird_feature'] = new_train_2.pickup_latitude + new_train_2.distance_km

# Compare validation scores
initial_score = get_cv_score(train)
new_score = get_cv_score(new_train_2)

print('Initial score is {} and the new score is {}'.format(initial_score, new_score))