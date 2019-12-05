from flask import Flask, jsonify, json, request
import json

app = Flask(__name__)

data_file = 'headlines.json'
with open(data_file) as f:
    headlines = json.load(f)

@app.route('/')
def home():
    return ('Hello, Biatch!')

@app.route('/headlines/all', methods=['GET'])
def send_headlines_all():
    return jsonify(headlines) 

@app.route('/headlines', methods=['GET'])
def headlines_sources():
    if 'source' in request.args:
        headlines_source = request.args['source']

    source_results = []

    for headline in headlines:
        if headline['source'] == headlines_source:
            source_results.append(headline)
    return jsonify(source_results)

if __name__ == '__main__':
    app.run(debug=True)