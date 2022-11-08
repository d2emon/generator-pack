coverage run -m unittest -v tests.database.test_data_block \
    tests.factories.test_factory \
    tests.genesys.fng.test_database \
    tests.genesys.fng.test_fantasy_name_factories
coverage xml
coverage html
