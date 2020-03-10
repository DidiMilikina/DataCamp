'''
Impute missing data
You've found that "price" and "building_id" columns have missing values in the Rental Listing Inquiries dataset. So, before passing the data to the models you need to impute these values.

Numerical feature "price" will be encoded with a mean value of non-missing prices.

Imputing categorical feature "building_id" with the most frequent category is a bad idea, because it would mean that all the apartments with a missing "building_id" are located in the most popular building. The better idea is to impute it with a new category.

The DataFrame rental_listings with competition data is read for you.

Instructions 1/2
50 XP
1
Create a SimpleImputer object with "mean" strategy.
Impute missing prices with the mean value.

2
Create an imputer with "constant" strategy. Use "MISSING" as fill_value.
Impute missing buildings with a constant value.
'''
SOLUTION

1
# Import SimpleImputer
from sklearn.impute import SimpleImputer

# Create mean imputer
mean_imputer = SimpleImputer(strategy='mean')

# Price imputation
rental_listings[['price']] = mean_imputer.fit_transform(rental_listings[['price']])

2
# Import SimpleImputer
from sklearn.impute import SimpleImputer

# Create constant imputer
constant_imputer = SimpleImputer(strategy='constant', fill_value='MISSING')

# building_id imputation
rental_listings[['building_id']] = constant_imputer.fit_transform(rental_listings[['building_id']])