from flask import Flask, request, json, Response
from keywords import get_keywords
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def root():
    return 'hello'

@app.route("/keywords", methods=['POST'])
def extract_keywords():
    document = request.get_json()['text']

    response = Response(
        response=json.dumps(list(get_keywords(document))),
        status=200,
        mimetype="application/json",
    )

    return response
