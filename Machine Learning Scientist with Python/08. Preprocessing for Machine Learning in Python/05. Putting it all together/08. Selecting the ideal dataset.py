'''
Selecting the ideal dataset
Let's get rid of some of the unnecessary features. Because we have an encoded country column, country_enc, keep it and drop other columns related to location: city, country, lat, long, state.

We have columns related to month and year, so we don't need the date or recorded columns.

We vectorized desc, so we don't need it anymore. For now we'll keep type.

We'll keep seconds_log and drop seconds and minutes.

Let's also get rid of the length_of_time column, which is unnecessary after extracting minutes.

Instructions
100 XP
Use .corr() to run the correlation on seconds, seconds_log, and minutes in the ufo DataFrame.
Make a list of columns to drop, in alphabetical order.
Use drop() to drop the columns.
Use the words_to_filter() function we created previously. Pass in vocab, vec.vocabulary_, desc_tfidf, and let's keep the top 4 words as the last parameter.
'''
SOLUTION
# Check the correlation between the seconds, seconds_log, and minutes columns
print(ufo[['seconds', 'seconds_log', 'minutes']].corr())

# Make a list of features to drop
to_drop = ['city', 'country', 'lat','long', 'state', 'seconds', 'minutes', 'date', 'desc', 'length_of_time', 'recorded']

# Drop those features
ufo_dropped = ufo.drop(to_drop, axis=1)

# Let's also filter some words out of the text vector we created
filtered_words = words_to_filter(vocab, vec.vocabulary_, desc_tfidf, 4)