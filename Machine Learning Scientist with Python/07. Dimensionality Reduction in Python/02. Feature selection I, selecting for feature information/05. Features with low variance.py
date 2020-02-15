'''
Features with low variance
In the previous exercise you established that 0.001 is a good threshold to filter out low variance features in head_df after normalization. Now use the VarianceThreshold feature selector to remove these features.

Instructions
100 XP
Create the variance threshold selector with a threshold of 0.001.
Normalize the head_df dataframe by dividing it by its mean values and fit the selector.
Create a boolean mask from the selector using .get_support().
Create a reduced dataframe by passing the mask to the .loc[] method.
'''
SOLUTION
from sklearn.feature_selection import VarianceThreshold

# Create a VarianceThreshold feature selector
sel = VarianceThreshold(threshold=0.001)

# Fit the selector to normalized head_df
sel.fit(head_df / head_df.mean())

# Create a boolean mask
mask = sel.get_support()

# Apply the mask to create a reduced dataframe
reduced_df = head_df.loc[:, mask]

print("Dimensionality reduced from {} to {}.".format(head_df.shape[1], reduced_df.shape[1]))