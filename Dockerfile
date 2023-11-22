#!/bin/bash

# Utiliser une image de base officielle pour Python
FROM python:3.10

# Definir le dossier de travail dans le conteneur
WORKDIR /app

COPY requirements.txt /app/requirements.txt

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source de l'application dans le conteneur
COPY app.py /app/app.py

# Exposer le port que streamlit utilisera
EXPOSE 8501

# Commande à exécuter pour démarrer l'application
CMD ["streamlit", "run", "app.py"]