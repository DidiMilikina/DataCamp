'''
Visualizing the correlation matrix
Reading the correlation matrix of ansur_df in its raw, numeric format doesn't allow us to get a quick overview. Let's improve this by removing redundant values and visualizing the matrix using seaborn.

Seaborn has been pre-loaded as sns, matplotlib.pyplot as plt, NumPy as np and pandas as pd.

Instructions 1/4
100 XP
1
Create the correlation matrix.
Visualize it using Seaborn's heatmap function.

2
Create a boolean mask for the upper triangle of the plot.

3
Add the mask to the heatmap.
'''
SOLUTION

1
# Create the correlation matrix
corr = ansur_df.corr()

# Draw the heatmap
sns.heatmap(ansur_df.corr(),  cmap=cmap, center=0, linewidths=1, annot=True, fmt=".2f")
plt.show()

2
# Create the correlation matrix
corr = ansur_df.corr()

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

3
# Create the correlation matrix
corr = ansur_df.corr()

# Generate a mask for the upper triangle 
mask = np.triu(np.ones_like(corr, dtype=bool))

# Add the mask to the heatmap
sns.heatmap(corr, mask=mask, cmap=cmap, center=0, linewidths=1, annot=True, fmt=".2f")
plt.show()