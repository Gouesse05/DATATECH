from fastapi import FastAPI, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from typing import List, Optional

from .database import SessionLocal, engine
from . import query_helpers as helpers
from . import schemas



api_description = """
Bienvenue dans l'API **MovieLens**

Cette API permet d'interagir avec une base de données inspirée du célèbre
jeu de données [MovieLens](https://grouplens.org/datasets/movielens/).
Elle est idéale pour découvrir comment consommer une API REST avec des
données de films, d'utilisateurs, d'évaluations, de tags et de liens
externes (IMDB, TMDB).



### Fonctionnalités disponibles :

- Rechercher un film par ID, ou lister tous les films
- Consulter les évaluations (ratings) par utilisateur et/ou film
- Accéder aux tags appliqués par les utilisateurs sur les films
- Obtenir les liens IMDB / TMDB pour un film
- Voir des statistiques globales sur la base

Tous les endpoints supportent la pagination (`skip`, `limit`) et des
filtres optionnels selon les cas.

### Bon à savoir
- Vous pouvez tester tous les endpoints directement via l'interface Swagger
ci-dessous.
- Pour toute erreur (ex : ID inexistant), une réponse claire est retournée
avec le bon code HTTP.

"""

# Initialisation de l'application FastAPI
app = FastAPI(
    title="MovieLens API",
    description=api_description, version="0.1"
)
# dependance pour obtenir une session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes pour les films, Endpoints pour tester la santé de l'API
@app.get(
    "/",
    summary="Vérification de l'état de l'API",
    description="Verifie que l'API fonctionne correctement", 
    response_description="Statut de l'API", 
    operation_id="check_api_status",
    tags=["Monitoring"]
    
    )

async def root():
    return {"Message": "API MovieLens est opérationnelle!"}


# Endpoint pour obtenir un film par son ID
@app.get(
    "/movies/{movie_id}",
    summary="Obtenir un film par son ID",
    description="Récupère les détails d'un film en utilisant son ID unique `movie_id`.",
    response_model=schemas.MovieDetailed,
    tags=["Films"],
)
def read_movie(
    movie_id: int = Path(..., description="L'ID unique du film à récupérer"),
    db: Session = Depends(get_db)
):
    movie = helpers.get_movie(db, movie_id)

    if movie is None:
        raise HTTPException(status_code=404, detail="Film non trouvé")

    return movie

# Endpoint pour obtenir une liste de films avec (avec pagination et filtres optionnels title, genres, skip, limit)
@app.get(
    "/movies",
    summary="Lister des films",
    description="Récupère une liste de films avec pagination et filtres optionnels par titre ou genre.",
    response_description="Liste des films",
    response_model=List[schemas.MovieSimple],
    tags=["Films"],
)
def list_movies(
    skip: int = Query(0, ge=0, description="Nombre de films à ignorer pour la pagination"),
    limit: int = Query(100, le=1000, description="Nombre maximum de films à récupérer"),
    title: str = Query(None, description="Filtre par titre de film"),
    genres: str = Query(None, description="Filtre par genre de film"),
    db: Session = Depends(get_db)
):
    movies = helpers.get_movies(db, skip=skip, limit=limit, title=title, genres=genres)
    return movies

# Endpoint pour obtenir une évaluation par utilisateur et film
@app.get(
    "/ratings/{user_id}/{movie_id}",
    summary="Obtenir une évaluation par utilisateur et film",
    description="Récupère une évaluation spécifique donnée par un utilisateur pour un film particulier.",
    response_description="Détails de l'évaluation",     
    response_model=schemas.RatingSimple,
    tags=["Évaluations"],
)

def read_rating(
    user_id: int = Path(..., description="L'ID unique de l'utilisateur"),
    movie_id: int = Path(..., description="L'ID unique du film"),
    db: Session = Depends(get_db)
):
    rating = helpers.get_rating(db, user_id, movie_id)

    if rating is None:
        raise HTTPException(status_code=404, 
                            detail=f"Aucune évaluation trouvée pour l'utilisateur {user_id} et le film {movie_id}")

    return rating

