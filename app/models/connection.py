from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# MONGO_URI = os.getenv('MONGO_URI')
# client = MongoClient(MONGO_URI)
# db = client['chingaroshy123']

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            mongo_uri = os.getenv('MONGO_URI')
            cls._instance.client = MongoClient(mongo_uri) 
            cls._instance.db = cls._instance.client['chingaroshy123']
        return cls._instance

    @property
    def database(self):
        return self.db