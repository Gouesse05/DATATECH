# Movielens API

Bienvenue dans l'API **MovieLens** - une API RESTful dévéloppée avec **FastAPI** pour explorer la base de données Mobielens.
Elle vous permet d'interroger des informations sur les films, les évaluations, les utilisateurs, les tags et les liens vers bases de données externes(IMDB et TMDB)


## Fonctionnalités principales

- Recherche de films par titre, genre, ou ID
- Consulattions des évaluations par utilisateur et par film
- Gestion des tags associés aux films
- Récuperation des identifiants IMDB / TMDB
- Statistiques globales de la base


---

## Prérequis

- Python >= 3.12
- Un client HTTP comme 'httpx' ou 'requests'

Installation rapide de 'httpx'

```bash
pip install httpx
```
## Démarrer avec l'API

L'API est accessible à l'adresse suivant :

```
http://localhost:8000
```
L'interface swagger est disponible ici:

```
http://localhost:8000/docs
```

## Endpoint essentiels

| Méthode | URL                                     | Description                                    |
| ------- | --------------------------------------- | ---------------------------------------------- |
| GET     | `/`                                     | Vérification de l’état de l’API                |
| GET     | `/movies/{movie_id}`                    | Obtenir un film par son ID                     |
| GET     | `/movies`                               | Lister les films                               |
| GET     | `/ratings/{user_id}/{movie_id}`         | Obtenir une évaluation par utilisateur et film |
| GET     | `/ratings`                              | Lister les évaluations                         |
| GET     | `/tags/{user_id}/{movie_id}/{tag_text}` | Obtenir un tag spécifique                      |
| GET     | `/tags`                                 | Lister les tags                                |
| GET     | `/links/{movie_id}`                     | Obtenir le lien d’un film                      |
| GET     | `/links`                                | Lister les liens des films                     |
| GET     | `/analytics`                            | Obtenir les statistiques analytiques           |



## Exemples d'utilisation avec httpx

### Listes des films

```python
import httox

reponse = httpx.get("http://localhost:8000/movies", params={"limit": 5})
print(response.json())
```

### Obtenir un film par son ID

```python
import httpx

movie_id = 1
response = httpx.get(f"http://localhost:8000/movies/{movie_id}")

print(response.json())
```

### Lister les évaluations
```python
import httpx

response = httpx.get(
    "http://localhost:8000/ratings",
    params={"limit": 5}
)

print(response.json())

```

### Lister les tags d’un film
```python
import httpx

response = httpx.get(
    "http://localhost:8000/tags",
    params={"movie_id": 1, "limit": 5}
)

print(response.json())
```

### Obtenir les liens IMDB / TMDB d’un film
```python
import httpx

movie_id = 1
response = httpx.get(f"http://localhost:8000/links/{movie_id}")

print(response.json())
```

### Obtenir les statistiques analytiques
```python
import httpx

response = httpx.get("http://localhost:8000/analytics")

print(response.json())
```

## Conditions d'utilisation

- Cette API est conçue à des fins experimentales,
- Merci de ne pas effectuer d'appels massifs sans contrôle de frequence (rate-limiting non implementé pour l'instant),
- Vous pouvez l'integrer à des notebooks, applications ou projets de dataviz pour visualiser les données de Movilens.

## Contirbuer

Les contributions sont les bienvenue!
- Corriger des bugs
- Améliorer les performances des requêtes
- Ajout de nouveaux endpoints
- Rendre l'API disponible sur un hebergeur public

## Ressources utiles

- Swagger UI: http:/localhost:8000:docs
- Documentation technique : disponible via Swagger
- Base de données MovieLens : https://grouplens.org/datasets/movielens/

