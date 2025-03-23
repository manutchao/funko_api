import logging
from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config

logger = logging.getLogger(__name__)


# Initialisation de l'extension MongoDB
mongo = PyMongo()

def create_app():
    """Factory function pour créer une instance de l'application Flask."""
    app = Flask(__name__)
    
    # Charger la configuration depuis config.py
    app.config.from_object(Config)

    # Initialiser MongoDB avec l'application Flask
    mongo.init_app(app)

    logger.info(f"Connected to database: {mongo.db.name}")

    # Importer et enregistrer les blueprints (routes)
    from app.routes.funko_routes import funko_bp
    app.register_blueprint(funko_bp, url_prefix='/api')

    return app