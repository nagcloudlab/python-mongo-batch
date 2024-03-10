

from pymongo import MongoClient
client = MongoClient('mongodb://localhost:40001,localhost:40002,localhost:40003/?replicaSet=rs1&readPreference=secondaryPreferred')

db = client['test']

collection = db['todos']

# Insert a document
# collection.insert_one({'title': 'learn python'})

# Find a documents

todos = collection.find()
for todo in todos:
    print(todo)

