'''
Arithmetical features
To practice creating new features, you will be working with a subsample from the Kaggle competition called "House Prices: Advanced Regression Techniques". The goal of this competition is to predict the price of the house based on its properties. It's a regression problem with Root Mean Squared Error as an evaluation metric.

Your goal is to create new features and determine whether they improve your validation score. To get the validation score from 5-fold cross-validation, you're given the get_kfold_rmse() function. Use it with the train DataFrame, available in your workspace, as an argument.

Instructions 1/3
50 XP
1
Create a new feature representing the total area (basement, 1st and 2nd floors) of the house. The columns "TotalBsmtSF", "FirstFlrSF" and "SecondFlrSF" give the areas of the basement, 1st and 2nd floors, respectively.

2
Create a new feature representing the area of the garden. It is a difference between the total area of the property ("LotArea") and the first floor area ("FirstFlrSF").

3
Create a new feature representing the total number of bathrooms in the house. It is a sum of full bathrooms ("FullBath") and half bathrooms ("HalfBath").
'''
SOLUTION 

1
# Look at the initial RMSE
print('RMSE before feature engineering:', get_kfold_rmse(train))

# Find the total area of the house
train['TotalArea'] = train.TotalBsmtSF + train.FirstFlrSF + train.SecondFlrSF

# Look at the updated RMSE
print('RMSE with total area:', get_kfold_rmse(train))

2
# Look at the initial RMSE
print('RMSE before feature engineering:', get_kfold_rmse(train))

# Find the total area of the house
train['TotalArea'] = train['TotalBsmtSF'] + train['FirstFlrSF'] + train['SecondFlrSF']
print('RMSE with total area:', get_kfold_rmse(train))

# Find the area of the garden
train['GardenArea'] = train.LotArea - train.FirstFlrSF
print('RMSE with garden area:', get_kfold_rmse(train))  

3
# Look at the initial RMSE
print('RMSE before feature engineering:', get_kfold_rmse(train))

# Find the total area of the house
train['TotalArea'] = train['TotalBsmtSF'] + train['FirstFlrSF'] + train['SecondFlrSF']
print('RMSE with total area:', get_kfold_rmse(train))

# Find the area of the garden
train['GardenArea'] = train['LotArea'] - train['FirstFlrSF']
print('RMSE with garden area:', get_kfold_rmse(train))

# Find total number of bathrooms
train['TotalBath'] = train.FullBath + train.HalfBath
print('RMSE with number of bathrooms:', get_kfold_rmse(train))