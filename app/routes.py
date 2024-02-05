from flask import Flask, jsonify
from .counter import Counter

app = Flask(__name__)
counter = Counter()

@app.route('/api/increment', methods=['GET'])
def increment():
    return jsonify(value=counter.increment())

@app.route('/api/increment_by_5', methods=['GET'])  # New endpoint for incrementing by 5
def increment_by_five():
    return jsonify(value=counter.increment_by_five())

@app.route('/api/decrement', methods=['GET'])
def decrement():
    return jsonify(value=counter.decrement())

@app.route('/api/decrement_by_5', methods=['GET'])  # New endpoint for decrementing by 5
def decrement_by_five():
    return jsonify(value=counter.decrement_by_five())

@app.route('/api/reset', methods=['GET'])
def reset():
    return jsonify(value=counter.reset())