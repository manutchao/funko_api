# Utilisation de l'image Python officielle
FROM python:3.9

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers nécessaires
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exposition du port Flask
EXPOSE 5000

# Commande pour exécuter l'application
CMD ["python", "run.py"]