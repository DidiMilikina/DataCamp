'''
Plot recommendation engine
In this exercise, we will build a recommendation engine that suggests movies based on similarity of plot lines. You have been given a get_recommendations() function that takes in the title of a movie, a similarity matrix and an indices series as its arguments and outputs a list of most similar movies. indices has already been provided to you.

You have also been given a movie_plots Series that contains the plot lines of several movies. Your task is to generate a cosine similarity matrix for the tf-idf vectors of these plots.

Consequently, we will check the potency of our engine by generating recommendations for one of my favorite movies, The Dark Knight Rises.

Instructions
100 XP
Initialize a TfidfVectorizer with English stop_words. Name it tfidf.
Construct tfidf_matrix by fitting and transforming the movie plot data using fit_transform().
Generate the cosine similarity matrix cosine_sim using tfidf_matrix. Don't use cosine_similarity()!
Use get_recommendations() to generate recommendations for 'The Dark Knight Rises'.
'''
SOLUTION

# Initialize the TfidfVectorizer 
tfidf = TfidfVectorizer(stop_words='english')

# Construct the TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(movie_plots)

# Generate the cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
 
# Generate recommendations 
print(get_recommendations('The Dark Knight Rises', cosine_sim, indices))