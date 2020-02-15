'''
PCA explained variance
You'll be inspecting the variance explained by the different principal components of the pca instance you created in the previous exercise.

Instructions 1/4
25 XP
1
Print the explained variance ratio per principal component.

3
Calculate the cumulative sum of the explained variance ratio using a method of pca.explained_variance_ratio_.

4

'''
SOLUTION

1
# Inspect the explained variance ratio per component
print(pca.explained_variance_ratio_)

3
# Print the cumulative sum of the explained variance ratio
print(pca.explained_variance_ratio_.cumsum())