import requests
import random

API_key = '01e98ce45d199a2980980280719162c9'  # My TMDB API key
BASE_url = 'https://api.themoviedb.org/3'

def get_genres():
    """Fetch the list of genres and their IDs from TMDB API."""
    url = f"{BASE_url}/genre/movie/list"
    params = {"api_key": API_key, "language": "en-US"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        genres = response.json().get("genres", [])
        return {genre["name"]: genre["id"] for genre in genres}
    else:
        print("Failed to fetch genres.")
        return {}

def get_movies_by_genre(genre_id):
    """Fetch movies from a specific genre."""
    url = f"{BASE_url}/discover/movie"
    params = {
        "api_key": API_key,
        "language": "en-US",
        "with_genres": genre_id,
        "sort_by": "popularity.desc",
        "page": 1
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        movies = response.json().get("results", [])
        return movies
    else:
        print("Failed to fetch movies.")
        return []

def recommend_movie():
    """Main function to recommend a movie based on user input."""
    print("Fetching genres...")
    genres = get_genres()
    if not genres:
        return
    
    # Display available genres
    print("\nAvailable genres:")
    for genre in genres:
        print(f"- {genre}")
    
    # Get user input for genre
    user_genre = input("\nEnter a genre from the list above: ")
    if user_genre not in genres:
        print("Invalid genre. Please try again.")
        return
    
    genre_id = genres[user_genre]
    
    # Fetch movies from the selected genre
    print(f"\nFetching movies in the '{user_genre}' genre...")
    movies = get_movies_by_genre(genre_id)
    
    if not movies:
        print("No movies found for this genre.")
        return
    
    # Recommend a random movie
    recommended_movie = random.choice(movies)
    title = recommended_movie.get("title", "Unknown Title")
    overview = recommended_movie.get("overview", "No description available.")
    
    print(f"\nRecommended Movie: {title}")
    print(f"Overview: {overview}")

# Run the recommendation system
if __name__ == "__main__":
    recommend_movie()
