from flask import jsonify
from .app import app


@app.route('/')
def index():
    return "Hello, World!"


@app.errorhandler(404)
def not_found(error):
    print(error)
    return jsonify({'error': 'Not found'}), 404
