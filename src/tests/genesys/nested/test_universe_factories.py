import unittest
from genesys.nested.factories.universe import MultiverseFactory, SuperclusterFactory, UniverseFactory
from models.universe import Supercluster, Universe


class TestUniverseModels(unittest.TestCase):
    def test_multiverse_factory(self):
        factory = MultiverseFactory()
        model = factory()
        self.assertIn(model.name, factory.provider.multiverse)
        for item in model.universes:
            self.assertTrue(isinstance(item, Universe))

    def test_universe_model(self):
        factory = UniverseFactory()
        model = factory()
        self.assertEqual(model.name, 'Universe')
        for item in model.clusters:
            self.assertTrue(isinstance(item, Supercluster))

    def test_supercluster_model(self):
        factory = SuperclusterFactory()
        model = factory()
        self.assertEqual(model.name, 'galactic supercluster')


if __name__ == "__main__":
    unittest.main()
