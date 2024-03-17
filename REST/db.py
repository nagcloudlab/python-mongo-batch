
from pymongo import MongoClient
import os

# get database credentials from environment variables
# or use default values

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')    
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)

config={
    "host": "localhost",
    "port": 27017
}

def get_connection(db):
    connection = MongoClient(**config)
    return connection[db]
