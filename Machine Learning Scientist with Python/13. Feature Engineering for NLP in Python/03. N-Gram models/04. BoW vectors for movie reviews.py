'''
BoW vectors for movie reviews
In this exercise, you have been given two pandas Series, X_train and X_test, which consist of movie reviews. They represent the training and the test review data respectively. Your task is to preprocess the reviews and generate BoW vectors for these two sets using CountVectorizer.

Once we have generated the BoW vector matrices X_train_bow and X_test_bow, we will be in a very good position to apply a machine learning model to it and conduct sentiment analysis.

Instructions
100 XP
Import CountVectorizer from the sklearn library.
Instantiate a CountVectorizer object named vectorizer. Ensure that all words are converted to lowercase and english stopwords are removed.
Using X_train, fit vectorizer and then use it to transform X_train to generate the set of BoW vectors X_train_bow.
Transform X_test using vectorizer to generate the set of BoW vectors X_test_bow.
'''
SOLUTION
# Import CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer

# Create a CountVectorizer object
vectorizer = CountVectorizer(lowercase=True, stop_words='english')

# Fit and transform X_train
X_train_bow = vectorizer.fit_transform(X_train)

# Transform X_test
X_test_bow = vectorizer.transform(X_test)

# Print shape of X_train_bow and X_test_bow
print(X_train_bow.shape)
print(X_test_bow.shape)