'''
What does your data look like? (I)
Up until now you have focused on creating new features and dealing with issues in your data. Feature engineering can also be used to make the most out of the data that you already have and use it more effectively when creating machine learning models.
Many algorithms may assume that your data is normally distributed, or at least that all your columns are on the same scale. This will often not be the case, e.g. one feature may be measured in thousands of dollars while another would be number of years. In this exercise, you will create plots to examine the distributions of some numeric columns in the so_survey_df DataFrame, stored in so_numeric_df.

Instructions 1/3
50 XP
1
Generate a histogram of all columns in the so_numeric_df DataFrame.

2
Generate box plots of the Age and Years Experience columns in the so_numeric_df DataFrame.

3
Generate a box plot of the ConvertedSalary column in the so_numeric_df DataFrame.
'''
SOLUTION

1
# Create a histogram
so_numeric_df.hist()
plt.show()

2
# Create a boxplot of two columns
so_numeric_df[['Age', 'Years Experience']].boxplot()
plt.show()

3
# Create a boxplot of ConvertedSalary
so_numeric_df[['ConvertedSalary']].boxplot()
plt.show()