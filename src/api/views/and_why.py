from flask import jsonify
from genesys.and_why.factories.clothing import ClothingFactory
from ..app import app


@app.route('/api/v1.0/and_why')
def get_index():
    return jsonify([
        'doll',
        'clothing',
    ])


@app.route('/api/v1.0/and_why/clothing/<gender>')
def get_clothing(gender):
    factory = ClothingFactory()
    models = factory(gender=gender)

    result = []
    for item in models:
        result.append(str(item))

    return jsonify(result)


@app.route('/api/v1.0/and_why/doll')
def get_doll():
    return jsonify([
        'doll',
        'clothing',
    ])


@app.route('/api/v1.0/and_why/gender')
def get_gender():
    return jsonify([
        'doll',
        'clothing',
    ])


@app.route('/api/v1.0/and_why/slot')
def get_slot():
    return jsonify([
        'doll',
        'clothing',
    ])
