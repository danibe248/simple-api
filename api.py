import flask, boto3, json
from Encoder import Encoder
from flask import request, jsonify

# Flask app configuration
app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.json_encoder = Encoder

# DynamoDB table connection
TABLE_NAME = "questions"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

# Use this function to perform healthchecks
@app.route('/', methods=['GET'])
def home():
    return '''HEALTHCHECK'''

# This function returns all the records in the table
@app.route('/api/v1/resources/questions/all', methods=['GET'])
def api_all():
    response = table.scan()
    return jsonify(response['Items'])

# This function allows querying the DynamoDB table to get one element by ID
@app.route('/api/v1/resources/questions', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    response = table.get_item(Key={'id': id})

    return jsonify(response['Item'])

app.run(host='0.0.0.0',port=55500)