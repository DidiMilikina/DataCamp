'''
Tuning the number of boosting rounds
Let's start with parameter tuning by seeing how the number of boosting rounds (number of trees you build) impacts the out-of-sample performance of your XGBoost model. You'll use xgb.cv() inside a for loop and build one model per num_boost_round parameter.

Here, you'll continue working with the Ames housing dataset. The features are available in the array X, and the target vector is contained in y.

Instructions
100 XP
Create a DMatrix called housing_dmatrix from X and y.
Create a parameter dictionary called params, passing in the appropriate "objective" ("reg:linear") and "max_depth" (set it to 3).
Iterate over num_rounds inside a for loop and perform 3-fold cross-validation. In each iteration of the loop, pass in the current number of boosting rounds (curr_num_rounds) to xgb.cv() as the argument to num_boost_round.
Append the final boosting round RMSE for each cross-validated XGBoost model to the final_rmse_per_round list.
num_rounds and final_rmse_per_round have been zipped and converted into a DataFrame so you can easily see how the model performs with each boosting round. Hit 'Submit Answer' to see the results!
'''
SOLUTION
# Create the DMatrix: housing_dmatrix
housing_dmatrix = xgb.DMatrix(X, y)

# Create the parameter dictionary for each tree: params 
params = {"objective":"reg:linear", "max_depth":3}

# Create list of number of boosting rounds
num_rounds = [5, 10, 15]

# Empty list to store final round rmse per XGBoost model
final_rmse_per_round = []

# Iterate over num_rounds and build one model per num_boost_round parameter
for curr_num_rounds in num_rounds:

    # Perform cross-validation: cv_results
    cv_results = xgb.cv(dtrain=housing_dmatrix, params=params, nfold=3, num_boost_round=curr_num_rounds, metrics="rmse", as_pandas=True, seed=123)
    
    # Append final round RMSE
    final_rmse_per_round.append(cv_results["test-rmse-mean"].tail().values[-1])

# Print the resultant DataFrame
num_rounds_rmses = list(zip(num_rounds, final_rmse_per_round))
print(pd.DataFrame(num_rounds_rmses,columns=["num_boosting_rounds","rmse"]))