# Utilise une image légère de python 3.12 comme base
FROM python:3.12-slim
# Définit le répertoire de travail dans le conteneur
WORKDIR /app
# Copie les fichiers de dépendances dans le répertoire de travail
COPY requirements.txt . 
# Installe les dépendances nécessaires
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# Copie le reste des fichiers de l'application dans le répertoire de travail
COPY . .
# Lannce le serveur Uvicorn pour l'application FastAPI
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

