'''
Creating Hyperparameters
For a school assignment, your professor has asked your class to create a random forest model to predict the average test score for the final exam.

After developing an initial random forest model, you are unsatisfied with the overall accuracy. You realize that there are too many hyperparameters to choose from, and each one has a lot of possible values. You have decided to make a list of possible ranges for the hyperparameters you might use in your next model.

Your professor has provided de-identified data for the last ten quizzes to act as the training data. There are 30 students in your class.

Instructions 1/3
35 XP
1
Print.get_params() in the console to review the possible parameters of the model that you can tune.

2
Create a maximum depth list, [4, 8, 12] and a minimum samples list [2, 5, 10] that specify possible values for each hyperparameter.

3
Create one final list to use for the maximum features.
Use values 4 through the maximum number of features possible (10), by 2.
'''
SOLUTION

1
# Review the parameters of rfr
print(rfr.get_params())

2
# Review the parameters of rfr
print(rfr.get_params())

# Maximum Depth
max_depth = [4, 8, 12]

# Minimum samples for a split
min_samples_split = [2, 5, 10]

3
# Review the parameters of rfr
print(rfr.get_params())

# Maximum Depth
max_depth = [4, 8, 12]

# Minimum samples for a split
min_samples_split = [2, 5, 10]

# Max features 
max_features = [4, 6, 8, 10]