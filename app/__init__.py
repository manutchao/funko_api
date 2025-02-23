# app/__init__.py
from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)  # Initialisation de MongoDB avant d'importer les routes

    from app.routes import api  # Importation différée pour éviter l'import circulaire
    app.register_blueprint(api)

    return app