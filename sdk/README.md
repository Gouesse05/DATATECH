# FilmsAPISDK - Client Python pour MovieLens API

Un SDK Python entièrement typé et documenté pour consommer l'API REST MovieLens. Conçu pour les développeurs, data analysts et data scientists, il offre une interface Python idiomatique avec support multi-formats de sortie.

[![PyPI version](https://img.shields.io/pypi/v/filmsapisdk.svg)](https://pypi.org/project/filmsapisdk/)
[![Python version](https://img.shields.io/pypi/pyversions/filmsapisdk.svg)](https://pypi.org/project/filmsapisdk/)

## Vue d'ensemble

Le SDK fournit une abstraction simple et performante pour accéder aux données films, évaluations, tags et statistiques via l'API MovieLens. Il gère automatiquement la validation, la sérialisation et les appels HTTP.

### Fonctionnalités

- **Types Python** : Annotations complètes et support Pydantic v2
- **Multi-format** : Retour en objets Pydantic, dictionnaires ou DataFrames pandas
- **Configuration flexible** : URL d'API configurable (local ou cloud)
- **Gestion d'erreurs** : Exceptions structurées et messages informatifs
- **Tests inclus** : Suite de tests pour validation intégration
- **Documentation** : Docstrings complètes et exemples concrets

---

## Installation

### Via PyPI (recommandé)

```bash
pip install filmsapisdk
```

### Installation en développement (local)

```bash
cd sdk
pip install -e .
```

Cela installe le package en mode éditable, utile pour tester des modifications locales.

---

## Configuration rapide

### Configuration par défaut (local)

```python
from filmsapisdk import MovieClient

# Connexion à l'API locale (http://localhost:8000)
client = MovieClient()
```

### Configuration personnalisée

```python
from filmsapisdk import MovieClient, MovieConfig

# Connexion à une API distante (par exemple sur Render)
config = MovieConfig(movie_base_url="https://datatech.onrender.com")
client = MovieClient(config=config)

# Ou avec variables d'environnement
import os
api_url = os.getenv("MOVIES_API_URL", "http://localhost:8000")
config = MovieConfig(movie_base_url=api_url)
client = MovieClient(config=config)
```

---

## Utilisation - Exemples complets

### 1. Health Check - Vérifier la connexion

```python
from filmsapisdk import MovieClient

client = MovieClient()

try:
    status = client.health_check()
    print(f"API Status: {status}")  # {'status': 'API is running'}
except Exception as e:
    print(f"Erreur: {e}")
```

### 2. Récupérer un film détaillé

```python
from filmsapisdk import MovieClient

client = MovieClient()

# Retourner un objet Pydantic typé
movie = client.get_movie(movie_id=1)
print(f"Titre: {movie.title}")
print(f"Genres: {movie.genres}")
print(f"ID IMDB: {movie.imdbId}")
```

### 3. Lister les films

#### Format Pydantic (objets typés)

```python
movies = client.list_movies(limit=5, output_format="pydantic")

for movie in movies:
    print(f"{movie.movieId}: {movie.title}")
```

#### Format dictionnaire (sérialisation JSON)

```python
movies_dict = client.list_movies(limit=5, output_format="dict")

for movie in movies_dict:
    print(movie)
    # {'movieId': 1, 'title': 'Toy Story', 'genres': [...]}
```

#### Format Pandas DataFrame (analyse de données)

```python
import pandas as pd

movies_df = client.list_movies(limit=100, output_format="pandas")

# Analyse rapide
print(movies_df.head())
print(f"Nombre de films: {len(movies_df)}")
print(f"Genres uniques: {movies_df['genres'].nunique()}")

# Filtrer et exporter
action_movies = movies_df[movies_df['genres'].str.contains('Action', na=False)]
action_movies.to_csv('action_movies.csv', index=False)
```

### 4. Filtrer les films

```python
# Par titre
movies = client.list_movies(
    title="Toy",
    limit=10,
    output_format="pandas"
)
print(f"Films contenant 'Toy': {len(movies)}")

# Par genre
movies = client.list_movies(
    genre="Comedy",
    limit=10,
    output_format="pandas"
)
print(f"Comédies trouvées: {len(movies)}")
```

### 5. Gérer les évaluations

#### Récupérer une évaluation spécifique

```python
# Récupérer la note de l'utilisateur 1 pour le film 1
rating = client.get_rating(user_id=1, movie_id=1)
print(f"Note: {rating.rating}/5 ({rating.timestamp})")
```

#### Lister les évaluations

```python
# Toutes les notes (paginer pour les requêtes volumineuses)
ratings = client.list_ratings(limit=100, output_format="pandas")

# Notes d'un utilisateur spécifique
user_ratings = client.list_ratings(
    user_id=1,
    output_format="pandas"
)
print(f"Notes de l'utilisateur 1: {len(user_ratings)}")

# Statistiques
print(f"Moyenne des notes: {user_ratings['rating'].mean():.2f}")
print(f"Note max: {user_ratings['rating'].max()}")
print(f"Note min: {user_ratings['rating'].min()}")
```

### 6. Gérer les tags

#### Récupérer un tag spécifique

```python
tag = client.get_tag(
    user_id=1,
    movie_id=1,
    tag_text="classic"
)
print(f"Tag trouvé: {tag}")
```

#### Lister les tags

```python
# Tags d'un film
film_tags = client.list_tags(
    movie_id=1,
    output_format="pandas"
)
print(f"Tags du film 1: {film_tags}")

# Tags d'un utilisateur
user_tags = client.list_tags(
    user_id=1,
    limit=20,
    output_format="pandas"
)
print(f"Tags appliqués par l'utilisateur 1:")
print(user_tags)
```

### 7. Récupérer les liens externes

```python
# Lien d'un film
link = client.get_link(movie_id=1)
print(f"IMDB ID: {link.imdbId}")
print(f"TMDB ID: {link.tmdbId}")

# Tous les liens
links = client.list_links(limit=50, output_format="pandas")
print(links)
```

### 8. Statistiques analytiques

```python
analytics = client.get_analytics()

print(f"Total de films: {analytics['total_movies']}")
print(f"Total d'utilisateurs: {analytics['total_users']}")
print(f"Total d'évaluations: {analytics['total_ratings']}")
print(f"Moyenne des notes: {analytics['avg_rating']:.2f}")
```

---

## Formats de sortie

Le SDK supporte trois formats de sortie :

| Format | Usage | Exemple |
|--------|-------|---------|
| `pydantic` | Objets typés, validation automatique | `client.list_movies(output_format="pydantic")` |
| `dict` | Dictionnaires Python (sérialisation JSON) | `client.list_movies(output_format="dict")` |
| `pandas` | DataFrames pandas pour analytics | `client.list_movies(output_format="pandas")` |

---

## Gestion des erreurs

Le SDK lève des exceptions explicites en cas de problème :

```python
from filmsapisdk import MovieClient
import httpx

client = MovieClient()

try:
    # Film inexistant
    movie = client.get_movie(movie_id=999999)
except httpx.HTTPStatusError as e:
    if e.response.status_code == 404:
        print("Film non trouvé")
    else:
        print(f"Erreur API: {e.response.status_code}")
except httpx.RequestError as e:
    print(f"Erreur de connexion: {e}")
```

### Codes d'erreur courants

| Code | Cause | Solution |
|------|-------|----------|
| 404 | Ressource introuvable | Vérifier l'ID du film/utilisateur |
| 422 | Paramètres invalides | Consulter la validation Pydantic |
| 500 | Erreur serveur | Vérifier que l'API est accessible |
| Network error | API inaccessible | Vérifier l'URL et la connectivité |

---

## Paramètres de pagination

Tous les endpoints de liste supportent la pagination :

```python
# Skip et limit
movies = client.list_movies(
    skip=0,      # Sauter les N premiers résultats
    limit=50,    # Nombre maximum de résultats
    output_format="pandas"
)

# Paginer sur plusieurs appels
all_movies = []
skip = 0
while True:
    batch = client.list_movies(skip=skip, limit=100, output_format="dict")
    if not batch:
        break
    all_movies.extend(batch)
    skip += 100

print(f"Total: {len(all_movies)} films")
```

---

## Cas d'usage avancés

### Export de données complètes

```python
import pandas as pd

# Récupérer tous les films et notes
movies = client.list_movies(limit=10000, output_format="pandas")
ratings = client.list_ratings(limit=100000, output_format="pandas")

# Fusion sur movie_id
merged = movies.merge(
    ratings,
    left_on='movieId',
    right_on='movieId',
    how='left'
)

# Export
merged.to_csv('movies_with_ratings.csv', index=False)
```

### Analyse de tendances

```python
import pandas as pd

ratings = client.list_ratings(limit=50000, output_format="pandas")

# Note moyenne par film
avg_by_movie = ratings.groupby('movieId')['rating'].agg(['mean', 'count'])
avg_by_movie = avg_by_movie[avg_by_movie['count'] >= 10]  # Films avec 10+ notes
avg_by_movie = avg_by_movie.sort_values('mean', ascending=False)

print("Top 10 films les mieux notés:")
print(avg_by_movie.head(10))
```

### Intégration dans une application web

```python
from filmsapisdk import MovieClient
from flask import Flask, jsonify

app = Flask(__name__)
client = MovieClient(movie_base_url="https://api.example.com")

@app.route('/api/movies')
def list_movies():
    movies = client.list_movies(limit=100, output_format="dict")
    return jsonify(movies)

@app.route('/api/movies/<int:movie_id>')
def get_movie(movie_id):
    try:
        movie = client.get_movie(movie_id)
        return jsonify(movie.dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 404
```

---

## Tests

Exécuter la suite de tests du SDK :

```bash
cd sdk
pytest test_sdk.py -v
```

### Tests unitaires incluent

- Vérification des connexions
- Validation des formats de sortie
- Gestion des erreurs
- Sérialisation/désérialisation Pydantic
- Conversion en DataFrames pandas

---

## Support et ressources

- **Dépôt principal** : [DATATECH](../README.md)
- **API REST** : [Documentation API](../api/README.md)
- **Pydantic** : https://docs.pydantic.dev/
- **Pandas** : https://pandas.pydata.org/
- **httpx** : https://www.python-httpx.org/

---

## Versioning

Le SDK suit [Semantic Versioning](https://semver.org/) :
- Version actuelle : 0.0.2
- Compatible Python 3.8+
