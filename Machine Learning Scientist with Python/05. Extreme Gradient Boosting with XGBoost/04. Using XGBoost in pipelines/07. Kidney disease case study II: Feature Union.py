'''
Kidney disease case study II: Feature Union
Having separately imputed numeric as well as categorical columns, your task is now to use scikit-learn's FeatureUnion to concatenate their results, which are contained in two separate transformer objects - numeric_imputation_mapper, and categorical_imputation_mapper, respectively.

You may have already encountered FeatureUnion in Machine Learning with the Experts: School Budgets. Just like with pipelines, you have to pass it a list of (string, transformer) tuples, where the first half of each tuple is the name of the transformer.

Instructions
100 XP
Import FeatureUnion from sklearn.pipeline.
Combine the results of numeric_imputation_mapper and categorical_imputation_mapper using FeatureUnion(), with the names "num_mapper" and "cat_mapper" respectively.
'''
SOLUTION
# Import FeatureUnion
from sklearn.pipeline import FeatureUnion

# Combine the numeric and categorical transformations
numeric_categorical_union = FeatureUnion([
                                          ("num_mapper", numeric_imputation_mapper),
                                          ("cat_mapper", categorical_imputation_mapper)
                                         ])