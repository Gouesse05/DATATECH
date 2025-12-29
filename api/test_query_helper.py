from database import SessionLocal
from query_helpers import *

db = SessionLocal()

movies = get_movies(db, limit=5)
for film in movies:
    print(f"Movie ID: {film.movieId}, Titre: {film.title}, Genres: {film.genres}")   

rating = get_rating(db, user_id=1, movie_id=1)
print(f"Rating - User ID: {rating.userId}, Movie ID: {rating.movieId}, Rating: {rating.rating}")


nombredefilm = get_movie_count(db)
print(f"Nombre total de films dans la base de données: {nombredefilm}")


db.close()