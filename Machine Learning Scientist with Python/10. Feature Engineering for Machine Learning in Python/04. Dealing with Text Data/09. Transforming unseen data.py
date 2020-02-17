'''
Transforming unseen data
When creating vectors from text, any transformations that you perform before training a machine learning model, you also need to apply on the new unseen (test) data. To achieve this follow the same approach from the last chapter: fit the vectorizer only on the training data, and apply it to the test data.

For this exercise the speech_df DataFrame has been split in two:

train_speech_df: The training set consisting of the first 45 speeches.
test_speech_df: The test set consisting of the remaining speeches.
Instructions
100 XP
Instantiate TfidfVectorizer.
Fit the vectorizer and apply it to the text_clean column.
Apply the same vectorizer on the text_clean column of the test data.
Create a DataFrame of these new features from the test set.
'''
SOLUTION

# Instantiate TfidfVectorizer
tv = TfidfVectorizer(max_features=100, stop_words='english')

# Fit the vectroizer and transform the data
tv_transformed = tv.fit_transform(train_speech_df['text_clean'])

# Transform test data
test_tv_transformed = tv.transform(test_speech_df['text_clean'])

# Create new features for the test set
test_tv_df = pd.DataFrame(test_tv_transformed.toarray(), 
                          columns=tv.get_feature_names()).add_prefix('TFIDF_')
print(test_tv_df.head())