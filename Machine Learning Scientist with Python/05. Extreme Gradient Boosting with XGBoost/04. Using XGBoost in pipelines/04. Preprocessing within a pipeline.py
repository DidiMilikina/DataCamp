'''
Preprocessing within a pipeline
Now that you've seen what steps need to be taken individually to properly process the Ames housing data, let's use the much cleaner and more succinct DictVectorizer approach and put it alongside an XGBoostRegressor inside of a scikit-learn pipeline.

Instructions
100 XP
Import DictVectorizer from sklearn.feature_extraction and Pipeline from sklearn.pipeline.
Fill in any missing values in the LotFrontage column of X with 0.
Complete the steps of the pipeline with DictVectorizer(sparse=False) for "ohe_onestep" and xgb.XGBRegressor() for "xgb_model".
Create the pipeline using Pipeline() and steps.
Fit the Pipeline. Don't forget to convert X into a format that DictVectorizer understands by calling the to_dict("records") method on X.
'''
SOLUTION
# Import necessary modules
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline

# Fill LotFrontage missing values with 0
X.LotFrontage = X.LotFrontage.fillna(0)

# Setup the pipeline steps: steps
steps = [("ohe_onestep", DictVectorizer(sparse=False)),
         ("xgb_model", xgb.XGBRegressor())]

# Create the pipeline: xgb_pipeline
xgb_pipeline = Pipeline(steps)

# Fit the pipeline
xgb_pipeline.fit(X.to_dict("records"), y)