from genesys.nested.factories.nested_factory import NestedFactory
from models.materials import portal


class PortalFactory(NestedFactory):
    model = portal.Portal

    def children(self):
        from ..universe import UniverseFactory

        yield UniverseFactory.one()
