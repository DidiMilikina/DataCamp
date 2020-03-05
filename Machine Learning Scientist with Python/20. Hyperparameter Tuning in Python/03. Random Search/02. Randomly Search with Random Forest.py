'''
Randomly Search with Random Forest
To solidify your knowledge of random sampling, let's try a similar exercise but using different hyperparameters and a different algorithm.

As before, create some lists of hyperparameters that can be zipped up to a list of lists. You will use the hyperparameters criterion, max_depth and max_features of the random forest algorithm. Then you will randomly sample hyperparameter combinations in preparation for running a random search.

You will use a slightly different package for sampling in this task, random.sample().

Instructions
100 XP
Create lists of the values 'gini' and 'entropy' for criterion & "auto", "sqrt", "log2", None for max_features.
Create a list of values between 3 and 55 inclusive for the hyperparameter max_depth and assign to the list max_depth_list. Remember that range(N,M) will create a list from N to M-1.
Combine these lists into a list of lists to sample from using product().
Randomly sample 150 models from the combined list and print the result.
'''
SOLUTION

# Create lists for criterion and max_features
criterion_list = ['gini', 'entropy']
max_feature_list = ["auto", "sqrt", "log2", None]

# Create a list of values for the max_depth hyperparameter
max_depth_list = list(range(3, 56))

# Combination list
combinations_list = [list(x) for x in product(max_depth_list, max_feature_list, criterion_list)]

# Sample hyperparameter combinations for a random search
combinations_random_chosen = random.sample(combinations_list, 150)

# Print the result
print(combinations_random_chosen)