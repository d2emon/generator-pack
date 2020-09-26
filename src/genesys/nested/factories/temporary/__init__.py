from genesys.nested.factories.factory import Factory


class GalaxyArmLifeFactory(Factory):
    def children(self):
        # "galactic life,5%"
        yield None


class GalaxyCenterLifeFactory(Factory):
    def children(self):
        # "galactic life,10%"
        yield None


class NebulaLifeFactory(Factory):
    def children(self):
        # "galactic life,15%"
        yield None


class BlackHoleLifeFactory(Factory):
    def children(self):
        # "crustacean,0.2%"
        yield None


class StarLifeFactory(Factory):
    def children(self):
        # "ghost,0.1%"
        # "space monster,0.2%"
        yield None


class PlanetCoreLifeFactory(Factory):
    def children(self):
        # "space monster,0.5%"
        yield None


class BarrenPlanetLifeFactory(Factory):
    def children(self):
        # "galactic life,10%"
        yield None


class VisitorPlanetLifeFactory(Factory):
    def children(self):
        # "galactic life"
        yield None


class GasGiantLifeFactory(Factory):
    def children(self):
        # "galactic life,10%"
        yield None


class AsteroidLifeFactory(Factory):
    def children(self):
        # "space animal,0.5%"
        yield None


class AsteroidBeltLifeFactory(Factory):
    def children(self):
        # "galactic life,20%"
        yield None


class MoonLifeFactory(Factory):
    def children(self):
        # "ghost,0.1%"
        yield None


class ContinentFactory(Factory):
    def children(self):
        yield None


class MedievalContinentFactory(Factory):
    def children(self):
        yield None


class AncientContinentFactory(Factory):
    def children(self):
        yield None


class FutureContinentFactory(Factory):
    def children(self):
        yield None


class OceanFactory(Factory):
    def children(self):
        yield None


class SkyFactory(Factory):
    def children(self):
        yield None


class FutureSkyFactory(Factory):
    def children(self):
        yield None


class TerraformedSkyFactory(Factory):
    def children(self):
        yield None


class VisitorCityFactory(Factory):
    def children(self):
        yield None


class VisitorInstallationFactory(Factory):
    def children(self):
        yield None


class FutureMoonFactory(Factory):
    def children(self):
        yield None


class PastaFactory(Factory):
    def children(self):
        yield None


class BodyFactory(Factory):
    def children(self):
        yield None


class ClothingSetFactory(Factory):
    def children(self):
        yield None


class ComputerFactory(Factory):
    def children(self):
        yield None


class DysonSurfaceFactory(Factory):
    def children(self):
        yield None
