from models.v5 import materials
from factories.nested_factory import NestedFactory as Factory


class PortalFactory(Factory):
    default_model = materials.Portal

    def children(self):
        from ..universe import UniverseFactory

        yield from UniverseFactory()
