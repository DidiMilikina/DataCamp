'''
Iteratively tune multiple hyperparameters
In this exercise, you will build on the function you previously created to take in 2 hyperparameters, build a model and return the results. You will now use that to loop through some values and then extend this function and loop with another hyperparameter.

The function gbm_grid_search(learn_rate, max_depth) is available in this exercise.

If you need to remind yourself of the function you can run the function print_func() that has been created for you

Instructions 1/3
35 XP
1
Write a for-loop to test the values (0.01, 0.1, 0.5) for the learning_rate and (2, 4, 6) for the max_depth using the function you created gbm_grid_search and print the results.

2
Extend the gbm_grid_search function to include the hyperparameter subsample. Name this new function gbm_grid_search_extended.

3
Extend your loop to call gbm_grid_search (available in your console), then test the values [0.4 , 0.6] for the subsample hyperparameter and print the results. max_depth_list & learn_rate_list are available in your environment.
'''
SOLUTION

1
# Create the relevant lists
results_list = []
learn_rate_list = [0.01, 0.1, 0.5]
max_depth_list = [2, 4, 6]

# Create the for loop
for learn_rate in learn_rate_list:
    for max_depth in max_depth_list:
        results_list.append(gbm_grid_search(learn_rate, max_depth))

# Print the results
print(results_list)   

2
results_list = []
learn_rate_list = [0.01, 0.1, 0.5]
max_depth_list = [2,4,6]

# Extend the function input
def gbm_grid_search_extended(learn_rate, max_depth, subsample):

	# Extend the model creation section
    model = GradientBoostingClassifier(learning_rate=learn_rate, max_depth=max_depth, subsample=subsample)
    
    predictions = model.fit(X_train, y_train).predict(X_test)
    
    # Extend the return part
    return([learn_rate, max_depth, subsample, accuracy_score(y_test, predictions)])       

3
results_list = []

# Create the new list to test
subsample_list = [0.4, 0.6]

for learn_rate in learn_rate_list:
    for max_depth in max_depth_list:
    
    	# Extend the for loop
        for subsample in subsample_list:
        	
            # Extend the results to include the new hyperparameter
            results_list.append(gbm_grid_search_extended(learn_rate, max_depth, subsample))
            
# Print results
print(results_list)            