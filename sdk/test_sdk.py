from filmsapisdk import MovieClient, MovieConfig
import pandas as pd


# Initialisation du client avec l'URL de l'API
config = MovieConfig(movie_base_url="https://datatech.onrender.com")
client = MovieClient(config=config)


def main():
    print("=== HEALTH CHECK ===")
    try:
        health = client.health_check()
        print(health)
    except Exception as e:
        print("Health check failed:", e)

    print("\n=== LIST MOVIES (PYDANTIC) ===")
    try:
        movies = client.list_movies(limit=5)
        print(movies)
        print(type(movies[0]))
    except Exception as e:
        print("List movies (pydantic) failed:", e)

    print("\n=== LIST MOVIES (DICT) ===")
    try:
        movies_dict = client.list_movies(limit=5, output_format="dict")
        print(movies_dict)
        print(type(movies_dict[0]))
    except Exception as e:
        print("List movies (dict) failed:", e)

    print("\n=== LIST MOVIES (PANDAS) ===")
    try:
        movies_df = client.list_movies(limit=5, output_format="pandas")
        print(movies_df.head())
        print(type(movies_df))
    except Exception as e:
        print("List movies (pandas) failed:", e)

    print("\n=== GET MOVIE ===")
    try:
        movie = client.get_movie(movie_id=1)
        print(movie)
        print(type(movie))
    except Exception as e:
        print("Get movie failed:", e)

    print("\n=== LIST RATINGS (PANDAS) ===")
    try:
        ratings_df = client.list_ratings(limit=5, output_format="pandas")
        print(ratings_df.head())
    except Exception as e:
        print("List ratings failed:", e)

    print("\n=== LIST TAGS (DICT) ===")
    try:
        tags = client.list_tags(limit=5, output_format="dict")
        print(tags)
    except Exception as e:
        print("List tags failed:", e)

    print("\n=== LIST LINKS (PYDANTIC) ===")
    try:
        links = client.list_links(limit=5)
        print(links)
    except Exception as e:
        print("List links failed:", e)

    print("\n=== ANALYTICS ===")
    try:
        analytics = client.get_analytics()
        print(analytics)
    except Exception as e:
        print("Analytics failed:", e)


if __name__ == "__main__":
    main()
