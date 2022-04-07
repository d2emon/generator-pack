import unittest
from genesys.nested.factories.universe import MultiverseFactory, SuperclusterFactory, UniverseFactory
from genesys.nested.factories.universe.galaxy import GalaxyFactory, GalaxyArmFactory, GalaxyCenterFactory
from models.universe import Multiverse, Supercluster, Universe
from models.universe.galaxy import Galaxy, GalaxyArm, GalaxyCenter, GalaxyPart


class TestUniverseModels(unittest.TestCase):
    def test_multiverse_factory(self):
        factory = MultiverseFactory()
        model = factory()
        self.assertTrue(isinstance(model, Multiverse))
        self.assertIn(model.name, factory.provider.multiverse)
        for item in model.universes:
            self.assertTrue(isinstance(item, Universe))

    def test_universe_factory(self):
        factory = UniverseFactory()
        model = factory()
        self.assertTrue(isinstance(model, Universe))
        self.assertEqual(model.name, 'Universe')
        for item in model.clusters:
            self.assertTrue(isinstance(item, Supercluster))

    def test_supercluster_factory(self):
        factory = SuperclusterFactory()
        model = factory()
        self.assertTrue(isinstance(model, Supercluster))
        self.assertEqual(model.name, 'galactic supercluster')
        for item in model.galaxies:
            self.assertTrue(isinstance(item, Galaxy))

    def test_galaxy_factory(self):
        factory = GalaxyFactory()
        model = factory()
        self.assertTrue(isinstance(model, Galaxy))
        self.assertEqual(model.name, 'Galaxy')
        self.assertTrue(isinstance(model.center, GalaxyCenter))
        for item in model.arms:
            self.assertTrue(isinstance(item, GalaxyArm))

    def test_galaxy_center_factory(self):
        factory = GalaxyCenterFactory()
        model = factory()
        self.assertTrue(isinstance(model, GalaxyCenter))
        self.assertEqual(model.name, 'galactic center')
        for item in model.children:
            self.assertEqual(item.__class__, 'galactic supercluster')
            self.assertTrue(isinstance(item, Universe))

    def test_galaxy_arm_factory(self):
        factory = GalaxyArmFactory()
        model = factory()
        self.assertTrue(isinstance(model, GalaxyArm))
        self.assertEqual(model.name, 'arm')
        for item in model.children:
            self.assertEqual(item.__class__, 'galactic supercluster')
            self.assertTrue(isinstance(item, Universe))


if __name__ == "__main__":
    unittest.main()
