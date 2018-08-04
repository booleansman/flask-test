from flask import Flask, Response, abort, jsonify, request

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def start_counting():
    return "Hello !",200


@app.route('/', methods=['GET'])
def indexy():
    x = [{'/api' : "GET"}, {'/' : "GET"}]
    return jsonify(result = x),200

