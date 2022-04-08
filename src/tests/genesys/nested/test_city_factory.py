import unittest
from genesys.nested.universe import UniverseFactory
from models.universe import Supercluster, Universe
from models.universe.galaxy import Galaxy, GalaxyArm, GalaxyCenter
from models.universe.nebula import Nebula
from models.universe.planet import Planet
from models.universe.star import Star, StarSystem


class TestCityFactory(unittest.TestCase):
    def test_city_factory(self):
        print()
        universe_factory = UniverseFactory()

        universe = universe_factory()
        self.assertTrue(isinstance(universe, Universe))
        self.assertGreater(len(universe.clusters), 0)
        print(universe)

        cluster = universe.clusters[0]
        self.assertTrue(isinstance(cluster, Supercluster))
        self.assertGreater(len(cluster.galaxies), 0)
        print(cluster)

        galaxy = cluster.galaxies[0]
        self.assertTrue(isinstance(galaxy, Galaxy))
        print(galaxy)

        galaxy_center = galaxy.center
        self.assertTrue(isinstance(galaxy_center, GalaxyCenter))
        self.assertGreater(len(galaxy_center.stars), 0)
        print(galaxy_center)

        star_system = galaxy_center.stars[0]
        self.assertTrue(isinstance(star_system, StarSystem))
        print(star_system)

        planet = star_system.planets[0]
        self.assertTrue(isinstance(planet, Planet))
        print(planet)

        print(planet.children)


if __name__ == "__main__":
    unittest.main()
