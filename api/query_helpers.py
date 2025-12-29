from fastapi import FastAPI, Depends, HTTPException, Query, Path
from sqlalchemy.orm import Session
from typing import List, Optional

import models

# Films

def get_movies(db: Session, movie_id: int):
    """Récupère un film par son ID."""
    return db.query(models.Movie).filter(models.Movie.movieId == movie_id).first()

def get_movies(db: Session, skip: int = 0, limit: int = 100, title: str = None, genres: str = None):
    """Récupère une liste de films optionnels."""
    query = db.query(models.Movie)
    
    if title:
        query = query.filter(models.Movie.title.like(f"%{title}%"))
    if genres:
        query = query.filter(models.Movie.genres.like(f"%{genres}%"))
    return query.offset(skip).limit(limit).all()
# Évaluations

def get_rating(db: Session, user_id: int, movie_id: int):
    """Récupère une évaluation par user_id et movie_id."""
    return db.query(models.Rating).filter(
        models.Rating.userId == user_id,
        models.Rating.movieId == movie_id
    ).first()


def get_ratings(db: Session, skip: int = 0, limit: int = 100, movies_id: int = None, user_id: int = None, min_rating: float = None, max_rating: float = None):
    """Récupère une liste d'évaluations avec filtre optionnelles."""
    query = db.query(models.Rating)
    
    if movies_id is not None:
        query = query.filter(models.Rating.movieId == movies_id)
    if user_id is not None:
        query = query.filter(models.Rating.userId == user_id)
    if min_rating is not None:
        query = query.filter(models.Rating.rating >= min_rating)
    if max_rating is not None:
        query = query.filter(models.Rating.rating <= max_rating)
        
    return query.offset(skip).limit(limit).all()

# Tags

def get_tag(db: Session, user_id: int, movie_id: int, tag_text: str):
    """Récupère un tag par user_id, movie_id et tag."""
    return (db.query(models.Tag).filter(
        models.Tag.userId == user_id,
        models.Tag.movieId == movie_id,
        models.Tag.tag == tag_text
    ).first()
)

def get_tags(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        movie_id: Optional[int] = None,
        user_id: Optional[int] = None,
       
    ):
    """Récupère une liste de tags avec filtre optionnelles."""
    query = db.query(models.Tag)
    
    if movie_id is not None:
        query = query.filter(models.Tag.movieId == movie_id)
    if user_id is not None:
        query = query.filter(models.Tag.userId == user_id)
        
    return query.offset(skip).limit(limit).all()

# Links

def get_link(db: Session, movie_id: int):
    """Reourne le lien IMDB et TMDB associé à un film donné."""
    return db.query(models.Link).filter(models.Link.movieId == movie_id).first()

def get_links(db: Session, skip: int = 0, limit: int = 100):
    """Récupère une liste paginée de liens IMDB et TMDB de films."""
    return db.query(models.Link).offset(skip).limit(limit).all()

# Requetes analytiques

def get_movie_count(db: Session) -> int:
    """Retourne le nombre total de films dans la base de données."""
    return db.query(models.Movie).count()

def get_rating_count(db: Session) -> int:
    """Retourne le nombre total d'évaluations dans la base de données."""
    return db.query(models.Rating).count()

def get_tag_count(db: Session) -> int:
    """Retourne le nombre total de tags dans la base de données."""
    return db.query(models.Tag).count()

def get_link_count(db: Session) -> int:
    """Retourne le nombre total de liens dans la base de données."""
    return db.query(models.Link).count()

 