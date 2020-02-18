'''
Reusing model parameters
Replicating model performance is vital in model validation. Replication is also important when sharing models with co-workers, reusing models on new data or asking questions on a website such as Stack Overflow. You might use such a site to ask other coders about model errors, output, or performance. The best way to do this is to replicate your work by reusing model parameters.

In this exercise, you use various methods to recall which parameters were used in a model.

Instructions
100 XP
Print out the characteristics of the model rfc by simply printing the model.
Print just the random state of the model.
Print the dictionary of model parameters.
'''
SOLUTION

rfc = RandomForestClassifier(n_estimators=50, max_depth=6, random_state=1111)

# Print the classification model
print(rfc)

# Print the classification model's random state parameter
print('The random state is: {}'.format(rfc.random_state))

# Print all parameters
print('Printing the parameters dictionary: {}'.format(rfc.get_params()))