'''
Beyond binary classification
Of course, binary classification is just a single special case. Target encoding could be applied to any target variable type:

For binary classification usually mean target encoding is used
For regression mean could be changed to median, quartiles, etc.
For multi-class classification with N classes we create N features with target mean for each category in one vs. all fashion
The mean_target_encoding() function you've created could be used for any target type specified above. Let's apply it for the regression problem on the example of House Prices Kaggle competition.

Your goal is to encode a categorical feature "RoofStyle" using mean target encoding. The train and test DataFrames are already available in your workspace.

Instructions
100 XP
Specify all the missing parameters for the mean_target_encoding() function call. Target variable name is "SalePrice". Set α hyperparameter to 10.
Recall that the train and test parameters expect the train and test DataFrames.
While the target and categorical parameters expect names of the target variable and feature to be encoded.
'''
SOLUTION

# Create mean target encoded feature
train['RoofStyle_enc'], test['RoofStyle_enc'] = mean_target_encoding(train=train,
                                                                     test=test,
                                                                     target='SalePrice',
                                                                     categorical='RoofStyle',
                                                                     alpha=10)

# Look at the encoding
print(test[['RoofStyle', 'RoofStyle_enc']].drop_duplicates())