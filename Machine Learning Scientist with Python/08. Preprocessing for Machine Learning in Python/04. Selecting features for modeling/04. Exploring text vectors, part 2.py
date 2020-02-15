'''
Exploring text vectors, part 2
Using the function we wrote in the previous exercise, we're going to extract the top words from each document in the text vector, return a list of the word indices, and use that list to filter the text vector down to those top words.

Instructions
100 XP
Call return_weights to return the top weighted words for that document.
Call set on the returned filter_list so we don't get duplicated numbers.
Call words_to_filter, passing in the following parameters: vocab for the vocab parameter, tfidf_vec.vocabulary_ for the original_vocab parameter, text_tfidf for the vector parameter, and 3 to grab the top_n 3 weighted words from each document.
Finally, pass that filtered_words set into a list to use as a filter for the text vector.
'''
SOLUTION
def words_to_filter(vocab, original_vocab, vector, top_n):
    filter_list = []
    for i in range(0, vector.shape[0]):
    
        # Here we'll call the function from the previous exercise, and extend the list we're creating
        filtered = return_weights(vocab, original_vocab, vector, i, top_n)
        filter_list.extend(filtered)
    # Return the list in a set, so we don't get duplicate word indices
    return set(filter_list)

# Call the function to get the list of word indices
filtered_words = words_to_filter(vocab, tfidf_vec.vocabulary_, text_tfidf, top_n=3)

# By converting filtered_words back to a list, we can use it to filter the columns in the text vector
filtered_text = text_tfidf[:, list(filtered_words)]