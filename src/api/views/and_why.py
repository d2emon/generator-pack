from flask import jsonify
from genesys.and_why.factories.clothing import ClothingFactory
from genesys.and_why.factories.doll import DollFactory
from genesys.and_why.factories.gender import GenderFactory
from genesys.and_why.factories.slot import SlotFactory
from ..app import app


@app.route('/api/v1.0/and_why')
def get_index():
    return jsonify([
        'doll',
        'clothing',
    ])


@app.route('/api/v1.0/and_why/clothing')
@app.route('/api/v1.0/and_why/clothing/<gender>')
def get_clothing(gender=None):
    factory = ClothingFactory()
    models = factory(gender=gender)

    result = []
    for item in models:
        result.append(str(item))

    return jsonify(result)


@app.route('/api/v1.0/and_why/doll')
@app.route('/api/v1.0/and_why/doll/<gender>')
def get_doll(gender=None):
    factory = DollFactory()
    model = factory(gender=gender)
    return jsonify(model.values)


@app.route('/api/v1.0/and_why/gender')
@app.route('/api/v1.0/and_why/gender/<gender>')
def get_gender(gender=None):
    factory = GenderFactory()
    model = factory()
    return jsonify(model)


@app.route('/api/v1.0/and_why/slot')
def get_slot():
    factory = SlotFactory()
    models = factory()
    result = list(models)
    return jsonify(result)
