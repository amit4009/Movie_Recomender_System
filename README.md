# Movie_Recomender_System
Dataset from kaggle https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

# Description
The Movie Recommendation System is designed to suggest movies based on content similarity using data from the TMDB 5000 movies and credits datasets. The system employs a content-based filtering approach, analyzing features such as genres, keywords, cast, and crew to calculate the similarity between movies. By leveraging these features, the system can recommend movies that are similar to a given input movie.

# Dataset
The datasets used in this project are:

tmdb_5000_movies.csv: Contains detailed information about movies, including:
budget: The budget of the movie.<br>
genres: The genres associated with the movie.<br>
homepage: The official homepage URL of the movie.<br>
id: A unique identifier for the movie.<br>
keywords: Keywords describing the movie's content.<br>
original_language: The original language of the movie.<br>
original_title: The original title of the movie.<br>
overview: A brief summary of the movie.<br>
popularity: The popularity score of the movie.<br>
production_companies: Companies involved in the production.<br>
release_date: The release date of the movie.<br>
revenue: The revenue generated by the movie.<br>
runtime: The runtime of the movie.<br>
spoken_languages: Languages spoken in the movie.<br>
status: The release status of the movie (e.g., released, post-production).<br>
tagline: The tagline of the movie.<br>
title: The title of the movie.<br>
vote_average: The average vote score.<br>
vote_count: The number of votes received.<br>

tmdb_5000_credits.csv: Contains information about the cast and crew of 
the movies, including:

movie_id: A unique identifier for the movie.<br>
title: The title of the movie.<br>
cast: Details about the cast members.<br>
crew: Details about the crew members.<br>

# Key Features:
<u>Data Integration</u>: Combines movie details with credits data to enhance feature richness.<br>
<u>Feature Extraction</u>: Converts complex features into simplified, cohesive tags.<br>
<u>Similarity Calculation</u>: Utilizes cosine similarity to measure and compare movie similarities.<br>
<u>Personalized Recommendations</u>: Generates personalized movie recommendations based on user history.<br>

# Algorithm
The algorithm used in this recommendation system is based on content-based filtering. Here are the key steps:

<u>Data Preprocessing</u>: Merge the movies and credits datasets on the title.
Extract relevant features (genres, keywords, cast, crew) and convert them into a unified format.<br>

<u>Feature Engineering</u>: Create a 'tags' column that combines the selected features into a single string for each movie.
Convert the text data into numerical vectors using the CountVectorizer from scikit-learn, which limits the number of features to 5000 and removes English stop words.<br>

<u>Similarity Calculation</u>: Compute the cosine similarity between the vectors of movies to measure their similarity.
Convert the vectors into a sparse matrix for efficient computation.<br>

# Recommendation Generation:

For a given movie, find its vector representation and calculate the cosine similarity with all other movies.
Sort the movies based on their similarity scores and return the top 5 most similar movies.

# Results
The Movie Recommendation System provides effective content-based recommendations. For instance, when asked to recommend movies similar to 'Spider man -3', the system suggests:

Spider Man-2<br>
Spider Man<br>
The Amazing Spider Man-2<br>
The Amazing Spider Man<br>
Arachnophobia<br>

![alt text](movie_recomendation-1.png)

These recommendations showcase the system's ability to find movies with similar thematic elements and content.

# Observations:
<u>Enhanced Features</u>: Merging movie and credit data enriches the feature set, improving similarity calculations.<br>
<u>Effective Tagging</u>: Simplified feature conversion aids in creating cohesive tags for better recommendations.<br>
<u>Accurate Similarity</u>: Cosine similarity provides a robust measure for determining movie similarity.<br>
<u>User Personalization</u>: Aggregating recommendations based on user history enhances personalized suggestions.<br>

# Future Improvements
<u>Hybrid Recommendations</u>: Incorporate collaborative filtering techniques to enhance the recommendation accuracy.<br>
<u>User Feedback</u>: Integrate user feedback to continually refine and improve the recommendation system.<br>
<u>Scalability</u>: Optimize the system to handle larger datasets and provide faster recommendations.<br>