# 🎬 Movielens SDK — `filmsapisdk`

[![PyPI version](https://img.shields.io/pypi/v/filmsapisdk.svg)](https://pypi.org/project/filmsapisdk/)
[![Python version](https://img.shields.io/pypi/pyversions/filmsapisdk.svg)](https://pypi.org/project/filmsapisdk/)
[![License](https://img.shields.io/pypi/l/filmsapisdk.svg)](https://pypi.org/project/filmsapisdk/)

Un SDK Python simple et typé pour interagir avec l’API REST **Movielens**.  
Conçu pour les **Data Analysts** et **Data Scientists**, il permet d’accéder facilement aux films, notes, tags et statistiques analytiques.

Le SDK fournit :
- une interface Python claire et cohérente
- des modèles **Pydantic (v2)** pour la validation des données
- des sorties **Pandas DataFrame** prêtes pour l’analyse
- gestion simple des appels HTTP

---

## PyPI

Package officiel :  
https://pypi.org/project/filmsapisdk/

---

## Installation

```bash
pip install filmsapisdk

```
## Configuration 




``` python

from filmsapisdk import MovieClient, MovieConfig

# Configuration avec l'url de l'API (Render)
config = MovieConfig(movie_base_url="https://datatech.onrender.com")
client = MovieClient(config=config)
```

## Tester le SDK

# 1. Health check pour vérifier que l'API est joignable

``` python
health = client.health_check()
print("Health check :", health)
```
# 2 Récupérer un film détaillé

``` python
movie = client.get_movie(movie_id=1)
print("Film détaillé :", movie)
```
# 3 Lister les 5 premiers films (format Pydantic)

``` python
movies_list = client.list_movies(limit=5, output_format="pydantic")
print("Liste des films (Pydantic) :", movies_list)
```
# 4 Lister les 5 premiers films (format Pandas DataFrame)
``` python
movies_df = client.list_movies(limit=5, output_format="pandas")
print("Liste des films (DataFrame) :")
print(movies_df.head())
```
# Récupérer une note
``` python
rating = client.get_rating(user_id=1, movie_id=1)
print("Note :", rating)
```
# Lister les notes en DataFrame
``` python
ratings_df = client.list_ratings(limit=10, output_format="pandas")
print("Notes DataFrame :")
print(ratings_df.head())
```
# Récupérer un tag
``` python
tag = client.get_tag(user_id=1, movie_id=1, tag_text="classic")
print("Tag :", tag)
```
# Lister les tags (Pydantic)
``` python
tags_list = client.list_tags(limit=5, output_format="pydantic")
print("Tags :", tags_list)
```
# Récupérer un lien
``` python
link = client.get_link(movie_id=1)
print("Lien :", link)
```
# Lister les liens en DataFrame
``` python
links_df = client.list_links(limit=5, output_format="pandas")
print("Liens DataFrame :")
print(links_df.head())
```
# Analytics
``` python
analytics = client.get_analytics()
print("Analytics :", analytics)
```

## Tester en local 
Vous pouvez aussi tester l'API en local:

```python
config = MovieConfig(movie_base_url="http://localhost:8000")
client = MovieClient(config=config)

```

## Public cible 

- Data Analysts
- Data Scientists
- Étudiants et Curieux en Data


## Liens utiles

- API Render : [https://datatech.onrender.com](https://datatech.onrender.com)
- PypI : [https://pypi.org/project/filmsapisdk/](https://pypi.org/project/filmsapisdk/)
