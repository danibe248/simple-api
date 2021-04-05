import flask, json
from pymongo import MongoClient
from flask import request, jsonify

# Flask app configuration
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# mongodb connection
with open('api/config.json') as c:
    config = json.load(c)
    client = MongoClient(config['mongo_host'], config['mongo_port'])
    db = client[config['mongo_db']]
    collection = db[config['mongo_collection']]

# Use this function to perform healthchecks
@app.route('/', methods=['GET'])
def home():
    return '''Congratulations! You've found a very simple API!'''

# This function returns all the records in the table
@app.route('/api/v1/resources/questions/all', methods=['GET'])
def api_all():
    response = list(collection.find({}))
    return jsonify(response)

# This function allows querying the mongodb table to get one element by ID
@app.route('/api/v1/resources/questions', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    response = collection.find_one({"_id":id})

    return jsonify(response)

app.run(host='0.0.0.0',port=55500)