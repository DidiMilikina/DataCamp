'''
Text to DataFrame
Now that you have generated these count based features in an array you will need to reformat them so that they can be combined with the rest of the dataset. This can be achieved by converting the array into a pandas DataFrame, with the feature names you found earlier as the column names, and then concatenate it with the original DataFrame.

The numpy array (cv_array) and the vectorizer (cv) you fit in the last exercise are available in your workspace.

Instructions
100 XP
Create a DataFrame cv_df containing the cv_array as the values and the feature names as the column names.
Add the prefix Counts_ to the column names for ease of identification.
Concatenate this DataFrame (cv_df) to the original DataFrame (speech_df) column wise.
'''
SOLUTION 

 # Create a DataFrame with these features
cv_df = pd.DataFrame(cv_array, 
                     columns=cv.get_feature_names()).add_prefix('Counts_')

# Add the new columns to the original DataFrame
speech_df_new = pd.concat([speech_df, cv_df], axis=1, sort=False)
print(speech_df_new.head())