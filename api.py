import flask, boto3, json
from Encoder import Encoder
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.json_encoder = Encoder

TABLE_NAME = "questions"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

@app.route('/', methods=['GET'])
def home():
    return '''HEALTHCHECK'''


@app.route('/api/v1/resources/questions/all', methods=['GET'])
def api_all():
    response = table.scan()
    return jsonify(response['Items'])


@app.route('/api/v1/resources/questions', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    response = table.get_item(Key={'id': id})

    return jsonify(response['Item'])

app.run(host='0.0.0.0',port=55500)