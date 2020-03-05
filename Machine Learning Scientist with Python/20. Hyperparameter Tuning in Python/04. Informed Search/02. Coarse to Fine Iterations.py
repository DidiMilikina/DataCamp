'''
Coarse to Fine Iterations
You will now visualize the first random search undertaken, construct a tighter grid and check the results. You will have available:

results_df - a DataFrame that has the hyperparameter combination and the resulting accuracy of all 500 trials. Only the hyperparameters that had the strongest visualizations from the previous exercise are included (max_depth and learn_rate)
visualize_first() - This function takes no arguments but will visualize each of your hyperparameters against accuracy for your first random search.
Instructions 1/3
35 XP
1
Use the visualize_first() function to check the values of max_depth and learn_rate that tend to perform better. A convenient red line will be added to make this explicit.

2
Now create a more narrow grid search, testing for max_depth values between 1 and 20 and for 50 learning rates between 0.001 and 1.

3
We ran the 1,000 model grid search in the background based on those new combinations. Now use the visualize_second() function to visualize the second iteration (grid search) and see if there is any improved results.
'''
SOLUTION

1
# Use the provided function to visualize the first results
visualize_first()

2
# Use the provided function to visualize the first results
# visualize_first()

# Create some combinations lists & combine
max_depth_list = list(range(1, 21))
learn_rate_list = np.linspace(0.001, 1, 50)

3
# Use the provided function to visualize the first results
# visualize_first()

# Create some combinations lists & combine:
max_depth_list = list(range(1,21))
learn_rate_list = np.linspace(0.001,1,50)

# Call the function to visualize the second results
visualize_second()