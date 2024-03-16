
from pymongo import MongoClient

config={
    "host": "localhost",
    "port": 27017
}

def get_connection(db):
    connection = MongoClient(**config)
    return connection[db]
