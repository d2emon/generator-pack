from flask import jsonify
from config import DB_CONFIG
from ..app import app


__DATA = [
    'and_why',
    # data
    # genesys
    # models
    'campsite',
    # data
    # genesys
    'cp2020',
    # genesys
    'demographics',
    # genesys
    'distance',
    # models
    'dndspeak',
    # data
    # genesys
    'encounters',
    # genesys
    # models
    'events',
    # models
    'fixtures',
    # data
    # genesys
    'fng',
    # data
    # genesys
    # models
    'generator_models',
    # genesys
    # models
    'history',
    # models
    'item',
    # models
    'lexicon',
    # genesys
    'markov',
    # genesys
    'media',
    # genesys
    'model',
    # genesys
    'models',
    # models
    'name',
    # models
    'nested',
    # genesys
    'person',
    # models
    'r4f',
    # genesys
    'redlands',
    # data
    # genesys
    # models
    'rpa',
    # genesys
    'rpg',
    # genesys
    'scales',
    # data
    # genesys
    # models
    'storm',
    # data
    # genesys
    'timeline',
    # data
    # genesys
    'universe',
    # models
    'v4',
    # models
    'v5',
    # models
    'world',
    # genesys
    # models
    ##
    'genders',
    # data
]

@app.route('/api/v1.0/config')
def get_config():
    return jsonify(DB_CONFIG)


@app.route('/api/v1.0/data')
def get_data():
    return jsonify(__DATA)


@app.route('/api/v1.0/database')
def get_database():
    raise NotImplementedError()


@app.route('/api/v1.0/factories')
def get_factories():
    raise NotImplementedError()


@app.route('/api/v1.0/generated')
def get_generated():
    raise NotImplementedError()


@app.route('/api/v1.0/genesys')
def get_genesys():
    raise NotImplementedError()


@app.route('/api/v1.0/models')
def get_models():
    raise NotImplementedError()


@app.route('/api/v1.0/rpg')
def get_rpg():
    raise NotImplementedError()