# Endpoint pour obtenir une liste d'évaluations avec filtres optionnels
@app.get(
    "/ratings",
    summary="Lister des évaluations",
    description="Récupère une liste d'évaluations avec des filtres optionnels.",
    response_description="Liste des évaluations",
    response_model=List[schemas.RatingSimple],
    tags=["Évaluations"],
)
def list_ratings(
    skip: int = Query(0, ge=0, description="Nombre d'évaluations à ignorer pour la pagination"),
    limit: int = Query(100, le=1000, description="Nombre maximum d'évaluations à récupérer"),
    movies_id: int = Query(None, description="Filtre par ID de film"),
    user_id: int = Query(None, description="Filtre par ID d'utilisateur"),
    min_rating: float = Query(None, ge=0.0, le=5.0, description="Filtre par note minimale"),
    max_rating: float = Query(None, ge=0.0, le=5.0, description="Filtre par note maximale"),
    db: Session = Depends(get_db)
):
    ratings = helpers.get_ratings(
        db,
        skip=skip,
        limit=limit,
        movies_id=movies_id,
        user_id=user_id,
        min_rating=min_rating,
        max_rating=max_rating
    )
    return ratings

# Endpoint pour retourner un tag pour un utilisateur et un film donnés
# avec le texte du tag
@app.get(
    "/tags/{user_id}/{movie_id}/{tag_text}",
    summary="Obtenir un tag spécifique",
    description=(
        "Retourne un tag pour un utilisateur et un film donnés, "
        "avec le texte du tag."
    ),
    response_model=schemas.TagSimple,
    tags=["tags"],
)
def read_tag(
    user_id: int = Path(..., description="ID de l'utilisateur"),
    movie_id: int = Path(..., description="ID du film"),
    tag_text: str = Path(..., description="Contenu exact du tag"),
    db: Session = Depends(get_db),
):
    result = helpers.get_tag(
        db,
        user_id=user_id,
        movie_id=movie_id,
        tag_text=tag_text,
    )
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=(
                f"Tag non trouvé pour l'utilisateur {user_id}, "
                f"le film {movie_id} et le tag '{tag_text}'"
            ),
        )
    return result


# Endpoint pour lister les tags
@app.get(
    "/tags",
    summary="Lister les tags",
    description=(
        "Retourne une liste de tags avec pagination et filtres "
        "facultatifs par utilisateur ou film."
    ),
    response_model=List[schemas.TagSimple],
    tags=["tags"],
)
def list_tags(
    skip: int = Query(0, ge=0, description="Nombre de résultats à ignorer"),
    limit: int = Query(
        100, le=1000, description="Nombre maximal de résultats à retourner"
    ),
    movie_id: Optional[int] = Query(None, description="Filtrer par ID de film"),
    user_id: Optional[int] = Query(None, description="Filtrer par ID d'utilisateur"),
    db: Session = Depends(get_db),
):
    return helpers.get_tags(
        db,
        skip=skip,
        limit=limit,
        movie_id=movie_id,
        user_id=user_id,
    )


# Endpoint pour retourner les identifiants IMDB et TMDB pour un film donné
@app.get(
    "/links/{movie_id}",
    summary="Obtenir le lien d'un film",
    description="Retourne les identifiants IMDB et TMDB pour un film donné.",
    response_model=schemas.LinkSimple,
    tags=["links"],
)
def read_link(
    movie_id: int = Path(..., description="ID du film"),
    db: Session = Depends(get_db),
):
    result = helpers.get_link(db, movie_id=movie_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Aucun lien trouvé pour le film avec l'ID {movie_id}",
        )
    return result


# Endpoint pour lister les liens
@app.get(
    "/links",
    summary="Lister les liens des films",
    description=(
        "Retourne une liste paginée des identifiants IMDB et TMDB "
        "de tous les films."
    ),
    response_model=List[schemas.LinkSimple],
    tags=["links"],
)
def list_links(
    skip: int = Query(0, ge=0, description="Nombre de résultats à ignorer"),
    limit: int = Query(
        100, le=1000, description="Nombre maximal de résultats à retourner"
    ),
    db: Session = Depends(get_db),
):
    return helpers.get_links(db, skip=skip, limit=limit)


# Endpoint pour obtenir des statistiques sur la base de données
@app.get(
    "/analytics",
    summary="Obtenir les statistiques analytiques",
    description=
        """Retourne des statistiques analytiques sur la base de données :

        - Nombre total de films
        - Nombre total d'évaluations
        - Nombre total de tags
        - Nombre total de liens vers IMDB et TMDB
        """,
    response_model=schemas.AnalyticsResponse,
    tags=["analytics"],
)
def get_analytics(db: Session = Depends(get_db)):
    movie_count = helpers.get_movie_count(db)
    rating_count = helpers.get_rating_count(db)
    tag_count = helpers.get_tag_count(db)
    link_count = helpers.get_link_count(db)

    return schemas.AnalyticsResponse(
        movie_count=movie_count,
        rating_count=rating_count,
        tag_count=tag_count,
        link_count=link_count,
    )



