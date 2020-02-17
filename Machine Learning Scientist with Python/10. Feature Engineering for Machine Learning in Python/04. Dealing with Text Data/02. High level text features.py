'''
High level text features
Once the text has been cleaned and standardized you can begin creating features from the data. The most fundamental information you can calculate about free form text is its size, such as its length and number of words. In this exercise (and the rest of this chapter), you will focus on the cleaned/transformed text column (text_clean) you created in the last exercise.

Instructions
100 XP
Record the character length of each speech in the char_count column.
Record the word count of each speech in the word_count column.
Record the average word length of each speech in the avg_word_length column.
'''
SOLUTION

# Find the length of each text
speech_df['char_cnt'] = speech_df['text_clean'].str.len()

# Count the number of words in each text
speech_df['word_cnt'] = speech_df['text_clean'].str.split().str.len()

# Find the average length of word
speech_df['avg_word_length'] = speech_df['char_cnt'] / speech_df['word_cnt']

# Print the first 5 rows of these columns
print(speech_df[['text_clean', 'char_cnt', 'word_cnt', 'avg_word_length']])