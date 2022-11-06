coverage run -m unittest -v tests.factories.test_factory ^
    tests.genesys.fng.test_fantasy_name_factories
coverage xml
coverage html
