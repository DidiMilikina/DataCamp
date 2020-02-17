'''
Cleaning up your text
Unstructured text data cannot be directly used in most analyses. Multiple steps need to be taken to go from a long free form string to a set of numeric columns in the right format that can be ingested by a machine learning model. The first step of this process is to standardize the data and eliminate any characters that could cause problems later on in your analytic pipeline.

In this chapter you will be working with a new dataset containing the inaugural speeches of the presidents of the United States loaded as speech_df, with the speeches stored in the text column.

Instructions 1/2
50 XP
1
Print the first 5 rows of the text column to see the free text fields.

2
Replace all non letter characters in the text column with a whitespace.
Make all characters in the newly created text_clean column lower case.
'''
SOLUTION

1
# Print the first 5 rows of the text column
print(speech_df['text'].head(5))

2
# Replace all non letter characters with a whitespace
speech_df['text_clean'] = speech_df['text'].str.replace('[^a-zA-Z]', ' ')

# Change to lower case
speech_df['text_clean'] = speech_df['text_clean'].str.lower()

# Print the first 5 rows of the text_clean column
print(speech_df['text_clean'].head())