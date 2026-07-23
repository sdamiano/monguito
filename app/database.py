import base64
from pymongo import MongoClient
from app.config import Config

# Instancia del cliente MongoDB
mongo_client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)
db = mongo_client[Config.MONGO_DB_NAME]
posts_collection = db["posts"]


def get_couch_headers():
    """Genera las cabeceras HTTP de autenticación Basic para CouchDB."""
    auth_str = f"{Config.COUCHDB_USER}:{Config.COUCHDB_PASSWORD}"
    b64_auth = base64.b64encode(auth_str.encode()).decode()
    return {
        "Content-Type": "application/json",
        "Authorization": f"Basic {b64_auth}"
    }
