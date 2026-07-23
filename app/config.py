import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuración centralizada de la aplicación (Twelve-Factor App)."""
    # MongoDB Config
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://127.0.0.1:27017/")
    MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "blog")

    # CouchDB Config
    COUCHDB_URL = os.getenv("COUCHDB_URL", "http://127.0.0.1:5984")
    COUCHDB_USER = os.getenv("COUCHDB_USER", "admin")
    COUCHDB_PASSWORD = os.getenv("COUCHDB_PASSWORD", "secret")

    # Flask App Config
    DEBUG = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "t")
    PORT = int(os.getenv("PORT", 5000))
    HOST = os.getenv("HOST", "0.0.0.0")
