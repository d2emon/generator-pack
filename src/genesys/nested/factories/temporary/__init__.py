from genesys.nested.factories.factory import Factory


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


class ComputerFactory(Factory):
    def children(self):
        yield None


class DysonSurfaceFactory(Factory):
    def children(self):
        yield None
