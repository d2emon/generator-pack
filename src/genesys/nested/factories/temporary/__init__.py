from genesys.model.model import Model
from genesys.nested.factories.factory import Factory


class ContinentFactory(Factory):
    default_model = Model

    def children(self):
        yield None


class MedievalContinentFactory(ContinentFactory):
    def children(self):
        yield None


class AncientContinentFactory(ContinentFactory):
    def children(self):
        yield None


class FutureContinentFactory(ContinentFactory):
    def children(self):
        yield None


class VisitorCityFactory(Factory):
    default_model = Model

    def children(self):
        yield None


class VisitorInstallationFactory(Factory):
    default_model = Model

    def children(self):
        yield None


class FutureMoonFactory(Factory):
    default_model = Model

    def children(self):
        yield None


class PastaFactory(Factory):
    default_model = Model

    def children(self):
        yield None


class ComputerFactory(Factory):
    default_model = Model

    def children(self):
        yield None


class DysonSurfaceFactory(Factory):
    default_model = Model

    def children(self):
        yield None
