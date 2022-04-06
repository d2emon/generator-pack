import unittest
from models.universe import Multiverse, Supercluster, Universe


class TestUniverseModels(unittest.TestCase):
    def setUp(self) -> None:
        self.children = [
            *[Supercluster() for _ in range(10)],
            *[Universe() for _ in range(10)],
        ]
        return super().setUp()

    def test_supercluster_model(self):
        model = Supercluster()
        self.assertEqual(model.name, 'galactic supercluster')

    def test_universe_model(self):
        model = Universe(
            None,
            *self.children,
        )
        self.assertEqual(model.name, 'Universe')
        for item in model.clusters:
            self.assertTrue(isinstance(item, Supercluster))

    def test_multiverse_model(self):
        model = Multiverse(
            None,
            *self.children,
        )
        self.assertEqual(model.name, 'Multiverse')
        for item in model.universes:
            self.assertTrue(isinstance(item, Universe))


if __name__ == "__main__":
    unittest.main()
