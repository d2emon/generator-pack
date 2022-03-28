import random
import unittest
from genesys.world import WorldDataProvider, WorldFactory
from models.world import World


class TestWorldFactory(unittest.TestCase):
    def setUp(self) -> None:
        self.names = [str(random.uniform(0, 100)) for _ in range(10)]
        self.provider = WorldDataProvider(
            names=self.names
        )
        self.factory = WorldFactory(self.provider)

    def test_world_factory(self):
        world = self.factory()
        self.assertIsInstance(world, World)
        self.assertIn(world.name, self.names)


if __name__ == "__main__":
    unittest.main()
