# API REST MovieLens - Documentation technique

Une API RESTful performante et complète pour accéder à des données cinéma structurées (films, évaluations, tags, liens externes). Développée avec **FastAPI** et **SQLAlchemy**, elle offre une interface moderne et documentée pour les applications analytics et web.

## Vue d'ensemble

Cette API expose le dataset **MovieLens** via des endpoints RESTful robustes. Conçue pour la scalabilité et la maintenabilité, elle démontre les meilleures pratiques en architecture backend.

### Caractéristiques

- **Framework moderne** : FastAPI avec validation Pydantic v2
- **ORM puissant** : SQLAlchemy pour requêtes complexes et optimisées
- **Documentation interactive** : Swagger UI et ReDoc
- **Gestion d'erreurs cohérente** : Codes HTTP standard et messages explicites
- **Pagination** : Support skip/limit sur tous les endpoints de liste
- **Filtres avancés** : Recherche par titre, genre, utilisateur, etc.
- **Tests unitaires** : Suite de tests pour modèles et requêtes

---

## Installation et démarrage

### Prérequis

- Python 3.12 ou supérieur
- pip

### Installation locale

#### 1. Se placer dans le dossier API

```bash
cd api
```

#### 2. Créer un environnement virtuel (si ce n'est pas déjà fait)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### 3. Installer les dépendances

```bash
pip install -r ../requirements.txt
```

#### 4. Démarrer le serveur

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Sortie attendue :**
```
Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### Accéder à l'API

- **Base URL** : `http://localhost:8000`
- **Swagger UI** : `http://localhost:8000/docs`
- **ReDoc** : `http://localhost:8000/redoc`
- **Health check** : `http://localhost:8000/`

---

## Endpoints disponibles

### Films

| Méthode | Endpoint | Description | Paramètres |
|---------|----------|-------------|-----------|
| GET | `/movies/{movie_id}` | Récupérer un film par ID | `movie_id` (path) |
| GET | `/movies` | Lister les films avec pagination | `skip`, `limit`, `title`, `genre` |

### Évaluations

| Méthode | Endpoint | Description | Paramètres |
|---------|----------|-------------|-----------|
| GET | `/ratings/{user_id}/{movie_id}` | Obtenir l'évaluation d'un utilisateur pour un film | `user_id`, `movie_id` (path) |
| GET | `/ratings` | Lister les évaluations | `skip`, `limit`, `user_id`, `movie_id` |

### Tags

| Méthode | Endpoint | Description | Paramètres |
|---------|----------|-------------|-----------|
| GET | `/tags/{user_id}/{movie_id}/{tag_text}` | Récupérer un tag spécifique | `user_id`, `movie_id`, `tag_text` (path) |
| GET | `/tags` | Lister les tags | `skip`, `limit`, `user_id`, `movie_id` |

### Liens externes

| Méthode | Endpoint | Description | Paramètres |
|---------|----------|-------------|-----------|
| GET | `/links/{movie_id}` | Obtenir les identifiants IMDB/TMDB | `movie_id` (path) |
| GET | `/links` | Lister les liens | `skip`, `limit`, `movie_id` |

### Analytiques

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/analytics` | Statistiques globales de la base |

---

## Exemples d'utilisation

### 1. Vérifier l'état de l'API

```bash
curl -X GET "http://localhost:8000/"
```

**Réponse :**
```json
{"status": "API is running"}
```

### 2. Récupérer un film par ID

```bash
curl -X GET "http://localhost:8000/movies/1"
```

**Réponse :**
```json
{
  "movieId": 1,
  "title": "Toy Story",
  "genres": ["Adventure", "Animation", "Comedy"]
}
```

### 3. Lister les films avec pagination

```bash
curl -X GET "http://localhost:8000/movies?skip=0&limit=5"
```

**Paramètres optionnels :**
- `skip` : Nombre de résultats à sauter (défaut: 0)
- `limit` : Nombre de résultats à retourner (défaut: 100)
- `title` : Filtrer par titre (recherche partielle)
- `genre` : Filtrer par genre

### 4. Récupérer une évaluation utilisateur

```bash
curl -X GET "http://localhost:8000/ratings/1/1"
```

**Réponse :**
```json
{
  "userId": 1,
  "movieId": 1,
  "rating": 4.0,
  "timestamp": "1997-01-20T19:29:47"
}
```

### 5. Lister les évaluations avec filtres

```bash
curl -X GET "http://localhost:8000/ratings?user_id=1&limit=10"
```

### 6. Récupérer les tags d'un film

```bash
curl -X GET "http://localhost:8000/tags?movie_id=1&limit=5"
```

### 7. Statistiques analytiques

```bash
curl -X GET "http://localhost:8000/analytics"
```

**Réponse exemple :**
```json
{
  "total_movies": 10000,
  "total_ratings": 100000,
  "total_users": 610,
  "avg_rating": 3.54
}
```

---

## Exemples avec Python

### Avec httpx

```python
import httpx

