coverage run -m unittest -v \
    tests.database.test_data_block \
    tests.factories.test_factory \
    tests.genesys.fng.test_database \
    tests.genesys.fng.test_name_factory \
    tests.genesys.fng.test_name_block_factory \
    tests.genesys.fng.test_validators \
    tests.models.test_model \
    tests.models.test_preparable_model \
    tests.genesys.fng.test_fantasy_name_factories
coverage xml
coverage html
pylint genesys/fng/names/fantasy
pylint genesys/fng/names/real
pylint genesys/fng/names/place
