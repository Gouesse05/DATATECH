# DATATECH - Backend API REST pour l'Analyse de Données Cinéma

DATATECH est une **plateforme backend complète** conçue pour exposer et analyser des données cinéma à grande échelle. Le projet combine une **API REST performante** basée sur FastAPI, une **couche data** structurée avec SQLAlchemy, et un **SDK Python réutilisable** pour une intégration client fluide.

## Vue d'ensemble

Le projet démontre une architecture **production-ready** avec :
- **API REST** exposant des endpoints pour films, évaluations, tags et liens externes
- **Base de données** SQLite avec ORM SQLAlchemy pour la persistance
- **Validation de données** via Pydantic v2
- **SDK Python** packagé et distribué sur PyPI
- **Tests unitaires** pour assurer la qualité du code
- **Containerisation Docker** pour le déploiement

### Cas d'usage

- Intégration de données cinéma dans des applications web/mobile
- Pipelines analytics pour l'exploration de données MovieLens
- Systèmes de recommandation basés sur les évaluations utilisateurs
- Dashboards et visualisations de données cinéma

---

## Architecture

### Structure du projet

```
DATATECH/
├── api/                          # Backend FastAPI
│   ├── main.py                  # Application principale
│   ├── database.py              # Configuration SQLAlchemy et session
│   ├── models.py                # Modèles ORM SQLAlchemy
│   ├── schemas.py               # Schémas de requête/réponse Pydantic
│   ├── query_helpers.py         # Requêtes réutilisables
│   ├── test_models.py           # Tests unitaires modèles
│   ├── test_query_helper.py     # Tests unitaires query helpers
│   └── movies.db                # Base de données SQLite
│
├── sdk/                          # Client Python (SDK)
│   ├── src/filmsapisdk/
│   │   ├── film_client.py       # Classe client HTTP
│   │   ├── film_config.py       # Configuration du client
│   │   └── schemas/             # Modèles Pydantic partagés
│   ├── pyproject.toml           # Metadata du package
│   ├── test_sdk.py              # Tests SDK
│   └── dist/                    # Distributions packagées
│
├── data/                         # Datasets CSV
│   ├── movies.csv               # 10k films avec titres, genres
│   ├── ratings.csv              # Évaluations utilisateurs
│   ├── tags.csv                 # Tags appliqués aux films
│   └── links.csv                # Identifiants IMDB/TMDB
│
├── Dockerfile                    # Configuration pour déploiement
├── requirements.txt              # Dépendances Python
└── README.md                     # Ce fichier
```

### Stack technologique

| Composant | Technologie | Version |
|-----------|-------------|---------|
| Framework Web | FastAPI | 0.127+ |
| ORM | SQLAlchemy | 2.0+ |
| Base de données | SQLite | - |
| Validation | Pydantic | 2.12+ |
| Client HTTP | httpx | 0.24+ |
| Serveur ASGI | Uvicorn | 0.23+ |
| Serveur production | Gunicorn | 23.0+ |

---

## Installation et démarrage

### Prérequis

- Python 3.12 ou supérieur
- pip ou uv (gestionnaire de packages)
- (Optionnel) Docker

### Installation locale

#### 1. Cloner le dépôt

```bash
git clone https://github.com/Gouesse05/DATATECH.git
cd DATATECH
```

#### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

#### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

#### 4. Démarrer l'API

```bash
cd api
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

L'API sera accessible à : `http://localhost:8000`

**Documentation interactive (Swagger UI)** : `http://localhost:8000/docs`

---

## Déploiement Docker

```bash
docker build -t datatech-api .
docker run -p 8000:8000 datatech-api
```

---

## Utilisation rapide

### Avec l'API directement

```bash
curl -X GET "http://localhost:8000/movies?limit=5"
```

### Avec le SDK Python

```python
from filmsapisdk import MovieClient, MovieConfig

# Configuration
config = MovieConfig(movie_base_url="http://localhost:8000")
client = MovieClient(config=config)

# Récupérer un film
movie = client.get_movie(1)
print(f"Film: {movie.title}")

# Lister les films
movies = client.list_movies(limit=10, output_format="pandas")
print(movies)
```

Pour plus de détails, consultez :
- **[API - Guide complet](./api/README.md)**
- **[SDK - Documentation Python](./sdk/README.md)**

---

## Fonctionnalités principales

- GET `/movies/{id}` - Récupérer un film par ID
- GET `/movies` - Lister les films avec pagination et filtres
- GET `/ratings` - Accéder aux évaluations des utilisateurs
- GET `/tags` - Consulter les tags appliqués aux films
- GET `/links/{id}` - Obtenir les identifiants IMDB/TMDB
- GET `/analytics` - Statistiques globales de la base

---

## Tests

### Tests API

```bash
cd api
pytest test_models.py -v
pytest test_query_helper.py -v
```

### Tests SDK

```bash
cd sdk
pytest test_sdk.py -v
```

---

## Architecture et design patterns

### API REST (FastAPI)

- **Endpoints RESTful** conformes aux conventions HTTP
- **Dépendance d'injection** pour la gestion des sessions DB
- **Pydantic** pour la validation et la sérialisation
- **HTTPException** pour la gestion d'erreurs cohérente

### Accès aux données (SQLAlchemy)

- **ORM** pour l'abstraction de la base de données
- **Sessions** gérées automatiquement par dépendance
- **Queries réutilisables** dans `query_helpers.py`

### Client SDK (httpx)

- **Client typé** avec support Pydantic, Dict et Pandas DataFrame
- **Gestion d'erreurs** et validation côté client
- **Configuration centralisée** pour adapter l'URL de l'API

---

## Contribution

Les contributions sont bienvenues. Pour contribuer :

1. **Fork** le dépôt
2. **Créer une branche** : `git checkout -b feature/nouvelle-fonctionnalite`
3. **Committer vos changements** : `git commit -m "Ajouter nouvelle fonctionnalité"`
4. **Pousser la branche** : `git push origin feature/nouvelle-fonctionnalite`
5. **Ouvrir une Pull Request**

### Directives de contribution

- Respecter le style de code existant (PEP 8)
- Ajouter des tests pour toute nouvelle fonctionnalité
- Mettre à jour la documentation
- Assurer la compatibilité avec Python 3.12+

---

## Licence

Ce projet est sous licence MIT. Voir [LICENSE](./LICENSE) pour plus de détails.

---

## Support et ressources

- **Documentation FastAPI** : https://fastapi.tiangolo.com/
- **Documentation SQLAlchemy** : https://docs.sqlalchemy.org/
- **Dataset MovieLens** : https://grouplens.org/datasets/movielens/
- **Pydantic** : https://docs.pydantic.dev/

---

## Auteur

**Gouesse05** - Développeur backend, data engineering
