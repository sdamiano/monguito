from pymongo import MongoClient
from app.config import Config

# Instancia del cliente MongoDB
mongo_client = MongoClient(Config.MONGO_URI, serverSelectionTimeoutMS=5000)
db = mongo_client[Config.MONGO_DB_NAME]
posts_collection = db["posts"]
