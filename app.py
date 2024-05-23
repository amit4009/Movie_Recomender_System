from flask import Flask, request, render_template
import pandas as pd
import pickle
import requests

app = Flask(__name__)

# Load the precomputed data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity_sparse.pkl', 'rb'))

def fetch_poster(movie_id):
    api_key = '9d81c4c34ee0a3b026b451893950c805'  # Replace with your TMDB API key
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return full_path
    return None

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

@app.route('/', methods=['GET', 'POST'])
def home():
    movie_list = movies['title'].values
    selected_movie = None
    recommendations = []
    posters = []

    if request.method == 'POST':
        selected_movie = request.form['movie']
        recommendations, posters = recommend(selected_movie)

    return render_template('index.html', movie_list=movie_list, selected_movie=selected_movie, recommendations=recommendations, posters=posters, zip=zip)

if __name__ == '__main__':
    app.run(debug=True)
