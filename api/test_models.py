from database import SessionLocal

from models import Movie, Rating, Tag, Link

db = SessionLocal()

## tester la recupération des films
movies = db.query(Movie).limit(10).all()

if movies:
    for movie in movies:
        print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")

else:
    print("No movies found.")


# recuperer les film du genre action 

action_movies = db.query(Movie).filter(Movie.genres.like('%Action%')).limit(10).all()

if action_movies:
    for movie in action_movies:
        print(f"Action Movie ID: {movie.movieId}, Title: {movie.title}, Genres: {movie.genres}")
else:
    print("No action movies found.")

# tester la recupertion de quelques evaluations qui est representé par la table ratings
ratings = db.query(Rating).limit(10).all()

if ratings:
    for rating in ratings:
        print(
            f"User ID: {rating.userId}, "
            f"Movie ID: {rating.movieId}, "
            f"Rating: {rating.rating}, "
            f"Timestamp: {rating.timestamp}"
        )
else:
    print("No ratings found.")


high_ratings = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4.5)
    .limit(10)
    .all()
)

if high_ratings:
    for title, rating in high_ratings:
        print(title, rating)
else:
    print("No high rated movies found.")



high_rated_movies = (
    db.query(Movie.title, Rating.rating)
    .join(Rating)
    .filter(Rating.rating >= 4.5)
    .with_entities(Movie.title, Rating.rating)
    .limit(10)
    .all()
)   

if high_rated_movies:
    for title, rating in high_rated_movies:
        print(f"Title: {title}, Rating: {rating}")
else:
    print("No high rated movies found.")



# autre façon de recuperer les films les mieux notés
high_rated_movies_v2 = (
    db.query(Movie)
    .join(Rating)
    .filter(Rating.rating >= 4.5, Movie.movieId == Rating.movieId)
    .limit(10)
    .all()
)
if high_rated_movies_v2:
    for movie in high_rated_movies_v2:
        print(f"Title: {movie.title}")
else:
    print("No high rated movies found.")    

# recupérer les tags associés aux   films
tags = db.query(Tag).limit(10).all()
if tags:
    for tag in tags:
        print(
            f"User ID: {tag.userId}, "
            f"Movie ID: {tag.movieId}, "
            f"Tag: {tag.tag}, "
            f"Timestamp: {tag.timestamp}"
        )
else:
    print("No tags found.")


# teste de la classe Link
links = db.query(Link).limit(10).all()
if links:
    for link in links:
        print(
            f"Movie ID: {link.movieId}, "
            f"IMDB ID: {link.imdbId}, "
            f"TMDB ID: {link.tmdbId}"
        )
else:
    print("No links found.")    

# fermer la session
db.close()
