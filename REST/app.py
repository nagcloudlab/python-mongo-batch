from flask import Flask, request 
from db import get_connection
from flask_cors import CORS

import json
from json import JSONEncoder
from bson import ObjectId


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return JSONEncoder.default(self, obj)


app = Flask(__name__)
CORS(app)
db=get_connection('populations')


# get all cities
# GET /api/cities
# Accept: application/json
# Content-Type: application/json

@app.get('/api/cities')
def get_cities():
    cities=db.cities.find({})
    # json response with content type
    return json.dumps(list(cities), cls=CustomJSONEncoder), 200, {'Content-Type': 'application/json'}

# get city by id
# GET /api/cities/<id>
# Accept: application/json
# Content-Type: application/json

@app.get('/api/cities/<id>')
def get_city(id):
    city=db.cities.find_one({'_id':ObjectId(id)})
    # json response with content type
    return json.dumps(city, cls=CustomJSONEncoder), 200, {'Content-Type': 'application/json'}

# create city
# POST /api/cities
# Conntent: application/json
# Content-Type: application/json

@app.post('/api/cities')
def create_city():
    city=request.json
    db.cities.insert_one(city)
    inserted_city=db.cities.find_one(city)
    # json response with content type
    return json.dumps(inserted_city, cls=CustomJSONEncoder), 201, {'Content-Type': 'application/json'}
    

# update city
# PUT /api/cities/<id>
# Conntent: application/json
# Content-Type: application/json

@app.put('/api/cities/<id>')
def update_city(id):
    city=request.json
    db.cities.update_one({'_id':ObjectId(id)},{"$set":city})
    updated_city=db.cities.find_one({'_id':ObjectId(id)})
    # json response with content type
    return json.dumps(updated_city, cls=CustomJSONEncoder), 200, {'Content-Type': 'application/json'}

# delete city
# DELETE /api/cities/<id>
# Accept: application/json
# Content-Type: application/json

@app.delete('/api/cities/<id>')
def delete_city(id):
    db.cities.delete_one({'_id':ObjectId(id)})
    # json response with content type
    return json.dumps({'message':'City deleted successfully'}), 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run(debug=True,port=5000)