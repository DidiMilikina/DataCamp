'''
Find missing data
Let's impute missing data on a real Kaggle dataset. For this purpose, you will be using a data subsample from the Kaggle "Two sigma connect: rental listing inquiries" competition.

Before proceeding with any imputing you need to know the number of missing values for each of the features. Moreover, if the feature has missing values, you should explore the type of this feature.

Instructions 1/2
50 XP
1
Read the "twosigma_train.csv" file using pandas.
Find the number of missing values in each column.

2
Select the columns with the missing values and look at the head of the DataFrame.
'''
SOLUTION

1
# Read DataFrame
twosigma = pd.read_csv('twosigma_train.csv')

# Find the number of missing values in each column
print(twosigma.isnull().sum())

2
# Read DataFrame
twosigma = pd.read_csv('twosigma_train.csv')

# Find the number of missing values in each column
print(twosigma.isnull().sum())

# Look at the columns with the missing values
print(twosigma[['building_id', 'price']].head())