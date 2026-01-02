# DATATECH 🎬📊

DATATECH est un projet **backend orienté data & analytics** dédié à l’analyse de données liées aux films  
(notes, popularité, genres, performances, etc.).

Le projet combine :
- un **backend Python** (API, services)
- une **couche analytics** pour l’exploration et l’analyse des données cinéma

---

## Objectifs du projet

- Construire une **API backend robuste** pour exposer des données films
- Centraliser et structurer des **données cinéma**
- Réaliser des **analyses statistiques et exploratoires**
- Préparer le terrain pour :
  - dashboards
  - recommandations
  - analyses de tendances

---

## Architecture (prévisionnelle)

```text
DATATECH/
.
├── api
│   ├── database.py
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── movies.db
│   ├── query_helpers.py
│   ├── README.md
│   ├── schemas.py
│   ├── test_models.py
│   └── test_query_helper.py
├── architecture.txt
├── data
│   ├── links.csv
│   ├── movies.csv
│   ├── ratings.csv
│   ├── README.txt
│   └── tags.csv
├── Dockerfile
├── movies.db
├── pooo.py
├── README.md
├── requirements.txt
└── sdk
    ├── dist
    │   ├── filmsapisdk-0.0.2-py3-none-any.whl
    │   └── filmsapisdk-0.0.2.tar.gz
    ├── pyproject.toml
    ├── README.md
    ├── src
    │   └── filmsapisdk
    │       ├── film_client.py
    │       ├── film_config.py
    │       ├── __init__.py
    │       └── schemas
    │           ├── __init__.py
    │           └── modos.py
    └── test_sdk.py
