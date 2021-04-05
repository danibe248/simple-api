import flask, boto3, json
from Encoder import Encoder
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.json_encoder = Encoder

TABLE_NAME = "questions"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''This was a get!'''


@app.route('/api/v1/resources/questions/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/questions', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    response = table.get_item(Key={'id': id})

    return jsonify(response['Item'])

app.run(host='0.0.0.0',port=55500)