# Client
client = httpx.Client(base_url="http://localhost:8000")

# Récupérer un film
response = client.get("/movies/1")
print(response.json())

# Lister les films
response = client.get("/movies", params={"limit": 5})
for movie in response.json():
    print(movie["title"])

# Fermer le client
client.close()
```

### Avec requests

```python
import requests

BASE_URL = "http://localhost:8000"

# Récupérer un film
response = requests.get(f"{BASE_URL}/movies/1")
movie = response.json()
print(f"Film: {movie['title']}")

# Lister les films avec filtrage
response = requests.get(
    f"{BASE_URL}/movies",
    params={"limit": 10, "genre": "Comedy"}
)
movies = response.json()
print(f"Nombre de films: {len(movies)}")
```

---

## Codes d'erreur HTTP

| Code | Description | Exemple |
|------|-------------|---------|
| 200 | Succès | Film trouvé et retourné |
| 400 | Requête invalide | Paramètres manquants ou invalides |
| 404 | Ressource introuvable | Film/évaluation n'existe pas |
| 422 | Entité non processable | Type de données invalide |
| 500 | Erreur serveur | Erreur base de données |

---

## Gestion des erreurs

Toutes les erreurs retournent une réponse JSON structurée :

```json
{
  "detail": "Movie with ID 999999 not found"
}
```

### Exemple de gestion d'erreur en Python

```python
import httpx

try:
    response = httpx.get("http://localhost:8000/movies/999999")
    response.raise_for_status()  # Lève une exception si code >= 400
    movie = response.json()
except httpx.HTTPStatusError as e:
    print(f"Erreur {e.response.status_code}: {e.response.json()['detail']}")
```

---

## Architecture technique

### Structure du code

```
api/
├── main.py              # Application FastAPI et endpoints
├── database.py          # Configuration SQLAlchemy, SessionLocal
├── models.py            # Modèles ORM (Movie, Rating, Tag, Link)
├── schemas.py           # Schémas Pydantic (requêtes/réponses)
├── query_helpers.py     # Fonctions de requête réutilisables
├── test_models.py       # Tests unitaires modèles
├── test_query_helper.py # Tests unitaires query helpers
└── movies.db            # Base de données SQLite
```

### Modèles de données

- **Movie** : Films avec titre et genres
- **Rating** : Évaluations utilisateurs (1-5 stars)
- **Tag** : Tags appliqués par utilisateurs aux films
- **Link** : Identifiants IMDB et TMDB

---

## Tests

Exécuter la suite de tests :

```bash
pytest test_models.py -v
pytest test_query_helper.py -v

# Ou tous les tests
pytest -v
```

---

## Déploiement en production

### Avec Gunicorn

```bash
gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --port 8000
```

### Avec Docker

```bash
docker build -t datatech-api .
docker run -p 8000:8000 datatech-api
```

---

## Performance et optimisation

- **Indexation** : Les modèles ORM incluent les index appropriés
- **Pagination** : Utiliser `skip` et `limit` pour les requêtes volumineuses
- **Caching** : À implémenter selon les cas d'usage
- **Connection pooling** : SQLAlchemy gère automatiquement le pool de connexions

---

## Support

Pour toute question ou problème :
- Consulter la [documentation principale](../README.md)
- Vérifier les [tests](./test_models.py) pour des exemples
- Accéder à Swagger UI pour tester les endpoints
